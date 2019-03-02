import pytest

@pytest.fixture(name='lue')
def ultimate_anser_to_life_the_universe_and_everythong():
    return 42

def test_everything(lue):
    assert lue == 42
