from enum import StrEnum


class ProductInformationChangeWebhookDataChangedFieldsItem(StrEnum):
    DESCRIPTION = "description"
    MAIN_IMAGES = "main_images"
    OTHERS = "others"
    PRODUCT_ATTRIBUTES = "product_attributes"
    SIZE_CHART_IMAGE = "size_chart_image"
    SIZE_CHART_TEMPLATE = "size_chart_template"
    TITLE = "title"

    def __str__(self) -> str:
        return str(self.value)
