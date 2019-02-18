import pytest
import tasks
from tasks import Task

def test_add_1():
    """tasks.get() using id returend from add() works."""
    task = Task('breathe', 'BRIAN', True)
    task_id = tasks.add(task)

    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)

@pytest.mark.parametrize('task', [Task('sleep', done=True),
                                   Task('wake', 'brian'),
                                   Task('breathe', 'BRIAN', True),
                                   Task('exercise', 'BrIaN', False)])
def test_add_2(task):
    """Demonstrate parameterize with one parameter."""
    task_id = tasks.add(task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, task)


def equivalent(t1, t2):
    """Check two tasks for equivalance."""
    return ((t1.summary == t2.summary) and (t1.owner == t2.owner) and (t1.done == t2.done))

@pytest.fixture(autouse=True)
def initialized_tasks_db(tmpdir):
    """Connect to db before testing, disconnect after."""
    # Setup
    tasks.start_tasks_db(str(tmpdir), 'tiny')

    yield # Excetute tests.

    # TearDown
    tasks.stop_tasks_db()
