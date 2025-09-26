# Pytest showcase: how session-scoped fixtres are not always uniqe

This repo shocases a wird issue I encountered when using pytest.

Running the following command will display the demo (requires python3 and pytest to be installed):

```sh
python -m pytest tests -s
```

This will output:

```
tests/test_a.py FIXTURE setup 1
TEST: a1
.TEST: a2
.
tests/test_b.py FIXTURE setup 2
TEST: b1
.TEST: b2
.FIXTURE teardown
FIXTURE teardown
```

showing that the fixture `foo` wasa run two time, while its scope of `session` should only allow it to run a ssingle time.
