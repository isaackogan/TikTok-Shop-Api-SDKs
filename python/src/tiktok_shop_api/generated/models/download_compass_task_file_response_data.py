from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.download_compass_task_file_response_data_file import DownloadCompassTaskFileResponseDataFile





T = TypeVar("T", bound="DownloadCompassTaskFileResponseData")



@_attrs_define
class DownloadCompassTaskFileResponseData:
    """ 
        Attributes:
            file (DownloadCompassTaskFileResponseDataFile | Unset):
     """

    file: DownloadCompassTaskFileResponseDataFile | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.download_compass_task_file_response_data_file import DownloadCompassTaskFileResponseDataFile # noqa: PLC0415
        file: dict[str, Any] | Unset = UNSET
        if not isinstance(self.file, Unset):
            file = self.file.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if file is not UNSET:
            field_dict["file"] = file

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.download_compass_task_file_response_data_file import DownloadCompassTaskFileResponseDataFile # noqa: PLC0415
        d = dict(src_dict)
        _file = d.pop("file", UNSET)
        file: DownloadCompassTaskFileResponseDataFile | Unset
        if isinstance(_file,  Unset):
            file = UNSET
        else:
            file = DownloadCompassTaskFileResponseDataFile.from_dict(_file)




        download_compass_task_file_response_data = cls(
            file=file,
        )


        download_compass_task_file_response_data.additional_properties = d
        return download_compass_task_file_response_data

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
