#coding:utf-8

# Lista o json formatado
#print json.dumps(<json_file>,indent=2, sort_keys=True)

from pyzabbix import ZabbixAPI
import json
import requests

zserver_url = "http://<domain.com>/zabbix"
zserver_url_api = zserver_url + "/api_jsonrpc.php"
zserver_user = "Admin"
zserver_password = "zabbix"

zserver = ZabbixAPI(zserver_url, user=zserver_user, password=zserver_password)

def get_zserver_version():
    zserver_version = zserver.do_request('apiinfo.version')
    print zserver_version['result']

def get_all_hosts():
    all_hosts = zserver.do_request('host.get')
    for hosts in all_hosts['result']:
        print (hosts['name'])
