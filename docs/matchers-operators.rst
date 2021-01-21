Matchers operators
==================

These operators use expectation arguments to perform their assertion logic.


Generic
-------

equal
^^^^^
same
^^^^

Performs a strict equality comparison between ``x`` and ``y`` values.

Uses ``==`` built-in binary operator for the comparison.

=======================  ========================
 **Chainable aliases**   ``value`` ``to`` ``of`` ``as`` ``data``
=======================  ========================

.. code-block:: python

    # should style
    'foo' | should.be.equal('foo')
    'foo' | should.be.equal.to('foo')
    'foo' | should.be.equal.to.value('foo')

    'foo' | should.not_be.equal.to.value('foo')

    # expect style
    expect('foo').to.equal('foo')
    expect('foo').to.equal.to('foo')
    expect('foo').to.equal.to.value('foo')
    
    expect('foo').to_not.equal.to.value('foo')


contain
^^^^^^^
contains
^^^^^^^^
includes
^^^^^^^^

Asserts if a given value or values can be found in a another object.

=======================  ========================
 **Chainable aliases**   ``value`` ``string`` ``text`` ``item`` ``expression`` ``data``
=======================  ========================

.. code-block:: python

    # should style
    'foo bar' | should.contain('bar')
    ['foo', 'bar'] | should.contain('bar')
    ['foo', 'bar'] | should.contain('foo', 'bar')
    [{'foo': True}, 'bar'] | should.contain({'foo': True})

    'foo bar' | should.do_not.contain('bar')
    ['foo', 'bar'] | should.do_not.contain('baz')

    # expect style
    expect('foo bar').to.contain('bar')
    expect(['foo', 'bar']).to.contain('bar')
    expect(['foo', 'bar']).to.contain('foo', 'bar')
    expect([{'foo': True}, 'bar']).to.contain({'foo': True})

    expect('foo bar').to_not.contain('bar')
    expect(['foo', 'bar']).to_not.contain('baz')


length
^^^^^^
size
^^^^

Asserts that a given object has exact length.

=======================  ========================
 **Chainable aliases**   ``of`` ``equal`` ``to``
=======================  ========================

.. code-block:: python

    # should style
    'foo' | should.have.length(3)
    [1, 2, 3] | should.have.length.of(3)
    iter([1, 2, 3]) | should.have.length.equal.to(3)

    'foobar' | should.not_have.length(3)
    [1, 2, 3, 4] | should.not_have.length.of(3)
    iter([1, 2, 3, 4]) | should.not_have.length.equal.to(3)

    # expect style
    expect('foo').to.have.length(3)
    expect([1, 2, 3]).to.have.length.of(3)
    expect(iter([1, 2, 3])).to.have.length.equal.to(3)

    expect('foobar').to_not.have.length(3)
    expect([1, 2, 3, 4]).to_not.have.length.of(3)
    expect(iter([1, 2, 3, 4])).to_not.have.length.equal.to(3)


start_with
^^^^^^^^^^
starts_with
^^^^^^^^^^^

Asserts if a given value starts with a specific items.

=======================  ========================
 **Chainable aliases**   ``by`` ``word`` ``number`` ``numbers`` ``item`` ``items`` ``value`` ``char`` ``letter`` ``character``
=======================  ========================

.. code-block:: python

    # should style
    'foo' | should.start_with('f')
    'foo' | should.start_with('fo')
    [1, 2, 3] | should.start_with.number(1)
    iter([1, 2, 3]) | should.start_with.numbers(1, 2)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.start_with.item('foo')

    'foo' | should.do_not.start_with('o')
    'foo' | should.do_not.start_with('o')
    [1, 2, 3] | should.do_not.start_with(2)
    iter([1, 2, 3]) | should.do_not.start_with.numbers(3, 4)
    OrderedDict([('foo', 0), ('bar', 1)]) | should._not.start_with('bar')

    # expect style
    expect('foo').to.start_with('f')
    expect('foo').to.start_with('fo')
    expect([1, 2, 3]).to.start_with.number(1)
    expect(iter([1, 2, 3])).to.start_with.numbers(1, 2)
    expect(OrderedDict([('foo', 0), ('bar', 1)])).to.start_with('foo')

    expect('foo').to_not.start_with('f')
    expect('foo').to_not.start_with('fo')
    expect([1, 2, 3]).to_not.start_with.number(1)
    expect(iter([1, 2, 3])).to_not.start_with.numbers(1, 2)
    expect(OrderedDict([('foo', 0), ('bar', 1)])).to_not.start_with('foo')


