from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_inbox_category_counts_response_data_data_group_count import GetInboxCategoryCountsResponseDataDataGroupCount





T = TypeVar("T", bound="GetInboxCategoryCountsResponseDataData")



@_attrs_define
class GetInboxCategoryCountsResponseDataData:
    """ 
        Attributes:
            group_counts (list[GetInboxCategoryCountsResponseDataDataGroupCount] | Unset): Conversation counts for each
                inbox category.
     """

    group_counts: list[GetInboxCategoryCountsResponseDataDataGroupCount] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_inbox_category_counts_response_data_data_group_count import GetInboxCategoryCountsResponseDataDataGroupCount # noqa: PLC0415
        group_counts: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.group_counts, Unset):
            group_counts = []
            for group_counts_item_data in self.group_counts:
                group_counts_item = group_counts_item_data.to_dict()
                group_counts.append(group_counts_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if group_counts is not UNSET:
            field_dict["group_counts"] = group_counts

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_inbox_category_counts_response_data_data_group_count import GetInboxCategoryCountsResponseDataDataGroupCount # noqa: PLC0415
        d = dict(src_dict)
        _group_counts = d.pop("group_counts", UNSET)
        group_counts: list[GetInboxCategoryCountsResponseDataDataGroupCount] | Unset = UNSET
        if _group_counts is not UNSET:
            group_counts = []
            for group_counts_item_data in _group_counts:
                group_counts_item = GetInboxCategoryCountsResponseDataDataGroupCount.from_dict(group_counts_item_data)



                group_counts.append(group_counts_item)


        get_inbox_category_counts_response_data_data = cls(
            group_counts=group_counts,
        )


        get_inbox_category_counts_response_data_data.additional_properties = d
        return get_inbox_category_counts_response_data_data

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
