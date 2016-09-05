#!/usr/bin/env python
#coding:utf-8

"""
# Instalar o modulo
pip install pyzabbix

# Lista o json formatado
print json.dumps(<json_file>,indent=2, sort_keys=True)
"""

from pyzabbix import ZabbixAPI
import json

ZSERVER_URL = "http://localhost/zabbix"
ZSERVER_URL_API = ZSERVER_URL + "/api_jsonrpc.php"
ZSERVER_USER = "Admin"
ZSERVER_PASSWORD = "zabbix"

zserver = ZabbixAPI(ZSERVER_URL, user=ZSERVER_USER, password=ZSERVER_PASSWORD)

def get_zserver_version():
    zserver_version = zserver.do_request('apiinfo.version')
    return zserver_version['result']

def get_all_hosts_monitored():
    all_hosts_monitored = zserver.do_request('host.get')
    for results in all_hosts_monitored['result']:
        print (results['host'])

# Informa a versao do zabbix Server
print "Zabbix Server:", get_zserver_version()

# Lista todos os hosts
print "\nServidores:"
get_all_hosts_monitored()
