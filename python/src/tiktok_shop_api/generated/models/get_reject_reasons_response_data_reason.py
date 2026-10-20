from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetRejectReasonsResponseDataReason")



@_attrs_define
class GetRejectReasonsResponseDataReason:
    """ 
        Attributes:
            name (str | Unset): The reject reason key. Pass this exact value to the corresponding seller reject API as the
                reject reason. Note: The available reject reasons may change depending on the current aftersales request
                context. To avoid using stale or inapplicable reason keys, call this API close to the reject action and use the
                latest returned name values instead of hardcoding them.
            text (str | Unset): The corresponding text to the reason name, localized based on the locale input parameter.
     """

    name: str | Unset = UNSET
    text: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        name = self.name

        text = self.text


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if name is not UNSET:
            field_dict["name"] = name
        if text is not UNSET:
            field_dict["text"] = text

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name", UNSET)

        text = d.pop("text", UNSET)

        get_reject_reasons_response_data_reason = cls(
            name=name,
            text=text,
        )


        get_reject_reasons_response_data_reason.additional_properties = d
        return get_reject_reasons_response_data_reason

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
