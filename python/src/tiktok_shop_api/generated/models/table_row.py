from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.table_row_cell import TableRowCell





T = TypeVar("T", bound="TableRow")



@_attrs_define
class TableRow:
    """ 
        Attributes:
            cells (list[TableRowCell]): Cells aligned by index with `table.headers`. Each row must contain exactly one cell
                for every header.
     """

    cells: list[TableRowCell]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.table_row_cell import TableRowCell # noqa: PLC0415
        cells = []
        for cells_item_data in self.cells:
            cells_item = cells_item_data.to_dict()
            cells.append(cells_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "cells": cells,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.table_row_cell import TableRowCell # noqa: PLC0415
        d = dict(src_dict)
        cells = []
        _cells = d.pop("cells")
        for cells_item_data in (_cells):
            cells_item = TableRowCell.from_dict(cells_item_data)



            cells.append(cells_item)


        table_row = cls(
            cells=cells,
        )


        table_row.additional_properties = d
        return table_row

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
