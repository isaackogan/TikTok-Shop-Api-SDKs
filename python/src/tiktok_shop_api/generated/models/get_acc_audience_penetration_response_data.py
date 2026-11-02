from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast
import datetime

if TYPE_CHECKING:
  from ..models.get_acc_audience_penetration_response_data_funnel import GetACCAudiencePenetrationResponseDataFunnel





T = TypeVar("T", bound="GetACCAudiencePenetrationResponseData")



@_attrs_define
class GetACCAudiencePenetrationResponseData:
    """ 
        Attributes:
            funnel (GetACCAudiencePenetrationResponseDataFunnel | Unset):
            latest_available_date (datetime.date | Unset): Latest available reporting date for the selected shop, brand, and
                industry, in YYYY-MM-DD format (UTC). This date is used when the request date is omitted or blank; it can be
                later than an explicitly requested date.
     """

    funnel: GetACCAudiencePenetrationResponseDataFunnel | Unset = UNSET
    latest_available_date: datetime.date | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_acc_audience_penetration_response_data_funnel import GetACCAudiencePenetrationResponseDataFunnel # noqa: PLC0415
        funnel: dict[str, Any] | Unset = UNSET
        if not isinstance(self.funnel, Unset):
            funnel = self.funnel.to_dict()

        latest_available_date: str | Unset = UNSET
        if not isinstance(self.latest_available_date, Unset):
            latest_available_date = self.latest_available_date.isoformat()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if funnel is not UNSET:
            field_dict["funnel"] = funnel
        if latest_available_date is not UNSET:
            field_dict["latest_available_date"] = latest_available_date

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_acc_audience_penetration_response_data_funnel import GetACCAudiencePenetrationResponseDataFunnel # noqa: PLC0415
        d = dict(src_dict)
        _funnel = d.pop("funnel", UNSET)
        funnel: GetACCAudiencePenetrationResponseDataFunnel | Unset
        if isinstance(_funnel,  Unset):
            funnel = UNSET
        else:
            funnel = GetACCAudiencePenetrationResponseDataFunnel.from_dict(_funnel)




        _latest_available_date = d.pop("latest_available_date", UNSET)
        latest_available_date: datetime.date | Unset
        if isinstance(_latest_available_date,  Unset):
            latest_available_date = UNSET
        else:
            latest_available_date = datetime.date.fromisoformat(_latest_available_date)




        get_acc_audience_penetration_response_data = cls(
            funnel=funnel,
            latest_available_date=latest_available_date,
        )


        get_acc_audience_penetration_response_data.additional_properties = d
        return get_acc_audience_penetration_response_data

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
