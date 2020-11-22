import re


class MIU:

    def __init__(self):
        # Definition of the primary chain.
        self.state = 'MI'

    def get_state(self):
        # Check the game status.
        return self.state

    def reset(self):
        # Restart the game state.
        self.state = 'MI'

    def axiom_one(self):
        # Definition of rule one of the MIU system.
        if self.state[-1] == 'I':

            self.state = self.state + 'U'

        else:

            print('Can not use this rule...')

        return self.state

    def rule_two(self):
        # Definition of rule two of the MIU system.
        self.state = self.state + self.state[1:]

        return self.state

    def rule_three(self):
        # Definition of rule three of the MIU system.
        word = self.state
        result = re.finditer(r'(?=(III))', word)

        words = dict()
        for i, j in enumerate(result):
            slices = [word[:j.start(1)], word[j.end(1):]]
            new_chain = 'U'.join(slices)
            words[i] = new_chain
            print('Option {}:'.format(i), new_chain)

        if words.keys():

            option = int(input('Choose an option: '))
            self.state = words.get(option)

        else:

            print('Can not use this rule...')

        return self.state

    def rule_four(self):
        # Definition of rule four of the MIU system.
        word = self.state
        result = re.finditer(r'(?=(UU))', word)

        words = dict()
        for i, j in enumerate(result):
            new_chain = word[:j.start(1)] + word[j.end(1):]
            words[i] = new_chain
            print('Option {}:'.format(i), new_chain)

        if words.keys():

            option = int(input('Choose an option: '))
            self.state = words.get(option)

        else:

            print('Can not use this rule...')

        return self.state
