from src.image_processing import ImageFactory, image_stitching, Image
import schemas
import api_utils

def stitch_images(data):
    # Validate JSON schema
    api_utils.validate_schema(schema=schemas.schema_stitching(), args=data)
    try:       
        # Create images array with Image objects
        images = [ImageFactory.create_image_from_base64(im) for im in data["images"]]

        # Verify if all the images are instances of Image:
        for im in images:
            if not isinstance(im, Image):
                raise Exception("Invalid instance of Image")

    
        result = image_stitching(images=images)                  
        result = result.to_base64()             
        return {                                                
            "image": result
        }
    except Exception as e:
        return f"something went wrong, {e}"
    
