from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PrintInboundOrderLabelsResponseData")


@_attrs_define
class PrintInboundOrderLabelsResponseData:
    """
    Attributes:
        download_url (str | Unset): URL containing labels for the inbound order.

            **Please note: the URL will be unicode-escaped. If attempting to manually paste the URL into a browser, you will
            need to unescape the URL first (e.g. '\\u0026'->'&')**
        task_status (str | Unset): * `PROCESSING`: Task is currently being processed. Continue to periodically poll.
            * `SUCCESS`:  Task is finished. `download_url` should be included in response
    """

    download_url: str | Unset = UNSET
    task_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        download_url = self.download_url

        task_status = self.task_status

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if download_url is not UNSET:
            field_dict["download_url"] = download_url
        if task_status is not UNSET:
            field_dict["task_status"] = task_status

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        download_url = d.pop("download_url", UNSET)

        task_status = d.pop("task_status", UNSET)

        print_inbound_order_labels_response_data = cls(
            download_url=download_url,
            task_status=task_status,
        )

        print_inbound_order_labels_response_data.additional_properties = d
        return print_inbound_order_labels_response_data

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
