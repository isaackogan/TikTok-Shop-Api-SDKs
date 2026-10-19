from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_the_blind_box_opening_results_request_blind_batch_box_result import (
        UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult,
    )
    from ..models.update_the_blind_box_opening_results_request_blind_box_result import (
        UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult,
    )


T = TypeVar("T", bound="UpdateTheBlindBoxOpeningResultsRequest")


@_attrs_define
class UpdateTheBlindBoxOpeningResultsRequest:
    """
    Attributes:
        main_order_id (str | Unset): The unique identifier for a TikTok Shop order.
        blind_box_results (list[UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult] | Unset): When using the legacy
            result shape, provide unboxing results for one or more blind-box line items in the specified order.
        blind_batch_box_results (list[UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult] | Unset): Unboxing
            batch results for line items under orders.
    """

    main_order_id: str | Unset = UNSET
    blind_box_results: list[UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult] | Unset = UNSET
    blind_batch_box_results: list[UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_order_id = self.main_order_id

        blind_box_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blind_box_results, Unset):
            blind_box_results = []
            for blind_box_results_item_data in self.blind_box_results:
                blind_box_results_item = blind_box_results_item_data.to_dict()
                blind_box_results.append(blind_box_results_item)

        blind_batch_box_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.blind_batch_box_results, Unset):
            blind_batch_box_results = []
            for blind_batch_box_results_item_data in self.blind_batch_box_results:
                blind_batch_box_results_item = blind_batch_box_results_item_data.to_dict()
                blind_batch_box_results.append(blind_batch_box_results_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if main_order_id is not UNSET:
            field_dict["main_order_id"] = main_order_id
        if blind_box_results is not UNSET:
            field_dict["blind_box_results"] = blind_box_results
        if blind_batch_box_results is not UNSET:
            field_dict["blind_batch_box_results"] = blind_batch_box_results

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_the_blind_box_opening_results_request_blind_batch_box_result import (
            UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult,  # noqa: PLC0415
        )
        from ..models.update_the_blind_box_opening_results_request_blind_box_result import (
            UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult,  # noqa: PLC0415
        )

        d = dict(src_dict)
        main_order_id = d.pop("main_order_id", UNSET)

        _blind_box_results = d.pop("blind_box_results", UNSET)
        blind_box_results: list[UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult] | Unset = UNSET
        if _blind_box_results is not UNSET:
            blind_box_results = []
            for blind_box_results_item_data in _blind_box_results:
                blind_box_results_item = UpdateTheBlindBoxOpeningResultsRequestBlindBoxResult.from_dict(
                    blind_box_results_item_data
                )

                blind_box_results.append(blind_box_results_item)

        _blind_batch_box_results = d.pop("blind_batch_box_results", UNSET)
        blind_batch_box_results: list[UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult] | Unset = UNSET
        if _blind_batch_box_results is not UNSET:
            blind_batch_box_results = []
            for blind_batch_box_results_item_data in _blind_batch_box_results:
                blind_batch_box_results_item = UpdateTheBlindBoxOpeningResultsRequestBlindBatchBoxResult.from_dict(
                    blind_batch_box_results_item_data
                )

                blind_batch_box_results.append(blind_batch_box_results_item)

        update_the_blind_box_opening_results_request = cls(
            main_order_id=main_order_id,
            blind_box_results=blind_box_results,
            blind_batch_box_results=blind_batch_box_results,
        )

        update_the_blind_box_opening_results_request.additional_properties = d
        return update_the_blind_box_opening_results_request

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
