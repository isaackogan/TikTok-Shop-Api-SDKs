from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_sps_benefits_response_data_benefit import GetSPSBenefitsResponseDataBenefit





T = TypeVar("T", bound="GetSPSBenefitsResponseData")



@_attrs_define
class GetSPSBenefitsResponseData:
    """ 
        Attributes:
            benefits (list[GetSPSBenefitsResponseDataBenefit] | Unset): Fixed complete set of benefits associated with the
                shop SPS score.
     """

    benefits: list[GetSPSBenefitsResponseDataBenefit] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_sps_benefits_response_data_benefit import GetSPSBenefitsResponseDataBenefit # noqa: PLC0415
        benefits: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.benefits, Unset):
            benefits = []
            for benefits_item_data in self.benefits:
                benefits_item = benefits_item_data.to_dict()
                benefits.append(benefits_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if benefits is not UNSET:
            field_dict["benefits"] = benefits

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sps_benefits_response_data_benefit import GetSPSBenefitsResponseDataBenefit # noqa: PLC0415
        d = dict(src_dict)
        _benefits = d.pop("benefits", UNSET)
        benefits: list[GetSPSBenefitsResponseDataBenefit] | Unset = UNSET
        if _benefits is not UNSET:
            benefits = []
            for benefits_item_data in _benefits:
                benefits_item = GetSPSBenefitsResponseDataBenefit.from_dict(benefits_item_data)



                benefits.append(benefits_item)


        get_sps_benefits_response_data = cls(
            benefits=benefits,
        )


        get_sps_benefits_response_data.additional_properties = d
        return get_sps_benefits_response_data

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
