from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.warning import Warning_





T = TypeVar("T", bound="MarkPackageAsShippedResponseData")



@_attrs_define
class MarkPackageAsShippedResponseData:
    """ 
        Attributes:
            order_id (str | Unset): TikTok Shop order ID.
            order_line_item_ids (list[str] | Unset): List of order line item IDs.
            package_id (str | Unset): Package ID.
            warning (Warning_ | Unset):
     """

    order_id: str | Unset = UNSET
    order_line_item_ids: list[str] | Unset = UNSET
    package_id: str | Unset = UNSET
    warning: Warning_ | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.warning import Warning_ # noqa: PLC0415
        order_id = self.order_id

        order_line_item_ids: list[str] | Unset = UNSET
        if not isinstance(self.order_line_item_ids, Unset):
            order_line_item_ids = self.order_line_item_ids



        package_id = self.package_id

        warning: dict[str, Any] | Unset = UNSET
        if not isinstance(self.warning, Unset):
            warning = self.warning.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if order_id is not UNSET:
            field_dict["order_id"] = order_id
        if order_line_item_ids is not UNSET:
            field_dict["order_line_item_ids"] = order_line_item_ids
        if package_id is not UNSET:
            field_dict["package_id"] = package_id
        if warning is not UNSET:
            field_dict["warning"] = warning

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.warning import Warning_ # noqa: PLC0415
        d = dict(src_dict)
        order_id = d.pop("order_id", UNSET)

        order_line_item_ids = cast(list[str], d.pop("order_line_item_ids", UNSET))


        package_id = d.pop("package_id", UNSET)

        _warning = d.pop("warning", UNSET)
        warning: Warning_ | Unset
        if isinstance(_warning,  Unset):
            warning = UNSET
        else:
            warning = Warning_.from_dict(_warning)




        mark_package_as_shipped_response_data = cls(
            order_id=order_id,
            order_line_item_ids=order_line_item_ids,
            package_id=package_id,
            warning=warning,
        )


        mark_package_as_shipped_response_data.additional_properties = d
        return mark_package_as_shipped_response_data

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
