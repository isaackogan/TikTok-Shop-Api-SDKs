from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="CreatorPreference")



@_attrs_define
class CreatorPreference:
    """ 
        Attributes:
            age_range (list[int] | Unset): Indexes of the selected creator age-range options in the campaign configuration.
            content_format (list[int] | Unset): Indexes of the selected content-format options in the campaign
                configuration.
            content_style (list[str] | Unset): Selected content-style keys or supported custom style text.
            follower_size (list[int] | Unset): Indexes of the selected creator follower-size options in the campaign
                configuration.
            notes (str | Unset): @redact Free-text creator preferences; may contain contact information.
            product_category_ids (list[str] | Unset): Product category IDs used to specify preferred creator categories.
     """

    age_range: list[int] | Unset = UNSET
    content_format: list[int] | Unset = UNSET
    content_style: list[str] | Unset = UNSET
    follower_size: list[int] | Unset = UNSET
    notes: str | Unset = UNSET
    product_category_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        age_range: list[int] | Unset = UNSET
        if not isinstance(self.age_range, Unset):
            age_range = self.age_range



        content_format: list[int] | Unset = UNSET
        if not isinstance(self.content_format, Unset):
            content_format = self.content_format



        content_style: list[str] | Unset = UNSET
        if not isinstance(self.content_style, Unset):
            content_style = self.content_style



        follower_size: list[int] | Unset = UNSET
        if not isinstance(self.follower_size, Unset):
            follower_size = self.follower_size



        notes = self.notes

        product_category_ids: list[str] | Unset = UNSET
        if not isinstance(self.product_category_ids, Unset):
            product_category_ids = self.product_category_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if age_range is not UNSET:
            field_dict["age_range"] = age_range
        if content_format is not UNSET:
            field_dict["content_format"] = content_format
        if content_style is not UNSET:
            field_dict["content_style"] = content_style
        if follower_size is not UNSET:
            field_dict["follower_size"] = follower_size
        if notes is not UNSET:
            field_dict["notes"] = notes
        if product_category_ids is not UNSET:
            field_dict["product_category_ids"] = product_category_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        age_range = cast(list[int], d.pop("age_range", UNSET))


        content_format = cast(list[int], d.pop("content_format", UNSET))


        content_style = cast(list[str], d.pop("content_style", UNSET))


        follower_size = cast(list[int], d.pop("follower_size", UNSET))


        notes = d.pop("notes", UNSET)

        product_category_ids = cast(list[str], d.pop("product_category_ids", UNSET))


        creator_preference = cls(
            age_range=age_range,
            content_format=content_format,
            content_style=content_style,
            follower_size=follower_size,
            notes=notes,
            product_category_ids=product_category_ids,
        )


        creator_preference.additional_properties = d
        return creator_preference

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
