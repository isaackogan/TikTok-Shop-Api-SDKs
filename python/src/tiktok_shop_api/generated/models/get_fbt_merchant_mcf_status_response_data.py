from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_fbt_merchant_mcf_status_response_data_mcf_status import (
        GetFBTMerchantMCFStatusResponseDataMcfStatus,
    )


T = TypeVar("T", bound="GetFBTMerchantMCFStatusResponseData")


@_attrs_define
class GetFBTMerchantMCFStatusResponseData:
    """
    Attributes:
        mcf_status (GetFBTMerchantMCFStatusResponseDataMcfStatus | Unset):
    """

    mcf_status: GetFBTMerchantMCFStatusResponseDataMcfStatus | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        mcf_status: dict[str, Any] | Unset = UNSET
        if not isinstance(self.mcf_status, Unset):
            mcf_status = self.mcf_status.to_dict()

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mcf_status is not UNSET:
            field_dict["mcf_status"] = mcf_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_fbt_merchant_mcf_status_response_data_mcf_status import (
            GetFBTMerchantMCFStatusResponseDataMcfStatus,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _mcf_status = d.pop("mcf_status", UNSET)
        mcf_status: GetFBTMerchantMCFStatusResponseDataMcfStatus | Unset
        if isinstance(_mcf_status, Unset):
            mcf_status = UNSET
        else:
            mcf_status = GetFBTMerchantMCFStatusResponseDataMcfStatus.from_dict(_mcf_status)

        get_fbt_merchant_mcf_status_response_data = cls(
            mcf_status=mcf_status,
        )

        get_fbt_merchant_mcf_status_response_data.additional_properties = d
        return get_fbt_merchant_mcf_status_response_data

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
