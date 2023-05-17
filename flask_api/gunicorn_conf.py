"""Gunicorn configuration file for the Flask API."""
# Flask will not run under Hypercorn it requires a WSGI server.
# sourcery skip: avoid-global-variables
import os


# Create the log directory if it does not exist.
my_logs = os.path.basename(os.getcwd())
log_directory = f"../logs/{my_logs}"
os.makedirs(log_directory, mode=0o777, exist_ok=True)


# Settings for the gunicorn server.
access_log_format = "%(t)s %(p)s %(h)s %(r)s %(s)s %(b)s %(M)s"
accesslog = f"{log_directory}/access.log"
capture_output = True
bind = "127.0.0.1:8091"
errorlog = f"{log_directory}/error.log"
loglevel = "INFO"
# DEBUG, INFO, WARNING, ERROR, CRITICAL
print_config = False
workers = 1