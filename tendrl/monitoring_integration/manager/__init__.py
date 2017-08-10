import __builtin__
import traceback
import sys
import json


import maps
import gevent


from tendrl.monitoring_integration.grafana import utils
from tendrl.monitoring_integration.grafana import exceptions
from tendrl.monitoring_integration.grafana import dashboard
from tendrl.monitoring_integration.grafana import datasource
from tendrl.commons import manager as common_manager
from tendrl import monitoring_integration
from tendrl.monitoring_integration import sync


class MonitoringIntegrationManager(common_manager.Manager):

    def __init__(self):
        self._complete = gevent.event.Event()
        super(
            MonitoringIntegrationManager,
            self
        ).__init__(
            NS.state_sync_thread
        )


    def start():
        pass

    def stop():
        pass


def main():


    monitoring_integration.MonitoringIntegrationNS()

    TendrlNS()

    NS.state_sync_thread = MonitoringIntegrationSdsSyncThread()


    monitoring_integration_manager = MonitoringIntegrationManager()
    monitoring_integration_manager.start()
    complete = gevent.event.Event()


    def shutdown():
        complete.set()

    gevent.signal(signal.SIGTERM, shutdown)
    gevent.signal(signal.SIGINT, shutdown)

    while not complete.is_set():
        complete.wait(timeout=1)


    # Creating Default Dashboards
    dashboards = []
    config = utils.get_conf("/etc/tendrl/monitoring-integration/" +
                            "monitoring-integration.conf.yaml")
    setattr(__builtin__, "NS", maps.NamedDict())
    setattr(NS, "conf", config)

    dashboards = dashboard.get_all_dashboards()

    title = []

    for dashboard_json in dashboards:
        title.append(dashboard_json["uri"].split('/')[1])

    for dashboard_json in config.dashboards:
        if dashboard_json in title:
            sys.stdout.write('\n' + "Dashboard " + str(dashboard_json) +
                             " already exists" + '\n')
            continue
        response = dashboard.create_dashboard(dashboard_json)

        if response.status_code == 200:
            sys.stdout.write('\n' + "Dashboard " + str(dashboard_json) +
                             " uploaded successfully" + '\n')
        else:
            sys.stdout.write('\n' + "Dashboard " + str(dashboard_json) +
                             " upload failed with error code " +
                             str(response.status_code) + '\n')
    try:
        dashboard_json = dashboard.get_dashboard(config.home_dashboard)

        if 'dashboard' in dashboard_json:
            dashboard_id = dashboard_json.get('dashboard').get('id')
            response = dashboard.set_home_dashboard(dashboard_id)

            response = dashboard.set_home_dashboard(dashboard_id)
            if response.status_code == 200:
                sys.stdout.write('\n' + "Dashboard " +
                                 str(config.home_dashboard) +
                                 " is set as home dashboard" + '\n')
        else:
            sys.stdout.write('\n' + str(dashboard_json.get('message')) + '\n')
    except exceptions.ConnectionFailedException:
        traceback.print_exc()
        raise exceptions.ConnectionFailedException

    # Creating datasource
    response = datasource.create_datasource()
    if response.status_code == 200:
        sys.stdout.write('\n' + "Datasource " +
                         " uploaded successfully" + '\n')
    else:
        if isinstance(json.loads(response._content), list):
            message = str(json.loads(response._content)[0]["message"])
        else:
            message = str(json.loads(response._content)["message"])
        sys.stdout.write('\n' + "Datasource " +
                         " upload failed with" + '\n' + "Message \"" +
                         message + "\"" +
                         " and Error code " + str(response.status_code) + '\n')


if __name__ == '__main__':
    main()

