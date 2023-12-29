from file_io.data_loading import get_dataloader
from file_io.data_saving import get_datasaver

def get_image_inverter(args):
    ii = ImageInverter(args)
    return ii

class ImageInverter:
    def __init__(self,args):
        self.dataloader = get_dataloader(args)
        self.datasaver = get_datasaver(args)

    def invert_skeleton_image(self):
        skeleton_image = self.dataloader.load_input_skeleton()
        inverted_skeleton_image = self._invert_image(skeleton_image)
        self.datasaver.save_output_skeleton(inverted_skeleton_image)

    def _invert_image(self,image):
        inverted_image = 255 - image
        return inverted_image