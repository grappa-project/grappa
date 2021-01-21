# -*- coding: utf-8 -*-
from array import array
from ..operator import Operator


class PropertyOperator(Operator):
    """
    Asserts if a given object has property or properties.

    Example::

        class Foo(object):
            bar = 'foo'

            def baz():
                pass

        # Should style
        Foo() | should.have.property('bar')
        Foo() | should.have.properties('bar', 'baz')
        Foo() | should.have.properties.present.equal.to('bar', 'baz')

        # Should style - negation form
        Foo() | expect.to_not.have.property('bar')
        Foo() | expect.to_not.have.properties('bar', 'baz')
        Foo() | expect.to_not.have.properties.present.equal.to('bar', 'baz')

        # Expect style
        Foo() | expect.to.have.property('bar')
        Foo() | expect.to.have.properties('bar', 'baz')
        Foo() | expect.to.have.properties.present.equal.to('bar', 'baz')

        # Expect style - negation form
        Foo() | expect.to_not.have.property('bar')
        Foo() | expect.to_not.have.properties('bar', 'baz')
        Foo() | expect.to_not.have.properties.present.equal.to('bar', 'baz')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Disable diff report
    show_diff = False

    # Operator keywords
    operators = ('properties', 'property', 'attribute', 'attributes')

    # Operator chain aliases
    aliases = ('present', 'equal', 'to')

    # Expected template message
    expected_message = Operator.Dsl.Message(
        'an object that has the following properties "{value}"',
        'an object that has not the following properties "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with data "{value}"',
    )

    LIST_TYPES = (tuple, list, set, array)

    def after_success(self, obj, *keys):
        if self.ctx.negate:
            return

        if len(keys) == 1 and isinstance(keys[0], self.LIST_TYPES):
            keys = list(keys[0])

        self.ctx.subject = [getattr(obj, x) for x in keys]

        if len(keys) == 1 and len(self.ctx.subject):
            self.ctx.subject = self.ctx.subject[0]

    def match(self, subject, *keys):
        reasons = []

        if len(keys) == 1 and isinstance(keys[0], self.LIST_TYPES):
            keys = list(keys[0])

        for name in keys:
            if hasattr(subject, name):
                has_property = True
                reason = 'property {0!r} found'.format(name)
            else:
                has_property = False
                reason = 'property {0!r} not found'.format(name)

            if not has_property:
                return False, [reason]

            reasons.append(reason)

        return True, reasons
