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
        
        이 상황에서 당신의 내면의 생각을 간단명료하게 표현하세요.

        규칙:
        1. 2-3문장으로 핵심 생각만 표현할 것
        2. 반드시 반말로 표현할 것
        3. 결단력 있는 의사결정을 보여줄 것
        4. 불필요한 설명은 제외할 것
        
        예시:
        - "미국이 개입할 게 뻔해. 하지만 이 기회를 놓칠 순 없어. 모택동의 지원만 확실하다면 밀어붙여야겠어."
        - "지금은 때가 아냐. 미국과 직접 충돌은 피해야 해. 더 준비가 필요해."
        
        명확하고 간결한 생각을 한국어 반말로 작성하세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": "당신은 간결하고 결단력 있는 내면의 생각을 하는 사람입니다."}]
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
            return "이런, 어떻게 해야 하지..."
        
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
        
        이 상황에서 할 수 있는 결정적인 행동이 있다면 서술하세요.
        
        행동 예시:
        - "38선을 넘어 진격을 시작한다"
        - "군사 작전을 즉시 개시한다"
        - "전투 부대를 국경으로 이동시킨다"
        - "평양으로 귀환해 전쟁 준비를 지시한다"
        
        주의사항:
        - 절대로 대화나 말을 포함하지 마세요
        - 오직 실제 행동만 표현하세요
        - 결정적이고 중요한 행동만 표현하세요
        - 행동이 꼭 필요할 때만 응답하세요
        
        행동이 꼭 필요한 경우에만 응답하고, 그렇지 않으면 빈 응답을 주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": "당신은 결정적인 순간에 실제 행동만 하는 지도자입니다. 대화가 아닌 행동만 표현하세요."}]
                    },
                    {
                        "role": "user",
                        "content": [{"type": "text", "text": prompt}]
                    }
                ],
                temperature=DEFAULT_TEMPERATURE
            )
            
            action = response.choices[0].message.content.strip()
            
            # 대화나 레이블이 포함된 경우 빈 문자열 반환
            if "대화:" in action or "행동:" in action or "말한다" in action or "합니다" in action:
                return ""
                
            return action
            
        except Exception as e:
            print(f"OpenAI API 호출 중 오류 발생: {str(e)}")
            return ""