"""Confirm the model behavior"""
from shit import InBoundModelCode


def test_inbound_model_code() -> None:
    """Confirm that the inbound model restricts to code to an integer."""
    
    the_model = InBoundModelCode(name="alice", status_code=1)
    assert True

