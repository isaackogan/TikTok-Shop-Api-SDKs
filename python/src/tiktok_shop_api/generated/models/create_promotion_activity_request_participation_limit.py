from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..models.create_promotion_activity_request_participation_limit_type import CreatePromotionActivityRequestParticipationLimitType






T = TypeVar("T", bound="CreatePromotionActivityRequestParticipationLimit")



@_attrs_define
class CreatePromotionActivityRequestParticipationLimit:
    """ 
        Attributes:
            type_ (CreatePromotionActivityRequestParticipationLimitType): Determines whether each buyer can receive the
                activity benefit more than once.
                Possible values:
                - `BUYER_NO_LIMIT`: A buyer can benefit from this activity across multiple orders.
                - `BUYER_LIMIT_ONLY_ONE`: A buyer can benefit from this activity for no more than one order.
     """

    type_: CreatePromotionActivityRequestParticipationLimitType
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        type_ = self.type_.value


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "type": type_,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        type_ = CreatePromotionActivityRequestParticipationLimitType(d.pop("type"))




        create_promotion_activity_request_participation_limit = cls(
            type_=type_,
        )


        create_promotion_activity_request_participation_limit.additional_properties = d
        return create_promotion_activity_request_participation_limit

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
