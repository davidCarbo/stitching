def schema_stitching():
    return {
        "type": "object",
        "properties": {
            "images": {
                "type": "array",
                "minItems": 1,
                "items": {
                    "type": "string"
                }
            }
        }
    }