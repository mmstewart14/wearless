import boto3


def list_images_in_bucket(bucket_name: str) -> list[str]:
    """
    Retrieves all images in S3 bucket

    Args:
        bucket_name (str): The name of the S3 bucket.

    Returns:
        bytes: The encoded image
    """

    s3_client = boto3.client("s3")
    image_keys = []

    try:
        response = s3_client.list_objects_v2(Bucket=bucket_name)

        for obj in response["Contents"]:
            obj_key = obj["Key"]

            if obj_key.endswith(".jpg"):
                image_keys.append(obj_key)

        return image_keys
    except Exception as e:
        print(f"Error listing objects: {e}")
        return None
