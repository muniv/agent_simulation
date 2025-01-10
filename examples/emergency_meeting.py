import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agent_simulation.core.agent import MBTIAgent
from agent_simulation.core.world import SimulationWorld

# MBTI 에이전트 생성
president = MBTIAgent(
    name="윤대통령",
    mbti_type="ESTJ",  # 체계적, 결단력 있는 지도자
    background="""
    대한민국 대통령
    북한의 도발에 대한 강경한 대응을 선호
    미국과의 동맹을 매우 중시
    """
)

defense_minister = MBTIAgent(
    name="김장관",
    mbti_type="ISTJ",  # 신중하고 책임감 있는 참모
    background="""
    국방부 장관
    군사 전략 전문가
    실질적인 군사적 대응 능력을 중시
    """
)

intelligence_chief = MBTIAgent(
    name="박국장",
    mbti_type="INTP",  # 분석적이고 전략적인 참모
    background="""
    국가정보원장
    북한 내부 동향 분석 전문가
    다양한 시나리오를 고려하는 신중파
    """
)

foreign_minister = MBTIAgent(
    name="이장관",
    mbti_type="ENFJ",  # 외교적 감각이 뛰어난 참모
    background="""
    외교부 장관
    국제 관계 전문가
    외교적 해결을 선호
    미국, 중국과의 관계를 고려
    """
)

# 시뮬레이션 환경 설정
location = "청와대 지하 벙커 긴급 안보회의실"
scenario = """
북한이 심야에 미사일 도발을 감행한 직후의 긴급 안보회의
- 북한이 10분 전 동해상으로 ICBM급 미사일 발사
- 미사일은 일본 EEZ 인근 해상에 낙하
- 미국이 긴급 대응을 요청해온 상황
- 중국은 상황 악화를 경고하는 메시지 전달

현재 논의 중인 대응 방안:
1. 즉각적인 군사적 대응
2. 외교적 항의와 제재
3. 미국과 공조한 연합 군사훈련
4. 중국을 통한 중재 요청
"""

# 시뮬레이션 월드 생성 및 실행
world = SimulationWorld(
    location=location,
    scenario=scenario,
    agents=[president, defense_minister, intelligence_chief, foreign_minister]
)

# 5턴 동안 시뮬레이션 실행
world.run(turns=5) 