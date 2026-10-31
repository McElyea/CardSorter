# Tests

This area will contain automated software tests, protocol simulations, mechanical
cycle data, image-recognition evaluation sets, and milestone acceptance reports.
Published reliability claims must link to the underlying configuration and raw
results.

Run `python -m unittest discover -s tests -p "test_*.py" -v` from the project root.
The initial suite validates the sorting model, finite-capacity chunk order, and
reload-error counterexamples. Passing these tests makes no claim about physical
reliability or recognition accuracy.
