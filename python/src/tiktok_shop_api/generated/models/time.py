from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.create_time import CreateTime
  from ..models.update_time import UpdateTime





T = TypeVar("T", bound="Time")



@_attrs_define
class Time:
    """ 
        Attributes:
            create_time (CreateTime | Unset):
            update_time (UpdateTime | Unset):
     """

    create_time: CreateTime | Unset = UNSET
    update_time: UpdateTime | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.create_time import CreateTime # noqa: PLC0415
        from ..models.update_time import UpdateTime # noqa: PLC0415
        create_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.create_time, Unset):
            create_time = self.create_time.to_dict()

        update_time: dict[str, Any] | Unset = UNSET
        if not isinstance(self.update_time, Unset):
            update_time = self.update_time.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.create_time import CreateTime # noqa: PLC0415
        from ..models.update_time import UpdateTime # noqa: PLC0415
        d = dict(src_dict)
        _create_time = d.pop("create_time", UNSET)
        create_time: CreateTime | Unset
        if isinstance(_create_time,  Unset):
            create_time = UNSET
        else:
            create_time = CreateTime.from_dict(_create_time)




        _update_time = d.pop("update_time", UNSET)
        update_time: UpdateTime | Unset
        if isinstance(_update_time,  Unset):
            update_time = UNSET
        else:
            update_time = UpdateTime.from_dict(_update_time)




        time = cls(
            create_time=create_time,
            update_time=update_time,
        )


        time.additional_properties = d
        return time

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
