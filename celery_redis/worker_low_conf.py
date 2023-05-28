"""Configuration for the low concurrency worker."""
# Number tasks do not need to finish quickly so this worker deals with number queue.
# sourcery skip: avoid-global-variables
logging = "DEBUG"
worker_redirect_stdouts = False
worker_concurrency = 1
task_routes = (
    {
        "celery_queue_rabbit.tasks.numbers.*": {"queue": "number_queue"},
    },
)
