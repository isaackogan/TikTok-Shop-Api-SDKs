from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_acc_audience_penetration_response_data_funnel_clicked import GetACCAudiencePenetrationResponseDataFunnelClicked
  from ..models.get_acc_audience_penetration_response_data_funnel_ordered import GetACCAudiencePenetrationResponseDataFunnelOrdered
  from ..models.get_acc_audience_penetration_response_data_funnel_total import GetACCAudiencePenetrationResponseDataFunnelTotal
  from ..models.get_acc_audience_penetration_response_data_funnel_viewed import GetACCAudiencePenetrationResponseDataFunnelViewed





T = TypeVar("T", bound="GetACCAudiencePenetrationResponseDataFunnel")



@_attrs_define
class GetACCAudiencePenetrationResponseDataFunnel:
    """ 
        Attributes:
            clicked (GetACCAudiencePenetrationResponseDataFunnelClicked | Unset):
            ordered (GetACCAudiencePenetrationResponseDataFunnelOrdered | Unset):
            total (GetACCAudiencePenetrationResponseDataFunnelTotal | Unset):
            viewed (GetACCAudiencePenetrationResponseDataFunnelViewed | Unset):
     """

    clicked: GetACCAudiencePenetrationResponseDataFunnelClicked | Unset = UNSET
    ordered: GetACCAudiencePenetrationResponseDataFunnelOrdered | Unset = UNSET
    total: GetACCAudiencePenetrationResponseDataFunnelTotal | Unset = UNSET
    viewed: GetACCAudiencePenetrationResponseDataFunnelViewed | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_penetration_response_data_funnel_clicked import GetACCAudiencePenetrationResponseDataFunnelClicked # noqa: PLC0415
        from ..models.get_acc_audience_penetration_response_data_funnel_ordered import GetACCAudiencePenetrationResponseDataFunnelOrdered # noqa: PLC0415
        from ..models.get_acc_audience_penetration_response_data_funnel_total import GetACCAudiencePenetrationResponseDataFunnelTotal # noqa: PLC0415
        from ..models.get_acc_audience_penetration_response_data_funnel_viewed import GetACCAudiencePenetrationResponseDataFunnelViewed # noqa: PLC0415
        clicked: dict[str, Any] | Unset = UNSET
        if not isinstance(self.clicked, Unset):
            clicked = self.clicked.to_dict()

        ordered: dict[str, Any] | Unset = UNSET
        if not isinstance(self.ordered, Unset):
            ordered = self.ordered.to_dict()

        total: dict[str, Any] | Unset = UNSET
        if not isinstance(self.total, Unset):
            total = self.total.to_dict()

        viewed: dict[str, Any] | Unset = UNSET
        if not isinstance(self.viewed, Unset):
            viewed = self.viewed.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if clicked is not UNSET:
            field_dict["clicked"] = clicked
        if ordered is not UNSET:
            field_dict["ordered"] = ordered
        if total is not UNSET:
            field_dict["total"] = total
        if viewed is not UNSET:
            field_dict["viewed"] = viewed

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_penetration_response_data_funnel_clicked import GetACCAudiencePenetrationResponseDataFunnelClicked # noqa: PLC0415
        from ..models.get_acc_audience_penetration_response_data_funnel_ordered import GetACCAudiencePenetrationResponseDataFunnelOrdered # noqa: PLC0415
        from ..models.get_acc_audience_penetration_response_data_funnel_total import GetACCAudiencePenetrationResponseDataFunnelTotal # noqa: PLC0415
        from ..models.get_acc_audience_penetration_response_data_funnel_viewed import GetACCAudiencePenetrationResponseDataFunnelViewed # noqa: PLC0415
        d = dict(src_dict)
        _clicked = d.pop("clicked", UNSET)
        clicked: GetACCAudiencePenetrationResponseDataFunnelClicked | Unset
        if isinstance(_clicked,  Unset):
            clicked = UNSET
        else:
            clicked = GetACCAudiencePenetrationResponseDataFunnelClicked.from_dict(_clicked)




        _ordered = d.pop("ordered", UNSET)
        ordered: GetACCAudiencePenetrationResponseDataFunnelOrdered | Unset
        if isinstance(_ordered,  Unset):
            ordered = UNSET
        else:
            ordered = GetACCAudiencePenetrationResponseDataFunnelOrdered.from_dict(_ordered)




        _total = d.pop("total", UNSET)
        total: GetACCAudiencePenetrationResponseDataFunnelTotal | Unset
        if isinstance(_total,  Unset):
            total = UNSET
        else:
            total = GetACCAudiencePenetrationResponseDataFunnelTotal.from_dict(_total)




        _viewed = d.pop("viewed", UNSET)
        viewed: GetACCAudiencePenetrationResponseDataFunnelViewed | Unset
        if isinstance(_viewed,  Unset):
            viewed = UNSET
        else:
            viewed = GetACCAudiencePenetrationResponseDataFunnelViewed.from_dict(_viewed)




        get_acc_audience_penetration_response_data_funnel = cls(
            clicked=clicked,
            ordered=ordered,
            total=total,
            viewed=viewed,
        )


        get_acc_audience_penetration_response_data_funnel.additional_properties = d
        return get_acc_audience_penetration_response_data_funnel

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
