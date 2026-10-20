from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.global_sku import GlobalSku
    from ..models.publish_result import PublishResult


T = TypeVar("T", bound="EditGlobalProductResponseData")


@_attrs_define
class EditGlobalProductResponseData:
    """
    Attributes:
        global_skus (list[GlobalSku] | Unset): A list of global Stock Keeping Units (SKUs) used to identify distinct
            variants of the product.
        publish_results (list[PublishResult] | Unset): Results of syncing the changes in the edited product to markets
            where it is published.
    """

    global_skus: list[GlobalSku] | Unset = UNSET
    publish_results: list[PublishResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        global_skus: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.global_skus, Unset):
            global_skus = []
            for global_skus_item_data in self.global_skus:
                global_skus_item = global_skus_item_data.to_dict()
                global_skus.append(global_skus_item)

        publish_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publish_results, Unset):
            publish_results = []
            for publish_results_item_data in self.publish_results:
                publish_results_item = publish_results_item_data.to_dict()
                publish_results.append(publish_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if global_skus is not UNSET:
            field_dict["global_skus"] = global_skus
        if publish_results is not UNSET:
            field_dict["publish_results"] = publish_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.global_sku import GlobalSku  # noqa: PLC0415
        from ..models.publish_result import PublishResult  # noqa: PLC0415

        d = dict(src_dict)
        _global_skus = d.pop("global_skus", UNSET)
        global_skus: list[GlobalSku] | Unset = UNSET
        if _global_skus is not UNSET:
            global_skus = []
            for global_skus_item_data in _global_skus:
                global_skus_item = GlobalSku.from_dict(global_skus_item_data)

                global_skus.append(global_skus_item)

        _publish_results = d.pop("publish_results", UNSET)
        publish_results: list[PublishResult] | Unset = UNSET
        if _publish_results is not UNSET:
            publish_results = []
            for publish_results_item_data in _publish_results:
                publish_results_item = PublishResult.from_dict(publish_results_item_data)

                publish_results.append(publish_results_item)

        edit_global_product_response_data = cls(
            global_skus=global_skus,
            publish_results=publish_results,
        )

        edit_global_product_response_data.additional_properties = d
        return edit_global_product_response_data

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
