import pytest
import tasks
from tasks import Task

def test_add_returns_valid_id(tasks_db):
    """tasks.add(<valid task>) should return an integer."""
    # GIVEN an initialized tasks db
    # WHEN a new task is added
    # THEN return task_id is of type int
    new_task = Task('do somthing')
    task_id = tasks.add(new_task)
    assert isinstance(task_id, int)

def test_add_increases_count(db_with_3_tasks):
    """Test tasks.add() after on tasks.count()."""
    # GIVEN a db with 3 tasks
    #  WHEN another task is added
    tasks.add(Task('throw a party'))

    # THEN the count increses by 1
    assert tasks.count() == 4
