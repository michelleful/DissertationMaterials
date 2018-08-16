"""Test constraints.py."""

import pytest
from ot.constraints import ConstraintSet


@pytest.fixture
def constraint_set():
    """Set up the ConstraintSet object as a fixture."""
    yield ConstraintSet()


def test_c_adj_v(constraint_set):
    """Test the C//V constraint."""
    assert constraint_set.c_adj_v(('C1', 'C2', 'C3')) == 3
    assert constraint_set.c_adj_v(('V1', 'V2', 'V3')) == 0
    assert constraint_set.c_adj_v(('C2', 'V1', 'C3')) == 0
    assert constraint_set.c_adj_v(('V5', 'C6', 'V7')) == 0
    assert constraint_set.c_adj_v(('V1', 'V2', 'C1', 'C2')) == 1
    assert constraint_set.c_adj_v(('C1', 'C2', 'C3', 'V1', 'V2')) == 2


def test_align_left_root(constraint_set):
    """Test the Align-Root-Left constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.align_left_root(('C1', 'V1', 'C2', 'C3', 'V2'),
                                          inputs) == 0
    assert constraint_set.align_left_root(('C3', 'V2', 'C1', 'V1', 'C2'),
                                          inputs) == 2
    assert constraint_set.align_left_root(('C3', 'C1', 'V2', 'V1', 'C2'),
                                          inputs) == 1


def test_align_left_residue(constraint_set):
    """Test the Align-Residue-Left constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.align_left_residue(('C1', 'V1', 'C2', 'C3', 'V2'),
                                             inputs) == 3
    assert constraint_set.align_left_residue(('C3', 'V2', 'C1', 'V1', 'C2'),
                                             inputs) == 0


def test_align_right_root(constraint_set):
    """Test the Align-Root-Right constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.align_right_root(('C1', 'V1', 'C2', 'C3', 'V2'),
                                           inputs) == 2
    assert constraint_set.align_right_root(('C3', 'V2', 'C1', 'V1', 'C2'),
                                           inputs) == 0


def test_align_right_residue(constraint_set):
    """Test the Align-Residue-Right constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.align_right_residue(('C1', 'V1', 'C2', 'C3', 'V2'),
                                              inputs) == 0
    assert constraint_set.align_right_residue(('C3', 'V2', 'C1', 'V1', 'C2'),
                                              inputs) == 3


def test_anchor_left_root(constraint_set):
    """Test the Anchor-Root-Left constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.anchor_left_root(('C1', 'V1', 'C2', 'C3', 'V2'),
                                           inputs) == 0
    assert constraint_set.anchor_left_root(('C3', 'V2', 'C1', 'V1', 'C2'),
                                           inputs) == 1
    assert constraint_set.anchor_left_root(('C3', 'C1', 'V2', 'V1', 'C2'),
                                           inputs) == 1


def test_anchor_left_residue(constraint_set):
    """Test the Anchor-Residue-Left constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.anchor_left_residue(('C1', 'V1', 'C2', 'C3', 'V2'),
                                              inputs) == 1
    assert constraint_set.anchor_left_residue(('C3', 'V2', 'C1', 'V1', 'C2'),
                                              inputs) == 0


def test_anchor_right_root(constraint_set):
    """Test the Anchor-Root-Right constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.anchor_right_root(('C1', 'V1', 'C2', 'C3', 'V2'),
                                            inputs) == 1
    assert constraint_set.anchor_right_root(('C3', 'V2', 'C1', 'V1', 'C2'),
                                            inputs) == 0


def test_anchor_right_residue(constraint_set):
    """Test the Anchor-Residue-Right constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.anchor_right_residue(('C1', 'V1', 'C2', 'C3', 'V2'),
                                               inputs) == 0
    assert constraint_set.anchor_right_residue(('C3', 'V2', 'C1', 'V1', 'C2'),
                                               inputs) == 1


def test_contiguity(constraint_set):
    """Test the CONTIGUITY constraint."""
    inputs = (('C1', 'V1', 'C2'), ('C3', 'V2'))
    assert constraint_set.contiguity(('C1', 'V1', 'C2', 'C3', 'V2'),
                                     inputs) == 0
    assert constraint_set.contiguity(('C1', 'V1', 'C3', 'C2', 'V2'),
                                     inputs) == 2
    assert constraint_set.contiguity(('C3', 'V2', 'C1', 'V1', 'C2'),
                                     inputs) == 0
    assert constraint_set.contiguity(('C1', 'C3', 'V1', 'V2', 'C2'),
                                     inputs) == 3
