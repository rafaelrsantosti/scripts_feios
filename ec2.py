#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Boto3 - Aws SDK python (https://boto3.readthedocs.io/en/latest/).

import boto3
import time
import sys
import os
import yaml

PROFILE = 'kptesteab'

def init_session():
    s = boto3.Session(profile_name=PROFILE)
    return s.resource('ec2')

def ls():
    ec2 = init_session()

    for i in ec2.instances.all():
        if i.tags is None:
            continue
        for t in i.tags:
            if t['Key'] == 'Name':
                print "{0} - {1} ({2}) - [{3}] - <{4}>".format(
                    i.id, t['Value'], i.instance_type, i.public_ip_address, i.state['Name']
                )
