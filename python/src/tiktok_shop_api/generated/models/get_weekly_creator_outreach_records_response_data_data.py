from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_weekly_creator_outreach_records_response_data_data_connect_list import GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList





T = TypeVar("T", bound="GetWeeklyCreatorOutreachRecordsResponseDataData")



@_attrs_define
class GetWeeklyCreatorOutreachRecordsResponseDataData:
    """ 
        Attributes:
            total (int | Unset): Total number of records matching the query before pagination.
            connect_list (list[GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList] | Unset): Return the list of
                newly connected creator records for the shop
     """

    total: int | Unset = UNSET
    connect_list: list[GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_weekly_creator_outreach_records_response_data_data_connect_list import GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList # noqa: PLC0415
        total = self.total

        connect_list: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.connect_list, Unset):
            connect_list = []
            for connect_list_item_data in self.connect_list:
                connect_list_item = connect_list_item_data.to_dict()
                connect_list.append(connect_list_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if total is not UNSET:
            field_dict["total"] = total
        if connect_list is not UNSET:
            field_dict["connect_list"] = connect_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_weekly_creator_outreach_records_response_data_data_connect_list import GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList # noqa: PLC0415
        d = dict(src_dict)
        total = d.pop("total", UNSET)

        _connect_list = d.pop("connect_list", UNSET)
        connect_list: list[GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList] | Unset = UNSET
        if _connect_list is not UNSET:
            connect_list = []
            for connect_list_item_data in _connect_list:
                connect_list_item = GetWeeklyCreatorOutreachRecordsResponseDataDataConnectList.from_dict(connect_list_item_data)



                connect_list.append(connect_list_item)


        get_weekly_creator_outreach_records_response_data_data = cls(
            total=total,
            connect_list=connect_list,
        )


        get_weekly_creator_outreach_records_response_data_data.additional_properties = d
        return get_weekly_creator_outreach_records_response_data_data

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
