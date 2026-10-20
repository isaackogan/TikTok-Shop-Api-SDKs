from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_bestselling_creators_response_data_creator import GetBestsellingCreatorsResponseDataCreator





T = TypeVar("T", bound="GetBestsellingCreatorsResponseData")



@_attrs_define
class GetBestsellingCreatorsResponseData:
    """ 
        Attributes:
            creators (list[GetBestsellingCreatorsResponseDataCreator] | Unset): List of bestselling creator records for the
                target date range.
     """

    creators: list[GetBestsellingCreatorsResponseDataCreator] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_bestselling_creators_response_data_creator import GetBestsellingCreatorsResponseDataCreator # noqa: PLC0415
        creators: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.creators, Unset):
            creators = []
            for creators_item_data in self.creators:
                creators_item = creators_item_data.to_dict()
                creators.append(creators_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if creators is not UNSET:
            field_dict["creators"] = creators

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bestselling_creators_response_data_creator import GetBestsellingCreatorsResponseDataCreator # noqa: PLC0415
        d = dict(src_dict)
        _creators = d.pop("creators", UNSET)
        creators: list[GetBestsellingCreatorsResponseDataCreator] | Unset = UNSET
        if _creators is not UNSET:
            creators = []
            for creators_item_data in _creators:
                creators_item = GetBestsellingCreatorsResponseDataCreator.from_dict(creators_item_data)



                creators.append(creators_item)


        get_bestselling_creators_response_data = cls(
            creators=creators,
        )


        get_bestselling_creators_response_data.additional_properties = d
        return get_bestselling_creators_response_data

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
