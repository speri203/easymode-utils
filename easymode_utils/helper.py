import re
from typing import Optional
from .exceptions import UnsupportedServiceARN


def split_arn_components(pattern: str, arn: str) -> Optional[dict]:
    match = re.match(pattern, arn)
    if match:
        return match.groupdict()
    return None


def decode_arn_components(arn: str) -> Optional[dict]:
    if "s3" in arn:
        pattern = r"^arn:(?P<partition>[^:]+):s3:(?P<region>[^:]+):(?P<account_id>[^:]+):(?P<bucket>[^/]+)/(?P<object_key>.+)$"
        return split_arn_components(pattern, arn)
    elif "dynamodb" in arn:
        pattern = r"^arn:(?P<partition>[^:]+):dynamodb:(?P<region>[^:]+):(?P<account_id>[^:]+):table/(?P<table_name>[^/]+)$"
        return split_arn_components(pattern, arn)
    elif "lambda" in arn:
        pattern = r"^arn:(?P<partition>[^:]+):lambda:(?P<region>[^:]+):(?P<account_id>[^:]+):function:(?P<function_name>[^:]+)$"
        return split_arn_components(pattern, arn)
    else:
        raise UnsupportedServiceARN(
            message=f"The ARN provided is not currently supported {arn}"
        )
