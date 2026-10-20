from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_aftersale_eligibility_response_data_sku_eligibility_line_item_eligibility import GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility





T = TypeVar("T", bound="GetAftersaleEligibilityResponseDataSkuEligibility")



@_attrs_define
class GetAftersaleEligibilityResponseDataSkuEligibility:
    """ 
        Attributes:
            sku_id (str | Unset): SKU ID.
            line_item_eligibility (list[GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility] | Unset):
                Eligibility results for order line items in this SKU, grouped by aftersale request type. A request type can
                include separate entries for eligible and ineligible order line items. Eligible entries can include
                available_reason_names, while ineligible entries include ineligible_code and ineligible_reason.
     """

    sku_id: str | Unset = UNSET
    line_item_eligibility: list[GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_aftersale_eligibility_response_data_sku_eligibility_line_item_eligibility import GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility # noqa: PLC0415
        sku_id = self.sku_id

        line_item_eligibility: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.line_item_eligibility, Unset):
            line_item_eligibility = []
            for line_item_eligibility_item_data in self.line_item_eligibility:
                line_item_eligibility_item = line_item_eligibility_item_data.to_dict()
                line_item_eligibility.append(line_item_eligibility_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sku_id is not UNSET:
            field_dict["sku_id"] = sku_id
        if line_item_eligibility is not UNSET:
            field_dict["line_item_eligibility"] = line_item_eligibility

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_aftersale_eligibility_response_data_sku_eligibility_line_item_eligibility import GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility # noqa: PLC0415
        d = dict(src_dict)
        sku_id = d.pop("sku_id", UNSET)

        _line_item_eligibility = d.pop("line_item_eligibility", UNSET)
        line_item_eligibility: list[GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility] | Unset = UNSET
        if _line_item_eligibility is not UNSET:
            line_item_eligibility = []
            for line_item_eligibility_item_data in _line_item_eligibility:
                line_item_eligibility_item = GetAftersaleEligibilityResponseDataSkuEligibilityLineItemEligibility.from_dict(line_item_eligibility_item_data)



                line_item_eligibility.append(line_item_eligibility_item)


        get_aftersale_eligibility_response_data_sku_eligibility = cls(
            sku_id=sku_id,
            line_item_eligibility=line_item_eligibility,
        )


        get_aftersale_eligibility_response_data_sku_eligibility.additional_properties = d
        return get_aftersale_eligibility_response_data_sku_eligibility

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
