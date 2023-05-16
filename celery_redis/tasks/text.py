""" Celery text manipulations. """
import logging
import time

import pkg_captain_black.text as config_text
from celery_redis.main import APP


@APP.task(bind=True)  # `bind=True` ensures that the arguments are passed.
def slowly_reverse_string(self, string_to_reverse: str) -> str:
    """Reverse the string but take 10 seconds to do it."""
    logger = logging.getLogger(self.request.id)
    logger.info(f"Reversing {string_to_reverse}.")
    counter = 10
    for i in range(counter):
        self.update_state(state="PROGRESS", meta={"done": i, "total": counter})
        logger.info(f"Reversing stage {i} of counter.")
        time.sleep(1)
    return config_text.reverse_string(string_to_reverse)
