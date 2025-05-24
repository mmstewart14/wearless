import boto3
from classification.classify_outfit import Outfit


def write_items_to_table(table_name: str, items: list[Outfit]):
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.Table(table_name)

    chunk_size = 25  # DyanmoDB can only handle batch writing up to 25 items
    chunks = [items[i : i + chunk_size] for i in range(0, len(items), chunk_size)]

    for chunk in chunks:
        with table.batch_writer() as writer:
            for item in chunk:
                writer.put_item(Item=item.to_json())
