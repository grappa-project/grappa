# -*- coding: utf-8 -*-
from ..decorators import attribute


@attribute(
    operators=(
        'to', 'has', 'have', 'satisfy', 'that', 'that_is',
        'satisfies', 'include', 'do', '_is', 'which', 'which_is'
    )
)
def be(ctx):
    """
    Semantic attributes providing chainable declarative DSL
    for assertions.
    """
    pass


@attribute(operators=(
    'not_to', 'to_not', 'does_not', 'do_not', '_not', 'not_satisfy',
    'not_have', 'not_has', 'have_not', 'has_not', 'dont', 'is_not',
    'which_not', 'that_not'
))
def not_be(ctx):
    """
    Semantic negation attributes providing chainable declarative DSL
    for assertions.
    """
    ctx.negate = True
