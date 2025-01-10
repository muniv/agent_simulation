class SimulationWorld:
    def __init__(self, location: str, scenario: str, agents: list):
        self.location = location
        self.scenario = scenario
        self.agents = agents
        self.conversation_history = []
        self.turn = 0
        
    def run(self, turns: int):
        """시뮬레이션 실행"""
        print(f"\n=== {self.location}에서의 시나리오 ===")
        print(f"{self.scenario}\n")
        print("=" * 50)
        
        for self.turn in range(turns):
            print(f"\n[Turn {self.turn + 1}]\n")
            
            # 현재 컨텍스트 생성
            context = self._get_current_context()
            
            for i, agent in enumerate(self.agents):
                # 이전 에이전트의 대화/행동을 컨텍스트에 추가
                if i > 0:
                    context = self._update_context_with_last_interaction(context)
                
                # 각 에이전트의 생각, 대화, 행동을 시뮬레이션
                interaction_data = {
                    'turn': self.turn + 1,
                    'agent': agent.name
                }
                
                # 생각 생성 및 저장
                thought = agent.think(context)
                if thought.strip():
                    interaction_data['thought'] = thought
                    print(f"🤔 {agent.name}의 생각:")
                    print(f"   {thought}\n")
                
                # 대화 생성 및 저장
                speech = agent.speak(context)
                if speech.strip():
                    interaction_data['speech'] = speech
                    print(f"💭 {agent.name}의 대화:")
                    print(f"   \"{speech}\"\n")
                
                # 행동 생성 및 저장
                action = agent.act(context)
                if action.strip():
                    interaction_data['action'] = action
                    print(f"👥 {agent.name}의 행동:")
                    print(f"   {action}\n")
                
                # 결과 저장
                self.conversation_history.append(interaction_data)
                print("-" * 50)
    
    def _update_context_with_last_interaction(self, context: str) -> str:
        """가장 최근의 상호작용을 컨텍스트에 추가하여 자연스러운 대화 흐름 유도"""
        if not self.conversation_history:
            return context
            
        # 마지막 상호작용 가져오기
        last_interaction = self.conversation_history[-1]
        agent_name = last_interaction.get('agent', '알 수 없음')
        last_speech = last_interaction.get('speech', '')
        last_action = last_interaction.get('action', '')
        
        context += "\n\n=== 직전 상대방의 반응 ==="
        context += f"\n[{agent_name}]"
        
        # 턴 타입(대화/행동)에 따라 다른 프롬프트 추가
        if self.turn % 2 == 0:  # 대화 턴
            if last_speech:
                context += f"""\n
                💬 방금 {agent_name}님이 말씀하신 내용: "{last_speech}"
                
                위 대화에 자연스럽게 이어서 대화를 해주세요."""
        else:  # 행동 턴
            if last_action:
                context += f"""\n
                👥 방금 {agent_name}님의 행동: {last_action}
                
                위 행동에 대한 자연스러운 반응을 행동으로 보여주세요."""
                
        context += """
        
        === 참고사항 ===
        - 상대방의 말이나 행동에 즉각적으로 반응해주세요
        - MBTI 성격 유형에 맞는 자연스러운 반응을 보여주세요
        - 대화는 일방적이지 않게, 서로 주고받는 형식으로 진행해주세요
        """
        
        return context
    
    def _get_current_context(self) -> str:
        """현재 상황에 대한 컨텍스트 생성"""
        context = f"""
        === 현재 상황 ===
        장소: {self.location}
        시나리오: {self.scenario}
        현재 턴: {self.turn + 1}
        턴 타입: {'대화' if self.turn % 2 == 0 else '행동'}
        
        === 이전 기록 ==="""
        
        # 최근 3개의 상호작용 기록 추가
        recent_history = self.conversation_history[-6:]  # 2명 x 3턴 = 최대 6개 기록
        if recent_history:
            for history in recent_history:
                agent_name = history.get('agent', '알 수 없음')
                speech = history.get('speech', '')
                action = history.get('action', '')
                
                context += f"\n\n[{agent_name}]"
                if speech:
                    context += f"\n💭 대화: \"{speech}\""
                if action:
                    context += f"\n👥 행동: {action}"
        else:
            context += "\n(이전 기록 없음)"
            
        context += """
        
        === 참고사항 ===
        - 이전 대화/행동에 자연스럽게 이어지도록 반응
        - 상대방의 말이나 행동에 적절히 응답
        - 대화는 자연스러운 흐름을 유지
        """
            
        return context
