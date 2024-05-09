
from engine_utils import Word

WORDS = []

def add_word():
    """sumary_line"""
    word = input("New word >")
    translation = input("Translation >")
    WORDS.append(Word(word, translation))
    return None

def choose_action():
    inp = input('chose work mode >')
    action = actions.get(inp)
    return action

def main():
    """sumary_line"""
    action = None
    while True:
        if not action:
            action = choose_action()
        else:
            action = action()

actions = {
    'add_word'  : add_word,
    'exit'      : exit,
    'change'    : choose_action,
}

if __name__ == '__main__':
    main()