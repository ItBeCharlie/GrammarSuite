from Dfa import Dfa


def main():
    dfa = Dfa.init_from_file('test_dfa.txt', True)
    print(dfa.check_string('abbababaabcaaab', True))
    dfa.show()


main()