end_with
^^^^^^^^
ends_with
^^^^^^^^^

Asserts if a given value ends with a specific items.

=======================  ========================
 **Chainable aliases**   ``by`` ``word`` ``number`` ``numbers`` ``item`` ``items`` ``value`` ``char`` ``letter`` ``character``
=======================  ========================

**Assertion form**:

.. code-block:: python

    # should style
    'foo' | should.ends_with('o')
    'foo' | should.ends_with('oo')
    [1, 2, 3] | should.ends_with.number(3)
    iter([1, 2, 3]) | should.ends_with.numbers(2, 3)
    OrderedDict([('foo', 0), ('bar', 1)]) | should.ends_with.item('bar')

    'foo' | should.do_not.ends_with('f')
    'foo' | should.do_not.ends_with('o')
    [1, 2, 3] | should.do_not.ends_with(2)
    iter([1, 2, 3]) | should.do_not.ends_with.numbers(3, 4)
    OrderedDict([('foo', 0), ('bar', 1)]) | should._not.ends_with('foo')

    # expect style
    expect('foo').to.ends_with('o')
    expect('foo').to.ends_with('oo')
    expect([1, 2, 3]).to.ends_with.number(3)
    expect(iter([1, 2, 3])).to.ends_with.numbers(2, 3)
    expect(OrderedDict([('foo', 0), ('bar', 1)])).to.ends_with('bar')

    expect('foo').to_not.ends_with('f')
    expect('foo').to_not.ends_with('oo')
    expect([1, 2, 3]).to_not.ends_with.number(2)
    expect(iter([1, 2, 3])).to_not.ends_with.numbers(1, 2)
    expect(OrderedDict([('foo', 0), ('bar', 1)])).to_not.ends_with('foo')


match
^^^^^
matches
^^^^^^^

Asserts if a given string matches a given regular expression.

=======================  ========================
 **Chainable aliases**   ``value`` ``string`` ``expression``, ``token``, ``to``, ``regex``, ``regexp``, ``word``, ``phrase``
=======================  ========================

.. code-block:: python

    # should style
    'hello world' | should.match(r'Hello \w+')
    'hello world' | should.match(r'hello [A-Z]+', re.I))
    'hello world' | should.match.expression(r'hello [A-Z]+', re.I))

    'hello w0rld' | should.do_not.match(r'Hello \w+')
    'hello w0rld' | should.do_not.match(r'hello [A-Z]+', re.I))
    'hello world' | should.do_not.match.expression(r'hello [A-Z]+', re.I))

    # expect style
    expect('hello world').to.match(r'Hello \w+')
    expect('hello world').to.match(r'hello [A-Z]+', re.I))
    expect('hello world').to.match.expression(r'hello [A-Z]+', re.I))

    expect('hello w0rld').to_not.match(r'Hello \w+')
    expect('hello w0rld').to_not.match(r'hello [A-Z]+', re.I))
    expect('hello world').to_not.match.expression(r'hello [A-Z]+', re.I))


Collections
-----------

key
^^^
keys
^^^^

Asserts that a given dictionary has a key or keys.

=======================  ========================
 **Chainable aliases**   ``present`` ``equal`` ``to``
-----------------------  ------------------------
 **Yields subject**      The key value, if present.
=======================  ========================

.. code-block:: python

    # should style
    {'foo': True} | should.have.key('foo')
    {'foo': True, 'bar': False} | should.have.keys('bar', 'foo')

    {'bar': True} | should.not_have.key('foo')
    {'baz': True, 'bar': False} | should.not_have.keys('bar', 'foo')

    # expect style
    expect({'foo': True}).to.have.key('foo')
    expect({'foo': True, 'bar': False}).to.have.keys('bar', 'foo')

    expect({'bar': True}).to_not.have.key('foo')
    expect({'baz': True, 'bar': False}).to_not.have.keys('bar', 'foo')


index
^^^^^

Asserts that a given iterable has an item in a specific index.

=======================  ========================
 **Chainable aliases**   ``present`` ``exists`` ``at``
