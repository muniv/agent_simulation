class SimulationWorld:
    def __init__(self, location: str, scenario: str, agents: list):
        self.location = location
        self.scenario = scenario
        self.agents = agents
        self.conversation_history = []
        self.turn = 0
        
    def _get_current_context(self) -> str:
        """현재 상황에 대한 컨텍스트 생성"""
        context = f"""
        장소: {self.location}
        
        상황: {self.scenario}
        
        참석자:
        """
        
        # 모든 참석자 정보 추가
        for agent in self.agents:
            context += f"\n- {agent.name} ({agent.personality.mbti_type})"
            
        return context
        
    def _update_context_with_recent_interactions(self, context: str) -> str:
        """최근 상호작용들을 컨텍스트에 추가"""
        if not self.conversation_history:
            return context
            
        # 마지막 턴의 모든 상호작용을 가져옴
        current_turn = self.conversation_history[-len(self.agents):]
        
        context += "\n\n=== 직전 상호작용 ==="
        for interaction in current_turn:
            agent_name = interaction.get('agent', '알 수 없음')
            speech = interaction.get('speech', '')
            action = interaction.get('action', '')
            
            if speech or action:
                context += f"\n[{agent_name}]"
                if speech:
                    context += f"\n💭 대화: \"{speech}\""
                if action:
                    context += f"\n👥 행동: {action}"
                
        return context
        
    def run(self, turns: int):
        """시뮬레이션 실행"""
        print(f"\n=== {self.location}에서의 시나리오 ===")
        print(f"{self.scenario}\n")
        print("참석자:")
        for agent in self.agents:
            print(f"- {agent.name} ({agent.personality.mbti_type})")
        print("=" * 50)
        
        for self.turn in range(turns):
            print(f"\n[Turn {self.turn + 1}]\n")
            
            # 현재 컨텍스트 생성
            context = self._get_current_context()
            
            # 모든 에이전트의 상호작용 처리
            for i, agent in enumerate(self.agents):
                # 이전 상호작용들을 컨텍스트에 추가
                if i > 0:
                    context = self._update_context_with_recent_interactions(context)
                
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
