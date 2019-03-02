import pytest

@pytest.fixture(name='lue')
def ultimate_anser_to_life_the_universe_and_everythong():
    """Return ultimate answer."""
    return 42

def test_everything(lue):
    """Use the shorter name."""
    assert lue == 42
