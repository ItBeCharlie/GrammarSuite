from Production import Production
from Grammar import Grammar


def main():
    productions = parse_file('test.txt')
    grammar = Grammar(productions)
    print(grammar)


def parse_file(file):
    productions = []
    with open(file) as f:
        lines = f.readlines()
    # print(lines)
    # Naive approach, assume file is correct
    for line in lines:
        new_line = line
        new_line = new_line.replace('\n', '')
        productions.append(Production(new_line))

    return productions


main()
