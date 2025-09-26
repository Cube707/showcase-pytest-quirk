import pytest

CONST = 0

@pytest.fixture(scope="session")
def foo():
    global CONST
    CONST += 1

    print(f"FIXTURE setup {CONST}")
    yield
    print("FIXTURE teardown")
