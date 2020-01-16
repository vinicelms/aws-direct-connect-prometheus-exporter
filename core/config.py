import os

class Config:

    def __init__(self):
        self.__aws_access_key = self.__get_aws_access_key()
        self.__aws_secret_key = self.__get_aws_secret_key()
        self.__aws_region = self.__get_aws_region()

    @property
    def aws_access_key(self):
        return self.__aws_access_key

    @property
    def aws_secret_key(self):
        return self.__aws_secret_key

    @property
    def aws_region(self):
        return self.__aws_region

    def __get_aws_access_key(self):
        if 'AWS_ACCESS_KEY' not in os.environ:
            raise EnvironmentError("Environment variable AWS_ACCESS_KEY has not been set")
        else:
            return os.environ['AWS_ACCESS_KEY']

    def __get_aws_secret_key(self):
        if 'AWS_SECRET_KEY' not in os.environ:
            raise EnvironmentError("Environment variable AWS_SECRET_KEY has not been set")
        else:
            return os.environ['AWS_SECRET_KEY']

    def __get_aws_region(self):
        if 'AWS_REGION' not in os.environ:
            raise EnvironmentError("Environment variable AWS_REGION has not been set")
        else:
            return os.environ['AWS_REGION']