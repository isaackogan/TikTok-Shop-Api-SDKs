from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_creator_sample_application_detail_response_data_sample_application import GetCreatorSampleApplicationDetailResponseDataSampleApplication





T = TypeVar("T", bound="GetCreatorSampleApplicationDetailResponseData")



@_attrs_define
class GetCreatorSampleApplicationDetailResponseData:
    """ 
        Attributes:
            sample_application (GetCreatorSampleApplicationDetailResponseDataSampleApplication | Unset):
     """

    sample_application: GetCreatorSampleApplicationDetailResponseDataSampleApplication | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_creator_sample_application_detail_response_data_sample_application import GetCreatorSampleApplicationDetailResponseDataSampleApplication # noqa: PLC0415
        sample_application: dict[str, Any] | Unset = UNSET
        if not isinstance(self.sample_application, Unset):
            sample_application = self.sample_application.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sample_application is not UNSET:
            field_dict["sample_application"] = sample_application

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_creator_sample_application_detail_response_data_sample_application import GetCreatorSampleApplicationDetailResponseDataSampleApplication # noqa: PLC0415
        d = dict(src_dict)
        _sample_application = d.pop("sample_application", UNSET)
        sample_application: GetCreatorSampleApplicationDetailResponseDataSampleApplication | Unset
        if isinstance(_sample_application,  Unset):
            sample_application = UNSET
        else:
            sample_application = GetCreatorSampleApplicationDetailResponseDataSampleApplication.from_dict(_sample_application)




        get_creator_sample_application_detail_response_data = cls(
            sample_application=sample_application,
        )


        get_creator_sample_application_detail_response_data.additional_properties = d
        return get_creator_sample_application_detail_response_data

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
