from dotenv_config import Config

config = Config('.env')

nutrition_api_key = config('NUTRITION_API_KEY')
nutrition_api_appid = config('NUTRITION_API_APPLICATION_ID')
nutrition_api_end_point = config('NUTRITION_API_END_POINT')