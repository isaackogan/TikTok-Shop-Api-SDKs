from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_fbt_goods_info_request_update_goods_dto import UpdateFBTGoodsInfoRequestUpdateGoodsDto





T = TypeVar("T", bound="UpdateFBTGoodsInfoRequest")



@_attrs_define
class UpdateFBTGoodsInfoRequest:
    """ 
        Attributes:
            update_goods_dto (UpdateFBTGoodsInfoRequestUpdateGoodsDto | Unset):
     """

    update_goods_dto: UpdateFBTGoodsInfoRequestUpdateGoodsDto | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_fbt_goods_info_request_update_goods_dto import UpdateFBTGoodsInfoRequestUpdateGoodsDto # noqa: PLC0415
        update_goods_dto: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_goods_dto, Unset):
            update_goods_dto = self.update_goods_dto.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if update_goods_dto is not UNSET:
            field_dict["update_goods_dto"] = update_goods_dto

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_fbt_goods_info_request_update_goods_dto import UpdateFBTGoodsInfoRequestUpdateGoodsDto # noqa: PLC0415
        d = dict(src_dict)
        _update_goods_dto = d.pop("update_goods_dto", UNSET)
        update_goods_dto: UpdateFBTGoodsInfoRequestUpdateGoodsDto | Unset
        if isinstance(_update_goods_dto,  Unset):
            update_goods_dto = UNSET
        else:
            update_goods_dto = UpdateFBTGoodsInfoRequestUpdateGoodsDto.from_dict(_update_goods_dto)




        update_fbt_goods_info_request = cls(
            update_goods_dto=update_goods_dto,
        )


        update_fbt_goods_info_request.additional_properties = d
        return update_fbt_goods_info_request

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
