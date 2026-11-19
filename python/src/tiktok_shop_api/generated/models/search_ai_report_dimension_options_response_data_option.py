from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.creator import Creator





T = TypeVar("T", bound="SearchAIReportDimensionOptionsResponseDataOption")



@_attrs_define
class SearchAIReportDimensionOptionsResponseDataOption:
    """ 
        Attributes:
            creator (Creator | Unset):
            image_url (str | Unset): Image for the candidate, when available.
            name (str | Unset): Display label; may be absent for an unknown entity.
            value (str | Unset): Value to send in filters[].values, such as LIVE or a product ID. Creator options use
                creator.creator_open_id instead.
     """

    creator: Creator | Unset = UNSET
    image_url: str | Unset = UNSET
    name: str | Unset = UNSET
    value: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.creator import Creator # noqa: PLC0415
        creator: dict[str, Any] | Unset = UNSET
        if not isinstance(self.creator, Unset):
            creator = self.creator.to_dict()

        image_url = self.image_url

        name = self.name

        value = self.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creator is not UNSET:
            field_dict["creator"] = creator
        if image_url is not UNSET:
            field_dict["image_url"] = image_url
        if name is not UNSET:
            field_dict["name"] = name
        if value is not UNSET:
            field_dict["value"] = value

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.creator import Creator # noqa: PLC0415
        d = dict(src_dict)
        _creator = d.pop("creator", UNSET)
        creator: Creator | Unset
        if isinstance(_creator,  Unset):
            creator = UNSET
        else:
            creator = Creator.from_dict(_creator)




        image_url = d.pop("image_url", UNSET)

        name = d.pop("name", UNSET)

        value = d.pop("value", UNSET)

        search_ai_report_dimension_options_response_data_option = cls(
            creator=creator,
            image_url=image_url,
            name=name,
            value=value,
        )


        search_ai_report_dimension_options_response_data_option.additional_properties = d
        return search_ai_report_dimension_options_response_data_option

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
