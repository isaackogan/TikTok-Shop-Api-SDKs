from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.create_fbt_goods_response_data_create_result_info import CreateFBTGoodsResponseDataCreateResultInfo


T = TypeVar("T", bound="CreateFBTGoodsResponseData")


@_attrs_define
class CreateFBTGoodsResponseData:
    """
    Attributes:
        create_result_info (CreateFBTGoodsResponseDataCreateResultInfo | Unset):
    """

    create_result_info: CreateFBTGoodsResponseDataCreateResultInfo | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_result_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_result_info, Unset):
            create_result_info = self.create_result_info.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if create_result_info is not UNSET:
            field_dict["create_result_info"] = create_result_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_fbt_goods_response_data_create_result_info import (
            CreateFBTGoodsResponseDataCreateResultInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _create_result_info = d.pop("create_result_info", UNSET)
        create_result_info: CreateFBTGoodsResponseDataCreateResultInfo | Unset
        if isinstance(_create_result_info, Unset):
            create_result_info = UNSET
        else:
            create_result_info = CreateFBTGoodsResponseDataCreateResultInfo.from_dict(_create_result_info)

        create_fbt_goods_response_data = cls(
            create_result_info=create_result_info,
        )

        create_fbt_goods_response_data.additional_properties = d
        return create_fbt_goods_response_data

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
