import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agent_simulation.core.agent import MBTIAgent
from agent_simulation.core.world import SimulationWorld

# MBTI 에이전트 생성
stalin = MBTIAgent(
    name="이오시프 스탈린",
    mbti_type="ISTJ",  # 규율, 질서, 체계를 중시하는 성향
    background="""
    71살 소련 최고지도자
    냉철한 전략가이자 독재자
    세계 공산화에 관심이 있으나 미국과의 직접 충돌은 피하고자 함
    중국의 영향력 확대를 견제하려는 의도도 있음
    """
)

kim_il_sung = MBTIAgent(
    name="김일성",
    mbti_type="ENTJ",  # 야망적이고 목표 지향적인 성향
    background="""
    38살 북한 지도자
    소련에서 군사 훈련을 받은 경험이 있음
    한반도 통일에 대한 강한 열망을 가지고 있음
    소련의 지원을 얻어 군사행동을 승인받고자 함
    """
)

# 시뮬레이션 환경 설정
location = "모스크바 크렘린궁 집무실"
scenario = """
1950년 4월, 한반도 군사작전 논의를 위한 극비 회담
- 김일성이 남한 진공 계획에 대한 승인을 요청하러 방문
- 스탈린은 미국의 개입 가능성을 우려
- 모택동의 지원 약속 여부가 중요한 변수
- 세계 정세와 군사적 위험을 저울질하는 중대한 순간
"""

# 시뮬레이션 월드 생성 및 실행
world = SimulationWorld(
    location=location,
    scenario=scenario,
    agents=[stalin, kim_il_sung]
)

# 6턴 동안 시뮬레이션 실행
world.run(turns=6) 