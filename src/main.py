from user_input_handling.arg_parsing import get_args
from user_input_handling.actions import actions_dict

if __name__ == '__main__':
    args = get_args()
    for action in args.actions:
        actions_dict[action](args)