-----------------------  ------------------------
 **Yields subject**      Value at the selected index, if present.
=======================  ========================

.. code-block:: python

    # should style
    [1, 2, 3] | should.have.index(2)
    [1, 2, 3] | should.have.index(1)
    [1, 2, 3] | should.have.index.at(1)
    [1, 2, 3] | should.have.index.present(1)
    [1, 2, 3] | should.have.index.at(1).equal.to(2)
    [1, 2, 3] | should.have.index.at(1) > should.be.equal.to(2)

    [1, 2, 3] | should.not_have.index(4)
    [1, 2, 3] | should.not_have.index.at(4)
    [1, 2, 3] | should.not_have.index.at(1).to_not.equal.to(5)

    # expect style
    expect([1, 2, 3]).to.have.index(2)
    expect([1, 2, 3]).to.have.index.at(1)
    expect([1, 2, 3]).to.have.index.at(1).equal.to(2)
    expect([1, 2, 3]).to.have.index.at(1) > expect.be.equal.to(2)

    expect([1, 2, 3]).to_not.have.index(2)
    expect([1, 2, 3]).to_not.have.index.at(1)
    expect([1, 2, 3]).to_not.have.index.at(1).equal.to(2)


Numbers
-------

below
^^^^^
lower
^^^^^
less
^^^^

Asserts if a given number is below to another number.

=======================  ========================
 **Chainable aliases**   ``of`` ``to`` ``than`` ``number``
=======================  ========================

.. code-block:: python

    # should style
    3 | should.be.below(5)
    3 | should.be.less.than(5)
    3 | should.be.lower.than(5)
    3 | should.be.below.to.number(5)
    3 | should.be.below.than.number(5)

    5 | should.not_be.below(3)
    3 | should.not_be.lower.than(5)
    5 | should.not_be.below.to.number(3)

    # expect style
    expect(3).to.be.below(5)
    expect(3).to.be.less.than(5)
    expect(3).to.be.lower.than(5)
    expect(3).to.be.below.to.number(5)
    expect(3).to.be.below.than.number(5)

    expect(5).to_not.be.below(3)
    expect(5).to_not.be.below.than(3)
    expect(5).to_not.be.below.to.number(3)
    expect(5).to_not.be.below.than.number(3)


above
^^^^^
higher
^^^^^^

Asserts if a given number is above to another number.

=======================  ========================
 **Chainable aliases**   ``of`` ``to`` ``than`` ``number``
=======================  ========================

.. code-block:: python

    # should style
    5 | should.be.above(3)
    5 | should.be.higher.than(3)
    5 | should.be.above.to.number(3)
    5 | should.be.above.than.number(3)

    3 | should.not_be.above(5)
    3 | should.not_be.higher.than(5)
    3 | should.not_be.above.to.number(5)
    3 | should.not_be.above.than.number(5)

    # expect style
    expect(5).to.be.above(3)
    expect(5).to.be.higher.than(3)
    expect(5).to.be.above.to.number(3)
    expect(5).to.be.above.than.number(3)

    expect(3).not_to.be.above(5)
    expect(3).not_to.be.higher.than(5)
    expect(3).not_to.be.above.to.number(5)
    expect(3).not_to.be.above.than.number(5)


least
^^^^^
above_or_equal
^^^^^^^^^^^^^^
higher_or_equal
^^^^^^^^^^^^^^^

Asserts if a given number is above to another number.

=======================  ========================
 **Chainable aliases**   ``of`` ``to`` ``than`` ``number``
=======================  ========================

.. code-block:: python

    # should style
    3 | should.be.least(3)
    3 | should.be.above_or_equal(3)
    3 | should.be.higher_or_equal.than(3)
    3 | should.be.above_or_equal.to.number(3)
    3 | should.be.above_or_equal.than.number(3)

    3 | should.not_be.least(3)
    3 | should.not_be.above_or_equal(5)
    3 | should.not_be.higher_or_equal.than(5)
    3 | should.not_be.higher_or_equal.to.number(5)
    3 | should.not_be.higher_or_equal.than.number(5)

    # expect style
    expect(3).to.be.least(3)
    expect(3).to.be.above_or_equal(3)
    expect(3).to.be.higher_or_equal.than(3)
    expect(3).to.be.above_or_equal.to.number(3)
    expect(3).to.be.above_or_equal.than.number(3)

    expect(3).not_be.least(3)
    expect(3).not_be.above_or_equal(5)
    expect(3).not_be.higher_or_equal.than(5)
    expect(3).not_be.higher_or_equal.to.number(5)
    expect(3).not_be.higher_or_equal.than.number(5)


