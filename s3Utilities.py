import boto3
import logging
import traceback
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(Path(__file__).stem)

class S3Utilities:
    def __init__(self, access_key_id, secret_access_key, session_key=None):
        try:
            if session_key:
                self.s3_client = boto3.client("s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key, aws_session_token=session_key)
            else:
                self.s3_client = boto3.client("s3", aws_access_key_id=access_key_id, aws_secret_access_key=secret_access_key)
        except Exception as e:
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))

    def get_list_of_buckets(self, region_name=None):
        bucket_list = []
        try:
            bucket_list = self.s3_client.list_buckets()
            bucket_list_objects = bucket_list["Buckets"]
            bucket_list = []
            for each_bucket in bucket_list_objects:
                if region_name and self.s3_client.get_bucket_location(Bucket=each_bucket['Name'])['LocationConstraint'] == region_name:
                    bucket_list.append(each_bucket["Name"])
                else:
                    bucket_list.append(each_bucket["Name"])
        except Exception as e:
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))
        return bucket_list

    def create_bucket(self, bucket_name, region_name=None):
        create_status = False
        try:
            if region_name:
                self.s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={"LocationConstraint": region_name})
            else:
                self.s3_client.create_bucket(Bucket=bucket_name)
        except Exception as e:
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))
        return create_status

    def write_data(self, data, bucket, file_key, content_type=None):
        write_status, resp = False, None
        try:
            if content_type:
                # For content_type, please refer to http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.17 or https://stackoverflow.com/questions/34550816/aws-content-type-settings-in-s3-using-boto3
                resp = self.s3_client.put_object(Body=data, Bucket=bucket, Key=file_key, ContentType=content_type)
            else:
                resp = self.s3_client.put_object(Body=data, Bucket=bucket, Key=file_key)
            if resp and type(resp)==dict and "ResponseMetadata" in resp and "HTTPStatusCode" in resp["ResponseMetadata"] and resp["ResponseMetadata"]["HTTPStatusCode"] == 200:
                write_status = True
        except Exception as e:
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))
        return write_status

    def upload_file(self, file_path, bucket_name, file_key):
        upload_status = False
        try:
            self.s3_client.upload_file(file_path, bucket_name, file_key)
            upload_status = True
        except Exception as e:
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))
        return upload_status

    def get_list_of_files(self, bucket, prefix="/", max_files=1000):
        # if max_files=-1, all the objects are returned
        # if prefix is not provided, root is considered
        list_of_objects, error = [], True
        try:
            resp_obj = self.s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix)
            if resp_obj is not None and type(resp_obj) == dict and resp_obj.get("Contents", False) and resp_obj["Contents"]:
                list_of_objects = [each["Key"] for each in resp_obj["Contents"] if each["Key"] != prefix]
                if (max_files == -1 or max_files > len(list_of_objects)) and resp_obj.get("IsTruncated", False) and resp_obj["IsTruncated"] and resp_obj.get("NextContinuationToken", False) and resp_obj["NextContinuationToken"]:
                    next_token, is_truncated = resp_obj["NextContinuationToken"], resp_obj["IsTruncated"]
                    while is_truncated and next_token:
                        resp_obj = self.s3_client.list_objects_v2(Bucket=bucket, Prefix=prefix, ContinuationToken=next_token)
                        is_truncated, next_token = False, None
                        if resp_obj is not None and type(resp_obj) == dict and resp_obj.get("Contents", False) and resp_obj["Contents"]:
                            x = [each["Key"] for each in resp_obj["Contents"] if each["Key"] != prefix]
                            list_of_objects.extend(x)
                        if (max_files == -1 or max_files > len(list_of_objects)) and resp_obj.get("IsTruncated", False) and resp_obj["IsTruncated"] and resp_obj.get("NextContinuationToken", False) and resp_obj["NextContinuationToken"]:
                            next_token, is_truncated = resp_obj["NextContinuationToken"], resp_obj["IsTruncated"]
            error = False
        except Exception as e:
            error = True
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))
        return list_of_objects, error

    def get_file_contents(self, bucket_name, file_key):
        file_content = None
        try:
            content = self.s3_client.get_object(Bucket=bucket_name, Key=file_key)
            if content:
                content = content["Body"].read()
                file_content = content.decode("utf-8")
        except Exception as e:
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))
        return file_content

    def delete_object(self, bucket_name, file_key):
        status, resp = False, None
        try:
            resp = self.s3_client.delete_object(Bucket=bucket_name, Key=file_key)
            if resp and type(resp)==dict and "ResponseMetadata" in resp and "HTTPStatusCode" in resp["ResponseMetadata"] and resp["ResponseMetadata"]["HTTPStatusCode"] in [200, 204]:
                status = True
        except Exception as e:
            logger.error("{0}\n{1}".format(e, traceback.format_exc()))
        return status
