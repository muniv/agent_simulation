import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from mbti_simulation.core.agent import MBTIAgent
from mbti_simulation.core.world import SimulationWorld

# MBTI 에이전트 생성
enfj_boyfriend = MBTIAgent(
    name="최지웅",
    mbti_type="ENFJ",
    background="""
    31살 AI컨설턴트
    기록과 뇌과학에 깊은 관심이 있음
    여자친구 주혜를 매우 아끼고 서로의 관심사를 공유하는 것을 좋아함
    최근 뇌과학 관련 독서모임을 시작하려고 계획 중
    """
)

istj_girlfriend = MBTIAgent(
    name="박주혜",
    mbti_type="ISTJ",
    background="""
    33살 AI엔지니어
    NLP와 수학을 좋아하며 뇌과학에도 관심이 있음
    체계적이고 논리적인 성격
    조용히 책 읽는 것을 즐기며 새로운 지식을 탐구하는 것을 좋아함
    """
)

# 시뮬레이션 환경 설정
location = "대형 서점 인문학 코너"
scenario = """
주말 오후, 뇌과학 서적을 구경하러 서점에 방문한 커플
- 지웅은 주혜가 관심 있어할 뇌과학 신간을 미리 찾아왔음
- 주혜는 최근 NLP와 뇌과학의 연관성에 대해 연구 중
- 서점 한켠의 독서 공간에서 함께 책을 살펴보며 대화를 나누는 중
- 지웅이 계획 중인 독서모임에 대해 이야기하려고 함
"""

# 시뮬레이션 월드 생성 및 실행
world = SimulationWorld(
    location=location,
    scenario=scenario,
    agents=[enfj_boyfriend, istj_girlfriend]
)

# 6턴 동안 시뮬레이션 실행
world.run(turns=6) 