"""Function for generating possible inputs and output candidates."""

import itertools


class Gen:
    """Generate possible inputs and output candidates."""

    def __init__(self, segments='CCCVV', root_length=3):
        """Initialize the list of segments."""
        # residue should be at least 1 segment long
        assert(root_length < len(segments))

        self.segments = segments
        self.root_length = root_length
        self.residue_length = len(segments) - root_length

    def inputs(self):
        """
        Generate roots and residues of appropriate length from self.segments.

        C's and V's are numbered in the order they appear.
        """
        # there's a better algorithm (Knuth's L-algorithm)
        # that generates this without duplications but isn't worth the effort
        possible_stems = sorted(set(itertools.permutations(self.segments)))

        # number the segments in the order they appear
        numbered_stems = [[seg + str(i+1) for i, seg in enumerate(stem)]
                          for stem in possible_stems]

        return [(tuple(stem[:self.root_length]),
                 tuple(stem[self.root_length:])) for stem in numbered_stems]

    def candidates(self, input):
        """
        Generate candidates for a given input.

        Assumptions:
        * MAX and DEP are undominated - no deletions or insertions generated
        * LINEARITY is undominated - no re-ordering of segments within a root
                                     or within a residue, although they may be
                                     interleaved non-concatenatively.
        """
        (root, residue) = input
        assert self.root_length == len(root)
        assert self.residue_length == len(residue)

        templates = sorted(set(
                           itertools.permutations([0] * self.root_length +
                                                  [1] * self.residue_length)))
        return [self._interleave(root, residue, template)
                for template in templates]

    def _interleave(self, arr1, arr2, template):
        """Interleave two strings given a template."""
        iters = [iter(arr1), iter(arr2)]
        return tuple(next(iters[i]) for i in template)
