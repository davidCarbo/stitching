import base64
import numpy as np
import cv2


def readb64(uri: str):
        nparr = np.fromstring(base64.b64decode(uri), np.uint8)
        img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        return img

def writeb64(image: cv2.Mat) -> str:
        _, buffer = cv2.imencode('.jpg', image)
        return base64.b64encode(buffer).decode("utf-8")