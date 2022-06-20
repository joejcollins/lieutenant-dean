import uuid
import celery

import example_custom_multi_queues
import task_queuing.tasks.text as text_tasks


def send_task_with_custom_callback(string_to_reverse, *args, **kwargs):
    """ Run a celery task which upon completion runs custom task. """
    task_id = uuid.uuid4()
    task_args = [string_to_reverse]
    task_args.extend(args)
    # Create a task with a callback.
    result = text_tasks.slowly_reverse_string.apply_async(
        args=tuple(task_args),
        kwargs=kwargs,
        task_id=str(task_id),
        queue="text_queue",
        link=example_custom_multi_queues.send_custom_message.si(),
    )
    # link = text_tasks.slowly_reverse_string.si(tuple(["reverse me again"])),
    # link=number_tasks.slowly_add_two_numbers.si(1, 3),
    return task_id


def send_task_as_chain(string_to_reverse, *args, **kwargs):
    task_id = uuid.uuid4()
    task_args = [string_to_reverse]
    task_args.extend(args)

    task1 = text_tasks.slowly_reverse_string.si(
        args=tuple(task_args),
        kwargs=kwargs,
        task_id=str(task_id),
        queue="text_queue",
    )

    task2 = example_custom_multi_queues.send_custom_message()

    result = celery.chain(task1, task2)()
    return task_id


if __name__ == "__main__":
    # task = send_task_with_custom_callback("reverse me")
    task = send_task_with_custom_callback("reverse me")
    print(f"tasks {task} on queue")
