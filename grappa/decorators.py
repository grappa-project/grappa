# -*- coding: utf-8 -*-
import inspect
import functools
import six
from .api import TestProxy
from .engine import Engine
from .operator import Operator


# Explicit module members to export
__all__ = (
    'operator',
    'attribute',
    'register'
)


def operator(name=None, operators=None, aliases=None, kind=None):
    """
    Registers a new operator function in the test engine.

    Arguments:
        *args: variadic arguments.
        **kw: variadic keyword arguments.

    Returns:
        function
    """
    def delegator(assertion, subject, expected, *args, **kw):
        return assertion.test(subject, expected, *args, **kw)

    def decorator(fn):
        operator = Operator(fn=fn, aliases=aliases, kind=kind)
        _name = name if isinstance(name, six.string_types) else fn.__name__
        operator.operators = (_name,)

        _operators = operators
        if isinstance(_operators, list):
            _operators = tuple(_operators)

        if isinstance(_operators, tuple):
            operator.operators += _operators

        # Register operator
        Engine.register(operator)
        return functools.partial(delegator, operator)

    return decorator(name) if inspect.isfunction(name) else decorator


def attribute(*args, **kw):
    """
    Registers a new attribute only operator function in the test engine.

    Arguments:
        *args: variadic arguments.
        **kw: variadic keyword arguments.

    Returns:
        function
    """
    return operator(kind=Operator.Type.ATTRIBUTE, *args, **kw)


def register(operator):
    """
    Registers a new operator class in the test engine.

    Arguments:
        operator (Operator): operator class to register.

    Returns:
        Operator: operator class.
    """
    Engine.register(operator)
    return operator


def mock_implementation_validator(func):
    """
    Validate that a mock conform to the implementation required to run
    have_been and have_been_with operators.

    Otherwise returns a Grappa tuple with missing implementation reasons.

    Arguments:
        operator (Operator): a been_called or been_called_with operator.
        subject: a mock whose implementation is to be validated.
        *args: variadic arguments.
        **kw: variadic keyword arguments.

    Returns:
        (function|tuple)
    """
    @functools.wraps(func)
    def wrapper(operator, subject, *args, **kwargs):
        expect = TestProxy('expect')

        propery_reason_template = 'a property named "{}" is expected'

        def validate_props(reasons, prop):
            try:
                expect(subject).to.have.property(prop)
            except AssertionError:
                reasons.append(propery_reason_template.format(prop))
            return reasons

        method_reason_template = 'a method named "{}" is expected'

        def validate_methods(reasons, method):
            try:
                expect(subject).to.implement.methods(method)
            except AssertionError:
                reasons.append(method_reason_template.format(method))
            return reasons

        expected_props = ('called', 'call_count')
        reasons = functools.reduce(validate_props, expected_props, [])

        expected_methods = ('assert_any_call',)
        reasons = functools.reduce(validate_methods, expected_methods, reasons)

        if reasons:
            operator.information = (
                Operator.Dsl.Help(
                    Operator.Dsl.Description(
                        'Required implementation is based on unittest.mock.Mock class.', # noqa E501
                        '',
                        'Properties required',
                        '    {}'.format(', '.join(expected_props)),
                        'Methods required',
                        '    {}'.format(', '.join(expected_methods)),
                        '',
                    ),
                    Operator.Dsl.Reference(
                        'https://docs.python.org/3/library/unittest.mock.html#the-mock-class', # noqa E501
                    ),
                    Operator.Dsl.Reference(
                        'https://pypi.org/project/pytest-mock/',
                    ),
                ),
            )

            reasons.insert(0, 'mock implementation is incomplete')
            return False, reasons

        return func(operator, subject, *args, **kwargs)

    return wrapper
