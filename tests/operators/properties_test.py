import pytest


def test_expect_properties(should):
    class foo(object):
        foo = 'bar'

        class baz(object):
            foo = 'bar'

        def bar(self):
            pass

    foo() | should.have.property('foo')
    foo() | should.have.property('foo') > should.be.equal.to('bar')

    should(foo()).have.property('foo') > should.be.equal.to('bar')
    should(foo()).have.property('foo').which.should.be.equal.to('bar')

    should(foo()).have.property('bar').which.should.be.a('method')
    should(foo()).have.properties('bar', 'foo')

    (foo()
        | should.have.property('foo')
        > should.be.a('string')
        > should.have.length.of(3)
        > should.be.equal.to('bar'))

    (foo()
        | should.have.property('baz')
        > should.be.an('object')
        > should.have.property('foo')
        > should.be.equal.to('bar'))

    with pytest.raises(AssertionError):
        should(foo()).have.property('boo')

    with pytest.raises(AssertionError):
        should(foo()).have.property('boo')

    with pytest.raises(AssertionError):
        should(foo()).have.property('foo') > should.be.equal.to('foo')

    with pytest.raises(AssertionError):
        should(foo()).have.property('foo').which.should.be.equal.to('pepe')

    foo() | should.have.properties('foo', 'bar')

    foo() | should.have.properties(('foo', 'bar'))

    foo() | should.have.properties(['foo', 'bar'])

    foo() | should.have.properties({'foo', 'bar'})


def test_not_expect_properties(should):
    class foo(object):
        foo = 'bar'

        class baz(object):
            foo = 'bar'

        def bar(self):
            pass

    foo() | should.not_have.property('fuu')
