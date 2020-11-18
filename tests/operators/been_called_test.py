import os
import platform
import pytest


def test_been_called(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called

    mock_called_several_times = mocker.patch('os.rename')
    os.rename('/home/log.txt', '/home/log_new.txt')
    os.rename('/home/log.txt', '/home/log_new.txt')

    expect(mock_called_several_times).to.have.been_called

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have_not.been_called


def test_been_called_times(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')
    os.remove('/home/log.txt')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_times(3)

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_times(3)

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have.been_called_times(0)
    expect(mock_not_called).to.have_not.been_called_times(3)

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_times(3)


def test_been_called_with(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_with('/home/log.txt')

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_with('/home/log.txt')


def test_been_called_once(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_once

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_once

    mock_called_several_times = mocker.patch('os.rename')
    os.rename('/home/log.txt', '/home/log_new.txt')
    os.rename('/home/log.txt', '/home/log_new.txt')

    expect(mock_called_several_times).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have.been_called_once


def test_been_called_once_with(expect, mocker):
    mock_called = mocker.patch('os.remove')
    os.remove('/home/log.txt')

    expect(mock_called).to.have.been_called_once_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_once_with('/home/log.txt')

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_once_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_once_with('/home/log.txt')

    mock_called_several_times = mocker.patch('os.rename')
    os.rename('/home/log.txt', '/home/log_new.txt')
    os.rename('/home/log.txt', '/home/log_new.txt')

    expect(mock_called_several_times).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have.been_called_once


def test_been_called_with_a_spy(expect, mocker):
    spy = mocker.spy(os.path, 'basename')
    os.path.basename('/home/log.txt')

    expect(spy).to.have.been_called
    expect(spy).to.have.been_called_once
    expect(spy).to.have.been_called_times(1)
    expect(spy).to.have.been_called_with('/home/log.txt')

    # TODO: on PyPy2, need to investigate why called once assertion
    #       fails indicating that the spy has been called 3 times
    #       instead of 1
    implementation = platform.python_implementation()
    major = platform.python_version_tuple()[0]

    if implementation != 'PyPy' and major != '2':
        expect(spy).to.have.been_called_once_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(spy).to.have_not.been_called

    with pytest.raises(AssertionError):
        expect(spy).to.have_not.been_called_with('/home/log.txt')

    # If previous called once assertion failed, these ones will fail to fail
    if implementation != 'PyPy' and major != '2':
        with pytest.raises(AssertionError):
            expect(spy).to.have_not.been_called_once

        with pytest.raises(AssertionError):
            expect(spy).to.have_not.been_called_times(1)

        with pytest.raises(AssertionError):
            expect(spy).to.have_not.been_called_once_with('/home/log.txt')


def test_been_called_with_a_stub(expect, mocker):
    def foo(on_something):
        on_something()

    stub = mocker.stub('on_something_stub')
    foo(stub)

    expect(stub).to.have.been_called
    # stubs are function like spies, we do not need to test everything again


def test_been_called_with_an_incompatible_object(expect, mocker):
    def foo():
        pass

    foo()

    with pytest.raises(AssertionError):
        expect(foo).to.have.been_called

    with pytest.raises(AssertionError):
        expect(foo).to.have.been_called_once

    with pytest.raises(AssertionError):
        expect(foo).to.have.been_called_times(1)

    with pytest.raises(AssertionError):
        expect(foo).to.have.been_called_with('something')

    with pytest.raises(AssertionError):
        expect(foo).to.have.been_called_once_with('something')
