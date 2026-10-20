from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.edit_open_collaboration_sample_rule_response_data import EditOpenCollaborationSampleRuleResponseData





T = TypeVar("T", bound="EditOpenCollaborationSampleRuleResponse")



@_attrs_define
class EditOpenCollaborationSampleRuleResponse:
    """ 
        Attributes:
            code (int | Unset): Status code; 0 means success.
            message (str | Unset): Success or failure message.
            request_id (str | Unset): Request log ID.
            data (EditOpenCollaborationSampleRuleResponseData | Unset):
     """

    code: int | Unset = UNSET
    message: str | Unset = UNSET
    request_id: str | Unset = UNSET
    data: EditOpenCollaborationSampleRuleResponseData | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.edit_open_collaboration_sample_rule_response_data import EditOpenCollaborationSampleRuleResponseData # noqa: PLC0415
        code = self.code

        message = self.message

        request_id = self.request_id

        data: dict[str, Any] | Unset = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if request_id is not UNSET:
            field_dict["request_id"] = request_id
        if data is not UNSET:
            field_dict["data"] = data

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.edit_open_collaboration_sample_rule_response_data import EditOpenCollaborationSampleRuleResponseData # noqa: PLC0415
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        request_id = d.pop("request_id", UNSET)

        _data = d.pop("data", UNSET)
        data: EditOpenCollaborationSampleRuleResponseData | Unset
        if isinstance(_data,  Unset):
            data = UNSET
        else:
            data = EditOpenCollaborationSampleRuleResponseData.from_dict(_data)




        edit_open_collaboration_sample_rule_response = cls(
            code=code,
            message=message,
            request_id=request_id,
            data=data,
        )


        edit_open_collaboration_sample_rule_response.additional_properties = d
        return edit_open_collaboration_sample_rule_response

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
