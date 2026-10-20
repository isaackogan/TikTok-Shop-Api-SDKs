from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="MapTokopediaToTikTokShopProductIDsRequest")



@_attrs_define
class MapTokopediaToTikTokShopProductIDsRequest:
    """ 
        Attributes:
            toko_pids (list[int] | Unset): List of Tokopedia product IDs to map to TikTok Shop product IDs.
     """

    toko_pids: list[int] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        toko_pids: list[int] | Unset = UNSET
        if not isinstance(self.toko_pids, Unset):
            toko_pids = self.toko_pids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if toko_pids is not UNSET:
            field_dict["toko_pids"] = toko_pids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        toko_pids = cast(list[int], d.pop("toko_pids", UNSET))


        map_tokopedia_to_tik_tok_shop_product_i_ds_request = cls(
            toko_pids=toko_pids,
        )


        map_tokopedia_to_tik_tok_shop_product_i_ds_request.additional_properties = d
        return map_tokopedia_to_tik_tok_shop_product_i_ds_request

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
