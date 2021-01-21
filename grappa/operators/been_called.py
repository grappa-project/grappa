# -*- coding: utf-8 -*-
from ..decorators import mock_implementation_validator
from ..operator import Operator


class BeenCalledOperator(Operator):
    """
    Asserts if a given mock subject have been called at least once.

    Warning::

        Piping style assertions is not yet supported.

    Example::

        # Should style
        should(mock).have.been_called

        # Should style - negation form
        should(mock).have_not.been_called

        # Expect style
        expect(mock).to.have.been_called

        # Expect style - negation form
        expect(mock).to.have_not.been_called
        expect(mock).to_not.have.been_called
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called at least once',
        'a mock that has not been called',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has not been called',
        'a mock that has been called at least once',
    )

    @mock_implementation_validator
    def match(self, subject):
        return subject.called


class BeenCalledOnceOperator(Operator):
    """
    Asserts if a given mock subject have been called once.

    Warning::

        Piping style assertions is not yet supported.

    Example::

        # Should style
        should(mock).have.been_called_once

        # Should style - negation form
        should(mock).have_not.been_called_once

        # Expect style
        expect(mock).to.have.been_called_once

        # Expect style - negation form
        expect(mock).to.have_not.been_called_once
        expect(mock).to_not.have.been_called_once
    """

    # Is the operator a keyword
    kind = Operator.Type.ACCESSOR

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_once',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called once',
        'a mock that has not been called once',
    )

    # Subject message template
    subject_message = Operator.Dsl.Message(
        'a mock that has been called {call_count} time(s)',
        'a mock that has been called once',
    )

    @mock_implementation_validator
    def match(self, subject):
        return subject.call_count == 1


class BeenCalledTimesOperator(Operator):
    """
    Asserts if a given mock subject have been called n times.

    Warning::

        Piping style assertions is not yet supported.

    Example::

        # Should style
        should(mock).have.been_called_times(3)

        # Should style - negation form
        should(mock).have_not.been_called_times(3)

        # Expect style
        expect(mock).to.have.been_called_times(0)

        # Expect style - negation form
        expect(mock).to.have_not.been_called_times(1)
        expect(mock).to_not.have.been_called_times(3)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('been_called_times',)

    # Error message templates
    expected_message = Operator.Dsl.Message(
        'a mock that has been called {value} times',
        'a mock that has not been called {value} times',
    )

    subject_message = Operator.Dsl.Message(
        'a mock that has not been called {call_count} times',
        'a mock that has been called {call_count} times',
    )

    @mock_implementation_validator
    def match(self, subject, expected):
        return subject.call_count == expected
