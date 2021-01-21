import os
import pytest


def test_been_called(expect, mocker):
    mock_called = mocker.patch('os.path.join')
    os.path.join('home', 'log.txt')

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
    mock_called = mocker.patch('os.path.join')
    os.path.join('home', 'log.txt')
    os.path.join('home', 'log.txt')
    os.path.join('home', 'log.txt')

    expect(mock_called).to.have.been_called_times(3)

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_times(3)

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have.been_called_times(0)
    expect(mock_not_called).to.have_not.been_called_times(3)

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_times(3)


def test_been_called_with(expect, mocker):
    mock_called = mocker.patch('os.path.join')
    os.path.join('home', 'log.txt')
    os.path.join('root', 'config.json')

    expect(mock_called).to.have.been_called_with('home', 'log.txt')
    expect(mock_called).to.have.been_called_with('root', 'config.json')

    with pytest.raises(AssertionError):
        expect(mock_called).to.have_not.been_called_with('home', 'log.txt')

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_with('home', 'log.txt')

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_with('home', 'log.txt')


def test_been_called_once(expect, mocker):
    mock_called = mocker.patch('os.path.join')
    os.path.join('home', 'log.txt')

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
    mock_called = mocker.patch('os.path.join')
    os.path.join('home', 'log.txt')

    expect(mock_called).to.have.been_called_once_with('home', 'log.txt')

    with pytest.raises(AssertionError):
        expect(mock_called).to_not.been_called_once_with('home', 'log.txt')

    mock_not_called = mocker.patch('os.rmdir')

    expect(mock_not_called).to.have_not.been_called_once_with('/home/log.txt')

    with pytest.raises(AssertionError):
        expect(mock_not_called).to.have.been_called_once_with('/home/log.txt')

    mock_called_several_times = mocker.patch('os.rename')
    os.rename('/home/log.txt', '/home/log_new.txt')
    os.rename('/home/log.txt', '/home/log_new.txt')

    expect(mock_called_several_times).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have.been_called_once_with(
            '/home/log.txt', '/home/log_new.txt'
        )

    with pytest.raises(AssertionError):
        expect(mock_called_several_times).to.have.been_called_once


def test_been_called_with_a_spy(expect, mocker):
    class Foo():
        def bar(self, string, padding):
            return string.zfill(padding)

    foo = Foo()
    spy = mocker.spy(foo, 'bar')

    expect(foo.bar('foo', 5)).to.be('00foo')

    expect(spy).to.have.been_called
    expect(spy).to.have.been_called_once
    expect(spy).to.have.been_called_times(1)
    expect(spy).to.have.been_called_with('foo', 5)
    expect(spy).to.have.been_called_once_with('foo', 5)

    with pytest.raises(AssertionError):
        expect(spy).to.have_not.been_called

    with pytest.raises(AssertionError):
        expect(spy).to.have_not.been_called_with('foo', 5)

    with pytest.raises(AssertionError):
        expect(spy).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(spy).to.have_not.been_called_times(1)

    with pytest.raises(AssertionError):
        expect(spy).to.have_not.been_called_once_with('foo', 5)


def test_been_called_with_a_stub(expect, mocker):
    def foo(bar):
        bar('test')

    stub = mocker.stub('bar_stub')
    foo(stub)

    expect(stub).to.have.been_called
    expect(stub).to.have.been_called_once
    expect(stub).to.have.been_called_times(1)
    expect(stub).to.have.been_called_with('test')
    expect(stub).to.have.been_called_once_with('test')

    with pytest.raises(AssertionError):
        expect(stub).to.have_not.been_called

    with pytest.raises(AssertionError):
        expect(stub).to.have_not.been_called_with('test')

    with pytest.raises(AssertionError):
        expect(stub).to.have_not.been_called_once

    with pytest.raises(AssertionError):
        expect(stub).to.have_not.been_called_times(1)

    with pytest.raises(AssertionError):
        expect(stub).to.have_not.been_called_once_with('test')


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
