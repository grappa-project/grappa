# -*- coding: utf-8 -*-
from ..operator import Operator


class RaisesOperator(Operator):
    """
    Asserts if a given function raises an exception.

    Example::

        def fn():
            raise ValueError('error')

        # Should style
        fn | should.raise_error()
        fn | should.raise_error(ValueError)
        fn | should.raise_error(AttributeError, ValueError)

        # Should style - negation form
        fn | should.do_not.raise_error()
        fn | should.do_not.raise_error(ValueError)
        fn | should.do_not.raise_error(AttributeError, ValueError)

        # Expect style
        fn | expect.to.raise_error()
        fn | expect.to.raise_error(ValueError)
        fn | expect.to.raise_error(AttributeError, ValueError)

        # Expect style - negation form
        fn | expect.to_not.raise_error()
        fn | expect.to_not.raise_error(ValueError)
        fn | expect.to_not.raise_error(AttributeError, ValueError)
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('raises', 'raise_error', 'raise_errors')

    # Operator chain aliases
    aliases = ('to', 'that', 'are', 'instance', 'of')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'a callable object that raises the exception(s) "{value}"',
        'a callable object that do not raise the exception(s) "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with reference "{value}"',
    )

    def after_success(self, obj, *keys):
        message = getattr(self.value, 'message', None)

        if not message and self.value:
            message = ' '.join([str(item) for item in self.value.args])

        self.ctx.subject = message

    def match(self, fn, *errors):
        if not callable(fn):
            return False, ['subject must be a function or method']

        try:
            fn()
        except Exception as err:
            self.value = err

            return isinstance(err, *errors), ['invalid raised exception']
        else:
            return False, ['did not raise any exception']
