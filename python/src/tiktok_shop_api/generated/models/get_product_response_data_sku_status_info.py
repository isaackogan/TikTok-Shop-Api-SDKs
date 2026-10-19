from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.get_product_response_data_sku_status_info_deactivation_source import (
    GetProductResponseDataSkuStatusInfoDeactivationSource,
)
from ..models.get_product_response_data_sku_status_info_status import GetProductResponseDataSkuStatusInfoStatus
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetProductResponseDataSkuStatusInfo")


@_attrs_define
class GetProductResponseDataSkuStatusInfo:
    """
    Attributes:
        deactivation_source (GetProductResponseDataSkuStatusInfoDeactivationSource | Unset): The deactivation source of
            the SKU with `DEACTIVATED` status.
            Possible values:
            - SELLER: Indicates that the seller deactivated the SKU
            - PLATFORM: Indicates that the platform de-activated the SKU due to violation reasons
            - COMBO_RELATION: Indicates that the platform de-activated the bundle-SKU due to the deactivation of sub-SKU.
        status (GetProductResponseDataSkuStatusInfoStatus | Unset): The SKU status in TikTok Shop.
            Possible values:
            - NORMAL
            - DEACTIVATED
    """

    deactivation_source: GetProductResponseDataSkuStatusInfoDeactivationSource | Unset = UNSET
    status: GetProductResponseDataSkuStatusInfoStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        deactivation_source: str | Unset = UNSET
        if not isinstance(self.deactivation_source, Unset):
            deactivation_source = self.deactivation_source.value

        status: str | Unset = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if deactivation_source is not UNSET:
            field_dict["deactivation_source"] = deactivation_source
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        _deactivation_source = d.pop("deactivation_source", UNSET)
        deactivation_source: GetProductResponseDataSkuStatusInfoDeactivationSource | Unset
        if isinstance(_deactivation_source, Unset):
            deactivation_source = UNSET
        else:
            deactivation_source = GetProductResponseDataSkuStatusInfoDeactivationSource(_deactivation_source)

        _status = d.pop("status", UNSET)
        status: GetProductResponseDataSkuStatusInfoStatus | Unset
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = GetProductResponseDataSkuStatusInfoStatus(_status)

        get_product_response_data_sku_status_info = cls(
            deactivation_source=deactivation_source,
            status=status,
        )

        get_product_response_data_sku_status_info.additional_properties = d
        return get_product_response_data_sku_status_info

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
