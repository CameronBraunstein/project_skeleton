from visualizations.skeleton_visualizer import get_skeleton_visualizer
from your_idea.image_inverter import get_image_inverter

#NOTE_2: This dictionary is used to map user input to lambda functions.
#When parsing user input, we only accept actions which are keys in this dictionary.
actions_dict = {
    'visualize_skeleton'   :lambda args: get_skeleton_visualizer(args).visualize_skeleton(),
    'invert_skeleton_image':lambda args: get_image_inverter(args).invert_skeleton_image()
    }