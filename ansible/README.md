# Ansible Example

`sudo ansible-playbook ubuntu-20.04-playbook.yml --connection=local --inventory 127.0.0.1,`

```
ansible/                        # contains the ansible.cfg
ansible/playbooks/              # where you run playbooks
ansible/playbooks/environment   # playbooks for managing environments
ansible/playbooks/pod           # playbooks for managing pods
ansible/playbooks/recovery      # playbooks for recovering from failure
ansible/library/                # custom modules
ansible/module_utils/           # if any custom module_utils to support modules
ansible/filter_plugins/         # filter plugins
ansible/roles/                  # same just a list
```
