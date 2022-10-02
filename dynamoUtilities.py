import boto3
import traceback
from boto3.dynamodb.conditions import Key, And, NotEquals, Attr


class DynamoUtilities:
    def __init__(self, access_key_id, secret_access_key, session_key=None, region_name = "us-east-1"):
        self.max_allowed_batch_writing = 25
        try:
            # Ref: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html
            if session_key:
                self.dynamo_resource = boto3.resource("dynamodb", aws_access_key_id=access_key_id,
                                                      aws_secret_access_key=secret_access_key,
                                                      aws_session_token=session_key,
                                                      region_name=region_name)
            else:
                self.dynamo_resource = boto3.resource("dynamodb", aws_access_key_id=access_key_id,
                                                      aws_secret_access_key=secret_access_key,
                                                      region_name=region_name)
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))

    def batch_write(self, table_name, list_of_dicts):
        try:
            print("Got total {0} data to write".format(len(list_of_dicts)))
            i = 0
            update_list = list_of_dicts[0:self.max_allowed_batch_writing]
            while update_list:
                print("Writing {0}-{1} data out of {2}".format(i, len(update_list) + i - 1, len(list_of_dicts)))
                api_compatible_list = []
                for each_dict in update_list:
                    key_list = list(each_dict.keys())
                    x = dict()
                    for each_key in key_list:
                        x[each_key] = each_dict[each_key]
                    final_dict = {'PutRequest': {'Item': x}}
                    api_compatible_list.append(final_dict)
                self.dynamo_resource.batch_write_item(RequestItems={table_name: api_compatible_list})
                i += self.max_allowed_batch_writing
                update_list = list_of_dicts[i:i + self.max_allowed_batch_writing]
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))

    def list_tables(self):
        table_list = []
        try:
            table_list = list(self.dynamo_resource.tables.all())
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))
        return table_list

    def delete_table(self, table_name):
        status = False
        try:
            self.dynamo_resource.delete_table(table_name)
            status = True
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))
        return status

    def get_data(self, table_name, condition_dict={}, projection_list=[]):
        # https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/LegacyConditionalParameters.KeyConditions.html
        result = []
        try:
            table_obj = self.dynamo_resource.Table(table_name)
            if not condition_dict and not projection_list:
                response = table_obj.scan(ConsistentRead=True)
                while "LastEvaluatedKey" in response:
                    response = table_obj.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
                    result.extend(response['Items'])
            elif not condition_dict and projection_list:
                projection_list = [each.strip() for each in projection_list if each.strip()]
                projections = ",".join(projection_list)
                response = table_obj.scan(ProjectionExpression=projections, ConsistentRead=True)
                while "LastEvaluatedKey" in response:
                    response = table_obj.scan(ExclusiveStartKey=response['LastEvaluatedKey'], ProjectionExpression=projections, ConsistentRead=True)
                    result.extend(response['Items'])
            elif condition_dict and not projection_list:
                response = table_obj.scan(ScanFilter=condition_dict, ConsistentRead=True)
                result = response['Items']
                while "LastEvaluatedKey" in response:
                    response = table_obj.scan(ExclusiveStartKey=response['LastEvaluatedKey'], ScanFilter=condition_dict, ConsistentRead=True)
                    result.extend(response['Items'])
            else:
                projection_list = [each.strip() for each in projection_list if each.strip()]
                projections = ",".join(projection_list)
                FilterExpression = And(*[(Key(key).eq(value)) for key, value in condition_dict.items()])
                response = table_obj.scan(ProjectionExpression=projections, FilterExpression=FilterExpression, ConsistentRead=True)
                while "LastEvaluatedKey" in response:
                    response = table_obj.scan(ExclusiveStartKey=response['LastEvaluatedKey'], ProjectionExpression=projections, FilterExpression=FilterExpression, ConsistentRead=True)
                    result.extend(response['Items'])
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))
        return result

    def incremental_update_data(self, table_name, condition_dict, frequency_value):
        status = False
        try:
            table_obj = self.dynamo_resource.Table(table_name)
            table_obj.update_item(Key=condition_dict,
                                  UpdateExpression="set Frequency = Frequency + :val",
                                  ExpressionAttributeValues={':val': frequency_value}
                                  )
            status = True
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))
        return status

    def insert_single_data(self, table_name, item_dict):
        status = False
        try:
            table_obj = self.dynamo_resource.Table(table_name)
            table_obj.put_item(Item=item_dict)
            status = True
        except Exception as e:
            print("Error: {0}\nException: {1}".format(e, traceback.format_exc()))
        return status
