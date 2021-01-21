Attributes operators
====================

These operators provide positive and negative assertion logic.

They semantically describe assertions to make them more expressive.


Positive
--------

be
^^
to
^^
has
^^^
have
^^^^
do
^^
include
^^^^^^^
satisfy
^^^^^^^
satisfies
^^^^^^^^^
_is
^^^
which
^^^^^
that
^^^^
that_is
^^^^^^^
which_is
^^^^^^^^

Chainable semantic attributes which define positive assertions.

.. code-block:: python

    # should style
    'foo' | should.be.equal.to('bar')
    'foo' | should.have.length.of(3)

    {'foo': 'bar'} | should.have.key('foo').which.should.be.equal.to('bar')
    {'foo': 'bar'} | should.have.key('foo').that.should.have.length.of(3)

    # expect style
    expect('foo').to.equal.to('bar')
    expect('foo').to.have.length.of(3)

    expect({'foo': 'bar'}).to.have.key('foo').which.expect.to.be.equal('bar')
    expect({'foo': 'bar'}).to.have.key('foo').which.expect.to.have.length.of(3)


Negative
--------

not_be
^^^^^^
not_present
^^^^^^^^^^^
not_to
^^^^^^
to_not
^^^^^^
does_not
^^^^^^^^
do_not
^^^^^^
dont
^^^^
have_not
^^^^^^^^
not_have
^^^^^^^^
has_not
^^^^^^^
not_has
^^^^^^^
that_not
^^^^^^^^
which_not
^^^^^^^^^
is_not
^^^^^^
_not
^^^^
not_satisfy
^^^^^^^^^^^

Chainable semantic attributes which define negative assertions.

.. code-block:: python

    # should style
    'foo' | should.not_be.equal.to('bar')
    'foo' | should.have_not.length.of(3)

    # expect style
    expect('foo').to_not.equal.to('bar')
    expect('foo').to.not_have.length.of(3)
