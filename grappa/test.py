# -*- coding: utf-8 -*-
from .log import log
from .empty import empty
from .base import BaseTest
from .engine import Engine
from .context import Context
from .resolver import OperatorResolver


class Test(BaseTest):
    """
    Test represents the test definition in `grappa` with extensible and
    dynamic, runtime inferred DSL based on registered operators and
    third-party plugins.

    Arguments:
        subject (mixed): subject value to test.
    """

    # Tracks context manager scopes
    _context = 0

    # Tracks yielded value by context manager
    _context_subject = empty

    # Global flag, only used by global singleton instance
    _global = False

    def __init__(self, subject=empty):
        self._engine = Engine()
        self._ctx = Context()
        self._ctx.subjects = []
        self._ctx.subject = subject
        self._ctx.chained = False
        self._ctx.style = 'should'

    @property
    def should(self):
        """
        Alias name to self reference the current instance.
        Required for DSL API.
        """
        return self

    @property
    def expect(self):
        """
        Alias name to self reference the current instance.
        Required for DSL API.
        """
        return self

    @property
    def _root(self):
        return test

    def __call__(self, subject, overload=False):
        """
        Overloads function invokation of `Test` class instance.

        This is magical and widely used in `grappa` test execution by both
        developers and internal engine.

        Arguments:
            subject (mixed): test subject to use.
            overload (bool): `True` if the call if triggered via operator
                overloading invokation, otherise `False`.

        Returns:
            grappa.Test: new test instance with the given subject.
        """
        self._ctx.subject = subject

        __tracebackhide__ = True
        return self._trigger() if overload else Test(subject)

    def __getattr__(self, name):
        """
        Overloads class attribute accessor proxying calls dynamically
        into assertion operators calls.

        This method is invoked by Python runtime engine, not by developers.
        """
        # Return a new test instance if running as global
        if self._global:
            # If using context manager, use context defined subject
            subject = self._context_subject if self._context else empty
            # Create new test and proxy attribute call
            return Test(subject).__getattr__(name)

        # Resolve and register operator by name
        __tracebackhide__ = True
        return OperatorResolver(self).resolve(name)

    def _trigger(self):
        """
        Trigger assertions in the current test engine.

        Raises:
            AssertionError: in case of assertion error.
            Exception: in case of any other assertion error.
        """
        log.debug('[test] trigger with context: {}'.format(self._ctx))

        try:
            err = self._engine.run(self._ctx)
        except Exception as _err:
            err = _err
        finally:
            # Important: reset engine state to defaults
            self._engine.reset()
            self._root._engine.reset()

        # If error is present, raise it!
        if err:
            __tracebackhide__ = True
            raise err

        return self

    def _clone(self):
        """
        Clones the current `Test` instance.

        Returns:
            grappa.Test
        """
        test = Test(self._ctx.subject)
        test._ctx = self._ctx.clone()
        test._engine = self._engine.clone()
        return test

    def _flush(self):
        """
        Flushes the current test state, including test engine, assertions and
        current context.
        """
        self.__init__()

    # Assertions composition
    def all(self, *tests):
        """
        Composes multiple tests and executes them, in series, once a
        subject is received.

        Conditional composition operator equivalent to `all` built-in
        Python function.

        Arguments:
            *tests (grappa.Test): test instances to run.
        """
        def run_tests(subject):
            for test in tests:
                try:
                    test(subject, overload=True)
                except Exception as err:
                    return err
            return True
        self._engine.add_assertion(run_tests)
        return self

    def any(self, *tests):
        """
        Composes multiple tests and executes them, in series, once a
        subject is received.

        Conditional composition operator equivalent to `any` built-in
        Python function.

        Arguments:
            *tests (grappa.Test): test instances to run.
        """
        def run_tests(subject):
            err = None
            for test in tests:
                try:
                    test(subject, overload=True)
                except Exception as _err:
                    err = _err
                else:
                    return True
            return err

        self._engine.add_assertion(run_tests)
        return self

    def __overload__(self, subject):
        """
        Method triggered by magic methods executed via operator overloading.
        """
        if isinstance(subject, Test):
            # Clone test instance to make it side-effects free
            fork = subject._clone()
            fork._ctx.chained = True
            fork._ctx.subject = self._ctx.subject
            # Trigger assertions

            __tracebackhide__ = True
            return fork._trigger()

        # Otherwise invoke the test function with a subject
        __tracebackhide__ = True
        return self.__call__(subject, overload=True)

    def __or__(self, value):
        """
        Overloads ``|`` as from left-to-right operator precedence expression.
        """
        __tracebackhide__ = True
        return self.__overload__(value)

    def __ror__(self, value):
        """
        Overloads ``|`` operator.
        """
        __tracebackhide__ = True
        return self.__overload__(value)

    def __gt__(self, value):
        """
        Overloads ``>`` operator.
        """
        __tracebackhide__ = True
        return self.__overload__(value)

    def __enter__(self):
        """
        Initializes context manager.
        """
        log.debug('creates new test context manager: {}'.format(self._ctx))
        test._context += 1
        test._context_subject = self._ctx.subject

    def __exit__(self, etype, value, traceback):
        """
        Exists context manager.
        """
        log.debug('exists test context manager: {}'.format(value))
        test._context -= 1

        if test._context == 0:
            test._context_subject = empty


# Create global singleton instance
test = Test()

# This is black magic in order to deal with chainable states
# and operator precedence.
test._global = True
