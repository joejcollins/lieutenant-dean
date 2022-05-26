"""
Deleting an environment
=======================

Very First
----------

* e-update-power-state.yml

Delete the networking
---------------------

First:

* p-destroy-vlan.yml (firewall, switches, renamed).  Area of risk.
* p-ensure-public-ip.yml  firewall

Then:

* delete environment network  does this work

Delete the environment itself
-----------------------------

First:

* e-destroy-vms.yml (delete the VMs in Vcenter)
* e-destroy-node-cache.yml (this is the edge cache which doesn't work).
* e-destroy-dns.yml
* e-destroy-monitoring.yml

Then:

* delete the configuration files

"""
from celery_apps.redis_tasks.text import slowly_reverse_string
import celery

power_down = slowly_reverse_string.s("lmy.etats-rewop-etadpu-e")

delete_network_prep = []
delete_network_prep.append(slowly_reverse_string.si("lmy.nalv-yortsed-p"))
delete_network_prep.append(slowly_reverse_string.si("lmy.pi-cilbup-erusne-p"))
# The final task is immutable because we don't need the result of the previous tasks.
delete_network_final = slowly_reverse_string.si("krowten tnemnorivne eteled")
delete_network = celery.chord(delete_network_prep, delete_network_final)


delete_environment_prep = []
delete_environment_prep.append(slowly_reverse_string.si("lmy.smv-yortsed-e"))
delete_environment_prep.append(slowly_reverse_string.si("lmy.ehcac-edon-yortsed-e"))
delete_environment_prep.append(slowly_reverse_string.si("lmy.snd-yortsed-e"))
delete_environment_prep.append(slowly_reverse_string.si("lmy.gnirotinom-yortsed-e"))
# The final task is immutable because we don't need the result of the previous tasks.
delete_environment_final = slowly_reverse_string.si("selif tnemnorivne eteled")
delete_environment = celery.chord(delete_environment_prep, delete_environment_final)

delete_everything = celery.chain(power_down, delete_network, delete_environment)
result = delete_everything()
