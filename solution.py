import json
import pickle


# 1
def write_file():
    with open('solution.txt', mode='w') as f:
        user_input = input('What is your name? ')
        f.write(user_input)


# 2
def read_file():
    with open('solution.txt', mode='r') as f:
        print(f.read())


def app_flow():
    app_options = input(
        'Please select an option:\n 1: Write to the file\n 2: read the file\n')

    if app_options == '1':
        write_file()
    elif app_options == '2':
        read_file()


# 3
def ask_user():
    user_input_list = []
    user_input = input('What is your name? ')
    user_input_list.append(user_input)
    write_file_to_list(user_input_list)
    write_pickle_to_list(user_input_list)


def write_file_to_list(txt_list):
    with open('solution.txt', mode='w') as f:
        f.write(json.dumps(txt_list))


def write_pickle_to_list(txt_list):
    with open('solution.p', mode='wb') as f:
        pickle.dump(txt_list, f)


# 4
def load_files():
    with open('solution.p', mode='rb') as f:
        print(pickle.load(f))
        with open('solution.txt', mode='r') as g:
            print(g.read())
