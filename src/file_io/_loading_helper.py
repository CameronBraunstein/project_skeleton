import cv2
def _load_jpg(path):
    image = cv2.imread(path)
    return image