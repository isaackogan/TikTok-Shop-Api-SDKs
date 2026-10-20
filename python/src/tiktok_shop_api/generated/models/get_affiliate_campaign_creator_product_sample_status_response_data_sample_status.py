from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_affiliate_campaign_creator_product_sample_status_response_data_sample_status_tracking_result import GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult





T = TypeVar("T", bound="GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus")



@_attrs_define
class GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatus:
    """ 
        Attributes:
            shipping_provider_name (str | Unset): The name of the shipping provider
            delivery_option (str | Unset): The delivery option:
                - ECONOMY_SHIPPING
                - PREMIUM_SHIPPING
            estimated_earliest_delivery_date (str | Unset): The earliest estimated delivery date in Unix epoch format.
            estimated_latest_delivery_date (str | Unset): The latest estimated delivery date in Unix epoch format.
            quantity (int | Unset): The quantity of products delivered.
            tracking_results (list[GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult] |
                Unset): A list of objects representing tracking events.
     """

    shipping_provider_name: str | Unset = UNSET
    delivery_option: str | Unset = UNSET
    estimated_earliest_delivery_date: str | Unset = UNSET
    estimated_latest_delivery_date: str | Unset = UNSET
    quantity: int | Unset = UNSET
    tracking_results: list[GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_affiliate_campaign_creator_product_sample_status_response_data_sample_status_tracking_result import GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult # noqa: PLC0415
        shipping_provider_name = self.shipping_provider_name

        delivery_option = self.delivery_option

        estimated_earliest_delivery_date = self.estimated_earliest_delivery_date

        estimated_latest_delivery_date = self.estimated_latest_delivery_date

        quantity = self.quantity

        tracking_results: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.tracking_results, Unset):
            tracking_results = []
            for tracking_results_item_data in self.tracking_results:
                tracking_results_item = tracking_results_item_data.to_dict()
                tracking_results.append(tracking_results_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if shipping_provider_name is not UNSET:
            field_dict["shipping_provider_name"] = shipping_provider_name
        if delivery_option is not UNSET:
            field_dict["delivery_option"] = delivery_option
        if estimated_earliest_delivery_date is not UNSET:
            field_dict["estimated_earliest_delivery_date"] = estimated_earliest_delivery_date
        if estimated_latest_delivery_date is not UNSET:
            field_dict["estimated_latest_delivery_date"] = estimated_latest_delivery_date
        if quantity is not UNSET:
            field_dict["quantity"] = quantity
        if tracking_results is not UNSET:
            field_dict["tracking_results"] = tracking_results

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_affiliate_campaign_creator_product_sample_status_response_data_sample_status_tracking_result import GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult # noqa: PLC0415
        d = dict(src_dict)
        shipping_provider_name = d.pop("shipping_provider_name", UNSET)

        delivery_option = d.pop("delivery_option", UNSET)

        estimated_earliest_delivery_date = d.pop("estimated_earliest_delivery_date", UNSET)

        estimated_latest_delivery_date = d.pop("estimated_latest_delivery_date", UNSET)

        quantity = d.pop("quantity", UNSET)

        _tracking_results = d.pop("tracking_results", UNSET)
        tracking_results: list[GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult] | Unset = UNSET
        if _tracking_results is not UNSET:
            tracking_results = []
            for tracking_results_item_data in _tracking_results:
                tracking_results_item = GetAffiliateCampaignCreatorProductSampleStatusResponseDataSampleStatusTrackingResult.from_dict(tracking_results_item_data)



                tracking_results.append(tracking_results_item)


        get_affiliate_campaign_creator_product_sample_status_response_data_sample_status = cls(
            shipping_provider_name=shipping_provider_name,
            delivery_option=delivery_option,
            estimated_earliest_delivery_date=estimated_earliest_delivery_date,
            estimated_latest_delivery_date=estimated_latest_delivery_date,
            quantity=quantity,
            tracking_results=tracking_results,
        )


        get_affiliate_campaign_creator_product_sample_status_response_data_sample_status.additional_properties = d
        return get_affiliate_campaign_creator_product_sample_status_response_data_sample_status

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
