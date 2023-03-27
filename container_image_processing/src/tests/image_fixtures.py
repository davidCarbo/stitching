import pytest
import cv2 as cv
from ..image_processing import Image, ImageFactory

@pytest.fixture(scope="function")
def first_image_slice(request):
    return Image(cv.imread('/src/tests/assets/pi1.png'))

@pytest.fixture(scope="function")
def second_image_slice(request):
    return Image(cv.imread('/src/tests/assets/pi2.png'))


@pytest.fixture(scope="function")
def wrong_image_slice(request):
    return Image(cv.imread('/src/tests/assets/activia_shelf.jpg'))
