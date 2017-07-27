import __builtin__
import maps
import os
import yaml
from grafana.connection import get_conf
from grafana.dashboard import create_dashboard

def test_creat_dashboard():

    cfg = get_conf("grafana.conf.yml")
    setattr(__builtin__, "NS", maps.NamedDict())
    setattr(NS, "conf", cfg)
    for dashboard in NS.conf.dashboards:
        create_dashboard("grafana/dashboards",dashboard)
