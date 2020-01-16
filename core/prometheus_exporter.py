from prometheus_client.core import GaugeMetricFamily
import prometheus_client as prom
from aws_integration import AWSInfo
import logging
import time

class AWSDCExporter:

    def __init__(self):
        pass

    def collect(self):
        logging.info("Starting the information gathering process")
        aws = AWSInfo()
        dc_list = aws.list_direct_connect()

        for dc in dc_list:
            for vi in dc.virtual_interfaces:
                for bgp in vi.bgp:
                    label_list = [
                        'owner_account',
                        'connection_id',
                        'connection_name',
                        'connection_region',
                        'connection_location',
                        'connection_bandwidth',
                        'virtual_interface_id',
                        'virtual_interface_name',
                        'virtual_interface_region',
                        'virtual_interface_type',
                        'virtual_interface_state',
                        'bgp_id',
                        'bgp_address_family',
                        'bgp_amazon_address',
                        'bgp_customer_address',
                        'bgp_state',
                        'bgp_status'
                    ]
                    label_values = [
                        dc.owner_account,
                        dc.connection_id,
                        dc.name,
                        dc.region,
                        dc.location,
                        dc.bandwidth,
                        vi.id,
                        vi.name,
                        vi.region,
                        vi.type,
                        vi.state,
                        bgp.id,
                        bgp.address_family,
                        bgp.amazon_address,
                        bgp.customer_address,
                        bgp.state,
                        bgp.status
                    ]
                    logging.debug("Values ​​Generated: {}".format(label_values))

                    gauge = GaugeMetricFamily(
                        name="dc_status".format(dc.name, vi.name),
                        documentation="Virtual Interface info",
                        labels = label_list
                    )
                    gauge.add_metric(
                        labels=label_values,
                        value=0
                    )
                    logging.info("Gauge returned!")
                    yield gauge

if __name__ == "__main__":
    logging.info("Starting")
    custom_exporter = AWSDCExporter()
    prom.REGISTRY.register(custom_exporter)
    prom.start_http_server(9120)

    while True:
        time.sleep(10)
