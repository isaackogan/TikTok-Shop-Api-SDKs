from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="GetBrandsResponseDataBrand")


@_attrs_define
class GetBrandsResponseDataBrand:
    """
    Attributes:
        id (str | Unset): The brand ID.
        name (str | Unset): The brand name.
        authorized_status (str | Unset): A status to indicate whether the seller has obtained prior authorization to
            sell goods bearing the brand's trademark, name, or logo.
            Possible values:
            - UNAUTHORIEZD
            - AUTHORIZED

            **Note**: If the brand is unauthorized, check `is_t1_brand` to determine if you can use it during product
            creation.
        is_t1_brand (bool | Unset): A flag to indicate whether the brand is a T1 brand, which refers to internationally
            renowned brands that may have compliance risks and require sellers to obtain brand authorization.

            **Note**:
            - You cannot create products with unauthorized T1 brands.
            - You can create products with unauthorized non-T1 brands, **but** the brand information will not appear on the
            product display page.
            You can obtain authorization by submitting the required qualifications through TikTok Shop Seller Center >
            Qualification Center > Brand qualification.
        brand_status (str | Unset): The availability of an **authorized brand** in the requested category.
            Possible values:
            - AVAILABLE
            - UNAVAILABLE

            **Note**: Not applicable if you did not specify the category ID, or the brand is unauthorized.
    """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    authorized_status: str | Unset = UNSET
    is_t1_brand: bool | Unset = UNSET
    brand_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        name = self.name

        authorized_status = self.authorized_status

        is_t1_brand = self.is_t1_brand

        brand_status = self.brand_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if authorized_status is not UNSET:
            field_dict["authorized_status"] = authorized_status
        if is_t1_brand is not UNSET:
            field_dict["is_t1_brand"] = is_t1_brand
        if brand_status is not UNSET:
            field_dict["brand_status"] = brand_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        authorized_status = d.pop("authorized_status", UNSET)

        is_t1_brand = d.pop("is_t1_brand", UNSET)

        brand_status = d.pop("brand_status", UNSET)

        get_brands_response_data_brand = cls(
            id=id,
            name=name,
            authorized_status=authorized_status,
            is_t1_brand=is_t1_brand,
            brand_status=brand_status,
        )

        get_brands_response_data_brand.additional_properties = d
        return get_brands_response_data_brand

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
