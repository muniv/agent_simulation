# MBTI 다중 에이전트 시뮬레이션

MBTI 성격 유형을 가진 여러 에이전트들이 대화하고 상호작용하는 시뮬레이션입니다.

## 🚀 시작하기

### 1. 저장소 클론
```bash
git clone https://github.com/muniv/agent_simulation.git
cd agent_simulation
```

### 2. 가상환경 설정
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 필요한 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. OpenAI API 키 설정
1. 프로젝트 루트 폴더에 `.env` 파일 생성
2. 아래 내용 추가 (자신의 API 키로 교체)
```
OPENAI_API_KEY=your-api-key-here
```

## 💻 실행하기

### 기본 예제 실행
```bash
# Windows
python -m mbti_simulation.examples.emergency_meeting

# macOS/Linux
python3 -m mbti_simulation.examples.emergency_meeting
```

### 사용 가능한 예제들
- `emergency_meeting.py`: 긴급 안보회의 시나리오
- `family_dinner.py`: 가족 저녁 식사 시나리오
- `historical_meeting.py`: 역사적 회담 시나리오
- `cafe_meeting.py`: 카페 소개팅 시나리오

## 🎨 새로운 시나리오 만들기

1. `examples` 폴더에 새 Python 파일 생성 (예: `my_scenario.py`)
2. 아래 템플릿 사용:

```python
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from mbti_simulation.core.agent import MBTIAgent
from mbti_simulation.core.world import SimulationWorld

# 에이전트 생성
agent1 = MBTIAgent(
    name="홍길동",
    mbti_type="ENFJ",
    background="""
    32살 회사원
    성격이 밝고 적극적
    팀 프로젝트를 이끄는 것을 좋아함
    """
)

agent2 = MBTIAgent(
    name="김철수",
    mbti_type="ISTP",
    background="""
    28살 프리랜서
    기술적인 문제 해결을 잘함
    조용하지만 실력있는 전문가
    """
)

# 시뮬레이션 환경 설정
location = "카페"
scenario = """
프로젝트 미팅을 위해 만난 두 사람
- 새로운 웹서비스 개발 논의 중
- 서로 다른 접근 방식을 선호
- 좋은 방향을 찾아가려 노력 중
"""

# 시뮬레이션 월드 생성 및 실행
world = SimulationWorld(
    location=location,
    scenario=scenario,
    agents=[agent1, agent2]  # 원하는 만큼 에이전트 추가 가능
)

# 원하는 턴 수만큼 시뮬레이션 실행
world.run(turns=5)
```

## ⚙️ 주요 설정

### MBTI 유형
- 16가지 MBTI 유형 중 선택 (예: ENFJ, ISTP, ENTJ 등)
- 각 에이전트의 성격을 결정

### 시뮬레이션 설정
- `location`: 상황이 벌어지는 장소
- `scenario`: 상황 설명과 배경
- `turns`: 시뮬레이션 진행 턴 수
- `agents`: 참여하는 에이전트들의 리스트

## ⚠️ 주의사항

1. OpenAI API 사용량에 따라 비용이 발생할 수 있습니다
2. API 키는 절대 공개하지 마세요
3. `.env` 파일은 깃허브에 올리지 마세요
4. 시뮬레이션 결과는 매번 다르게 나올 수 있습니다

## 🤔 문제해결

- "API key not found" 에러 → `.env` 파일 확인
- 모듈 임포트 에러 → 가상환경 활성화 확인
- OpenAI API 에러 → API 키 유효성 확인

## 📝 라이선스

MIT License 