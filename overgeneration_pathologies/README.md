# Code for section 3.1: Pathological predictions

This code is used to calculate how many non-concatenative and unattested languages are generated in (a) the generative model laid out in Chapter 2 and (b) Optimality Theory, for various assumptions. See Chapter 3, section 1 for full details.

## Running the code

* Using `virtualenv` or `pipenv`, install the requirements in `requirements.txt`
* Activate the virtualenv/pipenv
* To replicate the numbers for the base Arabic model
  * In `my_model/` directory,
	* `python count_simulations.py > my_model_typology_results`
* To replicate the numbers for Optimality Theory:
  * In the `ot/` directory,
  * Edit `run_typologies.py` for the list of typology types you're interested in.
  * `python run_typologies.py > ot_typology_results.txt`

## Testing the Optimality Theory code

* In `ot/`, run `pytest` from the command line.

## Supporting files:
* `ot/constraints.py` defines functions for the various OT constraints
* `ot/gen.py` generates inputs and output candidates
* `ot/tableau.py` computes the winning candidate for a given constraint ranking
* `ot/typology.py` permutes the rankings to form the factorial typology

* `my_model/simulation.py` contains classes for running a single simulation over the model.
