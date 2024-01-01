import cv2

def _display_image(image_title,image):
    cv2.imshow(image_title,image)
    while True:
        if cv2.waitKey(1) & 0xFF == ord('q') or cv2.getWindowProperty(image_title, cv2.WND_PROP_VISIBLE) < 1:
            break
    cv2.destroyAllWindows()