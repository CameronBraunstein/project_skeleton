from file_io.data_loading import get_dataloader
from visualizations._visualizer_helper import _display_image

def get_skeleton_visualizer(args):
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