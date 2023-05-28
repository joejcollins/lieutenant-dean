"""Configuration for the low concurrency worker."""
# Text tasks need to finish quickly so this worker deals with text queue.
# sourcery skip: avoid-global-variables
logging = "DEBUG"
worker_redirect_stdouts = False
worker_concurrency = 4
task_routes = (
    {
        "celery_queue_rabbit.tasks.text.*": {"queue": "text_queue"},
    },
)
