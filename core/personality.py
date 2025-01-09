# core/personality.py
class MBTIPersonality:
    def __init__(self, mbti_type: str):
        self.mbti_type = mbti_type.upper()
        self.traits = {
            'E/I': self.mbti_type[0],  # 외향/내향
            'S/N': self.mbti_type[1],  # 감각/직관
            'T/F': self.mbti_type[2],  # 사고/감정
            'J/P': self.mbti_type[3]   # 판단/인식
        }
        
    def get_thinking_style(self, situation: str) -> str:
        """MBTI 유형에 따른 생각 스타일 반환"""
        if self.traits['S/N'] == 'S':
            # 감각형: 구체적이고 현실적인 사고
            return f"구체적인 사실에 기반하여 생각: {situation}"
        else:
            # 직관형: 가능성과 패턴 중심의 사고
            return f"전체적인 패턴과 가능성 고려: {situation}"
            
    def get_decision_style(self, options: list) -> str:
        """MBTI 유형에 따른 의사결정 스타일 반환"""
        if self.traits['T/F'] == 'T':
            # 사고형: 논리적 분석
            return "논리적 분석을 통한 결정"
        else:
            # 감정형: 가치와 영향 고려
            return "감정과 가치를 고려한 결정"