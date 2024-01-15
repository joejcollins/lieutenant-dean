"""Handles the text endpoint."""
from pkg_shared import text


def _reverse_fast(string_to_reverse):
    """Provide a json response with the reversal."""
    reversed_string = text.reverse_string(string_to_reverse)
    return {"original": string_to_reverse, "reversed": reversed_string}
