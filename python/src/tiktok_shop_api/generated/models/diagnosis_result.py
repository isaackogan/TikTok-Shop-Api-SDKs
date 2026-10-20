from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="DiagnosisResult")


@_attrs_define
class DiagnosisResult:
    """
    Attributes:
        code (str | Unset): A machine-readable code that represents an identified issue.
            Refer to [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd) for the
            full list of identified issues and the corresponding recommendations.
        how_to_solve (str | Unset): The recommendation for resolving the identified issue, returned in the default
            locale language of the shop.
            Refer to [Listing quality diagnosis](https://partner.tiktokshop.com/docv2/page/66eb8f5c6f2da702e96a49dd) for the
            full list of recommendations.
        quality_tier (str | Unset): The listing quality tier you can reach by implementing the recommendation.
            Possible values:
            - FAIR
            - GOOD

            **Note**:
            - To reach a higher tier, you must implement all recommendations from the destination tier and all preceding
            tiers. For example, a product will reach the "GOOD" tier once all "FAIR" and "GOOD" recommendations are
            addressed or implemented.
            - Available only for the US market.
    """

    code: str | Unset = UNSET
    how_to_solve: str | Unset = UNSET
    quality_tier: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        code = self.code

        how_to_solve = self.how_to_solve

        quality_tier = self.quality_tier

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code is not UNSET:
            field_dict["code"] = code
        if how_to_solve is not UNSET:
            field_dict["how_to_solve"] = how_to_solve
        if quality_tier is not UNSET:
            field_dict["quality_tier"] = quality_tier

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        how_to_solve = d.pop("how_to_solve", UNSET)

        quality_tier = d.pop("quality_tier", UNSET)

        diagnosis_result = cls(
            code=code,
            how_to_solve=how_to_solve,
            quality_tier=quality_tier,
        )

        diagnosis_result.additional_properties = d
        return diagnosis_result

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
