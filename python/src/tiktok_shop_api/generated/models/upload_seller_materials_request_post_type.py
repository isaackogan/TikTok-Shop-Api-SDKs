from enum import StrEnum

class UploadSellerMaterialsRequestPostType(StrEnum):
    ONE_PRODUCT_MULTIPLE_IMAGES = "ONE_PRODUCT_MULTIPLE_IMAGES"
    ONE_PRODUCT_ONE_IMAGE = "ONE_PRODUCT_ONE_IMAGE"

    def __str__(self) -> str:
        return str(self.value)
