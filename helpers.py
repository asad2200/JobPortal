import random
import string
import boto3
from credentials import *

s3 = boto3.resource('s3', aws_access_key_id=S3_ACCESS_KEY_ID,
                    aws_secret_access_key=S3_SECRET_ACCESS_KEY)


def random_str(n=20):
    return "".join(random.choice(string.ascii_letters) for s in range(n))


def upload_s3(request):
    name = random_str(10)
    s3.Bucket("django-jobfinder-asad").put_object(Key=name,
                                                  Body=request.FILES["file"])
    return name


def get_s3(name):
    obj = s3.Object("django-jobfinder-asad", name)
    return obj.get()


def base64_encode(message):
    import base64
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message
