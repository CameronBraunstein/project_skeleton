import os
def get_path_tracker(args):
    pt = PathTracker(args)
    return pt

class PathTracker:
    def __init__(self,args):
        pass

    def get_input_skeleton_path(self):
        input_directory = self._get_input_directory()
        file_name = 'skeleton.jpg'
        input_skeleton_path = os.path.join(input_directory,file_name)
        return input_skeleton_path
    
    def _get_input_directory(self):
        input_directory = os.path.join('input_data')
        return input_directory
    
    def get_output_skeleton_path(self):
        output_directory = self._get_output_directory()
        file_name = 'skeleton.jpg'
        output_skeleton_path = os.path.join(output_directory,file_name)
        return output_skeleton_path

    def _get_output_directory(self):
        output_directory = os.path.join('output_data')
        return output_directory
