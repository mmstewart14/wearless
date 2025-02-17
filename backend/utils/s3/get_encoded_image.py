import boto3
import base64


def get_encoded_image(bucket_name: str, object_key: str) -> str:
    """
    Retrieves an image from Amazon S3.

    Args:
        bucket_name (str): The name of the S3 bucket.
        object_key (str): The key of the object to retrieve.

    Returns:
        encoded_image (str): The base64 encoded image
    """

    s3_client = boto3.client("s3")

    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=object_key)
        encoded_image = base64.b64encode(response["Body"].read()).decode("utf-8")

        return encoded_image
    except Exception as e:
        print(f"Error retrieving object: {e}")
        return None
