from __future__ import annotations

from collections.abc import Mapping
from io import BytesIO
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from .. import types
from ..models.upload_product_image_request_use_case import UploadProductImageRequestUseCase
from ..types import UNSET, File, Unset

T = TypeVar("T", bound="UploadProductImageRequest")


@_attrs_define
class UploadProductImageRequest:
    """
    Attributes:
        data (File): The local image file to be uploaded.

            **Note**:
            - Supported formats: JPG, JPEG, PNG, WEBP, HEIC, BMP
            - Zero-byte files are rejected.
            - Max size: 10MB
            - Dimensions: [100x100 px, 20000x20000 px]
            - For `use_case=MAIN_IMAGE`, the dimensions must be between 300x300 px and 4000x4000 px.
            - For `use_case=SIZE_CHART_IMAGE`, the dimension must be at least 1024 px on the shorter side.
        use_case (UploadProductImageRequestUseCase | Unset): The usage scenario of the image.
            Possible values:
            - MAIN_IMAGE: An image displayed in the product image gallery.
            - ATTRIBUTE_IMAGE: An image that represents a product variant (e.g. color).
            - DESCRIPTION_IMAGE: An image used within the product description.
            - CERTIFICATION_IMAGE: An image to provide supporting information to meet TikTok Shop requirements for listing
            restricted products (e.g., images of certifications, product packaging, labeling).
            - SIZE_CHART_IMAGE: An image that displays the product's measurement details.
            - CUSTOMIZATION_IMAGE: Images used for POD product customization, such as background images, mask images, or
            default images configured for customizable areas. These images are used to render or preview consumer-
            customizable product content.

            **Note**: Images for use cases `MAIN_IMAGE` and `ATTRIBUTE_IMAGE` that do not fit within the 3:4 to 4:3 aspect
            ratio range will be automatically converted to 1:1.
    """

    data: File
    use_case: UploadProductImageRequestUseCase | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        data = self.data.to_tuple()

        use_case: str | Unset = UNSET
        if not isinstance(self.use_case, Unset):
            use_case = self.use_case.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
            }
        )
        if use_case is not UNSET:
            field_dict["use_case"] = use_case

        return field_dict

    def to_multipart(self) -> types.RequestFiles:
        files: types.RequestFiles = []

        files.append(("data", self.data.to_tuple()))

        if not isinstance(self.use_case, Unset):
            files.append(("use_case", (None, str(self.use_case.value).encode(), "text/plain")))

        for prop_name, prop in self.additional_properties.items():
            files.append((prop_name, (None, str(prop).encode(), "text/plain")))

        return files

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        data = File(payload=BytesIO(d.pop("data")))

        _use_case = d.pop("use_case", UNSET)
        use_case: UploadProductImageRequestUseCase | Unset
        if isinstance(_use_case, Unset):
            use_case = UNSET
        else:
            use_case = UploadProductImageRequestUseCase(_use_case)

        upload_product_image_request = cls(
            data=data,
            use_case=use_case,
        )

        upload_product_image_request.additional_properties = d
        return upload_product_image_request

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
