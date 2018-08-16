"""Test tableau.py."""

import pytest
from ot.tableau import Tableau
from ot.constraints import ConstraintSet
from ot.gen import Gen


@pytest.fixture
def gen():
    """Set up Gen object as a fixture."""
    yield Gen()


@pytest.fixture
def tableau_concat_suffix(gen):
    """Set up a Tableau, which should yield suffixing residue, as a fixture."""
    inputs = (('C1', 'C2', 'V3'), ('V4', 'C5'))
    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "contiguity",
            "align_left_root",
            "align_right_residue",
            "align_left_residue",
            "align_right_root",
            "c_adj_v",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_concat_suffix(tableau_concat_suffix):
    """Test with a tableau that should yield suffixing residue."""
    assert tableau_concat_suffix.winners == [('C1', 'C2', 'V3', 'V4', 'C5')]
    assert tableau_concat_suffix.typology == 'concat_suffix'
    # assert tableau_concat.violations() for a couple of candidates
    print('\n')
    print(tableau_concat_suffix.typology)
    print(tableau_concat_suffix)


@pytest.fixture
def tableau_concat_prefix(gen):
    """Set up a Tableau, which should yield prefixing residue, as a fixture."""
    inputs = (('C1', 'C2', 'V3'), ('V4', 'C5'))
    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "contiguity",
            "align_left_residue",
            "align_right_root",
            "align_left_root",
            "align_right_residue",
            "c_adj_v",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_concat_prefix(tableau_concat_prefix):
    """Test with a tableau that should yield prefixing residue."""
    assert tableau_concat_prefix.winners == [('V4', 'C5', 'C1', 'C2', 'V3')]
    assert tableau_concat_prefix.typology == 'concat_prefix'
    print('\n')
    print(tableau_concat_prefix.typology)
    print(tableau_concat_prefix)


@pytest.fixture
def tableau_arabic_like(gen):
    """Set up a Tableau, which should yield Arabic-like interleaving."""
    inputs = (('C1', 'C2', 'C3'), ('V4', 'V5'))
    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "c_adj_v",
            "align_left_root",
            "align_right_root",
            "align_left_residue",
            "align_right_residue",
            "contiguity",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_arabic_like(tableau_arabic_like):
    """Test with a tableau that should yield concatenativity."""
    assert tableau_arabic_like.winners == [('C1', 'V4', 'C2', 'V5', 'C3')]
    assert tableau_arabic_like.typology == 'nonconcat_cv'
    print('\n')
    print(tableau_arabic_like.typology)
    print(tableau_arabic_like)


@pytest.fixture
def tableau_infixing(gen):
    """Set up a Tableau that should yield infixing."""
    inputs = (('C1', 'C2', 'V3'), ('V4', 'C5'))
    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "c_adj_v",
            "align_left_root",
            "align_right_root",
            "align_left_residue",
            "contiguity",
            "align_right_residue",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_infixing(tableau_infixing):
    """Test with a tableau that should result in an infixing result."""
    assert tableau_infixing.winners == [('C1', 'V4', 'C5', 'C2', 'V3')]
    assert tableau_infixing.typology == 'infix'
    print('\n')
    print(tableau_infixing.typology)
    print(tableau_infixing)


@pytest.fixture
def tableau_unattested(gen):
    """Set up a Tableau that should yield an unattested result."""
    inputs = (('C1', 'C2', 'V3'), ('V4', 'C5'))
    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "c_adj_v",
            "align_left_root",
            "align_right_residue",
            "align_left_residue",
            "align_right_root",
            "contiguity",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_unattested(tableau_unattested):
    """Test with a tableau that should result in an unattested result."""
    assert tableau_unattested.winners == [('C1', 'V4', 'C2', 'V3', 'C5')]
    assert tableau_unattested.typology == 'unattested'
    print('\n')
    print(tableau_unattested.typology)
    print(tableau_unattested)


@pytest.fixture
def tableau_multiple(gen):
    """Set up a Tableau that should yield multiple winners."""
    inputs = (('V1', 'C2', 'V3'), ('C4', 'C5'))
    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "align_left_root",
            "align_right_residue",
            "align_right_root",
            "c_adj_v",
            "contiguity",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_multiple(tableau_multiple):
    """Test with a tableau that should result in multiple winners."""
    assert(set(tableau_multiple.winners) ==
           set([('V1', 'C4', 'C2', 'V3', 'C5'),
                ('V1', 'C2', 'C4', 'V3', 'C5')]))
    assert tableau_multiple.typology == 'unattested'
    print('\n')
    print(tableau_multiple.typology)
    print(tableau_multiple)


@pytest.fixture
def tableau_anchor_unattested(gen):
    """Set up a Tableau with ANCHOR constraints that should yield an unattested result."""
    inputs = (('C1', 'C2', 'V3'), ('V4', 'C5'))
    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "anchor_right_residue",
            "anchor_left_root",
            "anchor_right_root",
            "anchor_left_residue",
            "c_adj_v",
            "contiguity",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_anchor_unattested(tableau_anchor_unattested):
    """Test with a tableau that should result in an unattested result."""
    assert tableau_anchor_unattested.winners == [('C1', 'V4', 'C2', 'V3', 'C5')]
    assert tableau_anchor_unattested.typology == 'unattested'
    print('\n')
    print(tableau_anchor_unattested.typology)
    print(tableau_anchor_unattested)


@pytest.fixture
def tableau_anchor_multiple(gen):
    """
    Set up a Tableau that should yield an unattested result.

    Also uses the ANCHOR constraints.
    """
    inputs = (('V1', 'C2', 'V3'), ('C4', 'C5'))

    yield Tableau(
        inputs=inputs,
        ranked_constraints=ConstraintSet([
            "c_adj_v",
            "anchor_left_root",
            "contiguity",
            "anchor_left_residue",
            "anchor_right_root",
            "anchor_right_residue",
        ]),
        candidates=gen.candidates(inputs)
    )


def test_tableau_anchor_multiple(tableau_anchor_multiple):
    """Test with a tableau with ANCHOR constraints and multiple winners."""
    assert(set(tableau_anchor_multiple.winners) ==
           set([('V1', 'C4', 'C2', 'V3', 'C5'),
                ('V1', 'C2', 'C4', 'V3', 'C5')]))
    assert tableau_anchor_multiple.typology == 'unattested'
    print('\n')
    print(tableau_anchor_multiple.typology)
    print(tableau_anchor_multiple)
