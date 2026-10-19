from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_bestselling_live_sessions_response_data_live import GetBestsellingLIVESessionsResponseDataLive


T = TypeVar("T", bound="GetBestsellingLIVESessionsResponseData")


@_attrs_define
class GetBestsellingLIVESessionsResponseData:
    """
    Attributes:
        lives (list[GetBestsellingLIVESessionsResponseDataLive] | Unset): List of bestselling LIVE session records for
            the target date range.
    """

    lives: list[GetBestsellingLIVESessionsResponseDataLive] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        lives: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.lives, Unset):
            lives = []
            for lives_item_data in self.lives:
                lives_item = lives_item_data.to_dict()
                lives.append(lives_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if lives is not UNSET:
            field_dict["lives"] = lives

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_bestselling_live_sessions_response_data_live import (
            GetBestsellingLIVESessionsResponseDataLive,  # noqa: PLC0415
        )

        d = dict(src_dict)
        _lives = d.pop("lives", UNSET)
        lives: list[GetBestsellingLIVESessionsResponseDataLive] | Unset = UNSET
        if _lives is not UNSET:
            lives = []
            for lives_item_data in _lives:
                lives_item = GetBestsellingLIVESessionsResponseDataLive.from_dict(lives_item_data)

                lives.append(lives_item)

        get_bestselling_live_sessions_response_data = cls(
            lives=lives,
        )

        get_bestselling_live_sessions_response_data.additional_properties = d
        return get_bestselling_live_sessions_response_data

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
