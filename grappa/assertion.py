# -*- coding: utf-8 -*-
from .base import BaseTest


class AssertionProxy(BaseTest):
    """
    AssertionProxy is used as proxy delegator call chain for test
    definitions.
    """

    def __init__(self, resolver, operator, fn):
        self._called = False
        self._accessed = False
        self._fn = fn
        self._op = operator
        self._resolver = resolver
        self._test = resolver.test

    def __call__(self, expected, *args, **kw):
        if self._called:
            raise RuntimeError('grappa: operator already called')
        if not self._called:
            self._called = True

        __tracebackhide__ = True
        return self._fn(expected, *args, **kw)

    def _match_alias(self, name):
        return hasattr(self._op, 'aliases') and name in self._op.aliases

    def _match_suboperator(self, name):
        def create(operator):
            return self._resolver.run_matcher(operator(self._test._ctx))

        # Check that operator has suboperators
        if not getattr(self._op, 'suboperators', None):
            return False

        # Match parent operators
        for op in self._op.suboperators:
            # Match suboperator names ignoring first words
            for opname in op.operators:
                if name == opname:
                    return create(op)
                if '_' in opname and name == '_'.join(opname.split('_')[1:]):
                    return create(op)

    def _on_access(self):
        # Define on_access operator function
        def on_access(subject):
            try:
                self._op.on_access(subject)
            finally:
                return True

        # Add assertion function
        self._test._engine.add_assertion(on_access)

        # Flag proxy state as accessed operator
        self._accessed = True

    def is_on_access(self):
        # Trigger operator on_access operator event method, if available
        return hasattr(self._op, 'on_access') and not self._accessed

    def __getattr__(self, name):
        """
        Overloads attribute accessor in order to load the assertion
        operator dynamically.
        """
        # Match operator aliases for chaining
        if self._match_alias(name):
            self._test._engine.add_keyword(name)
            return self

        # Trigger operator on_access operator event method, if available
        if self.is_on_access():
            self._on_access()

        # Match suboperator, if needed
        suboperator = self._match_suboperator(name)
        if suboperator:
            # Register keyword for suboperator
            self._test._engine.add_keyword(name)

            # Trigger suboperator on_access event method, if available
            if suboperator.is_on_access():
                suboperator._on_access()

            # Return suboperator proxy
            return suboperator

        # Delegate access to global assertion instance
        return getattr(self._test, name)

    def __ror__(self, value):
        """
        Overloads ``|`` operator.
        """
        return self._fn(value)._trigger()

    def __gt__(self, value):
        """
        Overloads ``>`` operator.
        """
        return self.__ror_(value)
