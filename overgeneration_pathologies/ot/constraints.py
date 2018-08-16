"""Class defining the set of relevant OT constraints and possible rankings."""

LIST_OF_CONSTRAINTS = ['contiguity', 'c_adj_v',
                       'align_left_root', 'align_left_residue',
                       'align_right_root', 'align_right_residue']


class ConstraintSet:
    """Implements constraints."""

    def __init__(self, constraints=LIST_OF_CONSTRAINTS):
        """Initialize list of constraints."""
        self.constraint_strings = constraints
        self.constraints = list()
        for constraint in constraints:
            self.constraints.append(getattr(self, constraint))

    def _is_consonant(self, segment):
        """Return True if segment is of the form C1, C2, C3."""
        return segment[0] == 'C'

    def c_adj_v(self, candidate, inputs=None):
        """
        Implement the C//V constraint.

        Assign * for every C not adjacent to a V.
        """
        violations = 0

        for i, segment in enumerate(candidate):
            if self._is_consonant(segment):
                # if initial, assign * if second segment is also C
                if i == 0 and self._is_consonant(candidate[1]):
                    violations += 1

                # if final, assign * if penultimate segment is also C
                elif (i == len(candidate)-1 and
                      self._is_consonant(candidate[i-1])):
                    violations += 1

                # if medial, assign * if surrounding segments are both also C's
                else:
                    if (self._is_consonant(candidate[i-1]) and
                       self._is_consonant(candidate[i+1])):
                        violations += 1

        return violations

    def align_left_root(self, candidate, inputs):
        """
        Implement the ALIGN(Root, Left, Stem, Left) constraint.

        Assign a * for every segment that intervenes between the left
        edge of the root and the left edge of the stem.

        Note: because LINEARITY is respected, the precedence order
        of segments in each of the root and residue is the same as
        that in each candidate. Therefore, the left edge of the root
        and residue in the output is well-defined as the leftmost
        segment of that morpheme in the output.
        """
        root, residue = inputs
        for i, segment in enumerate(candidate):
            if segment == root[0]:
                return i

    def align_left_residue(self, candidate, inputs):
        """Implement the ALIGN(Residue, Left, Stem, Left) constraint."""
        root, residue = inputs
        for i, segment in enumerate(candidate):
            if segment == residue[0]:
                return i

    def align_right_root(self, candidate, inputs):
        """Implement the ALIGN(Root, Right, Stem, Right) constraint."""
        root, residue = inputs
        for i, segment in enumerate(candidate[::-1]):
            if segment == root[-1]:
                return i

    def align_right_residue(self, candidate, inputs):
        """Implement the ALIGN(Residue, Right, Stem, Right) constraint."""
        root, residue = inputs
        for i, segment in enumerate(candidate[::-1]):
            if segment == residue[-1]:
                return i

    def anchor_left_root(self, candidate, inputs):
        """
        Implement categorical ALIGN(Root, Left, Stem, Left) constraint.

        Assign a * if the left edge of the root does not coincide
        with the left edge of the stem.
        """
        root, residue = inputs
        if candidate[0] != root[0]:
            return 1
        return 0

    def anchor_left_residue(self, candidate, inputs):
        """
        Implement categorical ALIGN(Residue, Left, Stem, Left) constraint.

        Assign a * if the left edge of the residue does not coincide
        with the left edge of the stem.
        """
        root, residue = inputs
        if candidate[0] != residue[0]:
            return 1
        return 0

    def anchor_right_root(self, candidate, inputs):
        """
        Implement categorical ALIGN(Root, Right, Stem, Right) constraint.

        Assign a * if the right edge of the root does not coincide
        with the right edge of the stem.
        """
        root, residue = inputs
        if candidate[-1] != root[-1]:
            return 1
        return 0

    def anchor_right_residue(self, candidate, inputs):
        """
        Implement categorical ALIGN(Residue, Right, Stem, Right) constraint.

        Assign a * if the right edge of the residue does not coincide
        with the right edge of the stem.
        """
        root, residue = inputs
        if candidate[-1] != residue[-1]:
            return 1
        return 0

    def _generate_contiguous_relations(self, segments):
        """Generate the contiguity relations in a tuple of segments."""
        rels = list()
        for i, segment1 in enumerate(segments[:len(segments)-1]):
            rels.append((segment1, segments[i+1]))
        return rels

    def contiguity(self, candidate, inputs):
        """
        Implement the CONTIGUITY constraint.

        Assign a * for every pair of segments that is adjacent in the input
        and not in the output.
        """
        root, res = inputs[0], inputs[1]
        contig_input = self._generate_contiguous_relations(root)
        contig_input.extend(self._generate_contiguous_relations(res))

        contig_candidate = self._generate_contiguous_relations(candidate)
        return (len(set(contig_input) -
                    set(contig_candidate)))

    def __str__(self):
        """Create a nice representation of the constraints."""
        return ' >> '.join(self.constraint_strings)

    def __iter__(self):
        """Iterate over the constraint functions."""
        return iter(self.constraints)

    def __len__(self):
        """Define the length as the number of constraints in this set."""
        return len(self.constraints)

# Pengo suffix (Kenstowicz and Kisseberth '77 and '78)
# metathesis cause to think it's not synchronically active

# affix has been distributed
# there are cases called non-concatenative that might meet their criterion
# root ends in VC and add suffix, V occurs after the C
# Hungarian is an example - bokor, bokrot.

# concat, infixation (rearrangement of residue OK), non-concat (good + bad)
# r-volume
# over-generation is still a problem

# Align-R-Res, Align-L-Rt, Onset *CC >> Contiguity
# C1C2V1 + V2C3 -> C1V2C2V1C3
# CVCCV was probably harmonically bound by infixing VC entirely into CVCVC.
