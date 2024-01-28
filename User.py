class User:
    
    def __init__(self):
        self.states_remembered_count = 0
        self.states_remembered_list = []
        
    def get_states_remembered_list(self):
        return self.states_remembered_list
    
    def get_states_remembered_count(self):
        return  self.states_remembered_count
    
    