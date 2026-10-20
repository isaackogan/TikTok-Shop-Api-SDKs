from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.check_creator_outreach_eligibility_request_creator_info import (
        CheckCreatorOutreachEligibilityRequestCreatorInfo,
    )


T = TypeVar("T", bound="CheckCreatorOutreachEligibilityRequest")


@_attrs_define
class CheckCreatorOutreachEligibilityRequest:
    """
    Attributes:
        creator_infos (list[CheckCreatorOutreachEligibilityRequestCreatorInfo]): Creator information to evaluate for the
            shop's outreach eligibility. Provide one to 100 entries with unique Creator Open IDs.
    """

    creator_infos: list[CheckCreatorOutreachEligibilityRequestCreatorInfo]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        creator_infos = []
        for creator_infos_item_data in self.creator_infos:
            creator_infos_item = creator_infos_item_data.to_dict()
            creator_infos.append(creator_infos_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "creator_infos": creator_infos,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.check_creator_outreach_eligibility_request_creator_info import (
            CheckCreatorOutreachEligibilityRequestCreatorInfo,  # noqa: PLC0415
        )

        d = dict(src_dict)
        creator_infos = []
        _creator_infos = d.pop("creator_infos")
        for creator_infos_item_data in _creator_infos:
            creator_infos_item = CheckCreatorOutreachEligibilityRequestCreatorInfo.from_dict(creator_infos_item_data)

            creator_infos.append(creator_infos_item)

        check_creator_outreach_eligibility_request = cls(
            creator_infos=creator_infos,
        )

        check_creator_outreach_eligibility_request.additional_properties = d
        return check_creator_outreach_eligibility_request

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
