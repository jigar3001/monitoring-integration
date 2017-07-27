import __builtin__
import os
import yaml
import json
import traceback
import sys
from requests import get, post, put
from grafana.connection import fread
from grafana.connection import port_open
from grafana.connection import get_conf
from grafana.exceptions import FileNotFoundException


HEADERS = {"Accept": "application/json",
           "Content-Type": "application/json"
           }


'''Create Dashboard'''

def post_dashboard(dashboard_json):
    cfg = NS.conf
    if port_open(cfg.port, cfg.host):
        upload_str = json.dumps(dashboard_json)
        resp = post("http://{}:{}/api/dashboards/"
                    "db".format(cfg.host,
                                cfg.port),
                    headers=HEADERS,
                    auth=cfg.credentials,
                    data=upload_str)

    return resp


def get_dashboard(dashboard_name):
    config = NS.conf
    resp = get("http://{}:{}/api/dashboards/"
               "db/{}".format(config.host,
                              config.port,
                              dashboard_name),
               auth=config.credentials)
    return resp.json()


def get_all_dashboards():
    config = NS.conf
    resp = get("http://{}:{}/api/search/"
               .format(config.host,
                       config.port),
               auth=config.credentials)
    return resp.json()

def set_home_dashboard(dash_id):
    config = NS.conf
    resp = put('http://{}:{}/api/org/'
                       'preferences'.format(config.host,
                                            config.port),
                       headers=HEADERS,
                       auth=config.credentials,
                       data=json.dumps({"name": "Main Org.",
                                        "theme": "light",
                                        "homeDashboardId": dash_id}))


def create_dashboard(dashboard_dir,dashboard_name):
    dashboard_path = os.path.join(dashboard_dir,
                                    "{}.json".format(dashboard_name))
    if os.path.exists(dashboard_path):
        dashboard_data = fread(dashboard_path)
        try:
            dbjson = json.loads(dashboard_data)
            ret = post_dashboard(dbjson)
            return ret.status_code
        except Exception as ex:
            sys.stdout.write(str(ex))
            raise Exception
    else:
        raise FileNotFoundException
