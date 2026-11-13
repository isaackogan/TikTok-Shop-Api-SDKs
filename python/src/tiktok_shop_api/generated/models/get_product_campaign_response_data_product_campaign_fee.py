from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.policy import Policy





T = TypeVar("T", bound="GetProductCampaignResponseDataProductCampaignFee")



@_attrs_define
class GetProductCampaignResponseDataProductCampaignFee:
    """ 
        Attributes:
            description (str | Unset): General fee information. Omitted if unavailable; this does not mean participation is
                free or fees are unconfigured, and does not guarantee the final billed amount.
            policies (list[Policy] | Unset): Fee policies applicable to the shop. Omitted if unknown; [] when there are
                explicitly no applicable policies. An empty list does not rule out other fees.
     """

    description: str | Unset = UNSET
    policies: list[Policy] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.policy import Policy # noqa: PLC0415
        description = self.description

        policies: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.policies, Unset):
            policies = []
            for policies_item_data in self.policies:
                policies_item = policies_item_data.to_dict()
                policies.append(policies_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if description is not UNSET:
            field_dict["description"] = description
        if policies is not UNSET:
            field_dict["policies"] = policies

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.policy import Policy # noqa: PLC0415
        d = dict(src_dict)
        description = d.pop("description", UNSET)

        _policies = d.pop("policies", UNSET)
        policies: list[Policy] | Unset = UNSET
        if _policies is not UNSET:
            policies = []
            for policies_item_data in _policies:
                policies_item = Policy.from_dict(policies_item_data)



                policies.append(policies_item)


        get_product_campaign_response_data_product_campaign_fee = cls(
            description=description,
            policies=policies,
        )


        get_product_campaign_response_data_product_campaign_fee.additional_properties = d
        return get_product_campaign_response_data_product_campaign_fee

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
