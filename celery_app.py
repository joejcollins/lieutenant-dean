"""  """
import celery

celery_queue = celery.Celery("__name__")

celery_queue.autodiscover_tasks(["stringsfoo"])

celery_queue.conf.update(
    broker_url="redis://localhost:6379/1",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"]
    )