from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_product_campaign_response_data_product_campaign_shop_participation_registration_statistic import GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic
  from ..models.relation import Relation





T = TypeVar("T", bound="GetProductCampaignResponseDataProductCampaignShopParticipation")



@_attrs_define
class GetProductCampaignResponseDataProductCampaignShopParticipation:
    """ 
        Attributes:
            has_joined (bool | Unset): Whether a participation record exists. Omission means unknown. A record does not
                establish approval or effective benefits.
            pending_confirmation_count (int | Unset): Number of products awaiting seller confirmation of registration. Known
                nonnegative values are retained; omitted if unknown or inapplicable. Does not mean pending review.
            registration_statistics (GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic |
                Unset):
            relation (Relation | Unset):
     """

    has_joined: bool | Unset = UNSET
    pending_confirmation_count: int | Unset = UNSET
    registration_statistics: GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic | Unset = UNSET
    relation: Relation | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_product_campaign_response_data_product_campaign_shop_participation_registration_statistic import GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic # noqa: PLC0415
        from ..models.relation import Relation # noqa: PLC0415
        has_joined = self.has_joined

        pending_confirmation_count = self.pending_confirmation_count

        registration_statistics: dict[str, Any] | Unset = UNSET
        if not isinstance(self.registration_statistics, Unset):
            registration_statistics = self.registration_statistics.to_dict()

        relation: dict[str, Any] | Unset = UNSET
        if not isinstance(self.relation, Unset):
            relation = self.relation.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if has_joined is not UNSET:
            field_dict["has_joined"] = has_joined
        if pending_confirmation_count is not UNSET:
            field_dict["pending_confirmation_count"] = pending_confirmation_count
        if registration_statistics is not UNSET:
            field_dict["registration_statistics"] = registration_statistics
        if relation is not UNSET:
            field_dict["relation"] = relation

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_product_campaign_response_data_product_campaign_shop_participation_registration_statistic import GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic # noqa: PLC0415
        from ..models.relation import Relation # noqa: PLC0415
        d = dict(src_dict)
        has_joined = d.pop("has_joined", UNSET)

        pending_confirmation_count = d.pop("pending_confirmation_count", UNSET)

        _registration_statistics = d.pop("registration_statistics", UNSET)
        registration_statistics: GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic | Unset
        if isinstance(_registration_statistics,  Unset):
            registration_statistics = UNSET
        else:
            registration_statistics = GetProductCampaignResponseDataProductCampaignShopParticipationRegistrationStatistic.from_dict(_registration_statistics)




        _relation = d.pop("relation", UNSET)
        relation: Relation | Unset
        if isinstance(_relation,  Unset):
            relation = UNSET
        else:
            relation = Relation.from_dict(_relation)




        get_product_campaign_response_data_product_campaign_shop_participation = cls(
            has_joined=has_joined,
            pending_confirmation_count=pending_confirmation_count,
            registration_statistics=registration_statistics,
            relation=relation,
        )


        get_product_campaign_response_data_product_campaign_shop_participation.additional_properties = d
        return get_product_campaign_response_data_product_campaign_shop_participation

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
