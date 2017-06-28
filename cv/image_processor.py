"""OpenCV processor for images"""
import logging
import cv2
class ImageProcessor(object):
    def __init__(self):
        super().__init__()
        self.image = None
    @classmethod
    def load_file(self, path):
        """load file with path"""
        logging.info("Loading: {}".format(path))
        try:
            self.image = cv2.imread(path)
        except:
            raise IOError("Can not load file")
