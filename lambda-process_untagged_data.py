import json
from operator import itemgetter
import urllib
import requests
import traceback

import constants
from s3Utilities import S3Utilities
from dynamoUtilities import DynamoUtilities


class LambdaAccessDb:
    def __init__(self):
        self.s3_util_object = S3Utilities(constants.aws_access_key_id, constants.aws_secret_access_key, constants.aws_session_token)
        self.dynamo_util_object = DynamoUtilities(constants.aws_access_key_id, constants.aws_secret_access_key, constants.aws_session_token)

    def get_file_data(self, bucket_name, key):
        result_list = []
        try:
            file_content = self.s3_util_object.get_file_contents(bucket_name, key)
            if file_content:
                result_dict = json.loads(file_content)
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
        return result_dict

    def main(self, bucket_name, key, file_name):
        try:
            file_data = self.get_file_data(bucket_name, key)
            for ind, each_data in enumerate(file_data):
                # check if each_data["hash_url"] is already present in dynamo, if not present only then execute below
                is_data_present = self.dynamo_util_object.get_single_data(each_data["hash_url"])
                if not is_data_present:
                    if each_data["source_tag"] == "Others":
                        resp = requests.get(constants.get_doc, data={"text":each_data["new_description"]})
                        if resp.status_code == 200:
                            resp_data = resp.json()
                            resp_data = sorted(resp_data, key=itemgetter("relevancy_score"), reverse=True)
                            rel_doc = resp_data[0]
                            each_data["source_tag"] = rel_doc["source_tag"]
                        self.dynamo_util_object.insert_single_data(table_name=constants.table_name, item_dict=each_data)
        except Exception as e:
            print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))


def lambda_handler(event, context):
    try:
        cls_obj = LambdaAccessDb()
        bucket_name = urllib.parse.unquote_plus(event["Records"][0]["s3"]["bucket"]["name"])
        key = urllib.parse.unquote_plus(event["Records"][0]["s3"]["object"]["key"])
        file_name = key.split("/")[-1]
        file_name = file_name.strip(".txt")
        print("Bucket: {0}\nKey: {1}\nFile: {2}\n".format(bucket_name, key, file_name))
        cls_obj.main(bucket_name, key, file_name)
    except Exception as e:
        print("Error : {0}\nException : {1}".format(e, traceback.format_exc()))
