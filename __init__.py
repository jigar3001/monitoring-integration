import __builtin__
import os
import maps
import json
import yaml
import sys
from grafana.connection import get_conf
from grafana.dashboard import create_dashboard
from grafana.dashboard import set_home_dashboard
from grafana.dashboard import get_dashboard
from grafana.dashboard import get_all_dashboards
from grafana.datasource import create_datasource

if __name__ == '__main__':

    ret = []
    cfg = get_conf("grafana.conf.yml")
    setattr(__builtin__, "NS", maps.NamedDict())
    setattr(NS, "conf", cfg)

    ret = get_all_dashboards()

    if len(ret) > 0:
        exit(0) 

    for dashboard in cfg.dashboards:
        ret = create_dashboard("grafana/dashboards", dashboard)
        if ret == 200:
            sys.stdout.write('\n' + "Dashboard " + str(dashboard) + " uploaded successfully" + '\n')
        else:
            sys.stdout.write('\n' + "Dashboard " + str(dashboard) + " upload failed with error code " + str(ret) + '\n')
    try:
        dashjson = get_dashboard(cfg.home_dashboard)
        dash_id = dashjson.get('dashboard').get('id')
        set_home_dashboard(dash_id)
    except:
        sys.stdout.write("JSON ERROR")

    ret = []
    
    for datasource in cfg.datasource:
        cfg = get_conf(str(datasource) + ".conf.yml")
        setattr(NS, "datasource_conf", cfg)
        ret = create_datasource("", datasource)
        if ret == 200:
            sys.stdout.write('\n' + "Datasource " + str(datasource) + " uploaded successfully" + '\n')
        else:
            sys.stdout.write('\n' + "Datasource " + str(datasource) + " upload failed with error code " + str(ret) + '\n')
