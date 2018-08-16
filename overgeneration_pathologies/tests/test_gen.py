"""Test gen.py."""

import pytest
from ot.gen import Gen


@pytest.fixture
def gen():
    """Set up the Gen object as a fixture."""
    yield Gen(segments='CCCVV', root_length=3)


def test_inputs(gen):
    """Test inputs."""
    assert (('C1', 'V2', 'C3'), ('C4', 'V5')) in gen.inputs()
    assert (('C1', 'C2', 'C3'), ('V4', 'V5')) in gen.inputs()
    assert (('C1', 'C2', 'V3'), ('V4', 'C5')) in gen.inputs()


def test_candidate_presence(gen):
    """Test that select candidates are present."""
    candidates = gen.candidates((('C1', 'V2', 'C3'), ('C4', 'V5')))
    assert ('C1', 'V2', 'C3', 'C4', 'V5') in candidates
    assert ('C1', 'C4', 'V2', 'C3', 'V5') in candidates


def test_candidate_absence(gen):
    """Test that select candidates are NOT generated."""
    candidates = gen.candidates((('C1', 'V2', 'C3'), ('C4', 'V5')))
    assert ('C1', 'V2', 'C3', 'V5', 'C4') not in candidates
    assert ('V2', 'C1', 'C4', 'C3', 'V5') not in candidates
