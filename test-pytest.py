""" pytest test-pytest.py """
import pytest
import tasks

def test():
    task = tasks.fetch_data.signature(url='http://bees.bagbatch.co.uk/').apply()
    print(task)
    #assert task.update_state == 'TURKEY'
    assert task.status == 'SUCCESS'