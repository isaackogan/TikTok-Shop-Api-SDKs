from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.list_opportunities_request_opportunity_type import ListOpportunitiesRequestOpportunityType
from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="ListOpportunitiesRequest")



@_attrs_define
class ListOpportunitiesRequest:
    """ 
        Attributes:
            opportunity_type (ListOpportunitiesRequestOpportunityType): The type of opportunity.
                Possible values:
                - `PRODUCT`: Product opportunity
                - `KEYWORD`: Search keyword opportunity
                - `CATEGORY`: Category opportunity
            category_ids (list[str] | Unset): Filter by category IDs. Leave empty to return all leads that available to the
                seller.
            create_time_ge (int | Unset): Filter opportunities created at or after this time. Provide a Unix timestamp in
                seconds (UTC).
            create_time_lt (int | Unset): Filter opportunities created before this time. timestamp in seconds
            tag_codes (list[str] | Unset): A list of tag codes used to filter the results. You can provide at most 20
                values. Use lowercase tag codes. The `core_product` and `top_product` tag codes are supported only when
                `opportunity_type` is `PRODUCT`; their availability also depends on the seller and market configuration.
     """

    opportunity_type: ListOpportunitiesRequestOpportunityType
    category_ids: list[str] | Unset = UNSET
    create_time_ge: int | Unset = UNSET
    create_time_lt: int | Unset = UNSET
    tag_codes: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        opportunity_type = self.opportunity_type.value

        category_ids: list[str] | Unset = UNSET
        if not isinstance(self.category_ids, Unset):
            category_ids = self.category_ids



        create_time_ge = self.create_time_ge

        create_time_lt = self.create_time_lt

        tag_codes: list[str] | Unset = UNSET
        if not isinstance(self.tag_codes, Unset):
            tag_codes = self.tag_codes




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "opportunity_type": opportunity_type,
        })
        if category_ids is not UNSET:
            field_dict["category_ids"] = category_ids
        if create_time_ge is not UNSET:
            field_dict["create_time_ge"] = create_time_ge
        if create_time_lt is not UNSET:
            field_dict["create_time_lt"] = create_time_lt
        if tag_codes is not UNSET:
            field_dict["tag_codes"] = tag_codes

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        opportunity_type = ListOpportunitiesRequestOpportunityType(d.pop("opportunity_type"))




        category_ids = cast(list[str], d.pop("category_ids", UNSET))


        create_time_ge = d.pop("create_time_ge", UNSET)

        create_time_lt = d.pop("create_time_lt", UNSET)

        tag_codes = cast(list[str], d.pop("tag_codes", UNSET))


        list_opportunities_request = cls(
            opportunity_type=opportunity_type,
            category_ids=category_ids,
            create_time_ge=create_time_ge,
            create_time_lt=create_time_lt,
            tag_codes=tag_codes,
        )


        list_opportunities_request.additional_properties = d
        return list_opportunities_request

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
