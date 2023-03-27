import cv2
from typing import List
import base64
import numpy as np

class Image:
    def __init__(self, mat=cv2.Mat):
        self.mat = mat
        self.shape = mat.shape

    def to_base64(self):
        _, buffer = cv2.imencode('.jpg', self.mat)
        return base64.b64encode(buffer).decode("utf-8")

class ImageFactory:
    
    def create_image_from_base64(uri: str) -> Image:
        nparr = np.fromstring(base64.b64decode(uri), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        if img is None:
            raise Exception("OpenCV can not read Image from given base64 string")
        return Image(img)



def image_stitching(images: List[ Image ]) -> Image:
    stitcher = cv2.Stitcher_create(mode=cv2.Stitcher_SCANS)
    assert len(images) > 1, f"Expected two or more images, got {len(images)}"
    assert all(images), "Some Images are not loaded correctly"
    images = [ im.mat for im in images]
    status, panorama = stitcher.stitch(images)
    if status == cv2.Stitcher_ERR_CAMERA_PARAMS_ADJUST_FAIL:
        raise Exception("Could not stitch images: Could not adjust images.")
    if status == cv2.Stitcher_ERR_HOMOGRAPHY_EST_FAIL:
        raise Exception("Could not stitch images: Could not compute homography to connect images correctly.")
    if status == cv2.Stitcher_ERR_NEED_MORE_IMGS:
        raise Exception("Could not stitch images: More images are needed.")
    return Image(panorama)