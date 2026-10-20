from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info_hazmat_and_expiration_dto_list import SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoList





T = TypeVar("T", bound="SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfo")



@_attrs_define
class SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfo:
    """ 
        Attributes:
            hazmat_and_expiration_dto_list
                (list[SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoList] | Unset):
                Per-SKU hazmat, lot-control, and expiration-management results. Correlate each entry with the requested SKU
                using `tts_sku_id`.
     """

    hazmat_and_expiration_dto_list: list[SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info_hazmat_and_expiration_dto_list import SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoList # noqa: PLC0415
        hazmat_and_expiration_dto_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.hazmat_and_expiration_dto_list, Unset):
            hazmat_and_expiration_dto_list = []
            for hazmat_and_expiration_dto_list_item_data in self.hazmat_and_expiration_dto_list:
                hazmat_and_expiration_dto_list_item = hazmat_and_expiration_dto_list_item_data.to_dict()
                hazmat_and_expiration_dto_list.append(hazmat_and_expiration_dto_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if hazmat_and_expiration_dto_list is not UNSET:
            field_dict["hazmat_and_expiration_dto_list"] = hazmat_and_expiration_dto_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info_hazmat_and_expiration_dto_list import SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoList # noqa: PLC0415
        d = dict(src_dict)
        _hazmat_and_expiration_dto_list = d.pop("hazmat_and_expiration_dto_list", UNSET)
        hazmat_and_expiration_dto_list: list[SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoList] | Unset = UNSET
        if _hazmat_and_expiration_dto_list is not UNSET:
            hazmat_and_expiration_dto_list = []
            for hazmat_and_expiration_dto_list_item_data in _hazmat_and_expiration_dto_list:
                hazmat_and_expiration_dto_list_item = SearchGoodsHazmatAndExpirationInfoResponseDataHazmatAndExpirationInfoHazmatAndExpirationDtoList.from_dict(hazmat_and_expiration_dto_list_item_data)



                hazmat_and_expiration_dto_list.append(hazmat_and_expiration_dto_list_item)


        search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info = cls(
            hazmat_and_expiration_dto_list=hazmat_and_expiration_dto_list,
        )


        search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info.additional_properties = d
        return search_goods_hazmat_and_expiration_info_response_data_hazmat_and_expiration_info

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
