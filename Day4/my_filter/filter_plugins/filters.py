#!/usr/bin/python

import re
from ansible.errors import AnsibleFilterTypeError, AnsibleFilterError


def format_mac(mac: str) -> str:
    '''return formatted mac'''
    if not isinstance(mac, str):
        raise AnsibleFilterTypeError(
            "expected string, but got {} type".format(type(mac)))
    if len(mac) != 12:
        raise AnsibleFilterError(
            "Expected 12 characters but got {}".format(len(mac)))
    if re.search(r'([0-9A-F]{12})', mac) is None:
        raise AnsibleFilterError(
            "Variable could contain only A-F, 0-9 character")
    mac = ':'.join(re.findall('..', mac))
    return mac


class FilterModule(object):
    def filters(self):
        return {
            'format_mac': format_mac
        }
