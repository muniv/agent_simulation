import os
from dotenv import load_dotenv
import openai

# .env 파일 로드
load_dotenv()

# OpenAI API 키 설정
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-default-api-key-here')
openai.api_key = OPENAI_API_KEY

# 기타 설정들
DEFAULT_MODEL = "gpt-4o"
DEFAULT_TEMPERATURE = 0.7

# API 키 확인
def check_api_key():
    if not OPENAI_API_KEY:
        raise ValueError("OpenAI API key is not set. Please set it in .env file or environment variables.")
    return True 