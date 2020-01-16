import boto3
from config import Config

CONFIG = Config()

class AWSInfo:

    def __init__(self):
        self.__client = boto3.client(
            aws_access_key_id=CONFIG.aws_access_key,
            aws_secret_access_key=CONFIG.aws_secret_key,
            service_name='directconnect',
            region_name=CONFIG.aws_region
        )

    def list_direct_connect(self):
        conns = self.__client.describe_connections()
        for conn in conns['connections']:
            dc = DirectConnect()
            dc.owner_account = conn['ownerAccount']
            dc.connection_id = conn['connectionId']
            dc.name = conn['connectionName']
            dc.region = conn['region']
            dc.location = conn['location']
            dc.bandwidth = conn['bandwidth']
            dc.tags = self.__get_tag_as_dict(conn['tags'])
            dc.virtual_interfaces = self.__list_virtual_interfaces(conn['connectionId'])
            yield dc

    def __get_tag_as_dict(self, tag_list):
        tag_dict = {}
        for tag in tag_list:
            tag_dict[tag['key']] = tag['value']

        return tag_dict

    def __list_virtual_interfaces(self, direct_connect_id):
        vir_ints = self.__client.describe_virtual_interfaces(
            connectionId=direct_connect_id
        )
        vi_list = []

        for vir_int in vir_ints['virtualInterfaces']:
            vi = VirtualInterface()
            vi.id = vir_int['virtualInterfaceId']
            vi.name = vir_int['virtualInterfaceName']
            vi.region = vir_int['region']
            vi.type = vir_int['virtualInterfaceType']
            vi.state = vir_int['virtualInterfaceState']

            for bgp_info in vir_int['bgpPeers']:
                bgp = BGP()
                bgp.id = bgp_info['bgpPeerId']
                bgp.address_family = bgp_info['addressFamily']
                bgp.amazon_address = bgp_info['amazonAddress']
                bgp.customer_address = bgp_info['customerAddress']
                bgp.state = bgp_info['bgpPeerState']
                bgp.status = bgp_info['bgpStatus']
                vi.bgp = bgp

            vi_list.append(vi)

        return vi_list

class DirectConnect:

    def __init__(self):
        self.owner_account = None
        self.connection_id = None
        self.name = None
        self.region = None
        self.location = None
        self.bandwidth = None
        self.tags = {}
        self.__virtual_interfaces = []

    @property
    def virtual_interfaces(self):
        return self.__virtual_interfaces

    @virtual_interfaces.setter
    def virtual_interfaces(self, value):
        self.__virtual_interfaces.extend(value)

class VirtualInterface:

    def __init__(self):
        self.id = None
        self.name = None
        self.region = None
        self.type = None
        self.state = None
        self.__bgp = []

    @property
    def bgp(self):
        return self.__bgp

    @bgp.setter
    def bgp(self, value):
        self.__bgp.append(value)

class BGP:

    def __init__(self):
        self.id = None
        self.address_family = None
        self.amazon_address = None
        self.customer_address = None
        self.state = None
        self.status = None