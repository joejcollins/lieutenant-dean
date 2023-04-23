def _reverse_fast(string_to_reverse):
    """ Provide a json response with the reversal. """
    reversed_string = info_text.reverse_string(string_to_reverse)
    message = {
        'original': string_to_reverse,
        'reversed': reversed_string
    }
    return message