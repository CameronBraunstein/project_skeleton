from file_io.data_loading import get_dataloader
from file_io.data_saving import get_datasaver

def get_image_inverter(args):
    ii = ImageInverter(args)
    return ii

class ImageInverter:
    def __init__(self,args):
        #NOTE_4: Constructors do not contain any sophisticated logic. Instead, they
        #fetch objects from other modules, and store them as instance variables.
        #Each constructor takes a single argument, args, a Namespace object.
        self.dataloader = get_dataloader(args)
        self.datasaver = get_datasaver(args)

    def invert_skeleton_image(self):
        #NOTE_5: This is the main method of this class. Observe that it is very few lines 
        #of code, but it is very readable and clear what occurs. All file I/O logic
        #is handled elsewhere, allowing this method to focus on the core logic of the class.
        skeleton_image = self.dataloader.load_input_skeleton()
        inverted_skeleton_image = self._invert_image(skeleton_image)
        self.datasaver.save_output_skeleton(inverted_skeleton_image)

    def _invert_image(self,image):
        inverted_image = 255 - image
        return inverted_image