most
^^^^
below_or_equal
^^^^^^^^^^^^^^
lower_or_equal
^^^^^^^^^^^^^^^

Asserts if a given number is above to another number.

=======================  ========================
 **Chainable aliases**   ``of`` ``to`` ``than`` ``number``
=======================  ========================

.. code-block:: python

    # should style
    3 | should.be.most(3)
    3 | should.be.below_or_equal(3)
    3 | should.be.lower_or_equal.than(3)
    3 | should.be.lower_or_equal.to.number(3)
    3 | should.be.lower_or_equal.than.number(3)

    3 | should.not_be.most(5)
    3 | should.not_be.below_or_equal(5)
    3 | should.not_be.lower_or_equal.than(5)
    3 | should.not_be.lower_or_equal.to.number(5)
    3 | should.not_be.lower_or_equal.than.number(5)

    # expect style
    expect(3).to.be.most(3)
    expect(3).to.be.below_or_equal(3)
    expect(3).to.be.lower_or_equal.than(3)
    expect(3).to.be.lower_or_equal.to.number(3)
    expect(3).to.be.lower_or_equal.than.number(3)

    expect(3).not_be.most(5)
    expect(3).not_be.below_or_equal(5)
    expect(3).not_be.lower_or_equal.than(5)
    expect(3).not_be.lower_or_equal.to.number(5)
    expect(3).not_be.lower_or_equal.than.number(5)


within
^^^^^^
between
^^^^^^^

Asserts that a number is within a range.

=======================  ========================
 **Chainable aliases**   ``to`` ``numbers`` ``range``
=======================  ========================

.. code-block:: python

    # should style
    4 | should.be.within(2, 5)
    5 | should.be.between(2, 5)
    4.5 | should.be.within(4, 5)

    4 | should.not_be.within(2, 5)
    5 | should.not_be.between(2, 5)
    4.5 | should.not_be.within(4, 5)

    # expect style
    expect(4).to.be.within(2, 5)
    expect(5).to.be.between(2, 5)
    expect(4.5).to.be.within(4, 5)

    expect(4).to_not.be.within(2, 5)
    expect(5).to_not.be.between(2, 5)
    expect(4.5).to_not.be.within(4, 5)


Objects
-------

a
^
an
^^
type
^^^^
types
^^^^^
instance
^^^^^^^^

Asserts if a given object satisfies a type.
You can use both a type alias string or a ``type`` object.

Supported type aliases:

- string
- int
- integer
- number
- object
- float
- bool
- boolean
- complex
- list
- dict
- dictionary
- tuple
- set
- array
- lambda
- generator
- asyncgenerator
- class
- method
- module
- function
- coroutine
- generatorfunction
- generator function
- coroutinefunction

=======================  ========================
 **Chainable aliases**   ``type`` ``types`` ``to`` ``of``, ``equal``
=======================  ========================

