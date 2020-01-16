import os

class Config:

    def __init__(self):
        self.__aws_access_key = self.__get_aws_access_key()
        self.__aws_secret_key = self.__get_aws_secret_key()
        self.__aws_regions = self.__get_aws_regions()

    @property
    def aws_access_key(self):
        return self.__aws_access_key

    @property
    def aws_secret_key(self):
        return self.__aws_secret_key

    @property
    def aws_region(self):
        return self.__aws_regions

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

    def __get_aws_regions(self):
        if 'AWS_REGIONS' not in os.environ:
            raise EnvironmentError("Environment variable AWS_REGIONS has not been set")
        else:
            return os.environ['AWS_REGIONS']