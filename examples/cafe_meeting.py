# examples/cafe_meeting.py
import os
import sys
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()

sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agent_simulation.core.agent import MBTIAgent
from agent_simulation.core.world import SimulationWorld

# MBTI 에이전트 생성
intj_man = MBTIAgent(
    name="서준호",
    mbti_type="INTJ",
    background="""
    29살 IT 개발자
    취미는 독서와 클래식 음악 감상
    조용하고 분석적인 성격이지만 관심 있는 주제에 대해서는 열정적으로 대화함
    """
)

enfp_woman = MBTIAgent(
    name="김다은",
    mbti_type="ENFP",
    background="""
    27살 프리랜서 일러스트레이터
    취미는 여행과 새로운 카페 탐방
    활발하고 호기심 많은 성격으로 다양한 주제에 관심이 많음
    """
)

# 시뮬레이션 환경 설정
location = "서울 연남동의 아늑한 카페"
scenario = """
친구의 소개로 처음 만난 소개팅
- 상황: 토요일 오후 2시, 따뜻한 분위기의 카페
- 서로에 대해 알아가는 첫 만남
- 공통 관심사를 찾아가며 대화를 나누는 중
"""

# 시뮬레이션 월드 생성 및 실행
world = SimulationWorld(
    location=location,
    scenario=scenario,
    agents=[intj_man, enfp_woman]
)

# 6턴 동안 시뮬레이션 실행
world.run(turns=6)