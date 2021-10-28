"""  """
from celery import Celery

def make_celery(app):
    celery = Celery(
        app.import_name
    )
    celery.conf.update(
        broker_url="redis://localhost:6379/1",
        worker_prefetch_multiplier="1",
        result_backend="redis://localhost:6379/1",
        task_serializer="json",
        accept_content=["json", "pickle"],
        imports=['strings.reverse']
    )

    class ContextTask(celery.Task):
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    holder.celery.Task = ContextTask
    return celery
