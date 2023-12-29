from file_io.path_tracking import get_path_tracker
from file_io._saving_helper import _save_jpg
def get_datasaver(args):
    ds = DataSaver(args)
    return ds

class DataSaver:
    def __init__(self,args):
        self.path_tracker = get_path_tracker(args)
    def save_output_skeleton(self,skeleton_image):
        path = self.path_tracker.get_output_skeleton_path()
        _save_jpg(path,skeleton_image)