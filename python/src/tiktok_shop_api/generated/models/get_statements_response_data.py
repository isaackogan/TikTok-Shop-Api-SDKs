from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.get_statements_response_data_statement import GetStatementsResponseDataStatement


T = TypeVar("T", bound="GetStatementsResponseData")


@_attrs_define
class GetStatementsResponseData:
    """
    Attributes:
        next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. If this
            value is non-empty, provide it in the `page_token` parameter of the next request. An empty `next_page_token`
            means there are no more results.
        statements (list[GetStatementsResponseDataStatement] | Unset): The list of statements that meet the query
            conditions.
    """

    next_page_token: str | Unset = UNSET
    statements: list[GetStatementsResponseDataStatement] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        next_page_token = self.next_page_token

        statements: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.statements, Unset):
            statements = []
            for statements_item_data in self.statements:
                statements_item = statements_item_data.to_dict()
                statements.append(statements_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if statements is not UNSET:
            field_dict["statements"] = statements

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_statements_response_data_statement import GetStatementsResponseDataStatement  # noqa: PLC0415

        d = dict(src_dict)
        next_page_token = d.pop("next_page_token", UNSET)

        _statements = d.pop("statements", UNSET)
        statements: list[GetStatementsResponseDataStatement] | Unset = UNSET
        if _statements is not UNSET:
            statements = []
            for statements_item_data in _statements:
                statements_item = GetStatementsResponseDataStatement.from_dict(statements_item_data)

                statements.append(statements_item)

        get_statements_response_data = cls(
            next_page_token=next_page_token,
            statements=statements,
        )

        get_statements_response_data.additional_properties = d
        return get_statements_response_data

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
