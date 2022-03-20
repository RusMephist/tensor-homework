#!/usr/bin/python

from __future__ import (absolute_import, division, print_function)
from ansible.module_utils.basic import AnsibleModule
import requests
__metaclass__ = type

DOCUMENTATION = r'''
---
module: http_py
short_description: Module for receiving a response code from the HTTP server
version_added: "1.0.0"
description: Module for receiving a response code from the HTTP server.

options:
    action:
        description: What action do you want
        required: true
        type: str
    server:
        description: Server hostname or ip
        required: false
        type: str

author:
    - Mikhail Vorontsov
'''

EXAMPLES = r'''
- name: Get answer code from HTTP server
  http_py:
    action: get_code
    server: localhost
'''

RETURN = r'''
msg:
  description: Errors if occured
  returned: always
  type: str
  sample: ""
server_code:
  description: HTTP server code
  returned: when action: get
  type: str
  sample: 200
rc:
  description: Return code
  returned: always
  type: int
  sample: 0
'''


def get_server_code(server: str):
    failed = False
    rc = 0
    server_code = "000"
    try:
        r = requests.head(server)
        server_code = r.status_code
    except requests.ConnectionError:
        failed = True
        rc = 1
    return(failed, server_code, rc)


def main():
    module_args = dict(
        action=dict(type='str', required=True),
        server=dict(type='str', required=False)
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    if module.params['action'] == 'get_code':
        answer = get_server_code(module.params['server'])

    if answer[0]:
        module.fail_json(msg='Can\'t connect to server',
                         changed=False,
                         failed=answer[0],
                         server_code=answer[1],
                         rc=answer[2])
    else:
        module.exit_json(changed=False,
                         failed=answer[0],
                         server_code=answer[1],
                         rc=answer[2])


if __name__ == '__main__':
    main()
