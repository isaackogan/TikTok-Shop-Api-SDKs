from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_package_detail_response_data_order_sku import GetPackageDetailResponseDataOrderSku





T = TypeVar("T", bound="Order")



@_attrs_define
class Order:
    """ 
        Attributes:
            id (str | Unset): TikTok Shop order ID.
            skus (list[GetPackageDetailResponseDataOrderSku] | Unset): [Deprecated]SKU information.
     """

    id: str | Unset = UNSET
    skus: list[GetPackageDetailResponseDataOrderSku] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_package_detail_response_data_order_sku import GetPackageDetailResponseDataOrderSku # noqa: PLC0415
        id = self.id

        skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.skus, Unset):
            skus = []
            for skus_item_data in self.skus:
                skus_item = skus_item_data.to_dict()
                skus.append(skus_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if skus is not UNSET:
            field_dict["skus"] = skus

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_package_detail_response_data_order_sku import GetPackageDetailResponseDataOrderSku # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _skus = d.pop("skus", UNSET)
        skus: list[GetPackageDetailResponseDataOrderSku] | Unset = UNSET
        if _skus is not UNSET:
            skus = []
            for skus_item_data in _skus:
                skus_item = GetPackageDetailResponseDataOrderSku.from_dict(skus_item_data)



                skus.append(skus_item)


        order = cls(
            id=id,
            skus=skus,
        )


        order.additional_properties = d
        return order

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
