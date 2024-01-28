class User:
    
    def __init__(self):
        self.states_remembered_count = 0
        self.states_remembered_list = []
        self.continue_game = True
        self.missing_states_list = []
        
    def get_states_remembered_list(self):
        return self.states_remembered_list
    
    def get_states_remembered_count(self):
        return  self.states_remembered_count
    
    def exit_game(self):
        self.continue_game = False
        
    def add_state(self, state):
        self.states_remembered_count += 1
        self.states_remembered_list.append(state)
