from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_message_templates_response_data_message_template_coupon_card_rule import GetMessageTemplatesResponseDataMessageTemplateCouponCardRule
  from ..models.get_message_templates_response_data_message_template_product_card_rule import GetMessageTemplatesResponseDataMessageTemplateProductCardRule





T = TypeVar("T", bound="GetMessageTemplatesResponseDataMessageTemplate")



@_attrs_define
class GetMessageTemplatesResponseDataMessageTemplate:
    """ 
        Attributes:
            id (str | Unset): The template ID.
            message_title (str | Unset): The message title.
            message_body (str | Unset): The message body.
            product_card_rules (GetMessageTemplatesResponseDataMessageTemplateProductCardRule | Unset):
            coupon_card_rules (GetMessageTemplatesResponseDataMessageTemplateCouponCardRule | Unset):
     """

    id: str | Unset = UNSET
    message_title: str | Unset = UNSET
    message_body: str | Unset = UNSET
    product_card_rules: GetMessageTemplatesResponseDataMessageTemplateProductCardRule | Unset = UNSET
    coupon_card_rules: GetMessageTemplatesResponseDataMessageTemplateCouponCardRule | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_message_templates_response_data_message_template_coupon_card_rule import GetMessageTemplatesResponseDataMessageTemplateCouponCardRule # noqa: PLC0415
        from ..models.get_message_templates_response_data_message_template_product_card_rule import GetMessageTemplatesResponseDataMessageTemplateProductCardRule # noqa: PLC0415
        id = self.id

        message_title = self.message_title

        message_body = self.message_body

        product_card_rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product_card_rules, Unset):
            product_card_rules = self.product_card_rules.to_dict()

        coupon_card_rules: dict[str, Any] | Unset = UNSET
        if not isinstance(self.coupon_card_rules, Unset):
            coupon_card_rules = self.coupon_card_rules.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if message_title is not UNSET:
            field_dict["message_title"] = message_title
        if message_body is not UNSET:
            field_dict["message_body"] = message_body
        if product_card_rules is not UNSET:
            field_dict["product_card_rules"] = product_card_rules
        if coupon_card_rules is not UNSET:
            field_dict["coupon_card_rules"] = coupon_card_rules

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_message_templates_response_data_message_template_coupon_card_rule import GetMessageTemplatesResponseDataMessageTemplateCouponCardRule # noqa: PLC0415
        from ..models.get_message_templates_response_data_message_template_product_card_rule import GetMessageTemplatesResponseDataMessageTemplateProductCardRule # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        message_title = d.pop("message_title", UNSET)

        message_body = d.pop("message_body", UNSET)

        _product_card_rules = d.pop("product_card_rules", UNSET)
        product_card_rules: GetMessageTemplatesResponseDataMessageTemplateProductCardRule | Unset
        if isinstance(_product_card_rules,  Unset):
            product_card_rules = UNSET
        else:
            product_card_rules = GetMessageTemplatesResponseDataMessageTemplateProductCardRule.from_dict(_product_card_rules)




        _coupon_card_rules = d.pop("coupon_card_rules", UNSET)
        coupon_card_rules: GetMessageTemplatesResponseDataMessageTemplateCouponCardRule | Unset
        if isinstance(_coupon_card_rules,  Unset):
            coupon_card_rules = UNSET
        else:
            coupon_card_rules = GetMessageTemplatesResponseDataMessageTemplateCouponCardRule.from_dict(_coupon_card_rules)




        get_message_templates_response_data_message_template = cls(
            id=id,
            message_title=message_title,
            message_body=message_body,
            product_card_rules=product_card_rules,
            coupon_card_rules=coupon_card_rules,
        )


        get_message_templates_response_data_message_template.additional_properties = d
        return get_message_templates_response_data_message_template

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
