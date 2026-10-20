from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.get_sps_metric_problem_details_response_data_aht_problem_order_item import GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem
  from ..models.get_sps_metric_problem_details_response_data_im_dsat_chat_item import GetSPSMetricProblemDetailsResponseDataImDsatChatItem
  from ..models.get_sps_metric_problem_details_response_data_nbfr_problem_order_item import GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem
  from ..models.get_sps_metric_problem_details_response_data_nrr_problem_order_item import GetSPSMetricProblemDetailsResponseDataNrrProblemOrderItem
  from ..models.get_sps_metric_problem_details_response_data_otdr_problem_order_item import GetSPSMetricProblemDetailsResponseDataOtdrProblemOrderItem
  from ..models.get_sps_metric_problem_details_response_data_sfcr_problem_order_item import GetSPSMetricProblemDetailsResponseDataSfcrProblemOrderItem





T = TypeVar("T", bound="GetSPSMetricProblemDetailsResponseData")



@_attrs_define
class GetSPSMetricProblemDetailsResponseData:
    """ 
        Attributes:
            aht_problem_order_items (list[GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem] | Unset): AHT problem
                order items.
            im_dsat_chat_items (list[GetSPSMetricProblemDetailsResponseDataImDsatChatItem] | Unset): IM_DSAT chat session
                items.
            metric_code (str | Unset): Stable metric code. Possible values: NRR, NBFR, SFCR, OTDR, AHT, and IM_DSAT.
            nbfr_problem_order_items (list[GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem] | Unset): NBFR
                problem order items.
            next_page_token (str | Unset): An opaque token used to retrieve the next page of a paginated result set. Returns
                an empty string when there are no more results.
            nrr_problem_order_items (list[GetSPSMetricProblemDetailsResponseDataNrrProblemOrderItem] | Unset): NRR problem
                order items.
            otdr_problem_order_items (list[GetSPSMetricProblemDetailsResponseDataOtdrProblemOrderItem] | Unset): OTDR
                problem order items.
            sfcr_problem_order_items (list[GetSPSMetricProblemDetailsResponseDataSfcrProblemOrderItem] | Unset): SFCR
                problem order items.
            total_count (int | Unset): Total number of available records.
     """

    aht_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem] | Unset = UNSET
    im_dsat_chat_items: list[GetSPSMetricProblemDetailsResponseDataImDsatChatItem] | Unset = UNSET
    metric_code: str | Unset = UNSET
    nbfr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem] | Unset = UNSET
    next_page_token: str | Unset = UNSET
    nrr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataNrrProblemOrderItem] | Unset = UNSET
    otdr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataOtdrProblemOrderItem] | Unset = UNSET
    sfcr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataSfcrProblemOrderItem] | Unset = UNSET
    total_count: int | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.get_sps_metric_problem_details_response_data_aht_problem_order_item import GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_im_dsat_chat_item import GetSPSMetricProblemDetailsResponseDataImDsatChatItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_nbfr_problem_order_item import GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_nrr_problem_order_item import GetSPSMetricProblemDetailsResponseDataNrrProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_otdr_problem_order_item import GetSPSMetricProblemDetailsResponseDataOtdrProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_sfcr_problem_order_item import GetSPSMetricProblemDetailsResponseDataSfcrProblemOrderItem # noqa: PLC0415
        aht_problem_order_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.aht_problem_order_items, Unset):
            aht_problem_order_items = []
            for aht_problem_order_items_item_data in self.aht_problem_order_items:
                aht_problem_order_items_item = aht_problem_order_items_item_data.to_dict()
                aht_problem_order_items.append(aht_problem_order_items_item)



        im_dsat_chat_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.im_dsat_chat_items, Unset):
            im_dsat_chat_items = []
            for im_dsat_chat_items_item_data in self.im_dsat_chat_items:
                im_dsat_chat_items_item = im_dsat_chat_items_item_data.to_dict()
                im_dsat_chat_items.append(im_dsat_chat_items_item)



        metric_code = self.metric_code

        nbfr_problem_order_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nbfr_problem_order_items, Unset):
            nbfr_problem_order_items = []
            for nbfr_problem_order_items_item_data in self.nbfr_problem_order_items:
                nbfr_problem_order_items_item = nbfr_problem_order_items_item_data.to_dict()
                nbfr_problem_order_items.append(nbfr_problem_order_items_item)



        next_page_token = self.next_page_token

        nrr_problem_order_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.nrr_problem_order_items, Unset):
            nrr_problem_order_items = []
            for nrr_problem_order_items_item_data in self.nrr_problem_order_items:
                nrr_problem_order_items_item = nrr_problem_order_items_item_data.to_dict()
                nrr_problem_order_items.append(nrr_problem_order_items_item)



        otdr_problem_order_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.otdr_problem_order_items, Unset):
            otdr_problem_order_items = []
            for otdr_problem_order_items_item_data in self.otdr_problem_order_items:
                otdr_problem_order_items_item = otdr_problem_order_items_item_data.to_dict()
                otdr_problem_order_items.append(otdr_problem_order_items_item)



        sfcr_problem_order_items: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.sfcr_problem_order_items, Unset):
            sfcr_problem_order_items = []
            for sfcr_problem_order_items_item_data in self.sfcr_problem_order_items:
                sfcr_problem_order_items_item = sfcr_problem_order_items_item_data.to_dict()
                sfcr_problem_order_items.append(sfcr_problem_order_items_item)



        total_count = self.total_count


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if aht_problem_order_items is not UNSET:
            field_dict["aht_problem_order_items"] = aht_problem_order_items
        if im_dsat_chat_items is not UNSET:
            field_dict["im_dsat_chat_items"] = im_dsat_chat_items
        if metric_code is not UNSET:
            field_dict["metric_code"] = metric_code
        if nbfr_problem_order_items is not UNSET:
            field_dict["nbfr_problem_order_items"] = nbfr_problem_order_items
        if next_page_token is not UNSET:
            field_dict["next_page_token"] = next_page_token
        if nrr_problem_order_items is not UNSET:
            field_dict["nrr_problem_order_items"] = nrr_problem_order_items
        if otdr_problem_order_items is not UNSET:
            field_dict["otdr_problem_order_items"] = otdr_problem_order_items
        if sfcr_problem_order_items is not UNSET:
            field_dict["sfcr_problem_order_items"] = sfcr_problem_order_items
        if total_count is not UNSET:
            field_dict["total_count"] = total_count

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.get_sps_metric_problem_details_response_data_aht_problem_order_item import GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_im_dsat_chat_item import GetSPSMetricProblemDetailsResponseDataImDsatChatItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_nbfr_problem_order_item import GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_nrr_problem_order_item import GetSPSMetricProblemDetailsResponseDataNrrProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_otdr_problem_order_item import GetSPSMetricProblemDetailsResponseDataOtdrProblemOrderItem # noqa: PLC0415
        from ..models.get_sps_metric_problem_details_response_data_sfcr_problem_order_item import GetSPSMetricProblemDetailsResponseDataSfcrProblemOrderItem # noqa: PLC0415
        d = dict(src_dict)
        _aht_problem_order_items = d.pop("aht_problem_order_items", UNSET)
        aht_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem] | Unset = UNSET
        if _aht_problem_order_items is not UNSET:
            aht_problem_order_items = []
            for aht_problem_order_items_item_data in _aht_problem_order_items:
                aht_problem_order_items_item = GetSPSMetricProblemDetailsResponseDataAhtProblemOrderItem.from_dict(aht_problem_order_items_item_data)



                aht_problem_order_items.append(aht_problem_order_items_item)


        _im_dsat_chat_items = d.pop("im_dsat_chat_items", UNSET)
        im_dsat_chat_items: list[GetSPSMetricProblemDetailsResponseDataImDsatChatItem] | Unset = UNSET
        if _im_dsat_chat_items is not UNSET:
            im_dsat_chat_items = []
            for im_dsat_chat_items_item_data in _im_dsat_chat_items:
                im_dsat_chat_items_item = GetSPSMetricProblemDetailsResponseDataImDsatChatItem.from_dict(im_dsat_chat_items_item_data)



                im_dsat_chat_items.append(im_dsat_chat_items_item)


        metric_code = d.pop("metric_code", UNSET)

        _nbfr_problem_order_items = d.pop("nbfr_problem_order_items", UNSET)
        nbfr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem] | Unset = UNSET
        if _nbfr_problem_order_items is not UNSET:
            nbfr_problem_order_items = []
            for nbfr_problem_order_items_item_data in _nbfr_problem_order_items:
                nbfr_problem_order_items_item = GetSPSMetricProblemDetailsResponseDataNbfrProblemOrderItem.from_dict(nbfr_problem_order_items_item_data)



                nbfr_problem_order_items.append(nbfr_problem_order_items_item)


        next_page_token = d.pop("next_page_token", UNSET)

        _nrr_problem_order_items = d.pop("nrr_problem_order_items", UNSET)
        nrr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataNrrProblemOrderItem] | Unset = UNSET
        if _nrr_problem_order_items is not UNSET:
            nrr_problem_order_items = []
            for nrr_problem_order_items_item_data in _nrr_problem_order_items:
                nrr_problem_order_items_item = GetSPSMetricProblemDetailsResponseDataNrrProblemOrderItem.from_dict(nrr_problem_order_items_item_data)



                nrr_problem_order_items.append(nrr_problem_order_items_item)


        _otdr_problem_order_items = d.pop("otdr_problem_order_items", UNSET)
        otdr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataOtdrProblemOrderItem] | Unset = UNSET
        if _otdr_problem_order_items is not UNSET:
            otdr_problem_order_items = []
            for otdr_problem_order_items_item_data in _otdr_problem_order_items:
                otdr_problem_order_items_item = GetSPSMetricProblemDetailsResponseDataOtdrProblemOrderItem.from_dict(otdr_problem_order_items_item_data)



                otdr_problem_order_items.append(otdr_problem_order_items_item)


        _sfcr_problem_order_items = d.pop("sfcr_problem_order_items", UNSET)
        sfcr_problem_order_items: list[GetSPSMetricProblemDetailsResponseDataSfcrProblemOrderItem] | Unset = UNSET
        if _sfcr_problem_order_items is not UNSET:
            sfcr_problem_order_items = []
            for sfcr_problem_order_items_item_data in _sfcr_problem_order_items:
                sfcr_problem_order_items_item = GetSPSMetricProblemDetailsResponseDataSfcrProblemOrderItem.from_dict(sfcr_problem_order_items_item_data)



                sfcr_problem_order_items.append(sfcr_problem_order_items_item)


        total_count = d.pop("total_count", UNSET)

        get_sps_metric_problem_details_response_data = cls(
            aht_problem_order_items=aht_problem_order_items,
            im_dsat_chat_items=im_dsat_chat_items,
            metric_code=metric_code,
            nbfr_problem_order_items=nbfr_problem_order_items,
            next_page_token=next_page_token,
            nrr_problem_order_items=nrr_problem_order_items,
            otdr_problem_order_items=otdr_problem_order_items,
            sfcr_problem_order_items=sfcr_problem_order_items,
            total_count=total_count,
        )


        get_sps_metric_problem_details_response_data.additional_properties = d
        return get_sps_metric_problem_details_response_data

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
