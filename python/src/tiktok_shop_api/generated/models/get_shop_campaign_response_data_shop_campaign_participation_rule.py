from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.other_rule import OtherRule
  from ..models.shop_rule import ShopRule





T = TypeVar("T", bound="GetShopCampaignResponseDataShopCampaignParticipationRule")



@_attrs_define
class GetShopCampaignResponseDataShopCampaignParticipationRule:
    """ 
        Attributes:
            other_rules (list[OtherRule] | Unset): Prerequisites applicable to the shop, such as required agreements.
                Excludes individual product requirements, registration prices, inventory, and tier rules.
            shop_rules (list[ShopRule] | Unset): Includes exemption information applicable to the shop, without exemption
                lists.
     """

    other_rules: list[OtherRule] | Unset = UNSET
    shop_rules: list[ShopRule] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.other_rule import OtherRule # noqa: PLC0415
        from ..models.shop_rule import ShopRule # noqa: PLC0415
        other_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.other_rules, Unset):
            other_rules = []
            for other_rules_item_data in self.other_rules:
                other_rules_item = other_rules_item_data.to_dict()
                other_rules.append(other_rules_item)



        shop_rules: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shop_rules, Unset):
            shop_rules = []
            for shop_rules_item_data in self.shop_rules:
                shop_rules_item = shop_rules_item_data.to_dict()
                shop_rules.append(shop_rules_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if other_rules is not UNSET:
            field_dict["other_rules"] = other_rules
        if shop_rules is not UNSET:
            field_dict["shop_rules"] = shop_rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.other_rule import OtherRule # noqa: PLC0415
        from ..models.shop_rule import ShopRule # noqa: PLC0415
        d = dict(src_dict)
        _other_rules = d.pop("other_rules", UNSET)
        other_rules: list[OtherRule] | Unset = UNSET
        if _other_rules is not UNSET:
            other_rules = []
            for other_rules_item_data in _other_rules:
                other_rules_item = OtherRule.from_dict(other_rules_item_data)



                other_rules.append(other_rules_item)


        _shop_rules = d.pop("shop_rules", UNSET)
        shop_rules: list[ShopRule] | Unset = UNSET
        if _shop_rules is not UNSET:
            shop_rules = []
            for shop_rules_item_data in _shop_rules:
                shop_rules_item = ShopRule.from_dict(shop_rules_item_data)



                shop_rules.append(shop_rules_item)


        get_shop_campaign_response_data_shop_campaign_participation_rule = cls(
            other_rules=other_rules,
            shop_rules=shop_rules,
        )


        get_shop_campaign_response_data_shop_campaign_participation_rule.additional_properties = d
        return get_shop_campaign_response_data_shop_campaign_participation_rule

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
