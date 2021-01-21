Accessors operators
===================

These operators perform simple assertion logic.


true
----

Asserts if a given subject is ``True`` value.

.. code-block:: python

    # should style
    'foo' | should.be.true
    'foo' | should.not_be.true

    # expect style
    expect('foo').to.be.true
    expect('foo').to_not.be.true


false
-----

Asserts if a given subject is ``False`` value.

.. code-block:: python

    # should style
    'foo' | should.be.false
    'foo' | should.not_be.false

    # expect style
    expect('foo').to.be.false
    expect('foo').to_not.be.false


callable
--------

Asserts if a given subject is a callable type or an object that
implements ``__call__()`` magic method.

.. code-block:: python

    # should style
    (lambda x: x) | should.be.callable
    None | should.not_be.callable

    # expect style
    expect(lambda x: x).to.be.callable
    expect(None).to_not.be.callable


empty
-----

Asserts if a given subject is an empty object.

A subject is considered empty if it's ``None``, ``0`` or ``len(subject)``
is equals to ``0``.

.. code-block:: python

    # should style
    [] | should.be.empty
    [1, 2, 3] | should.not_be.empty

    # expect style
    expect(tuple()).to.be.empty
    expect((1, 2, 3)).to_not.be.empty   


none
----

Asserts if a given subject is ``None``.

.. code-block:: python

    # should style
    None | should.be.none
    'foo' | should.not_be.none

    # expect style
    expect(None).to.be.none
    expect('foo').to_not.be.none


exists
------
present
-------

Asserts if a given subject is not ``None`` or a negative value
if evaluated via logical unary operator.

This operator is the opposite of empty_.

.. code-block:: python

    # should style
    'foo' | should.be.present
    '' | should.not_be.present

    # expect style
    expect('foo').to.be.present
    expect(False).to_not.be.present
