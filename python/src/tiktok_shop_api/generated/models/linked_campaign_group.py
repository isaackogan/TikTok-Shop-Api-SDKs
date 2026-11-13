from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.official_sales_period import OfficialSalesPeriod





T = TypeVar("T", bound="LinkedCampaignGroup")



@_attrs_define
class LinkedCampaignGroup:
    """ 
        Attributes:
            id (str | Unset): Positive campaign group ID, always returned when the summary exists. A decimal string from 1
                to 9223372036854775807.
            official_sales_period (OfficialSalesPeriod | Unset):
            title (str | Unset): Nonempty campaign group name. Omitted if unavailable.
     """

    id: str | Unset = UNSET
    official_sales_period: OfficialSalesPeriod | Unset = UNSET
    title: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.official_sales_period import OfficialSalesPeriod # noqa: PLC0415
        id = self.id

        official_sales_period: dict[str, Any] | Unset = UNSET
        if not isinstance(self.official_sales_period, Unset):
            official_sales_period = self.official_sales_period.to_dict()

        title = self.title


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if official_sales_period is not UNSET:
            field_dict["official_sales_period"] = official_sales_period
        if title is not UNSET:
            field_dict["title"] = title

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.official_sales_period import OfficialSalesPeriod # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        _official_sales_period = d.pop("official_sales_period", UNSET)
        official_sales_period: OfficialSalesPeriod | Unset
        if isinstance(_official_sales_period,  Unset):
            official_sales_period = UNSET
        else:
            official_sales_period = OfficialSalesPeriod.from_dict(_official_sales_period)




        title = d.pop("title", UNSET)

        linked_campaign_group = cls(
            id=id,
            official_sales_period=official_sales_period,
            title=title,
        )


        linked_campaign_group.additional_properties = d
        return linked_campaign_group

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
