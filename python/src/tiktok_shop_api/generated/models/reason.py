from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast






T = TypeVar("T", bound="Reason")



@_attrs_define
class Reason:
    """ 
        Attributes:
            code (str | Unset): Returned for every reason represented by a defined public code. Confirmed participation-
                criteria failures return INELIGIBLE with the specific explanation in message. GMV Max eligibility blockers
                return GMV_MAX_PERMISSION_DENIED. Existing participation that blocks another registration returns
                CAMPAIGN_ALREADY_REGISTERED. Product quota, in-progress product registration, and required agreement blockers
                return PRODUCT_REGISTRATION_LIMIT_REACHED, PRODUCT_REGISTRATION_IN_PROGRESS, and REGISTRATION_AGREEMENT_REQUIRED
                respectively when applicable. Unclassified reasons may still omit code; a missing code does not mean that no
                blocker exists. Do not infer a code from localized message text.
                Business reason for blocked eligibility or registration, not an API request error code.
                - INELIGIBLE: The shop fails participation criteria. Multiple specific explanations may share this code.
                - NOT_IN_DESIGNATED_SHOP: The shop is outside the designated scope.
                - REGISTRATION_HAS_CLOSED: Registration has closed.
                - SHOP_NOT_ACTIVE: The shop is not operating normally.
                - NOT_IN_REGISTRATION_DATE: Outside the registration period.
                - NOT_ALLOW_REGISTER: Registration is explicitly prohibited by business rules.
                - CAMPAIGN_DEACTIVATE: The campaign is deactivated.
                - NOT_ALLOW_ADS: An existing advertising campaign registration causes a conflict. This does not mean
                insufficient advertising permissions.
                - NOT_INVITED_ADS: The shop is not invited to the advertising campaign.
                - SAME_TYPE_ACTIVE_REGISTRATION_EXISTS: Only one effective registration is allowed for this campaign type.
                - CAMPAIGN_ALREADY_REGISTERED: The shop already participates in this campaign and another registration is not
                allowed.
                - REGISTERED_AS_BUNDLE: Already participating in this campaign through a bundle.
                - REGISTERED_SAME_TYPE: Already registered for the same campaign type.
                - REGISTERED_ANOTHER_BUNDLE: Already registered for another bundle.
                - NOT_REGISTER_DESIGNATED_RESOURCE_PKG: Not registered for the required resource package.
                - NOT_ALLOW_SWITCH_TIER_ING: A tier change is in progress.
                - REGISTERED_AS_SAME_TYPE_BUNDLE: Already registered for the same campaign type through another bundle.
                - NOT_REGISTER_DESIGNATED_SHOP_CAMPAIGN: Not registered for the required shop campaign.
                - REGISTERED_SERVICE_FEE_CAMPAIGN_CONFLICT: An existing service fee campaign registration causes a conflict.
                - GMV_MAX_PERMISSION_DENIED: The shop does not meet this campaign's GMV Max eligibility requirements and no
                exemption applies.
                - PRODUCT_REGISTRATION_LIMIT_REACHED: The shop has reached the product registration quota for this campaign.
                - PRODUCT_REGISTRATION_IN_PROGRESS: A batch product registration for this shop and campaign is still in
                progress; another registration cannot be started yet.
                - REGISTRATION_AGREEMENT_REQUIRED: The shop has not accepted an agreement required to join this campaign.
                Already accepted agreements and agreements that do not require acceptance do not block registration. Accept the
                required agreement in Seller Center and query again; this query does not sign agreements.
            message (str | Unset): Always returned. Nonempty localized reason message visible to the shop.
            regions (list[str] | Unset): Regions associated with this reason. For EU cross-shop access, may include regions
                applicable to eligible shops belonging to the same seller. Region codes follow [ISO 3166-1
                alpha-2](https://www.iso.org/obp/ui/#search/code/); EU is also supported as an aggregate campaign region. A
                listed code does not guarantee campaign availability or extend authorization.
            related_campaign_id (str | Unset): Returned only when needed to explain a conflict or prerequisite and the
                related campaign is visible to the shop. A decimal string from 1 to 9223372036854775807.
            related_campaign_type (str | Unset): Type of the related campaign, used to select its detail endpoint. Returned
                together with related_campaign_id. Both fields are omitted if the type cannot be confirmed, without affecting
                the reason code or message.
                Unified campaign type with the same semantics in lists and all four detail models. Distinct from campaign group
                type.
                - PRODUCT: Product campaign.
                - SHOP: Shop campaign.
                - LIVESTREAM: Livestream campaign.
                - SHORT_VIDEO: Short video campaign.
     """

    code: str | Unset = UNSET
    message: str | Unset = UNSET
    regions: list[str] | Unset = UNSET
    related_campaign_id: str | Unset = UNSET
    related_campaign_type: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        code = self.code

        message = self.message

        regions: list[str] | Unset = UNSET
        if not isinstance(self.regions, Unset):
            regions = self.regions



        related_campaign_id = self.related_campaign_id

        related_campaign_type = self.related_campaign_type


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if code is not UNSET:
            field_dict["code"] = code
        if message is not UNSET:
            field_dict["message"] = message
        if regions is not UNSET:
            field_dict["regions"] = regions
        if related_campaign_id is not UNSET:
            field_dict["related_campaign_id"] = related_campaign_id
        if related_campaign_type is not UNSET:
            field_dict["related_campaign_type"] = related_campaign_type

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        code = d.pop("code", UNSET)

        message = d.pop("message", UNSET)

        regions = cast(list[str], d.pop("regions", UNSET))


        related_campaign_id = d.pop("related_campaign_id", UNSET)

        related_campaign_type = d.pop("related_campaign_type", UNSET)

        reason = cls(
            code=code,
            message=message,
            regions=regions,
            related_campaign_id=related_campaign_id,
            related_campaign_type=related_campaign_type,
        )


        reason.additional_properties = d
        return reason

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
