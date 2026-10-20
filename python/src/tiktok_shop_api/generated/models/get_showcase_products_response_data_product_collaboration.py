from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_showcase_products_response_data_product_collaboration_partner import GetShowcaseProductsResponseDataProductCollaborationPartner





T = TypeVar("T", bound="GetShowcaseProductsResponseDataProductCollaboration")



@_attrs_define
class GetShowcaseProductsResponseDataProductCollaboration:
    """ 
        Attributes:
            id (str | Unset): The collaboration identifier.
            type_ (str | Unset): The collaboration type. This an enumerated type with values:
                1 - Open Collaboration
                2 - Target Collaboration
                5 - Partner Campaign
                11 - Flat Fee
                12 - Collaboration Plus
                13 - Affiliate Promotion
            partner (GetShowcaseProductsResponseDataProductCollaborationPartner | Unset):
     """

    id: str | Unset = UNSET
    type_: str | Unset = UNSET
    partner: GetShowcaseProductsResponseDataProductCollaborationPartner | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_showcase_products_response_data_product_collaboration_partner import GetShowcaseProductsResponseDataProductCollaborationPartner # noqa: PLC0415
        id = self.id

        type_ = self.type_

        partner: dict[str, Any] | Unset = UNSET
        if not isinstance(self.partner, Unset):
            partner = self.partner.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if type_ is not UNSET:
            field_dict["type"] = type_
        if partner is not UNSET:
            field_dict["partner"] = partner

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_showcase_products_response_data_product_collaboration_partner import GetShowcaseProductsResponseDataProductCollaborationPartner # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        type_ = d.pop("type", UNSET)

        _partner = d.pop("partner", UNSET)
        partner: GetShowcaseProductsResponseDataProductCollaborationPartner | Unset
        if isinstance(_partner,  Unset):
            partner = UNSET
        else:
            partner = GetShowcaseProductsResponseDataProductCollaborationPartner.from_dict(_partner)




        get_showcase_products_response_data_product_collaboration = cls(
            id=id,
            type_=type_,
            partner=partner,
        )


        get_showcase_products_response_data_product_collaboration.additional_properties = d
        return get_showcase_products_response_data_product_collaboration

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
