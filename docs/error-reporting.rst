Error reporting
===============

Feedback while testing is key. Seeing errors in your tests is not a nice thing
because informs you something is wrong with your code.
This can even introduce frustration and FUD to developers.

``grappa`` provides a detailed and **human friendly** behavior-oriented error reporting
to intuitively and effectively help the developer answer the following questions:

- what test failed
- what are the reasons of the failure
- what we expect to pass the test
- what we got instead
- where the error actually is (with embedded code)
- how to solve the error
- additional information about the how the assertion works


Standard errors vs grappa errors
--------------------------------

A typical assertion error report using ``nosetests``:

.. code-block:: python

    def test_native_assertion():
        x = [1, 2, 3]
        assert len(x) > 3

.. code-block:: bash

    ======================================================================
    FAIL: tests.should_test.test_should_api
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File ".pyenv/versions/3.6.0/lib/python3.6/site-packages/nose/case.py", line 198, in runTest
    self.test(*self.arg)
    File "grappa/tests/should_test.py", line 11, in test_should_api
    assert len(x) > 3
    AssertionError

Now, a ``grappa`` error report using ``nosetests``:

.. code-block:: python

    def test_grappa_assertion():
        x = [1, 2, 3]
        x | should.be.have.length.of(4)


.. code-block:: bash

    ======================================================================
    FAIL: tests.should_test.test_grappa_assert
    ----------------------------------------------------------------------
    Traceback (most recent call last):
    File ".pyenv/versions/3.6.0/lib/python3.6/site-packages/nose/case.py", line 198, in runTest
    self.test(*self.arg)
    File "grappa/tests/should_test.py", line 16, in test_grappa_assert
    x | should.be.have.length.of(4)
    AssertionError: The following assertion was not satisfied
    subject "[1, 2, 3]" should be have length of "4"

    Reasons
    ▸ unexpected object length: 3

    What we expected
    an object that can be length measured and its length is equal to 4

    What we got instead
    an object of type "list" with length 3

    Information
    ▸ An empty object is typically tested via "len(x)"
      built-in function. Most built-in types and objects in Python
      can be tested that way, such as str, list, generator...
      as well as any object that implements "__len__()" method
      and returns "0" as length.
      — Reference: https://docs.python.org/3/library/functions.html#len

    Where
    File "grappa/tests/should_test.py", line 16, in test_grappa_assert

     8|
     9|  def test_native_assert():
    10|      x = [1, 2, 3]
    11|      assert len(x) == 4
    12|
    13|
    14|  def test_grappa_assert():
    15|      x = [1, 2, 3]
    16| >    x | should.be.have.length.of(4)
    17|
    18|
    19|  def test_bool():
    20|      True | should.be.true | should.be.present
    21|      False | should.be.false | should.be.equal.to(False)
    22|      False | should.be.false | should.not_be.equal.to(True)

Error behavior
--------------

``grappa`` raises an standard ``AssertionError`` exception when an assertion is not satisfied,
with some additional properties that provides context data from ``grappa`` for further debugging.

Additional error properties:

- **__grappa__** ``bool`` - Error flag that indicates the error was originated by ``grappa``.
- **__cause__** ``Exception`` - Original exception error, if any. Python >= 3.5 uses this property to enhance traceback.
- **context** ``grappa.Context`` - Current test ``grappa`` context instance. Only for low-level debugging.


Custom error messages
---------------------

You can include arbitrary custom messages that would be included in the error report providing additional context information.

.. code-block:: python

    'foo' | should.be.equal('bar', msg='additional error message')

    expect('foo').to.equal('bar', msg='additional error message')
