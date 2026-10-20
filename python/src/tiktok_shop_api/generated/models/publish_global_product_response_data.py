from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.publish_global_product_response_data_product import PublishGlobalProductResponseDataProduct
  from ..models.publish_result import PublishResult





T = TypeVar("T", bound="PublishGlobalProductResponseData")



@_attrs_define
class PublishGlobalProductResponseData:
    """ 
        Attributes:
            products (list[PublishGlobalProductResponseDataProduct] | Unset): The local products converted from the global
                product. Match each item to its publication result in `publish_result` by `region`. A region can have a
                `publish_result` item without a corresponding local product when its status is `FAILED`.
            publish_result (list[PublishResult] | Unset): Results of publishing the global product.
     """

    products: list[PublishGlobalProductResponseDataProduct] | Unset = UNSET
    publish_result: list[PublishResult] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_global_product_response_data_product import PublishGlobalProductResponseDataProduct # noqa: PLC0415
        from ..models.publish_result import PublishResult # noqa: PLC0415
        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        publish_result: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.publish_result, Unset):
            publish_result = []
            for publish_result_item_data in self.publish_result:
                publish_result_item = publish_result_item_data.to_dict()
                publish_result.append(publish_result_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if products is not UNSET:
            field_dict["products"] = products
        if publish_result is not UNSET:
            field_dict["publish_result"] = publish_result

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_global_product_response_data_product import PublishGlobalProductResponseDataProduct # noqa: PLC0415
        from ..models.publish_result import PublishResult # noqa: PLC0415
        d = dict(src_dict)
        _products = d.pop("products", UNSET)
        products: list[PublishGlobalProductResponseDataProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = PublishGlobalProductResponseDataProduct.from_dict(products_item_data)



                products.append(products_item)


        _publish_result = d.pop("publish_result", UNSET)
        publish_result: list[PublishResult] | Unset = UNSET
        if _publish_result is not UNSET:
            publish_result = []
            for publish_result_item_data in _publish_result:
                publish_result_item = PublishResult.from_dict(publish_result_item_data)



                publish_result.append(publish_result_item)


        publish_global_product_response_data = cls(
            products=products,
            publish_result=publish_result,
        )


        publish_global_product_response_data.additional_properties = d
        return publish_global_product_response_data

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
