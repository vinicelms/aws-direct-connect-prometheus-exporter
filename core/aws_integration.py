import boto3
from config import Config

CONFIG = Config()

class AWSInfo:

    def __init__(self):
        self.__client = boto3.client(
            aws_access_key_id=CONFIG.aws_access_key,
            aws_secret_access_key=CONFIG.aws_secret_key,
            service_name='directconnect'
        )

class DirectConnect:

    def __init__(self):
        self.owner_account = None
        self.connection_id = None
        self.region = None
        self.location = None
        self.bandwidth = None
        self.tags = {}

class VirtualInterface:

    def __init__(self):
        pass

class BGP:

    def __init__(self):
        pass