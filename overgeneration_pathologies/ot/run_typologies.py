"""Run typologies."""

import itertools
from typology import print_full_typology, print_count_typology


#  Define the various constraint sets and possible rankings.

def default_constraint_rankings():
    """Return all possible rankings of CONTIGUITY, C//V and gradient align."""
    return itertools.permutations(
                       ['contiguity', 'c_adj_v',
                        'align_left_root', 'align_left_residue',
                        'align_right_root', 'align_right_residue'])


def categorical_align_constraint_rankings():
    """Return all possible rankings of CONTIG, C//V and categorical align."""
    return itertools.permutations(
                       ['contiguity', 'c_adj_v',
                        'anchor_left_root', 'anchor_left_residue',
                        'anchor_right_root', 'anchor_right_residue'])


def zukoff_prefix_rankings():
    """
    Return all possible rankings where ALIGN-L-Res >> ALIGN-L-Rt.

    ALIGN-R-Res is inactive.
    """
    for ranking in itertools.permutations([
        'contiguity', 'c_adj_v',
        'align_left_residue', 'align_left_root', 'align_right_root'
    ]):
        if (ranking.index('align_left_residue') <
           ranking.index('align_left_root')):
            yield ranking


def zukoff_suffix_rankings():
    """
    Return all possible rankings where ALIGN-R-Res >> ALIGN-R-Rt.

    ALIGN-L-Res is inactive.
    """
    for ranking in itertools.permutations([
        'contiguity', 'c_adj_v',
        'align_right_residue', 'align_right_root', 'align_left_root'
    ]):
        if (ranking.index('align_right_residue') <
           ranking.index('align_right_root')):
            yield ranking


# -------------
#    MAIN
# -------------

# for ranking_type in ["default_constraint_rankings",
#                      "categorical_align_constraint_rankings",
#                      "zukoff_prefix_rankings",
#                      "zukoff_suffix_rankings"]:
#     rankings = locals()[ranking_type]()
#     print(ranking_type)
#     print("-"*50)
#     print_count_typology(rankings)
#     print("\n\n\n")


for ranking_type in [
#                    "default_constraint_rankings",
                     "categorical_align_constraint_rankings"
#                     "zukoff_prefix_rankings",
#                     "zukoff_suffix_rankings"
                    ]:
    rankings = locals()[ranking_type]()
    print(ranking_type)
    print("-"*50)
    print_full_typology(rankings)
    print("\n\n\n")
