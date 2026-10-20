from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetFBTMerchantMCFStatusResponseDataMcfStatus")



@_attrs_define
class GetFBTMerchantMCFStatusResponseDataMcfStatus:
    """ 
        Attributes:
            is_mcf (int | Unset): Flag indicating whether the seller has participated in Multi Channel Fulfillment. 0 means
                inactive and 1 means active.
     """

    is_mcf: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        is_mcf = self.is_mcf


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if is_mcf is not UNSET:
            field_dict["is_mcf"] = is_mcf

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        is_mcf = d.pop("is_mcf", UNSET)

        get_fbt_merchant_mcf_status_response_data_mcf_status = cls(
            is_mcf=is_mcf,
        )


        get_fbt_merchant_mcf_status_response_data_mcf_status.additional_properties = d
        return get_fbt_merchant_mcf_status_response_data_mcf_status

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
