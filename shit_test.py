from shit import InBoundModel

def test_inbound_model_code():
    """Confirm that the inbound model restricts to code to an integer."""
    the_model = InBoundModelCode(name="alice", status_code=1)

