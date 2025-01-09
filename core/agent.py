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
        
        당신의 MBTI 성격 유형을 반영하여, 이 상황에서 어떤 생각이 드는지 내면의 목소리로 표현해주세요.

        규칙:
        1. 반드시 반말로 생각을 표현할 것
        2. 내면의 독백처럼 자연스럽게 표현할 것
        3. 다른 사람에게 말하는 것이 아닌, 혼잣말/생각으로 표현할 것
        
        예시:
        - 좋음: "음... 이 주제는 정말 흥미로운데? 더 자세히 물어봐야겠어."
        - 좋음: "역시 예상했던 대로 대화가 잘 풀리고 있어. 다음은 취미 얘기를 해볼까?"
        - 나쁨: "흥미로운 주제네요. 더 자세히 여쭤보고 싶습니다." (존댓말 사용)
        - 나쁨: "그런 생각을 하시는군요." (상대방에게 말하는 형식)
        
        생각은 반드시 한국어로, 반말로 작성해주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": "당신은 내면의 생각을 반말로 표현하는 사람입니다. 자연스러운 독백 형식으로 생각하세요."}]
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
            return f"(이런, 뭐라고 생각해야 할지 모르겠어...)"
        
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
        
        이 상황에서 할 수 있는 구체적인 물리적 행동을 서술하세요.
        
        현재 상황(서점)에서 가능한 행동 예시:
        - "책장에서 관심 있는 책을 꺼내 특정 페이지를 펼쳐 보여준다"
        - "스마트폰으로 책의 리뷰를 검색해서 화면을 보여준다"
        - "메모장을 꺼내 중요한 내용을 기록한다"
        - "독서모임 일정표가 적힌 다이어리를 펼쳐 보여준다"
        
        주의사항:
        - 말하는 것은 행동이 아닙니다 ("~라고 말한다" 금지)
        - 일상적이고 반복적인 행동은 제외 ("책을 본다" 같은 일반적 행동 금지)
        - 현재 상황에서 의미 있고 구체적인 행동만 표현하세요
        - 행동이 꼭 필요한 순간이 아니라면 하지 않아도 됩니다
        
        행동이 필요하다고 판단되면 구체적으로 서술하고, 그렇지 않으면 빈 응답을 주세요.
        """
        
        try:
            response = self.client.chat.completions.create(
                model=DEFAULT_MODEL,
                messages=[
                    {
                        "role": "system",
                        "content": [{"type": "text", "text": "당신은 상황에 맞는 의미 있는 물리적 행동만을 하는 에이전트입니다."}]
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
            if "대화:" in action or "행동:" in action or "말한다" in action:
                return ""
                
            return action
            
        except Exception as e:
            print(f"OpenAI API 호출 중 오류 발생: {str(e)}")
            return ""