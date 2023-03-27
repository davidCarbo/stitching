import pytest
from ..image_processing import image_stitching
from .image_fixtures import first_image_slice, second_image_slice, wrong_image_slice

class TestImageStitching:
    def test_two_image_stitching_right(self, first_image_slice, second_image_slice):
        result = image_stitching(images=[first_image_slice, second_image_slice]) 
        assert len(first_image_slice.shape) == len(result.shape)
        for index, shape in enumerate(first_image_slice.shape):
            assert result.shape[index] <= shape + second_image_slice.shape[index] 
            
    def test_two_image_stitching_none_image(self, first_image_slice):
        with pytest.raises(AssertionError):
            image_stitching(images=[None, first_image_slice])

    def test_two_image_stitching_not_fitting(self, first_image_slice, wrong_image_slice):
        with pytest.raises(Exception):
            image_stitching(images=[first_image_slice, wrong_image_slice])