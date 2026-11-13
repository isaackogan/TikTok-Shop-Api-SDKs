from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.effective_period import EffectivePeriod
  from ..models.resource import Resource





T = TypeVar("T", bound="Policy")



@_attrs_define
class Policy:
    """ 
        Attributes:
            description (str | Unset): Complete policy information, including discount conditions and exceptions. Omitted
                when terms are expressed only through images or links; the relevant resources are then provided in resources.
            effective_period (EffectivePeriod | Unset):
            resources (list[Resource] | Unset): Fee images and explanatory links in the applicable language. Always returned
                when terms include resources. Use these resources to understand the complete fees.
            title (str | Unset): Nonempty policy name. Omitted if unavailable.
     """

    description: str | Unset = UNSET
    effective_period: EffectivePeriod | Unset = UNSET
    resources: list[Resource] | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.effective_period import EffectivePeriod # noqa: PLC0415
        from ..models.resource import Resource # noqa: PLC0415
        description = self.description

        effective_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.effective_period, Unset):
            effective_period = self.effective_period.to_dict()

        resources: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.resources, Unset):
            resources = []
            for resources_item_data in self.resources:
                resources_item = resources_item_data.to_dict()
                resources.append(resources_item)



        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if effective_period is not UNSET:
            field_dict["effective_period"] = effective_period
        if resources is not UNSET:
            field_dict["resources"] = resources
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.effective_period import EffectivePeriod # noqa: PLC0415
        from ..models.resource import Resource # noqa: PLC0415
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _effective_period = d.pop("effective_period", UNSET)
        effective_period: EffectivePeriod | Unset
        if isinstance(_effective_period,  Unset):
            effective_period = UNSET
        else:
            effective_period = EffectivePeriod.from_dict(_effective_period)




        _resources = d.pop("resources", UNSET)
        resources: list[Resource] | Unset = UNSET
        if _resources is not UNSET:
            resources = []
            for resources_item_data in _resources:
                resources_item = Resource.from_dict(resources_item_data)



                resources.append(resources_item)


        title = d.pop("title", UNSET)

        policy = cls(
            description=description,
            effective_period=effective_period,
            resources=resources,
            title=title,
        )


        policy.additional_properties = d
        return policy

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
