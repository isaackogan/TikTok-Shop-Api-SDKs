from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="CheckProductListingRequestOption")



@_attrs_define
class CheckProductListingRequestOption:
    """ 
        Attributes:
            need_trigger_gne_async_check (bool | Unset): Whether to trigger asynchronous product information verification.
                This asynchronous workflow is available only to enabled sellers in the US.
                Set this field to `true` together with a nonempty `gne_async_check_session_id` to start new asynchronous checks.
                To retry retrieval with the same session ID without creating new asynchronous tasks, set this field to `false`;
                any completed findings are returned in `pre_check_results`.
            gne_async_check_session_id (str | Unset): A caller-provided session ID for asynchronous product information
                verification. This asynchronous workflow is available only to enabled sellers in the US.
                Provide a nonempty session ID when you trigger asynchronous verification, then reuse the same session ID on
                later calls to this API with the same product information to retrieve any completed findings in
                `pre_check_results`.
                This API does not generate or return a new session ID for you.
     """

    need_trigger_gne_async_check: bool | Unset = UNSET
    gne_async_check_session_id: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        need_trigger_gne_async_check = self.need_trigger_gne_async_check

        gne_async_check_session_id = self.gne_async_check_session_id


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if need_trigger_gne_async_check is not UNSET:
            field_dict["need_trigger_gne_async_check"] = need_trigger_gne_async_check
        if gne_async_check_session_id is not UNSET:
            field_dict["gne_async_check_session_id"] = gne_async_check_session_id

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        need_trigger_gne_async_check = d.pop("need_trigger_gne_async_check", UNSET)

        gne_async_check_session_id = d.pop("gne_async_check_session_id", UNSET)

        check_product_listing_request_option = cls(
            need_trigger_gne_async_check=need_trigger_gne_async_check,
            gne_async_check_session_id=gne_async_check_session_id,
        )


        check_product_listing_request_option.additional_properties = d
        return check_product_listing_request_option

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
