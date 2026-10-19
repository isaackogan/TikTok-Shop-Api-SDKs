from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.confirm_order_split_request_splittable_group import ConfirmOrderSplitRequestSplittableGroup
    from ..models.confirm_order_split_request_splittable_groups_v2 import ConfirmOrderSplitRequestSplittableGroupsV2


T = TypeVar("T", bound="ConfirmOrderSplitRequest")


@_attrs_define
class ConfirmOrderSplitRequest:
    """
    Attributes:
        splittable_groups (list[ConfirmOrderSplitRequestSplittableGroup]): Groups of order line items to split. Each
            successfully split group is returned as a separate package.
        splittable_groups_v2 (list[ConfirmOrderSplitRequestSplittableGroupsV2] | Unset): This new parameter is
            completely backward compatible with the previous splittable groups field and in addition this supports bundle
            order splitting, use the sub items accordingly
    """

    splittable_groups: list[ConfirmOrderSplitRequestSplittableGroup]
    splittable_groups_v2: list[ConfirmOrderSplitRequestSplittableGroupsV2] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        splittable_groups = []
        for splittable_groups_item_data in self.splittable_groups:
            splittable_groups_item = splittable_groups_item_data.to_dict()
            splittable_groups.append(splittable_groups_item)

        splittable_groups_v2: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.splittable_groups_v2, Unset):
            splittable_groups_v2 = []
            for splittable_groups_v2_item_data in self.splittable_groups_v2:
                splittable_groups_v2_item = splittable_groups_v2_item_data.to_dict()
                splittable_groups_v2.append(splittable_groups_v2_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "splittable_groups": splittable_groups,
            }
        )
        if splittable_groups_v2 is not UNSET:
            field_dict["splittable_groups_v2"] = splittable_groups_v2

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.confirm_order_split_request_splittable_group import (
            ConfirmOrderSplitRequestSplittableGroup,  # noqa: PLC0415
        )
        from ..models.confirm_order_split_request_splittable_groups_v2 import (
            ConfirmOrderSplitRequestSplittableGroupsV2,  # noqa: PLC0415
        )

        d = dict(src_dict)
        splittable_groups = []
        _splittable_groups = d.pop("splittable_groups")
        for splittable_groups_item_data in _splittable_groups:
            splittable_groups_item = ConfirmOrderSplitRequestSplittableGroup.from_dict(splittable_groups_item_data)

            splittable_groups.append(splittable_groups_item)

        _splittable_groups_v2 = d.pop("splittable_groups_v2", UNSET)
        splittable_groups_v2: list[ConfirmOrderSplitRequestSplittableGroupsV2] | Unset = UNSET
        if _splittable_groups_v2 is not UNSET:
            splittable_groups_v2 = []
            for splittable_groups_v2_item_data in _splittable_groups_v2:
                splittable_groups_v2_item = ConfirmOrderSplitRequestSplittableGroupsV2.from_dict(
                    splittable_groups_v2_item_data
                )

                splittable_groups_v2.append(splittable_groups_v2_item)

        confirm_order_split_request = cls(
            splittable_groups=splittable_groups,
            splittable_groups_v2=splittable_groups_v2,
        )

        confirm_order_split_request.additional_properties = d
        return confirm_order_split_request

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
