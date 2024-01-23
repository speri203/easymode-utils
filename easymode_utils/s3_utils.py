import boto3
from logger import LoggerUtils


class S3:
    def __init__(self, bucket_name: str) -> None:
        self.logger = LoggerUtils()
        self.client = boto3.client("s3")
        self.bucket_name = bucket_name
