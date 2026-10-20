from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.query_order_line import QueryOrderLine


T = TypeVar("T", bound="SearchPODCustomizationDetailsRequest")


@_attrs_define
class SearchPODCustomizationDetailsRequest:
    """
    Attributes:
        main_order_id (str): TikTok Shop order ID.
        query_order_lines (list[QueryOrderLine]): The order lines for which to retrieve POD customization details.
    """

    main_order_id: str
    query_order_lines: list[QueryOrderLine]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        main_order_id = self.main_order_id

        query_order_lines = []
        for query_order_lines_item_data in self.query_order_lines:
            query_order_lines_item = query_order_lines_item_data.to_dict()
            query_order_lines.append(query_order_lines_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "main_order_id": main_order_id,
                "query_order_lines": query_order_lines,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_order_line import QueryOrderLine  # noqa: PLC0415

        d = dict(src_dict)
        main_order_id = d.pop("main_order_id")

        query_order_lines = []
        _query_order_lines = d.pop("query_order_lines")
        for query_order_lines_item_data in _query_order_lines:
            query_order_lines_item = QueryOrderLine.from_dict(query_order_lines_item_data)

            query_order_lines.append(query_order_lines_item)

        search_pod_customization_details_request = cls(
            main_order_id=main_order_id,
            query_order_lines=query_order_lines,
        )

        search_pod_customization_details_request.additional_properties = d
        return search_pod_customization_details_request

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
