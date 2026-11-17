from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.change_post_view_search_video_products_response_data_error import ChangePostViewSearchVideoProductsResponseDataError
  from ..models.change_post_view_search_video_products_response_data_product_result import ChangePostViewSearchVideoProductsResponseDataProductResult





T = TypeVar("T", bound="ChangePostViewSearchVideoProductsResponseData")



@_attrs_define
class ChangePostViewSearchVideoProductsResponseData:
    """ 
        Attributes:
            errors (list[ChangePostViewSearchVideoProductsResponseDataError] | Unset): Failed product operations only; empty
                when all operations succeed.
            product_result (ChangePostViewSearchVideoProductsResponseDataProductResult | Unset):
            request_id (str | Unset): Server-generated submission identifier, in openapi-<UUID v4> format. A new value is
                generated for every invocation; it is not an idempotency key. Distinct from the request log ID in the response
                envelope.
     """

    errors: list[ChangePostViewSearchVideoProductsResponseDataError] | Unset = UNSET
    product_result: ChangePostViewSearchVideoProductsResponseDataProductResult | Unset = UNSET
    request_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.change_post_view_search_video_products_response_data_error import ChangePostViewSearchVideoProductsResponseDataError # noqa: PLC0415
        from ..models.change_post_view_search_video_products_response_data_product_result import ChangePostViewSearchVideoProductsResponseDataProductResult # noqa: PLC0415
        errors: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()
                errors.append(errors_item)



        product_result: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_result, Unset):
            product_result = self.product_result.to_dict()

        request_id = self.request_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if errors is not UNSET:
            field_dict["errors"] = errors
        if product_result is not UNSET:
            field_dict["product_result"] = product_result
        if request_id is not UNSET:
            field_dict["request_id"] = request_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_post_view_search_video_products_response_data_error import ChangePostViewSearchVideoProductsResponseDataError # noqa: PLC0415
        from ..models.change_post_view_search_video_products_response_data_product_result import ChangePostViewSearchVideoProductsResponseDataProductResult # noqa: PLC0415
        d = dict(src_dict)
        _errors = d.pop("errors", UNSET)
        errors: list[ChangePostViewSearchVideoProductsResponseDataError] | Unset = UNSET
        if _errors is not UNSET:
            errors = []
            for errors_item_data in _errors:
                errors_item = ChangePostViewSearchVideoProductsResponseDataError.from_dict(errors_item_data)



                errors.append(errors_item)


        _product_result = d.pop("product_result", UNSET)
        product_result: ChangePostViewSearchVideoProductsResponseDataProductResult | Unset
        if isinstance(_product_result,  Unset):
            product_result = UNSET
        else:
            product_result = ChangePostViewSearchVideoProductsResponseDataProductResult.from_dict(_product_result)




        request_id = d.pop("request_id", UNSET)

        change_post_view_search_video_products_response_data = cls(
            errors=errors,
            product_result=product_result,
            request_id=request_id,
        )


        change_post_view_search_video_products_response_data.additional_properties = d
        return change_post_view_search_video_products_response_data

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
