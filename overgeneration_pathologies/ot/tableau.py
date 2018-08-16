"""Run a tableau and identify the winning candidate(s)."""

from collections import defaultdict


class Tableau:
    """Functions for executing and printing an OT tableau."""

    def __init__(self, inputs, ranked_constraints, candidates):
        """Initialize all the variables."""
        self.root, self.residue = inputs
        self.ranked_constraints = ranked_constraints
        self.candidates = candidates

        self._execute()

    def _execute(self):
        """
        Execute the Optimality Theory algorithm.

        Identify winning candidate(s) and populate violations table.
        """
        violations = defaultdict(list)
        viable_candidates = set(self.candidates)
        inputs = (self.root, self.residue)

        for constraint in self.ranked_constraints:
            min_violation = min(constraint(candidate, inputs)
                                for candidate in viable_candidates)
            for candidate in self.candidates:
                num_violations = constraint(candidate, inputs)
                num_violations_string = "*" * num_violations
                if num_violations > min_violation:
                    if candidate in viable_candidates:
                        # this candidate just got knocked out.
                        # remove the candidate from the list of viables.
                        viable_candidates.remove(candidate)
                        # change the violations string to include informative !
                        num_violations_string = ("*" * (min_violation + 1) +
                                                 "!" +
                                                 "*" * (num_violations -
                                                        min_violation - 1))
                violations[candidate].append(num_violations_string)

        # after everything, the candidate(s) left is/are the winner(s)
        self.winners = list(viable_candidates)
        self.violation_table = violations

    def typology_single(self, winner):
        """Determine type of a single winner."""
        if winner == self.root + self.residue:
            return 'concat_suffix'
        if winner == self.residue + self.root:
            return 'concat_prefix'
        if ''.join(self.residue) in ''.join(winner):
            return 'infix'
        if self.residue[0][0] == 'V' and self.residue[1][0] == 'V':
            return 'nonconcat_cv'
        return 'unattested'

    @property
    def typology(self):
        """
        Determine the type of output(s).

        * concatenative (suffixing and prefixing)
        * infixing
        * non-concat C/V respecting
        * unattested non-concat?
        """
        typologies = [self.typology_single(winner)
                      for winner in self.winners]
        assert len(set(typologies)) == 1
        return typologies[0]

    def __repr__(self):
        """Print out a nice tableau."""
        format_string = "{:20} " * (len(self.ranked_constraints) + 1)
        root, res = "".join(self.root), "".join(self.residue)
        constraint_line = ["/{},{}/".format(root, res)]
        constraint_line.extend(self.ranked_constraints.constraint_strings)
        string = format_string.format(*constraint_line)
        string += "\n"
        for candidate in self.candidates:
            if candidate in self.winners:
                tableau_line = ["> " + "".join(candidate)]
            else:
                tableau_line = ["  " + "".join(candidate)]
            tableau_line.extend(self.violation_table[candidate])
            string += format_string.format(*tableau_line)
            string += "\n"
        return string
