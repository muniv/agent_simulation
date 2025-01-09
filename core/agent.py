from .personality import MBTIPersonality
from openai import OpenAI
from ..config import DEFAULT_MODEL, DEFAULT_TEMPERATURE, check_api_key

class MBTIAgent:
    def __init__(self, name: str, mbti_type: str, background: str):
        self.name = name
        self.personality = MBTIPersonality(mbti_type)
        self.background = background
        self.memory = []
        check_api_key()  # API 키 확인
        self.client = OpenAI()
        
    def think(self, context: str) -> str:
        """MBTI 특성을 반영한 내면의 생각 생성"""
        prompt = f"""
        당신은 {self.name}입니다.
        MBTI: {self.personality.mbti_type}
        배경: {self.background}
        
        현재 상황: {context}
        
        당신의 MBTI 성격 유형을 반영하여, 이 상황에서 어떤 생각이 드는지 1-2문장으로 표현해주세요.
        생각은 반드시 한국어로 작성해주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "system", 
                        "content": [{"type": "text", "text": "당신은 MBTI 성격 유형에 따라 생각하고 행동하는 사람입니다."}]
                    },
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": prompt}]
                    }
                ],
                temperature=DEFAULT_TEMPERATURE
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API 호출 중 오류 발생: {str(e)}")
            return f"[오류 발생: 기본 응답] {self.name}이(가) 상황을 고려하고 있습니다."
        
    def speak(self, context: str) -> str:
        """MBTI 특성을 반영한 대화 생성"""
        prompt = f"""
        당신은 {self.name}입니다.
        MBTI: {self.personality.mbti_type}
        배경: {self.background}
        
        현재 상황: {context}
        
        당신의 MBTI 성격 유형을 반영하여, 이 상황에서 어떤 대화를 할지 1-2문장으로 표현해주세요.
        대화는 반드시 한국어로 작성해주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": "당신은 MBTI 성격 유형에 따라 생각하고 행동하는 사람입니다."}]
                    },
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": prompt}]
                    }
                ],
                temperature=DEFAULT_TEMPERATURE
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API 호출 중 오류 발생: {str(e)}")
            return f"[오류 발생: 기본 응답] {self.name}: 네, 알겠습니다."
            
    def act(self, context: str) -> str:
        """MBTI 특성을 반영한 행동 생성"""
        prompt = f"""
        당신은 {self.name}입니다.
        MBTI: {self.personality.mbti_type}
        배경: {self.background}
        
        현재 상황: {context}
        
        당신의 MBTI 성격 유형을 반영하여, 이 상황에서 어떤 행동을 할지 서술하세요.
        반드시 실제 물리적 행동으로만 표현하세요. (예: "노트북을 열고 회의록을 작성한다", "자리에서 일어나 화이트보드 앞으로 걸어간다")
        대화나 생각이 아닌 행동만을 한국어로 작성해주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": "당신은 MBTI 성격 유형에 따라 행동하는 사람입니다. 반드시 실제 물리적 행동만을 서술하세요."}]
                    },
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": prompt}]
                    }
                ],
                temperature=DEFAULT_TEMPERATURE
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"OpenAI API 호출 중 오류 발생: {str(e)}")
            return f"{self.name}이(가) 자리에서 가만히 앉아있다."