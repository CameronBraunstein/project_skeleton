from file_io.data_loading import get_dataloader
from visualizations._visualizer_helper import _display_image

def get_skeleton_visualizer(args):
    #NOTE_3: Object inheritence is handled in these get_<x> functions, which fetch a class.
    #This is a clean way to handle inheritence. It keeps our constructor logic minimal.
    #Even if there is no inheritence, I still implement the get_<x> functions for consistency,
    #and in case I need to add inheritence later.
    if args.skeleton_visualization_type == 'input_skeleton':
        sv = InputSkeletonVisualizer(args)
    elif args.skeleton_visualization_type == 'output_skeleton':
        sv = OutputSkeletonVisualizer(args)
    else:
        raise ValueError('Invalid skeleton visualization type: {}'.format(args.skeleton_visualization_type))
    return sv


class SkeletonVisualizer:
    def __init__(self,args):
        self.dataloader = get_dataloader(args)

    def visualize_skeleton(self):
        skeleton_image = self._get_skeleton_image()
        _display_image(skeleton_image)

class InputSkeletonVisualizer(SkeletonVisualizer):
    def _get_skeleton_image(self):
        skeleton_image = self.dataloader.load_input_skeleton()
        return skeleton_image
    
class OutputSkeletonVisualizer(SkeletonVisualizer):
    def _get_skeleton_image(self):
        skeleton_image = self.dataloader.load_output_skeleton()
        return skeleton_image