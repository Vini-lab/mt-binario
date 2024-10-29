class TuringMachine:
    def __init__(self, tape, equal_symbol="="):
        self.tape = list(tape)
        self.equal_symbol = equal_symbol
        self.head_position = 0
        self.current_state = 'q0'
        self.transition_function = {
            ('q0', '1'): ('1', 'R', 'q1'),
            ('q1', '0'): ('0', 'R', 'q2'),
            ('q2', '0'): ('0', 'R', 'q2'),
            ('q2', '1'): ('1', 'R', 'q2'),
            ('q2', '='): ('=', 'R', 'q3'),
        }
        self.sum = 2

    def step(self):
        symbol_under_head = self.tape[self.head_position]        
        if (self.current_state, symbol_under_head) in self.transition_function:
            write_symbol, direction, next_state = self.transition_function[(self.current_state, symbol_under_head)]            
            self.tape[self.head_position] = write_symbol
            self.current_state = next_state            
            self.head_position += 1 if direction == 'R' else -1
            if self.head_position >= len(self.tape):
                self.tape.append(self.equal_symbol)
            elif self.head_position < 0:
                self.head_position = 0
            if self.current_state == 'q2' and symbol_under_head in '01':
                self.sum += int(symbol_under_head)
        else:
            self.current_state = 'REJECTED'

    def run(self):
        while self.current_state not in {'q3', 'REJECTED'}:
            self.step()
        return self.current_state == 'q3', self.sum