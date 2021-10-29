""" Celery configuration. """
import celery

queue = celery.Celery("__name__")

queue.conf.update(
    broker_url="redis://localhost:6379/1",
    worker_prefetch_multiplier="1",
    result_backend="redis://localhost:6379/1",
    task_serializer="json",
    accept_content=["json", "pickle"]
    )


def make_celery(app):
    """ Return a configured what?  """
    celery_queue = celery.Celery(
        app.import_name,
        backend=app.config['CELERY_RESULT_BACKEND'],
        broker=app.config['CELERY_BROKER_URL'],
        CELERY_IMPORTS = ('strings.tasks', )

    )
    celery_queue.conf.update(app.config)

    class ContextTask(celery.Task):
        """ Over ride?  Why? """
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_queue.Task = ContextTask
    return celery_queue
