from user_input_handling.arg_parsing import get_args
from user_input_handling.actions import actions_dict

if __name__ == '__main__':
    #NOTE_1: This is the entry point of the program.
    #We parse user input, and then perform the actions specified by the user.
    #This logic should remain minimal, and should not be cluttered with the details of each action.
    args = get_args()
    for action in args.actions:
        actions_dict[action](args)