from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_fbt_goods_response_data_create_result_info_create_result_list import CreateFBTGoodsResponseDataCreateResultInfoCreateResultList





T = TypeVar("T", bound="CreateFBTGoodsResponseDataCreateResultInfo")



@_attrs_define
class CreateFBTGoodsResponseDataCreateResultInfo:
    """ 
        Attributes:
            create_result_list (list[CreateFBTGoodsResponseDataCreateResultInfoCreateResultList] | Unset): List of goods
                creation results.
     """

    create_result_list: list[CreateFBTGoodsResponseDataCreateResultInfoCreateResultList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_fbt_goods_response_data_create_result_info_create_result_list import CreateFBTGoodsResponseDataCreateResultInfoCreateResultList # noqa: PLC0415
        create_result_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.create_result_list, Unset):
            create_result_list = []
            for create_result_list_item_data in self.create_result_list:
                create_result_list_item = create_result_list_item_data.to_dict()
                create_result_list.append(create_result_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create_result_list is not UNSET:
            field_dict["create_result_list"] = create_result_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_fbt_goods_response_data_create_result_info_create_result_list import CreateFBTGoodsResponseDataCreateResultInfoCreateResultList # noqa: PLC0415
        d = dict(src_dict)
        _create_result_list = d.pop("create_result_list", UNSET)
        create_result_list: list[CreateFBTGoodsResponseDataCreateResultInfoCreateResultList] | Unset = UNSET
        if _create_result_list is not UNSET:
            create_result_list = []
            for create_result_list_item_data in _create_result_list:
                create_result_list_item = CreateFBTGoodsResponseDataCreateResultInfoCreateResultList.from_dict(create_result_list_item_data)



                create_result_list.append(create_result_list_item)


        create_fbt_goods_response_data_create_result_info = cls(
            create_result_list=create_result_list,
        )


        create_fbt_goods_response_data_create_result_info.additional_properties = d
        return create_fbt_goods_response_data_create_result_info

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