.. code-block:: python

    # should style
    1 | should.be.an('int')
    1 | should.be.an('number')
    True | should.be.a('bool')
    True | should.be.type(bool)
    'foo' | should.be.a(str)
    'foo' | should.be.a('string')
    [1, 2, 3] | should.be.a('list')
    [1, 2, 3] | should.have.type.of(list)
    (1, 2, 3) | should.be.a('tuple')
    (1, 2, 3) | should.have.type.of(tuple)
    (lamdba x: x) | should.be.a('lambda')
    'foo' | should.be.instance.of('string')
    'foo' | expect.be.types('string', 'int')

    1 | should.not_be.an('int')
    1 | should.not_be.an('number')
    True | should.not_be.a('bool')
    True | should.not_be.type(bool)
    'foo' | should.not_be.a(str)
    'foo' | should.not_be.a('string')
    [1, 2, 3] | should.not_be.a('list')
    [1, 2, 3] | should.have_not.type.of(list)
    (1, 2, 3) | should.not_be.a('tuple')
    (1, 2, 3) | should.have_not.type.of(tuple)
    (lamdba x: x) | should.not_be.a('lambda')
    'foo' | should.not_to.be.instance.of('string')
    'foo' | should.not_to.be.types('string', 'int')

    # expect style
    expect(1).to.be.an('int')
    expect(1).to.be.an('number')
    expect(True).to.be.a('bool')
    expect(True).to.be.type(bool)
    expect('foo').to.be.a(str)
    expect('foo').to.be.a('string')
    expect([1, 2, 3]).to.be.a('list')
    expect([1, 2, 3]).to.have.type.of(list)
    expect((1, 2, 3)).to.be.a('tuple')
    expect((1, 2, 3)).to.have.type.of(tuple)
    expect((lamdba x: x)).to.be.a('lambda')
    expect('foo').to.be.instance.of('string')
    expect('foo').to.be.types('string', 'int')

    expect(1).to_not.be.an('int')
    expect(1).to_not.be.an('number')
    expect(True).to_not.be.a('bool')
    expect(True).to_not.be.type(bool)
    expect('foo').to_not.be.a(str)
    expect('foo').to_not.be.a('string')
    expect([1, 2, 3]).to_not.be.a('list')
    expect([1, 2, 3]).to_not.have.type.of(list)
    expect((1, 2, 3)).to_not.be.a('tuple')
    expect((1, 2, 3)).to_not.have.type.of(tuple)
    expect((lamdba x: x)).to_not.be.a('lambda')
    expect('foo').to.not_to.be.instance.of('string')
    expect('foo').to.not_to.be.types('string', 'int')


property
^^^^^^^^^
properties
^^^^^^^^^^
attribute
^^^^^^^^^
attributes
^^^^^^^^^^

Asserts if a given object has property or properties.

=======================  ========================
 **Chainable aliases**   ``present`` ``equal`` ``to``
-----------------------  ------------------------
 **Yields subject**      The attribute value, if present.
=======================  ========================

.. code-block:: python

    # should style
    Foo() | should.have.property('bar')
    Foo() | should.have.properties('bar', 'baz')
    Foo() | should.have.properties.present.equal.to('bar', 'baz')

    Foo() | should.have_not.property('bar')
    Foo() | should.have_not.properties('bar', 'baz')
    Foo() | should.have_not.properties.present.equal.to('bar', 'baz')

    # expect style
    expect(Foo()).to_not.have.property('bar')
    expect(Foo()).to_not.have.properties('bar', 'baz')
    expect(Foo()).to_not.have.properties.present.equal.to('bar', 'baz')

    expect(Foo()).to_not.have.property('bar')
    expect(Foo()).to_not.have.properties('bar', 'baz')
    expect(Foo()).to_not.have.properties.present.equal.to('bar', 'baz')

implements
^^^^^^^^^^
implement
^^^^^^^^^
interface
^^^^^^^^^

Asserts if a given object implements an interface of methods.

=======================  ========================
 **Chainable aliases**   ``interface`` ``method`` ``methods``
=======================  ========================

.. code-block:: python

    # should style
    Foo() | should.implements('bar')
    Foo() | should.implements.method('bar')
    Foo() | should.implement.methods('bar', 'baz')
    Foo() | should.implement.interface('bar', 'baz')
    Foo() | should.satisfies.interface('bar', 'baz')

    Foo() | should.do_not.implements('bar')
    Foo() | should.do_not.implement.methods('bar', 'baz')
    Foo() | should.do_not.implement.interface('bar', 'baz')
    Foo() | should.do_not.satisfy.interface('bar', 'baz')

    # expect style
    expect(Foo()).to.implement('bar')
    expect(Foo()).to.implement.method('bar')
    expect(Foo()).to.implement.methods('bar', 'baz')
    expect(Foo()).to.implement.interface('bar', 'baz')
    expect(Foo()).to.satisfy.interface('bar', 'baz')

    expect(Foo()).to_not.implement('bar')
    expect(Foo()).to_not.implement.method('bar')
    expect(Foo()).to_not.implement.methods('bar', 'baz')
    expect(Foo()).to_not.implement.interface('bar', 'baz')
    expect(Foo()).to_not.satisfy.interface('bar', 'baz')


Exceptions
----------

raises
^^^^^^
raise_error
^^^^^^^^^^^
raises_errors
^^^^^^^^^^^^^

