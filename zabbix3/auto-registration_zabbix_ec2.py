#!/usr/bin/env python
#coding:utf-8

"""
# Instalar o modulo
pip install pyzabbix

#Lista o json formatado
print json.dumps(<json_file>,indent=2, sort_keys=True)
"""

from pyzabbix import ZabbixAPI
import json
import requests

ZSERVER_URL = "http://localhost/zabbix"
ZSERVER_URL_API = ZSERVER_URL + "/api_jsonrpc.php"
ZSERVER_USER = "Admin"
ZSERVER_PASSWORD = "zabbix"

zserver = ZabbixAPI(ZSERVER_URL)

zserver.login(ZSERVER_USER,ZSERVER_PASSWORD)

def get_zserver_version():
    zserver_version = zserver.do_request('apiinfo.version')
    return zserver_version['result']

def get_all_hosts():
    all_hosts = zserver.do_request('host.get')
    for hosts in all_hosts['result']:
        return (hosts['name'])

# Informa a versao do zabbix Server
#print get_zserver_version()

# Lista todos os hosts
#print get_all_hosts()
