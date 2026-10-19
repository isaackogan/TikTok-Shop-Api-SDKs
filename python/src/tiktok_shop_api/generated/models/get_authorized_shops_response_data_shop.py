from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_authorized_shops_response_data_shop_seller_type import GetAuthorizedShopsResponseDataShopSellerType
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetAuthorizedShopsResponseDataShop")


@_attrs_define
class GetAuthorizedShopsResponseDataShop:
    """
    Attributes:
        id (str | Unset): An internal identifier for the TikTok Shop.
        name (str | Unset): The TikTok Shop name.
        region (str | Unset): The region of the shop.
        seller_type (GetAuthorizedShopsResponseDataShopSellerType | Unset): The type of seller.
            Possible values:
            - CROSS_BORDER: Cross border sellers with multiple shops in different countries.
            - LOCAL: Local sellers with only 1 shop.
        cipher (str | Unset): An encrypted token used to securely identify a shop in API requests. There is no need for
            decryption on the receiving end.
        code (str | Unset): The TikTok Shop code, which is also displayed on Seller Center.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    region: str | Unset = UNSET
    seller_type: GetAuthorizedShopsResponseDataShopSellerType | Unset = UNSET
    cipher: str | Unset = UNSET
    code: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        region = self.region

        seller_type: str | Unset = UNSET
        if not isinstance(self.seller_type, Unset):
            seller_type = self.seller_type.value

        cipher = self.cipher

        code = self.code

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if region is not UNSET:
            field_dict["region"] = region
        if seller_type is not UNSET:
            field_dict["seller_type"] = seller_type
        if cipher is not UNSET:
            field_dict["cipher"] = cipher
        if code is not UNSET:
            field_dict["code"] = code

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        region = d.pop("region", UNSET)

        _seller_type = d.pop("seller_type", UNSET)
        seller_type: GetAuthorizedShopsResponseDataShopSellerType | Unset
        if isinstance(_seller_type, Unset):
            seller_type = UNSET
        else:
            seller_type = GetAuthorizedShopsResponseDataShopSellerType(_seller_type)

        cipher = d.pop("cipher", UNSET)

        code = d.pop("code", UNSET)

        get_authorized_shops_response_data_shop = cls(
            id=id,
            name=name,
            region=region,
            seller_type=seller_type,
            cipher=cipher,
            code=code,
        )

        get_authorized_shops_response_data_shop.additional_properties = d
        return get_authorized_shops_response_data_shop

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
