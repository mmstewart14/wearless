import uuid
import boto3
from boto3.dynamodb.conditions import Attr


def scan_for_random_item(table):
    random_id = uuid.uuid4()

    return table.scan(
        Limit=1,
        ExclusiveStartKey={
            'id': str(random_id)
        },
        FilterExpression=Attr('seasons').contains('Spring'),
        ReturnConsumedCapacity='TOTAL'
    )


def get_item(table_name: str, item_id: str):
    
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table(table_name)
    
    response = scan_for_random_item(table)

    if response['Items']:
       return response['Items'][0]
    
    else: # Catch edge case of starting at end of table
        response = scan_for_random_item(table)
        return response['Items'][0]

    