Asserts if a given function raises an exception. The function must be a zero
arity function (no arguments). If you need to pass arguments into your function
you can use ``functools.partial`` to create a zero arity function with your
arguments

=======================  ========================
 **Chainable aliases**   ``to`` ``that`` ``are`` ``instance`` ``of``
-----------------------  ------------------------
 **Yields subject**      Message of the exception, if present or joined exception arguments.
=======================  ========================

.. code-block:: python

    # should style
    fn | should.raise_error()
    fn | should.raise_error(ValueError)
    fn | should.raise_error(AttributeError, ValueError)
    fn | should.raise_error(ValueError) > should.equal('File not found')
    fn | should.raise_error(ValueError) > should.contain('not found')

    fn | should.do_not.raise_error()
    fn | should.do_not.raise_error(ValueError)
    fn | should.do_not.raise_error(AttributeError, ValueError)

    # expect style
    expect(fn).to.raise_error()
    expect(fn).to.raise_error(ValueError)
    expect(fn).to.raise_error(AttributeError, ValueError)
    expect(fn).to.raise_error(ValueError) > should.equal('File not found')
    expect(fn).to.raise_error(ValueError) > should.contain('not found')

    expect(fn).to_not.raise_error()
    expect(fn).to_not.raise_error(ValueError)
    expect(fn).to_not.raise_error(AttributeError, ValueError)


Predicates
----------

pass_test
^^^^^^^^^
pass_function
^^^^^^^^^^^^^

Asserts if a given subject is valid when passed to a predicate function.

=======================  ========================
 **Chainable aliases**   -
-----------------------  ------------------------
 **Optional keywords**   ``msg: str``
=======================  ========================

.. code-block:: python

    # should style
    'foo' | should.pass_test(lambda x: len(x) > 2)
    [1, 2, 3] | should.pass_function(lambda x: 2 in x)

    'foo' | should.do_not.pass_test(lambda x: len(x) > 3)
    [1, 2, 3] | should.do_not.pass_function(lambda x: 5 in x)

    # expect style
    expect('foo').to.pass_test(lambda x: len(x) > 2)
    expect([1, 2, 3]).to.pass_function(lambda x: 2 in x)

    expect('foo').to_not.pass_test(lambda x: len(x) > 3)
    expect([1, 2, 3]).to_not.pass_function(lambda x: 5 in x)

Mocks
-----

Required implementation of a mock subject is based on `unittest.mock.Mock`_ class.

To be compatible with ``grappa``, mocks must only implement:

- **called**: a boolean property which indicates whether the mock has been called, or not.
- **call_count**: an integer property which indicates the number of times the mock has been called.
- **assert_called_with(*args, **kwargs)**: a function which raises an ``AssertionError`` when the mock has not been called with given arguments.
- **assert_called_once_with(*args, **kwargs)**: a function which raises an ``AssertionError`` when the mock has not been called with given arguments.


.. warning::

    Mock matchers are not (yet) compatible with piping ``|`` assertion style.


been_called
^^^^^^^^^^^

Asserts if a given mock subject have been called at least once.

.. code-block:: python

    # expect style
    expect(mock).to.have.been_called

    expect(mock).to.have_not.been_called


been_called_once
^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called only once.

.. code-block:: python

    # expect style
    expect(mock).to.have.been_called_once

    expect(mock).to.have_not.been_called_once


been_called_times
^^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called n times.

**Assertion form**:

.. code-block:: python

    # expect style
    expect(mock).to.have.been_called_times(0)

    expect(mock).to.have_not.been_called_times(3)


been_called_with
^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called at least once
with specified arguments.

.. code-block:: python

    # expect style
    expect(mock).to.have.been_called_with('foo')
    expect(mock).to.have.been_called_with('foo', True, 150)

    expect(mock).to.have_not.been_called_with('bar', False)


been_called_once_with
^^^^^^^^^^^^^^^^^^^^^

Asserts if a given mock subject have been called only once
with specified arguments.

.. code-block:: python

    # expect style
    expect(mock).to.have.been_called_once_with('foo')
    expect(mock).to.have.been_called_once_with('foo', True, 150)

    expect(mock).to.have_not.been_called_once_with('bar', False)


.. _`unittest.mock.Mock`: https://docs.python.org/3/library/unittest.mock.html#the-mock-class
