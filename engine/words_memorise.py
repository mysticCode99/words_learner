
import os, random
from datetime import datetime

from engine_utils import Word
from engine_singltone import Engine_Singltone

def choose_lang():
    """sumary_line"""
    lang = input("Choose Language > ").strip()
    Engine_Singltone.set_lang(lang)

def add_word():
    """ Add word """
    if not Engine_Singltone.get_current_lang():
        choose_lang()
    word = input("New word > ").strip()
    translation = input("Translation > ").strip()
    Engine_Singltone.add_word(Word(word, translation))

def add_from_file():
    """ Adding words from file """
    if not Engine_Singltone.get_current_lang():
        choose_lang()
    fp = input("Enter file Path > ").strip()
    if not os.path.exists(fp):
        print(f"WARNING: {fp} not found")
        return
    with open(fp, 'r') as f:
        for line in f:
            word, translation = line.split(',')[:2]
            Engine_Singltone.add_word(Word(
                word.strip(),
                translation.strip()
            ))

def show_words():
    """sumary_line"""
    for w in Engine_Singltone.get_last_ten_words():
        date_obj = datetime.fromtimestamp(w.last_time)
        print(f"{w.word:>30} <-> {w.translation:>30} : {date_obj.strftime(r'%d:%m:%y %H:%M')}")
    
def repeat_words():
    """sumary_line"""
    w_list = Engine_Singltone.get_words()
    try:
        count = int(input("Enter count of words > "))
    except ValueError:
        print("Error: input need to be integer")
        return
    while count > 0:
        count -= 1
        w = random.choice(w_list)
        print(f"Translation -> {w.translation}")
        answer = input("Word -> ")
        if w.check_word(answer):
            print('Correct')
        else:
            print('Uncorrect !!!')
            print(f"Correct answer is -> {w.word}")
        print('-'*100)
        

def choose_action():
    """ Choose ation """
    actions = list(ACTIONS.keys())
    print(' | '.join(actions))
    inp = input("Choose work mode > ").strip()
    action = ACTIONS.get(inp)
    if not action:
        print("ERROR: Action not found")
    return action

def main():
    """sumary_line"""
    action = None
    while True:
        if not action:
            action = choose_action()
        else:
            action = action()

ACTIONS = {
    'add_word'          : add_word,
    'exit'              : exit,
    'change'            : choose_action,
    'choose_laguage'    : choose_lang,
    'add_from_file'     : add_from_file,
    'show_words'        : show_words,
    'repeat_words'      : repeat_words,
}

if __name__ == '__main__':
    main()