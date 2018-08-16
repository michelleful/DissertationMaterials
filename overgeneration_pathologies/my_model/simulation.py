"""Carry out simulation of my model."""

import re
import random
from collections import defaultdict, Counter
import numpy as np
from scipy.stats import poisson

p = 0.5
lambda_ = 5  # TODO
alpha = 0.9  # TODO  alpha < 1
beta = 5    # TODO  b >= -a


def generate_string_length(lambda_):
    """Generate a string length > 0 from Poisson distribution."""
    length = 0
    while not length:
        length = poisson(lambda_).rvs(1,)
    return length


def generate_string(length, zero, one, prob_one=0.5):
    string = ""
    for i in range(length):
        target = random.random()
        if target > prob_one:
            string += zero
        else:
            string += one
    return string


class Table:
    """A table at the CRP restaurant."""
    num_customers = 0

    def __init__(self, length, zero, one):
        if length == "any":
            length = generate_string_length(lambda_)[0]
        self.string = generate_string(length, zero, one)

    def seat(self):
        self.num_customers += 1

    def __str__(self):
        return self.string + " (" + str(self.num_customers) + ")"

    def __repr__(self):
        return self.__str__()


class Restaurant:
    """A CRP restaurant."""

    def select_table(self):
        # given a list of tables and num seated, pick either an existing table
        # or a new table

        # number of customers per table
        num_customers_per_table = [table.num_customers for table in self.tables]
        total_customers = sum(num_customers_per_table)
        table_probabilities = [(table.num_customers - alpha) /
                               (total_customers + beta)
                               for table in self.tables]

        target_number = random.random()
        cum_prob = 0
        for (table, table_prob) in zip(self.tables, table_probabilities):
            cum_prob += table_prob
            if target_number < cum_prob:
                return table
        return 'new'

    def seat_new_customer(self):
        table = self.select_table()

        if table == 'new':
            table = Table(self.length, self.zero, self.one)
            self.tables.append(table)

        table.seat()
        return table.string

    def __str__(self):
        if not self.tables:
            return f"Empty {self.type_} restaurant ({self.one}, {self.zero})"
        return "\t".join([str(table) for table in self.tables])

    def __repr__(self):
        return self.__str__()


class TemplateRestaurant(Restaurant):
    """A template restaurant."""

    def __init__(self):
        self.type_ = "template"
        self.length = "any"
        self.one = "r"
        self.zero = "s"
        self.tables = list()


class RootRestaurant(Restaurant):
    """A root restaurant."""

    def __init__(self, length):
        """Morphemes must have a specific length associated with them."""
        self.type_ = "root"
        self.one = "C"
        self.zero = "V"
        self.length = length
        self.tables = list()


class ResidueRestaurant(Restaurant):
    """A morpheme restaurant."""

    def __init__(self, length):
        """Morphemes must have a specific length associated with them."""
        self.type_ = "residue"
        self.one = "C"
        self.zero = "V"
        self.length = length
        self.tables = list()


class Simulation:
    """One pass of the simulation."""
    template_restaurant = TemplateRestaurant()
    root_restaurants = dict()  # length -> restaurant
    residue_restaurants = dict()  # length -> restaurant

    def simulate(self, n_words):
        typologies = list()
        while len(typologies) < n_words:
            template = self.template_restaurant.seat_new_customer()
            root_length = template.count('r')
            residue_length = template.count('s')

            if root_length == 0 or residue_length == 0:
                continue

            if root_length not in self.root_restaurants:
                self.root_restaurants[root_length] = RootRestaurant(root_length)
            root = self.root_restaurants[root_length].seat_new_customer()

            if residue_length not in self.residue_restaurants:
                self.residue_restaurants[residue_length] = ResidueRestaurant(residue_length)
            residue = self.residue_restaurants[residue_length].seat_new_customer()

            # characterize it
            if re.match("^r+s+$", template) or re.match("^s+r+$", template):
                typologies.append("concat")
            elif re.match("^r+s+r+$", template) or re.match("^s+r+s+$", template):
                typologies.append("infix")
            else:  # non-concat
                if ((set(root) == {"C"} and set(residue) == {"V"}) or
                   (set(root) == {"V"} and set(residue) == {"C"})):
                    typologies.append("nonconcat_cv")
                else:
                    typologies.append("unattested")
        return Counter(typologies)
