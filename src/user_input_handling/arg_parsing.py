import argparse
from user_input_handling.actions import actions_dict
def get_args():
    parser = argparse.ArgumentParser(
        prog='My Project Skeleton',
        description='A template for new research projects in Python',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--actions',
                        nargs='+',
                        choices=actions_dict.keys(),
                        default=[],
                        help='Which actions to perform')
    parser.add_argument('--skeleton_visualization_type',
                        choices=['input_skeleton','output_skeleton'],
                        help='Whether we view the input or the output skeleton')
    args = parser.parse_args()
    return args
    
