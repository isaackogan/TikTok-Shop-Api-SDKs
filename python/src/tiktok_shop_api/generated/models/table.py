from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.header import Header
    from ..models.row import Row


T = TypeVar("T", bound="Table")


@_attrs_define
class Table:
    """
    Attributes:
        headers (list[Header]): Ordered header definitions. Provide 1 to 20 headers.
        rows (list[Row]): Rows of the size chart. Provide 1 to 45 rows.
    """

    headers: list[Header]
    rows: list[Row]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        headers = []
        for headers_item_data in self.headers:
            headers_item = headers_item_data.to_dict()
            headers.append(headers_item)

        rows = []
        for rows_item_data in self.rows:
            rows_item = rows_item_data.to_dict()
            rows.append(rows_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "headers": headers,
                "rows": rows,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.header import Header  # noqa: PLC0415
        from ..models.row import Row  # noqa: PLC0415

        d = dict(src_dict)
        headers = []
        _headers = d.pop("headers")
        for headers_item_data in _headers:
            headers_item = Header.from_dict(headers_item_data)

            headers.append(headers_item)

        rows = []
        _rows = d.pop("rows")
        for rows_item_data in _rows:
            rows_item = Row.from_dict(rows_item_data)

            rows.append(rows_item)

        table = cls(
            headers=headers,
            rows=rows,
        )

        table.additional_properties = d
        return table

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
