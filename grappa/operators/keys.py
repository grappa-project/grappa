# -*- coding: utf-8 -*-
from array import array
from six.moves import collections_abc

from ..operator import Operator


class KeysOperator(Operator):
    """
    Asserts that a given dictionary has a key or keys.

    Example::

        # Should style
        {'foo': True} | should.have.key('foo')
        {'foo': True, 'bar': False} | should.have.keys('bar', 'foo')
        {'foo': True, 'bar': False} | should.have.keys(('bar', 'foo'))
        {'foo': True, 'bar': False} | should.have.keys(['bar', 'foo'])
        {'foo': True, 'bar': False} | should.have.keys({'bar', 'foo'})
        {1: True, 2: False} | should.have.keys(array('i', [1, 2]))

        # Should style - negation form
        {'bar': True} | should.not_have.key('foo')
        {'baz': True, 'bar': False} | should.not_have.keys('bar', 'foo')
        {'baz': True, 'bar': False} | should.not_have.keys(('bar', 'foo'))
        {'baz': True, 'bar': False} | should.not_have.keys(['bar', 'foo'])
        {'baz': True, 'bar': False} | should.not_have.keys({'bar', 'foo'})
        {10: True, 2: False} | should.not_have.keys(array('i', [1, 2]))

        # Expect style
        {'foo': True} | expect.to.have.key('foo')
        {'foo': True, 'bar': False} | expect.to.have.keys('bar', 'foo')
        {'foo': True, 'bar': False} | expect.to.have.keys(('bar', 'foo'))
        {'foo': True, 'bar': False} | expect.to.have.keys(['bar', 'foo'])
        {'foo': True, 'bar': False} | expect.to.have.keys({'bar', 'foo'})
        {1: True, 2: False} | expect.to.have.keys(array('i', [1, 2]))

        # Expect style - negation form
        {'bar': True} | expect.to_not.have.key('foo')
        {'baz': True, 'bar': False} | expect.to_not.have.keys('bar', 'foo')
        {'baz': True, 'bar': False} | expect.to_not.have.keys(('bar', 'foo'))
        {'baz': True, 'bar': False} | expect.to_not.have.keys(['bar', 'foo'])
        {'baz': True, 'bar': False} | expect.to_not.have.keys({'bar', 'foo'})
        {10: True, 2: False} | expect.to_not.have.keys(array('i', [1, 2]))
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

    LIST_TYPES = (tuple, list, set, array)

    def after_success(self, obj, *keys):
        if self.ctx.negate:
            return

        if len(keys) == 1 and isinstance(keys[0], self.LIST_TYPES):
            keys = list(keys[0])

        self.ctx.subject = [obj[x] for x in obj if x in keys]

        if len(keys) == 1 and len(self.ctx.subject):
            self.ctx.subject = self.ctx.subject[0]

    def match(self, subject, *keys):
        if not isinstance(subject, collections_abc.Mapping):
            return False, ['subject is not a dict type']

        reasons = []

        if len(keys) == 1 and isinstance(keys[0], self.LIST_TYPES):
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
