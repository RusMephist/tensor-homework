import time
import re
from prometheus_client.core import GaugeMetricFamily, REGISTRY, CounterMetricFamily, Counter
from prometheus_client import start_http_server


def parseLastLine(path):
    f = open(path, 'r')
    lastLine = f.readlines()[-1]
    content = re.sub("[,()\n]", "", lastLine).split(" ")
    return content


class CustomCollector(object):
    def __init__(self):
        pass

    def collect(self):
        metrics = parseLastLine('/var/log/dd.log')

        copiedBytes = GaugeMetricFamily(
            'copied_bytes', 'Bytes copied', labels=['app'])
        copiedBytes.add_metric(["dd"], metrics[0])
        yield copiedBytes

        copiedMB = GaugeMetricFamily(
            'copied_megabytes', 'Megabytes copied', labels=['app'])
        copiedMB.add_metric(["dd"], metrics[2])
        yield copiedMB

        copiedMib = GaugeMetricFamily(
            'copied_mebibytes', 'Mebibytes copied', labels=['app'])
        copiedMib.add_metric(["dd"], metrics[4])
        yield copiedMib

        copyTime = GaugeMetricFamily(
            'total_time', 'Сopy time', labels=['app'])
        copyTime.add_metric(["dd"], metrics[7])
        yield copyTime

        currentSpeed = GaugeMetricFamily(
            'current_speed', 'Current write speed (MB/s)', labels=['app'])
        currentSpeed.add_metric(["dd"], metrics[9])
        yield currentSpeed


if __name__ == '__main__':
    start_http_server(8000)
    REGISTRY.register(CustomCollector())
    while True:
        stats = parseLastLine('/var/log/dd.log')
        print(
            f'Copied: {stats[0]} {stats[1]}, {stats[2]} {stats[3]}, {stats[4]} {stats[5]}, time: {stats[7]} {stats[8]}, Write speed: {stats[9]} {stats[10]}')
        time.sleep(5)
