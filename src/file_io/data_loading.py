from file_io.path_tracking import get_path_tracker
from file_io._loading_helper import _load_jpg
def get_dataloader(args):
    dl = DataLoader(args)
    return dl

class DataLoader:
    def __init__(self,args):
        self.path_tracker = get_path_tracker(args)
        
    def load_input_skeleton(self):
        path = self.path_tracker.get_input_skeleton_path()
        skeleton = _load_jpg(path)
        return skeleton
    
    def load_output_skeleton(self):
        path = self.path_tracker.get_output_skeleton_path()
        skeleton = _load_jpg(path)
        return skeleton