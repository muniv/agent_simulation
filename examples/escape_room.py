import os
import sys
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agent_simulation.core.agent import MBTIAgent
from agent_simulation.core.world import SimulationWorld

# MBTI 에이전트 생성
detective = MBTIAgent(
    name="강민수",
    mbti_type="INTJ",  # 분석적이고 전략적인 문제해결사
    background="""
    28살 추리 게임 마니아
    논리적 사고에 능숙하며 퍼즐 해결을 좋아함
    방탈출 카페 100회 이상 경험
    """
)

hacker = MBTIAgent(
    name="이지은",
    mbti_type="ISTP",  # 실용적인 문제해결사
    background="""
    25살 컴퓨터공학 대학원생
    전자기기와 암호 해독에 전문가
    즉흥적이지만 위기상황에서 뛰어난 대처능력 보유
    """
)

explorer = MBTIAgent(
    name="박준호",
    mbti_type="ENFP",  # 창의적이고 열정적인 탐험가
    background="""
    31살 여행 작가
    엉뚱하지만 기발한 아이디어를 잘 떠올림
    호기심이 많아 구석구석 살피는 것을 좋아함
    """
)

leader = MBTIAgent(
    name="김서연",
    mbti_type="ESTJ",  # 체계적인 리더
    background="""
    27살 스타트업 대표
    팀원들의 의견을 잘 조율하고 시간 관리에 철저함
    압박감 속에서도 침착하게 판단하는 능력이 있음
    """
)

# 시뮬레이션 환경 설정
location = "고난이도 방탈출 카페 - 실험실 테마"
scenario = """
4명의 참가자들이 도전한 방탈출 게임의 마지막 15분
- 현재 최종 방에 도달했으나 시간이 얼마 남지 않음
- 책상 위에는 복잡한 화학 실험 도구들이 놓여있음
- 컴퓨터 화면에는 암호가 걸린 프로그램이 실행 중
- 벽면에는 수상한 차트와 수식들이 붙어있음
- UV랜턴, 시험관, 태블릿PC 등 다양한 도구가 있음

발견된 단서들:
1. 컴퓨터의 암호는 4자리 숫자
2. 시험관에는 서로 다른 색상의 액체가 들어있음
3. 벽면 차트의 일부가 형광물질로 그려져 있음
4. 태블릿PC에는 미완성된 화학식이 표시되어 있음
"""

# 시뮬레이션 월드 생성 및 실행
world = SimulationWorld(
    location=location,
    scenario=scenario,
    agents=[detective, hacker, explorer, leader]
)

# 5턴 동안 시뮬레이션 실행
world.run(turns=5) 