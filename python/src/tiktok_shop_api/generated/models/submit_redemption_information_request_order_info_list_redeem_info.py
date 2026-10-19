from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="SubmitRedemptionInformationRequestOrderInfoListRedeemInfo")


@_attrs_define
class SubmitRedemptionInformationRequestOrderInfoListRedeemInfo:
    """
    Attributes:
        redeem_type (str): What redeem type that you callback.
            'CODE' - type code
            'URL' - type url
            'CODE_PIN' - type pin and code
        redeem_data (str | Unset): Set the redeem data to this field with the maximum number of characters 1200. The
            example of each type is shown below,
            CODE: abc12344
            URL: https://{your_domain}/abc
            CODE_PIN(json format):
            {"type": "CODE_PIN","code": "12345","pin": "abc"}
        redeem_instruction_info (str | Unset): Additional redemption instruction in JSON format. Use instruction_url to
            specify a third-party website where the buyer completes redemption. This URL is included as a clickable link in
            the fulfillment email.
            Example: {"instruction_url": "https://example.com/redeem"}
    """

    redeem_type: str
    redeem_data: str | Unset = UNSET
    redeem_instruction_info: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        redeem_type = self.redeem_type

        redeem_data = self.redeem_data

        redeem_instruction_info = self.redeem_instruction_info

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "redeem_type": redeem_type,
            }
        )
        if redeem_data is not UNSET:
            field_dict["redeem_data"] = redeem_data
        if redeem_instruction_info is not UNSET:
            field_dict["redeem_instruction_info"] = redeem_instruction_info

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        redeem_type = d.pop("redeem_type")

        redeem_data = d.pop("redeem_data", UNSET)

        redeem_instruction_info = d.pop("redeem_instruction_info", UNSET)

        submit_redemption_information_request_order_info_list_redeem_info = cls(
            redeem_type=redeem_type,
            redeem_data=redeem_data,
            redeem_instruction_info=redeem_instruction_info,
        )

        submit_redemption_information_request_order_info_list_redeem_info.additional_properties = d
        return submit_redemption_information_request_order_info_list_redeem_info

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
