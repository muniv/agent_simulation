import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from mbti_simulation.core.agent import MBTIAgent
from mbti_simulation.core.world import SimulationWorld

# MBTI 에이전트 생성
isfj_mom = MBTIAgent(
    name="김미영",
    mbti_type="ISFJ",
    background="""
    45살 전업주부
    요리와 베이킹이 취미
    가족을 챙기는 것을 좋아하며 따뜻한 성격의 소유자
    최근 SNS로 요리 레시피를 공유하는 것에 관심이 생김
    """
)

entp_daughter = MBTIAgent(
    name="서지은",
    mbti_type="ENTP",
    background="""
    17살 고등학생
    호기심이 많고 새로운 것을 시도하기를 좋아함
    학교 토론동아리 회장
    요즘 채식에 관심이 생겨 이것저것 시도해보는 중
    """
)

# 시뮬레이션 환경 설정
location = "가족의 주방"
scenario = """
평화로운 주말 저녁 식사 준비 시간
- 엄마는 평소처럼 가족 저녁을 준비하려 했으나
- 딸이 채식 요리를 같이 만들어보자고 제안한 상황
- 엄마는 전통적인 요리를 선호하지만 딸의 관심사를 존중하려 노력 중
- 새로운 레시피를 함께 시도해보며 대화를 나누는 중
"""

# 시뮬레이션 월드 생성 및 실행
world = SimulationWorld(
    location=location,
    scenario=scenario,
    agents=[isfj_mom, entp_daughter]
)

# 6턴 동안 시뮬레이션 실행
world.run(turns=6) 