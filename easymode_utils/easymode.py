from .s3_utils import S3


class EasyMode:
    def __init__(self, **kwargs) -> None:
        # fetching s3 client related information
        bucket_name = kwargs.get("bucket_name", None)

        # init resources
        self.s3 = S3(bucket_name)
