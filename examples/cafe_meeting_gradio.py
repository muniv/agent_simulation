import os
import sys
from dotenv import load_dotenv
import gradio as gr
import time
import queue
import threading

load_dotenv()
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from agent_simulation.core.agent import MBTIAgent
from agent_simulation.core.world import SimulationWorld

def create_simulation(name1, mbti1, background1, name2, mbti2, background2, turns):
    conversation = ""  # 전체 대화를 누적할 변수
    try:
        # MBTI 에이전트 생성
        agent1 = MBTIAgent(
            name=name1,
            mbti_type=mbti1,
            background=background1
        )

        agent2 = MBTIAgent(
            name=name2,
            mbti_type=mbti2,
            background=background2
        )

        # 시뮬레이션 환경 설정
        location = "서울 연남동의 아늑한 카페"
        scenario = f"""
        친구의 소개로 처음 만난 소개팅
        - 상황: 토요일 오후 2시, 따뜻한 분위기의 카페
        - 서로에 대해 알아가는 첫 만남
        - 공통 관심사를 찾아가며 대화를 나누는 중
        """

        # 시뮬레이션 월드 생성 및 실행
        world = SimulationWorld(
            location=location,
            scenario=scenario,
            agents=[agent1, agent2]
        )

        # 초기 메시지들
        conversation += f"상황 설정:\n{scenario}\n\n"
        yield conversation
        time.sleep(1)

        conversation += f"참여자:\n1. {name1} ({mbti1}) - {background1}\n2. {name2} ({mbti2}) - {background2}\n\n"
        yield conversation
        time.sleep(1)

        # 시뮬레이션 실행을 위한 출력 캡처 및 실시간 전송
        class StreamingStringIO:
            def __init__(self):
                self.buffer = ""
            
            def write(self, string):
                self.buffer += string
                return len(string)
            
            def flush(self):
                temp = self.buffer
                self.buffer = ""
                return temp

        output = StreamingStringIO()
        original_stdout = sys.stdout
        sys.stdout = output

        def run_simulation():
            world.run(turns=turns)
            sys.stdout = original_stdout

        # 시뮬레이션을 별도 스레드에서 실행
        simulation_thread = threading.Thread(target=run_simulation)
        simulation_thread.start()

        # 출력을 실시간으로 전송
        while simulation_thread.is_alive() or output.buffer:
            if output.buffer:
                text = output.flush()
                conversation += text  # 새로운 텍스트를 conversation에 누적
                yield conversation   # 전체 대화 내용을 yield
            time.sleep(0.1)

        simulation_thread.join()

    except Exception as e:
        yield f"오류가 발생했습니다: {str(e)}"

# Gradio 인터페이스 생성
demo = gr.Interface(
    fn=create_simulation,
    inputs=[
        gr.Text(label="첫 번째 사람 이름", value="서준호"),
        gr.Dropdown(
            label="첫 번째 사람 MBTI",
            choices=["INTJ", "INFJ", "ISTJ", "ISFJ", "INTJ", "INFP", "ISTP", "ISFP",
                    "ENTJ", "ENFJ", "ESTJ", "ESFJ", "ENTP", "ENFP", "ESTP", "ESFP"],
            value="INTJ"
        ),
        gr.Text(label="첫 번째 사람 배경", value="29살 IT 개발자"),
        gr.Text(label="두 번째 사람 이름", value="김다은"),
        gr.Dropdown(
            label="두 번째 사람 MBTI",
            choices=["INTJ", "INFJ", "ISTJ", "ISFJ", "INTJ", "INFP", "ISTP", "ISFP",
                    "ENTJ", "ENFJ", "ESTJ", "ESFJ", "ENTP", "ENFP", "ESTP", "ESFP"],
            value="ENFP"
        ),
        gr.Text(label="두 번째 사람 배경", value="27살 일러스트레이터"),
        gr.Slider(label="대화 턴 수", minimum=1, maximum=10, value=3, step=1)
    ],
    outputs=gr.Textbox(label="시뮬레이션 결과", lines=20, max_lines=30),
    title="MBTI 소개팅 시뮬레이터",
    description="두 사람의 MBTI와 배경을 입력하여 소개팅 상황을 시뮬레이션해보세요."
)

if __name__ == "__main__":
    demo.queue()
    demo.launch(share=True) 