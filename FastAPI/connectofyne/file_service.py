import boto3
from botocore.exceptions import ClientError
from config import config


class S3Service:
    def __init__(self):
        self.s3_client = boto3.client(
            "s3",
            region_name=config.AWS_REGION,
            aws_access_key_id=config.AWS_ACCESS_KEY_ID,
            aws_secret_access_key=config.AWS_SECRET_ACCESS_KEY,
        )

    def generate_upload_url(
        self, filename: str, content_type: str, folder="uploads", expires_in=600
    ):
        try:
            key = f"{folder}/{filename}"
            presigned_url = self.s3_client.generate_presigned_url(
                "put_object",
                Params={
                    "Bucket": config.S3_BUCKET_NAME,
                    "Key": key,
                    "ContentType": content_type,
                },
                ExpiresIn=expires_in,
            )
            return {"upload_url": presigned_url, "file_path": key}
        except ClientError as e:
            raise RuntimeError(f"Error generating upload URL: {e}")

    def generate_download_url(self, file_path: str, expires_in=600):
        try:
            presigned_url = self.s3_client.generate_presigned_url(
                "get_object",
                Params={"Bucket": config.S3_BUCKET_NAME, "Key": file_path},
                ExpiresIn=expires_in,
            )
            return {"download_url": presigned_url}
        except ClientError as e:
            raise RuntimeError(f"Error generating download URL: {e}")
