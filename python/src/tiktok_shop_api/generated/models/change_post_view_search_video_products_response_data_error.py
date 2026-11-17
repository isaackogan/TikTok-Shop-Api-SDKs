from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.change_post_view_search_video_products_response_data_error_detail import ChangePostViewSearchVideoProductsResponseDataErrorDetail





T = TypeVar("T", bound="ChangePostViewSearchVideoProductsResponseDataError")



@_attrs_define
class ChangePostViewSearchVideoProductsResponseDataError:
    """ 
        Attributes:
            code (int): 100: choose a product relevant to the video. 200: the association update could not be confirmed;
                query current associations before deciding whether to retry. Do not replay successful items.
            detail (ChangePostViewSearchVideoProductsResponseDataErrorDetail):
            message (str): English failure explanation and corrective action.
     """

    code: int
    detail: ChangePostViewSearchVideoProductsResponseDataErrorDetail
    message: str
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.change_post_view_search_video_products_response_data_error_detail import ChangePostViewSearchVideoProductsResponseDataErrorDetail # noqa: PLC0415
        code = self.code

        detail = self.detail.to_dict()

        message = self.message


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "code": code,
            "detail": detail,
            "message": message,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.change_post_view_search_video_products_response_data_error_detail import ChangePostViewSearchVideoProductsResponseDataErrorDetail # noqa: PLC0415
        d = dict(src_dict)
        code = d.pop("code")

        detail = ChangePostViewSearchVideoProductsResponseDataErrorDetail.from_dict(d.pop("detail"))




        message = d.pop("message")

        change_post_view_search_video_products_response_data_error = cls(
            code=code,
            detail=detail,
            message=message,
        )


        change_post_view_search_video_products_response_data_error.additional_properties = d
        return change_post_view_search_video_products_response_data_error

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
