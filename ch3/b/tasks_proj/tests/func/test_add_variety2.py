import pytest
import tasks
from tasks import Task

tasks_to_try = (Task('sleep', done=True),
                Task('wake', 'brian'),
                Task('breathe', 'BRIAN', True),
                Task('exercise', 'BrIaN', False))

task_ids = ['TASK({}{}{})'.format(t.summary, t.owner, t.done) for t in tasks_to_try]

def equivalent(t1, t2):
    """Check two tasks for equivalance"""
    return ((t1.summary == t2.summary)and(t1.owner == t2.owner)and(t1.done==t2.done))

@pytest.fixture(params=tasks_to_try)
def a_task(request):
    """Using no ids."""
    return request.param

def test_add_a(tasks_db, a_task):
    """Using a_task fixture (no ids)."""
    task_id = tasks.add(a_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, a_task)

@pytest.fixture(params=tasks_to_try, ids=task_ids)
def b_task(request):
    """Using b_task fixture, with ids."""
    return request.param

def test_add_b(tasks_db, b_task):
    """Using b_task fixture, with ids."""
    task_id = tasks.add(b_task)
    t_from_db = tasks.get(task_id)
    assert equivalent(t_from_db, b_task)
