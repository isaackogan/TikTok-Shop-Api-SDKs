from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.create_fbt_goods_request_create_goods_dto_list import CreateFBTGoodsRequestCreateGoodsDtoList


T = TypeVar("T", bound="CreateFBTGoodsRequest")


@_attrs_define
class CreateFBTGoodsRequest:
    """
    Attributes:
        create_goods_dto_list (list[CreateFBTGoodsRequestCreateGoodsDtoList]): List of goods records to create.
    """

    create_goods_dto_list: list[CreateFBTGoodsRequestCreateGoodsDtoList]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        create_goods_dto_list = []
        for create_goods_dto_list_item_data in self.create_goods_dto_list:
            create_goods_dto_list_item = create_goods_dto_list_item_data.to_dict()
            create_goods_dto_list.append(create_goods_dto_list_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "create_goods_dto_list": create_goods_dto_list,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_fbt_goods_request_create_goods_dto_list import (
            CreateFBTGoodsRequestCreateGoodsDtoList,  # noqa: PLC0415
        )

        d = dict(src_dict)
        create_goods_dto_list = []
        _create_goods_dto_list = d.pop("create_goods_dto_list")
        for create_goods_dto_list_item_data in _create_goods_dto_list:
            create_goods_dto_list_item = CreateFBTGoodsRequestCreateGoodsDtoList.from_dict(
                create_goods_dto_list_item_data
            )

            create_goods_dto_list.append(create_goods_dto_list_item)

        create_fbt_goods_request = cls(
            create_goods_dto_list=create_goods_dto_list,
        )

        create_fbt_goods_request.additional_properties = d
        return create_fbt_goods_request

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
