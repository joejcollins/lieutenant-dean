# Ansible Example

`sudo ansible-playbook ubuntu-20.04-playbook.yml --connection=local --inventory 127.0.0.1,`

```
ansible/                        # contains the ansible.cfg
ansible/playbooks/              # where you run playbooks
ansible/playbooks/create        # playbooks for creating virtual machines
ansible/playbooks/recovery      # playbooks for recovering from failure
ansible/playbooks/upgrade       # playbooks for upgrading virtual machines
ansible/playbooks/delete        # playbooks for deleting virtual machines
ansible/library/                # custom modules
ansible/module_utils/           # if any custom module_utils to support modules
ansible/filter_plugins/         # filter plugins
ansible/roles/                  # roles for the playbooks to use
```
