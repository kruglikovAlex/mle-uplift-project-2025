import os 
from dotenv import load_dotenv

# подгружаем .env
load_dotenv()

os.environ["MLFLOW_S3_ENDPOINT_URL"] = "https://storage.yandexcloud.net" 
os.environ['AWS_ACCESS_KEY_ID'] = os.getenv('AWS_ACCESS_KEY_ID')
os.environ["AWS_SECRET_ACCESS_KEY"] = os.getenv('AWS_SECRET_ACCESS_KEY')
os.environ["AWS_BUCKET_NAME"] = os.getenv('S3_BUCKET_NAME')
os.environ["DB_DESTINATION_USER"] = os.getenv('DB_DESTINATION_USER')
os.environ["DB_DESTINATION_PASSWORD"] = os.getenv('DB_DESTINATION_PASSWORD')
os.environ["DB_DESTINATION_HOST"] = os.getenv('DB_DESTINATION_HOST')
os.environ["DB_DESTINATION_PORT"] = os.getenv('DB_DESTINATION_PORT')
os.environ["DB_DESTINATION_NAME"] = os.getenv('DB_DESTINATION_NAME')