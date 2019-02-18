import pytest
import tasks
from tasks import Task

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # Excetute tests.

    # TearDown
    tasks.stop_tasks_db()

@pytest.mark.skipif(tasks.__version__ < '0.2.0',
                    reason='not supported until version 0.2.0')
def test_unique_id():
    """Calling unique_id() twice should return different numbers."""
    id_1 = tasks.unique_id()
    id_2 = tasks.unique_id()

    assert id_1 != id_2

def test_unique_id_2():
    """unique_id() should return an unused id."""
    ids = []
    ids.append(tasks.add(Task('one')))
    ids.append(tasks.add(Task('two')))
    ids.append(tasks.add(Task('three')))

    uid = tasks.unique_id()

    assert uid not in ids
