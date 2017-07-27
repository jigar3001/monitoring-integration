import __builtin__
import json
import os
import traceback
from requests import get, post, put
from grafana.connection import fread
from grafana.connection import port_open
from grafana.connection import get_conf
from grafana.exceptions import FileNotFoundException

HEADERS = {"Accept": "application/json",
           "Content-Type": "application/json"
           }

''' Create Datasource '''

def post_datasource(datasource_json):
    if port_open(NS.conf.port, NS.conf.host):
        resp = post("http://{}:{}/api/datasources"
                    .format(NS.conf.host,
                            NS.conf.port),
                    headers=HEADERS,
                    auth=NS.conf.credentials,
                    data=datasource_json)

    return resp


def create_datasource(datasource_dir,datasource_name):
    datasource_path = os.path.join(datasource_dir,
                                    "{}.conf.yml".format(datasource_name))
    if os.path.exists(datasource_path):
        datasource_data = fread(datasource_path)
        try:
            cfg = NS.datasource_conf
            url = "http://" + str(cfg.host) + ":" + str(cfg.port)
            dsjson = {'name':cfg.name,'type':cfg.type ,'url':url,'access' : cfg.access , 'basicAuth': cfg.basicAuth,'isDefault': cfg.isDefault}
            ret = post_datasource(json.dumps(dsjson))
            return ret.status_code
        except Exception:
            traceback.print_stack()
            raise Exception
        return ret
    else:
        raise FileNotFoundException
