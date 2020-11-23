import re


class MIU:

    def __init__(self):
        # Definition of the primary chain.
        self.state = 'MI'
        self.options_by_axiom_three = dict()
        self.options_by_axiom_four = dict()

    def get_state(self):
        # Check the game status.
        return self.state

    def reset(self):
        # Restart the game state.
        self.state = 'MI'
        state = self.state
        return state

    def axiom_one(self):
        # Definition of axiom one of the MIU system.
        if self.state[-1] == 'I':
            self.state = self.state + 'U'
            state = self.state
        else:
            state = self.state
        return state

    def axiom_two(self):
        # Definition of rule two of the MIU system.
        self.state = self.state + self.state[1:]
        return self.state

    def axiom_three(self):
        # Definition of rule three of the MIU system.
        chain = self.state
        result = re.finditer(r'(?=(III))', chain)
        chains = dict()
        for i, j in enumerate(result):
            slices = [chain[:j.start(1)], chain[j.end(1):]]
            new_chain = 'U'.join(slices)
            chains[str(i)] = new_chain
        if chains.keys():
            state = chains
            self.options_by_axiom_three = chains
        else:
            state = self.state
        return state

    def apply_axiom_three(self, option):
        if option in list(self.options_by_axiom_three.keys()):
            self.state = self.options_by_axiom_three[option]
        self.options_by_axiom_three = dict()
        return self.state

    def axiom_four(self):
        # Definition of rule four of the MIU system.
        chain = self.state
        result = re.finditer(r'(?=(UU))', chain)
        chains = dict()
        for i, j in enumerate(result):
            new_chain = chain[:j.start(1)] + chain[j.end(1):]
            chains[str(i)] = new_chain
        if chains.keys():
            state = chains
            self.options_by_axiom_four = chains
        else:
            state = self.state
        return state

    def apply_axiom_four(self, option):
        if option in list(self.options_by_axiom_four.keys()):
            self.state = self.options_by_axiom_four[option]
        self.options_by_axiom_four = dict()
        return self.state
