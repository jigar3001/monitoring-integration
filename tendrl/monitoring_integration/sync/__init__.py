import gevent

from tendrl.commons import sds_sync


class MonitoringIntegrationSdsSyncThread(sds_sync.StateSyncThread):

    def __init__(self):
        super(MonitoringIntegrationSdsSyncStateThread, self).__init__()
        self._complete = gevent.event.Event()

    def _run(self):
        pass

