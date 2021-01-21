Assertion styles
================

``grappa`` is a behavior-oriented library that comes in two flavors: ``expect`` and ``should``.

Both use the same chainable language to construct assertions, but they differ
in the way an assertion is initially constructed by the use of different operators DSL.

The BDD style is exposed through ``expect`` or ``should`` interfaces.
In both scenarios, you chain together natural language assertions.


should
------

The should style allows for the same chainable assertions as the ``expect`` interface,
however it extends each object with a should property to start your chain.

.. code-block:: python

    from grappa import should

    foo = 'bar'
    beverages = { 'tea': [ 'grappa', 'matcha', 'long' ] }

    foo | should.be.a('string')
    foo | should.equal('bar')
    foo | should.have.length.of(3)
    beverages | should.have.property('tea').with.length.of(3)


.. note::

    ``should`` can be used as a function like how the ``expect`` verb is usually used.

    .. code-block:: python

        should(foo).be.a('string')
        should('foo').to.be.equal('foo')
        should('foo').have.length.of(3)
        should(beverages).have.property('tea').with.length.of(3)


.. tip::

    For this assertion style, accessors and matchers operators will raise ``pylint``
    warnings that can be disabled with these comments.

    To ignore rules for the whole module place them before ``import`` statements.

    .. code-block:: python

        True | should.be.true  # pylint: disable=W0104
        True | should.be.true  # pylint: disable=pointless-statement

        True | should.equal(True)  # pylint: disable=W0106
        True | should.equal(True)  # pylint: disable=expression-not-assigned

expect
------

.. code-block:: python

    from grappa import expect

    foo = 'bar'
    beverages = { 'tea': [ 'grappa', 'matcha', 'long' ] }

    expect(foo).to.be.a('string')
    expect(foo).to.equal('bar')
    expect(foo).to.have.length.of(3)
    expect(beverages).to.have.property('tea').that.has.length.of(3)


.. note::

    ``expect`` can be used with piping operator like how the ``should`` verb is usually used.

    .. code-block:: python

        foo | expect.to.be.a('string')
        foo | expect.to.equal('bar')
        foo | expect.to.have.length.of(3)
        beverages | expect.to.have.property('tea').that.has.length.of(3)


.. tip::

    For this assertion style, accessors operators will raise ``pylint``
    warnings that can be disabled with these comments.

    To ignore rules for the whole module place them before ``import`` statements.

    .. code-block:: python

        expect(True).to.be.true  # pylint: disable=W0106
        expect(True).to.be.true  # pylint: disable=expression-not-assigned

