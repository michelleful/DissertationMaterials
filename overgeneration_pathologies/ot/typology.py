"""
Given a list of constraint rankings, run the typology.

Either print out all the possibilities for inspection (warning: a lot!)
or count the number of different typologies that arise.
"""

from collections import Counter
import itertools
from gen import Gen
from constraints import ConstraintSet
from tableau import Tableau

gen = Gen()


def print_full_typology(rankings):
    """Print the full set of results: ranking, winner, and winner type."""
    for ranking in rankings:
        constraint_ranking = ConstraintSet(ranking)
        print("----------------------------------")
        print(constraint_ranking)
        print("----------------------------------")
        for inputs in gen.inputs():
            tableau = Tableau(inputs, constraint_ranking,
                              gen.candidates(inputs))
            print(inputs, tableau.winners, tableau.typology)


def print_count_typology(rankings):
    """Print each ranking and morphology count over all possible inputs."""
    print("\t".join(["ranking", "suffix", "prefix", "infix",
                     "nonconcat_cv", "nonconcat_unattested"]))

    count_at_least_1_nonconcat = 0
    count_at_least_half_nonconcat = 0
    count_at_least_1_unattested = 0
    count_at_least_half_unattested = 0
    total_count = 0

    for ranking in rankings:
        constraint_ranking = ConstraintSet(ranking)
        total_count += 1

        list_of_typologies = Counter()
        for inputs in gen.inputs():
            tableau = Tableau(inputs, constraint_ranking,
                              gen.candidates(inputs))
            list_of_typologies[tableau.typology] += 1

        assert(sum(list_of_typologies.values()) == 10)

        print("\t".join([
            str(constraint_ranking),
            str(list_of_typologies['concat_suffix']),
            str(list_of_typologies['concat_prefix']),
            str(list_of_typologies['infix']),
            str(list_of_typologies['nonconcat_cv']),
            str(list_of_typologies['unattested']),
        ]))

        # get meta stats
        if (list_of_typologies['nonconcat_cv'] +
           list_of_typologies['unattested'] >= 1):
            count_at_least_1_nonconcat += 1

        if (list_of_typologies['nonconcat_cv'] +
           list_of_typologies['unattested'] >= 6):
            count_at_least_half_nonconcat += 1

        if (list_of_typologies['unattested'] >= 1):
            count_at_least_1_unattested += 1

        if (list_of_typologies['unattested'] >= 6):
            count_at_least_half_unattested += 1

    print("\nSummary:\n")
    print(f"{count_at_least_1_nonconcat}/{total_count} "
          f"({100 * count_at_least_1_nonconcat/total_count:.1f}%) rankings "
          f"have at least one non-concatenative output.")
    print(f"{count_at_least_half_nonconcat}/{total_count} "
          f"({100 * count_at_least_half_nonconcat/total_count:.1f}%) rankings "
          f"have more than half non-concatenative outputs.")
    print(f"{count_at_least_1_unattested}/{count_at_least_1_nonconcat} "
          f"({100 * count_at_least_1_unattested/count_at_least_1_nonconcat:.1f}%) "
           "non-concat rankings have at least one unattested output.")
    print(f"{count_at_least_half_unattested}/{count_at_least_half_nonconcat} "
          f"({100 * count_at_least_half_unattested/count_at_least_half_nonconcat:.1f}%) "
           "majority non-concat rankings have more than half "
           "unattested outputs.")
