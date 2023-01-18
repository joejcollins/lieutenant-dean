"""Confirm the model behavior"""
import pydantic.error_wrappers as pydantic_errors
import pytest

from shit import InBoundModelCode, InBoundModelCodeOrDescription


def test_inbound_model_code_no_extras() -> None:
    """Confirm that the inbound model restricts to code to an integer."""
    # ACT
    with pytest.raises(pydantic_errors.ValidationError) as exception_info:
        InBoundModelCode(name="alice", status_code=4)
    # ASSERT
    assert "You have to set one" in str(exception_info.value)


def test_inbound_model_code_or_description_error_neither() -> None:
    """Confirm that at least one has to be supplied."""
    # ACT
    with pytest.raises(pydantic_errors.ValidationError) as exception_info:
        InBoundModelCodeOrDescription(name="alice")
    # ASSERT
    assert "You have to set one" in str(exception_info.value)


def test_inbound_model_code_or_description_error_both() -> None:
    """Confirm that you can't supply both."""
    # ACT
    with pytest.raises(pydantic_errors.ValidationError) as exception_info:
        InBoundModelCodeOrDescription(
            name="alice", status_code=1, status_description="One"
        )
    # ASSERT
    assert "You can't set both" in str(exception_info.value)
