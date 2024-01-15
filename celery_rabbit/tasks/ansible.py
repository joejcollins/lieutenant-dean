"""Tasks for handling environments."""
import logging
import os
import sys

import ansible_runner
import celery
import celery_queue_rabbit.celery_app as app
import celery_queue_rabbit.tasks.text as text_tasks


@app.queue_broker.task(bind=True)  # `bind=True` ensures that the arguments are passed.
def deploy_sites(self, alias):
    """Run the playbooks to deploy the sites for the environment."""
    logger = logging.getLogger(self.request.id)
    logger.info("Deploy Sites")


@app.queue_broker.task(bind=True)
def delete_environment(self, alias):
    """Delete the environment and it's network."""
    logger = logging.getLogger(self.request.id)
    logger.info(f"Deleting {alias}")
    power_down = text_tasks.slowly_reverse_string.s("lmy.etats-rewop-etadpu-e")

    delete_network_prep = []
    delete_network_prep.append(text_tasks.slowly_reverse_string.si("lmy.nalv-yortsed-p"))
    delete_network_prep.append(text_tasks.slowly_reverse_string.si("lmy.pi-cilbup-erusne-p"))
    # The final task is immutable because we don't need the result of the previous tasks.
    delete_network_final = text_tasks.slowly_reverse_string.si("krowten tnemnorivne eteled")
    delete_network = celery.chord(delete_network_prep, delete_network_final)

    delete_environment_prep = []
    delete_environment_prep.append(text_tasks.slowly_reverse_string.si("lmy.smv-yortsed-e"))
    delete_environment_prep.append(text_tasks.slowly_reverse_string.si("lmy.ehcac-edon-yortsed-e"))
    delete_environment_prep.append(text_tasks.slowly_reverse_string.si("lmy.snd-yortsed-e"))
    delete_environment_prep.append(text_tasks.slowly_reverse_string.si("lmy.gnirotinom-yortsed-e"))
    # The final task is immutable because we don't need the result of the previous tasks.
    delete_environment_final = text_tasks.slowly_reverse_string.si("selif tnemnorivne eteled")
    delete_environment = celery.chord(delete_environment_prep, delete_environment_final)

    delete_everything = celery.chain(power_down, delete_network, delete_environment)
    return delete_everything()


@app.queue_broker.task(bind=True)  # `bind=True` ensures that the arguments are passed.
def run_playbook(self):
    """Run a playbook for logging test."""
    logger = logging.getLogger(self.request.id)
    logger.info("BEGINS")
    # Weirdly I have to move to another directory before the run.  This makes no sense.
    os.chdir('/workspace/captain-black')
    out, err, rc = ansible_runner.run_command(
        executable_cmd="ansible-playbook",
        cmdline_args=[
            "./ansible/playbooks/inspection/system.yml",
            "--connection",
            "local",
            "--inventory",
            "127.0.0.1,",
            "--limit",
            "127.0.0.1"
        ],
        project_dir="./ansible",
        artifact_dir="./logs/runner_artifacts",
        input_fd=sys.stdin,
        output_fd=logger.handlers[0].stream,
        error_fd=sys.stderr
    )
    logger.info("ENDS")
    return True
