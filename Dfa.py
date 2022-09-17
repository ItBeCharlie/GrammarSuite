class Dfa:
    def __init__(self, start_state, accept_states, table):
        self.start_state = start_state
        self.accept_states = accept_states
        self.table = table

    def __str__(self):
        return 'Start State: ' + self.start_state + '\nAccept States: ' + str(self.accept_states) + '\nTable: ' + str(self.table)

    def init_from_list(file, trace=False):
        if trace:
            print('\nRaw File:', file, sep='\n')
        # 1. Clean the file. Remove all blank lines, newlines, and comments
        cleaned_file = []
        for count, _ in enumerate(file):
            line = file[count]
            line = ' '.join(line.split())
            if line == '':
                continue
            if line[:2] == '//':
                continue
            line = line.split('//')[0]
            line = ' '.join(line.split())
            cleaned_file.append(line)

        if trace:
            print('\nFirst Clean:', cleaned_file, sep='\n')

        # 2. Get start and accept states
        start_state = cleaned_file[0]
        accept_states = cleaned_file[1].replace(' ', '').split(',')
        cleaned_file = cleaned_file[2:]

        if trace:
            print(
                f'\nStart and Accept States:\nStart State: {start_state}\nAccept States: {accept_states}\n{cleaned_file}')

        # 3. Convert remaining lines to triples and check that each remaining line is a triple, otherwise error
        triples = []
        for line in cleaned_file:
            triples.append(line.split(' '))
            if len(triples[-1]) != 3:
                print(f'Error: Incorrect triple {line}')
                return None
        if trace:
            print(
                f'\nTriples:\n{triples}')

        # 4. Get the language from the 2nd column
        language = []
        for triple in triples:
            if triple[1] not in language:
                language.append(triple[1])
        if trace:
            print(
                f'\nLanguage:\n{language}')

        # 5. Verify that every non-terminal has exactly one production for every character in the language
        char_check_step = {}
        for triple in triples:
            if triple[0] not in char_check_step:
                char_check_step[triple[0]] = []
            if triple[1] not in char_check_step[triple[0]]:
                char_check_step[triple[0]].append(triple[1])
            else:
                print('Error: Cannot have same character go to 2 productions')
                return None

        if trace:
            print(
                f'\nCharacters in Productions:\n{char_check_step}')

        # 6. Verify that each production leads to a production that exists
        for triple in triples:
            if triple[0] not in char_check_step:
                print('Error: Left production doesn\'t exist on right side')

        if trace:
            print(f'\nProductions Balanced')

        # 7. All checks passed, can generate Dfa table successfully
        dfa_table = dict.fromkeys(char_check_step)
        for triple in triples:
            if dfa_table[triple[0]] == None:
                dfa_table[triple[0]] = {}
            dfa_table[triple[0]][triple[1]] = triple[2]

        print(triples)
        if trace:
            print(f'\nDfa Table:\n{dfa_table}')

        return Dfa(start_state, accept_states, dfa_table)

    def check_string(self, input, trace=False):
        cur_state = self.start_state
        for char in input:
            if char not in self.table[cur_state]:
                print('Error: Invalid character in string')
                return False
            if trace:
                print('[', cur_state, ' ', char, '] -> ', sep='', end='')
            cur_state = self.table[cur_state][char]
        if trace:
            print('[', cur_state, ']', sep='')

        return cur_state in self.accept_states

    def init_from_file(in_file, trace=False):
        with open(in_file, "r") as f:
            file = f.readlines()
        f.close()
        return Dfa.init_from_list(file, trace)
