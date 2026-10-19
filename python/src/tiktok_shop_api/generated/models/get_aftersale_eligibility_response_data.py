from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_aftersale_eligibility_response_data_sku_eligibility import (
        GetAftersaleEligibilityResponseDataSkuEligibility,
    )


T = TypeVar("T", bound="GetAftersaleEligibilityResponseData")


@_attrs_define
class GetAftersaleEligibilityResponseData:
    """
    Attributes:
        sku_eligibility (list[GetAftersaleEligibilityResponseDataSkuEligibility] | Unset): The eligible aftersale
            options for a given SKU.
    """

    sku_eligibility: list[GetAftersaleEligibilityResponseDataSkuEligibility] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        sku_eligibility: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sku_eligibility, Unset):
            sku_eligibility = []
            for sku_eligibility_item_data in self.sku_eligibility:
                sku_eligibility_item = sku_eligibility_item_data.to_dict()
                sku_eligibility.append(sku_eligibility_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if sku_eligibility is not UNSET:
            field_dict["sku_eligibility"] = sku_eligibility

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_aftersale_eligibility_response_data_sku_eligibility import (
            GetAftersaleEligibilityResponseDataSkuEligibility,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _sku_eligibility = d.pop("sku_eligibility", UNSET)
        sku_eligibility: list[GetAftersaleEligibilityResponseDataSkuEligibility] | Unset = UNSET
        if _sku_eligibility is not UNSET:
            sku_eligibility = []
            for sku_eligibility_item_data in _sku_eligibility:
                sku_eligibility_item = GetAftersaleEligibilityResponseDataSkuEligibility.from_dict(
                    sku_eligibility_item_data
                )

                sku_eligibility.append(sku_eligibility_item)

        get_aftersale_eligibility_response_data = cls(
            sku_eligibility=sku_eligibility,
        )

        get_aftersale_eligibility_response_data.additional_properties = d
        return get_aftersale_eligibility_response_data

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
