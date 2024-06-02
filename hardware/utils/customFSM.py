from transitions import Machine, State

# При написании конечных автоматов для EU и BIU выяснилось, что все
# они выполняют довольно простые функции, которые можно вынести в отдельный
# класс. Вот правила:
# 1. Передается список состояний. Первое состояние в списке берется как initial.
# 2. Два тригера: tick - для перехода, to_start - для возврата к state[0]
# 4. При переходе из A в B вызываетя phaseA который возвращает True.
# 5. Для переходов не последовательно используйте obj.set_state(<new state>)
#    в phase<old state name> верните False.
# 6. Состояния зациклены: [A, B, C]: A -[phaseA]-> B, B -[phaseB]-> C,
#    C -[phaseC]-> A.
class CustomFSM:
    def __init__(self, states: list):
        self.machine = Machine(model=self, states=states, initial=states[0])
        for i in range(len(states)-1):
            self.machine.add_transition(
                trigger='tick',
                source=states[i],
                dest=states[i+1],
                conditions=f'phase{str(states[i].name)}',
            )
        self.machine.add_transition(
            trigger='tick',
            source=states[len(states)-1],
            dest=states[0],
            conditions=f'phase{str(states[len(states)-1].name)}',
        )
        self.machine.add_transition(
            trigger='to_start',
            source='*',
            dest=states[0],
        )

    def set_state(self, state: State):
        self.machine.set_state(state)
