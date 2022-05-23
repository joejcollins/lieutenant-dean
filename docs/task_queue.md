# Task Queues

Long running tasks

Run Celery working process to watch a queue in Redis

To view events without Flower `celery --workdir=task_queue --app=celery_app events`

Don't name the tasks, it is just confusing.  Refer to them via their namespace.
Keep the namespace tidy and meaningful.