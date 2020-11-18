# -*- coding: utf-8 -*-
from six.moves import collections_abc

from ..operator import Operator


class KeysOperator(Operator):
    """
    Asserts that a given dictionary has a key or keys.

    Example::

        # Should style
        {'foo': True} | should.have.key('foo')
        {'foo': True, 'bar': False} | should.have.keys('bar', 'foo')

        # Should style - negation form
        {'bar': True} | should.not_have.key('foo')
        {'baz': True, 'bar': False} | should.not_have.keys('bar', 'foo')

        # Expect style
        {'foo': True} | expect.to.have.key('foo')
        {'foo': True, 'bar': False} | expect.to.have.keys('bar', 'foo')

        # Expect style - negation form
        {'bar': True} | expect.to_not.have.key('foo')
        {'baz': True, 'bar': False} | expect.to_not.have.keys('bar', 'foo')
    """

    # Is the operator a keyword
    kind = Operator.Type.MATCHER

    # Operator keywords
    operators = ('keys', 'key',)

    # Operator chain aliases
    aliases = ('present', 'equal', 'to')

    # Expected message templates
    expected_message = Operator.Dsl.Message(
        'a dictionary-like object that has the key(s) "{value}"',
        'a dictionary-like object that has not the key(s) "{value}"',
    )

    # Subject template message
    subject_message = Operator.Dsl.Message(
        'an object of type "{type}" with value "{value}"',
    )

    def after_success(self, obj, *keys):
        if not self.ctx.negate:
            self.ctx.subject = [obj[x] for x in obj if x in keys]

        if len(keys) == 1 and len(self.ctx.subject):
            if isinstance(self.ctx.subject, list):
                self.ctx.subject = self.ctx.subject[0]
            else:
                self.ctx.subject = list(self.ctx.subject.keys())[0]

    def match(self, subject, *keys):
        if not isinstance(subject, collections_abc.Mapping):
            return False, ['subject is not a dict type']

        reasons = []

        if isinstance(keys[0], tuple) or isinstance(keys[0], list) or isinstance(keys[0], set):
            keys = list(keys[0])

        for name in keys:
            if name in subject:
                has_key = True
                reason = 'key {0!r} found'.format(name)
            else:
                has_key = False
                reason = 'key {0!r} not found'.format(name)

            if not has_key:
                return False, [reason]

            reasons.append(reason)

        return True, reasons
