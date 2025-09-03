import boto3
from PIL import Image
from io import BytesIO

s3 = boto3.client('s3')   # create S3 client

def lambda_handler(event, context):
    bucket = key = "unknown"

    try:
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = event['Records'][0]['s3']['object']['key']

        print(f"Processing image {key} from bucket {bucket}")

        # 1. Download original image
        response = s3.get_object(Bucket=bucket, Key=key)
        img_data = response['Body'].read()

        # 2. Open and resize
        img = Image.open(BytesIO(img_data))
        img = img.resize((128, 128))

        # 3. Save to buffer
        buffer = BytesIO()
        img.save(buffer, "JPEG")
        buffer.seek(0)

        # 4. Upload to destination bucket
        s3.put_object(
            Bucket="resized-images-bucket-v1",
            Key=key,
            Body=buffer,
            ContentType="image/jpeg"
        )

        print(f"✅ Resized image saved to resized-images-bucket-v1/{key}")

    except Exception as e:
        print(f"❌ Error processing object {key} from bucket {bucket}: {e}")

