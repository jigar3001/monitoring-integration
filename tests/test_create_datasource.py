import __builtin__
import maps
import os
import yaml
from grafana.connection import get_conf
from grafana.datasource import create_datasource

def test_creat_dashboard():

    cfg = get_conf("graphite.conf.sample.yml")
    setattr(__builtin__, "NS", maps.NamedDict())
    setattr(NS, "datasource_conf", cfg)
    for datasource in cfg.datasource:
        create_datasource("",datasource)
