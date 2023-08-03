#!/usr/bin/env python
# docker_inventory.py

import os
import sys
import argparse
from subprocess import check_output

try:
    import json
except ImportError:
    import simplejson as json


class DockerInventory(object):

    def __init__(self):
        self.inventory = {}
        self.read_cli_args()

        # Called with `--list`.
        if self.args.list:
            self.inventory = self.docker_inventory()
        # Called with `--host [hostname]`.
        elif self.args.host:
            # Not implemented, since we return _meta info `--list`.
            self.inventory = self.empty_inventory()
        # If no groups or vars are present, return an empty inventory.
        else:
            self.inventory = self.empty_inventory()

        print(json.dumps(self.inventory));

    # Example inventory for testing.
    def example_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Empty inventory for testing.
    def empty_inventory(self):
        return {'_meta': {'hostvars': {}}}

    # Docker inventory for testing.
    def docker_inventory(self):
        output = check_output(['docker', 'ps', '-q']).split('\n')
        docker_containers = [container for container in output if container]

        return {
            'docker': {
                'hosts': docker_containers,
                'vars': {}
            },
            '_meta': {
                'hostvars': {}
            }
        }

    # Read the command line args passed to the script.
    def read_cli_args(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--list', action = 'store_true')
        parser.add_argument('--host', action = 'store')
        self.args = parser.parse_args()


# Get the inventory.
DockerInventory()
