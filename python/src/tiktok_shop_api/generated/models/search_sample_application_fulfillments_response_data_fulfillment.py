from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.search_sample_application_fulfillments_response_data_fulfillment_content import SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent
  from ..models.search_sample_application_fulfillments_response_data_fulfillment_product import SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct





T = TypeVar("T", bound="SearchSampleApplicationFulfillmentsResponseDataFulfillment")



@_attrs_define
class SearchSampleApplicationFulfillmentsResponseDataFulfillment:
    """ 
        Attributes:
            product (SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct | Unset):
            content (SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent | Unset):
     """

    product: SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct | Unset = UNSET
    content: SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.search_sample_application_fulfillments_response_data_fulfillment_content import SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent # noqa: PLC0415
        from ..models.search_sample_application_fulfillments_response_data_fulfillment_product import SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct # noqa: PLC0415
        product: dict[str, Any] | Unset = UNSET
        if not isinstance(self.product, Unset):
            product = self.product.to_dict()

        content: dict[str, Any] | Unset = UNSET
        if not isinstance(self.content, Unset):
            content = self.content.to_dict()


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if product is not UNSET:
            field_dict["product"] = product
        if content is not UNSET:
            field_dict["content"] = content

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.search_sample_application_fulfillments_response_data_fulfillment_content import SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent # noqa: PLC0415
        from ..models.search_sample_application_fulfillments_response_data_fulfillment_product import SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct # noqa: PLC0415
        d = dict(src_dict)
        _product = d.pop("product", UNSET)
        product: SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct | Unset
        if isinstance(_product,  Unset):
            product = UNSET
        else:
            product = SearchSampleApplicationFulfillmentsResponseDataFulfillmentProduct.from_dict(_product)




        _content = d.pop("content", UNSET)
        content: SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent | Unset
        if isinstance(_content,  Unset):
            content = UNSET
        else:
            content = SearchSampleApplicationFulfillmentsResponseDataFulfillmentContent.from_dict(_content)




        search_sample_application_fulfillments_response_data_fulfillment = cls(
            product=product,
            content=content,
        )


        search_sample_application_fulfillments_response_data_fulfillment.additional_properties = d
        return search_sample_application_fulfillments_response_data_fulfillment

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
