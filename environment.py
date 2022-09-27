from dotenv_config import Config

config = Config('.env')

nutrition_api_key = config('NUTRITION_API_KEY')
nutrition_api_appid = config('NUTRITION_API_APPLICATION_ID')
nutrition_api_end_point = config('NUTRITION_API_END_POINT')
nutrition_gener = config('NUTRITION_GENDER')
nutrition_weight = config('NUTRITION_WEIGHT')
nutrition_height_cm = config('NUTRITION_HEIGHT_CM')
nutrition_age = config('NUTRITION_AGE')

sheety_api_endpoint = config('SHEETY_API_END_POINT')
sheety_api_bearer_token = config('SHEETY_API_BEARER_TOKEN')
