import pytest
from functools import partial


def test_raises(should):
    def no_error():
        pass

    def error():
        raise AssertionError('foo')

    def error_with_params(foo_param):
        raise AssertionError(foo_param)

    error | should.raise_error(Exception)
    error | should.raise_error(AssertionError)
    error | should.do_not.raise_error(NotImplementedError)

    partial(error_with_params, "Foobar") | should.raise_error(AssertionError)
    partial(error_with_params, "Foobar") | should.to_not\
        .raise_error(NotImplementedError)

    with pytest.raises(AssertionError):
        error | should.raise_error(NotImplementedError)

    with pytest.raises(AssertionError):
        error | should.do_not.raise_error(AssertionError)

    with pytest.raises(AssertionError):
        None | should.raise_error(AssertionError)

    with pytest.raises(AssertionError):
        no_error | should.raise_error(AssertionError)

    no_error | should.do_not.raise_error(AssertionError)


def test_raises_with_message_redirection(should):
    def error():
        raise AssertionError('foo')

    def env_error():
        raise EnvironmentError(3501, 'bar')

    error | should.raise_error(AssertionError) > should.equal('foo')
    error | should.raise_error(AssertionError) > should.do_not.equal('fooed')

    error | should.raise_error(AssertionError) > should.contain('fo')

    error | should.do_not.raise_error(NotImplementedError) \
        > should.equal('foo')

    env_error | should.raise_error(EnvironmentError) > should.contain('bar')

    env_error | should.raise_error(EnvironmentError) > should.equal('3501 bar')

    with pytest.raises(AssertionError):
        error | should.raise_error(AssertionError) > should.equal('fooe')

    with pytest.raises(AssertionError):
        error | should.raise_error(NotImplementedError) > should.equal('foo')


def test_raises_custom_exception_message_redirection(should):
    class CustomException(Exception):
        message = 'foo'

        def __init__(self, *args):
            super(CustomException, self).__init__(self.message, *args)

    def custom_error():
        raise CustomException('bar')

    custom_error | should.raise_error(CustomException) > should.equal('foo')

    custom_error | should.raise_error(CustomException) \
        > should.do_not.equal('foo bar')
