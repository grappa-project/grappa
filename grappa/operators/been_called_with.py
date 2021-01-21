# -*- coding: utf-8 -*-
from ..decorators import mock_implementation_validator
from ..operator import Operator


class BeenCalledWithOperator(Operator):
    """
    Asserts if a given mock subject have been called at least once
    with specified arguments.

    Warning::

        Piping style assertions is not yet supported.

    Example::

        # Should style
        should(mock).have.been_called_with('foo')

        # Should style - negation form
        should(mock).have_not.been_called_with('foo', 10)

        # Expect style
        expect(mock).to.have.been_called_with('foo')

        # Expect style - negation form
        expect(mock).to.have_not.been_called_with('foo', True, 150)
        expect(mock).to_not.have.been_called_with('foo')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_with',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called at least once with arguments',
        'a mock that has not been called with arguments',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has not been called with arguments',
        'a mock that has been called at least once with arguments',
    )

    @mock_implementation_validator
    def match(self, subject, *args, **kwargs):
        try:
            subject.assert_any_call(*args, **kwargs)
            return True
        except AssertionError as error:
            return False, error.args[0].splitlines()


class BeenCalledOnceWithOperator(Operator):
    """
    Asserts if a given mock subject have been called once
    with specified arguments.

    Warning::

        Piping style assertions is not yet supported.

    Example::

        # Should style
        should(mock).have.been_called_once_with('foo')

        # Should style - negation form
        should(mock).have_not.been_called_once_with('foo', 10)

        # Expect style
        expect(mock).to.have.been_called_once_with('foo')

        # Expect style - negation form
        expect(mock).to.have_not.been_called_once_with('foo', True, 150)
        expect(mock).to_not.have.been_called_once_with('foo')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_once_with',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called once with arguments',
        'a mock that has not been called once with arguments',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has been called {call_count} time(s) with arguments',
        'a mock that has been called once with arguments',
    )

    @mock_implementation_validator
    def match(self, subject, *args, **kwargs):
        try:
            subject.assert_any_call(*args, **kwargs)
            return subject.call_count == 1
        except AssertionError as error:
            return False, error.args[0].splitlines()
