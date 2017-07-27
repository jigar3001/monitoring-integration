import os
import sys
import json
import yaml
from requests import get, post, put
import socket
from grafana.exceptions import ConfigNotFoundException
from grafana.exceptions import InvalidConfig
from grafana.config import Config


def get_conf(file_name):

    if os.path.exists(file_name):
        config_data = fread(file_name)
        try:
            yaml_config = yaml.load(config_data)
        except:
            raise InvalidConfig

        cfg = Config()
        cfg.host = yaml_config.get('host')
        cfg.name = yaml_config.get('name',None)
        cfg.type = yaml_config.get('type',"graphite")
        cfg.access = yaml_config.get('access',"direct")
        cfg.basicAuth = yaml_config.get('basicAuth',"true")
        cfg.isDefault = yaml_config.get('isDefault',"false")
        cfg.dashboards = yaml_config.get('dashboards', [])
        cfg.datasource = yaml_config.get('datasource', [])
        cfg.auth = yaml_config.get('credentials',None)
        if cfg.auth:
            cfg.credentials = (cfg.auth.get('user'),
                                       cfg.auth.get('password'))
        cfg.port = yaml_config.get('port', 3000)
        cfg.home_dashboard = yaml_config.get('home_dashboard',
                                             'home_dashboard')
        cfg.yaml = yaml_config
        return cfg
    else:
        raise ConfigNotFoundException


def port_open(port, host='localhost'):
    """
    Check a given port is accessible
    :param port: (int) port number to check
    :param host: (str)hostname to check, default is localhost
    :return: (bool) true if the port is accessible
    """

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect_ex((host, port))
        sock.shutdown(socket.SHUT_RDWR)
        sock.close()
        return True
    except socket.error:	
        return False


def fread(file_name):
    with open(file_name) as f:
        f_data = f.read()
    return f_data

