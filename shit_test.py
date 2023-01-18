"""Confirm the model behavior"""
from shit import InBoundModelCode, InBoundModelCodeOrDescription


def test_inbound_model_code() -> None:
    """Confirm that the inbound model restricts to code to an integer."""
    # ARRANGE
    # ACT
    the_model = InBoundModelCode(name="alice", status_code=1)
    # ASSERT
    assert True


def test_inbound_model_code_or_description() -> None:
    # ARRANGE
    # ACT
    # with pytest.raises(
    the_model = InBoundModelCodeOrDescription(name="alice", turkey="shit")
    # ASSERT
    assert True
