# ansible_example
## 1. create your own inventory named by your ip and put it in all_hosts
## 2. execute the playbook `deploy.yml`
```bash
## push
ansible-playbook ansible-playbook deploy.yml -i dynamic_inv.py
## pull
ansible-pull -U https://github.com/CHIUWEINING/ansible_example.git -i dynamic_inv.py deploy.yml -l all