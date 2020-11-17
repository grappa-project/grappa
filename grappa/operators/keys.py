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
        self.ctx.subject = [obj[x] for x in obj if x in keys]

    def match(self, subject, *keys, **kw):
        if self._not_a_dict(subject):
            return False, ['subject is not a dict type']
        return self._matches(subject, (keys, kw))

    def _not_a_dict(self, value):
        return not isinstance(value, collections_abc.Mapping)

    def _matches(self, subject, expected):
        args, kwargs = expected

        reasons = []
        for name in args:
            has_key, reason = self._has_key(subject, name)
            if not has_key:
                return False, [reason]
            else:
                reasons.append(reason)

        for name, value in kwargs.items():
            has_key, reason = self._has_key(subject, name, value)
            if not has_key:
                return False, [reason]
            else:
                reasons.append(reason)

        return True, reasons

    def _has_key(self, subject, name, *args):
        if args:
            expected_value = args[0]

            try:
                value = subject[name]
            except KeyError:
                return False, 'key {0!r} {1!r} not found'.format(
                    name, expected_value)
            else:
                result, _ = expected_value._match(value)
                reason_message = 'not found' if not result else 'found'
                return result, 'key {0!r} {1!r} {2}'.format(
                    name, expected_value, reason_message)

        if name in subject:
            return True, 'key {0!r} found'.format(name)

        return False, 'key {0!r} not found'.format(name)
