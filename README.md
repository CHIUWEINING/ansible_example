# ansible_example
### 1. please create your own inventory named by your ip and put it in /all_hosts(dynamic_inv.py would use your ip to search the json file of inventory)(the two json files in /all_hosts are two examples)
### 2. execute the playbook `deploy.yml`
```bash
## push
ansible-playbook ansible-playbook deploy.yml -i dynamic_inv.py
## pull
ansible-pull -U https://github.com/CHIUWEINING/ansible_example.git -i dynamic_inv.py deploy.yml -l all