from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.update_promotion_activity_products_request_product import UpdatePromotionActivityProductsRequestProduct





T = TypeVar("T", bound="UpdatePromotionActivityProductsRequest")



@_attrs_define
class UpdatePromotionActivityProductsRequest:
    """ 
        Attributes:
            activity_id (str): A unique ID that identifies activities.
                You cannot update the products in `DEACTIVATED` or `EXPIRED` activities.
            products (list[UpdatePromotionActivityProductsRequestProduct] | Unset): The items to add to the list or the
                existing items in the list of promotion activity to edit. The length must not exceed `300`.
            benefit_product_ids (list[str] | Unset): IDs of benefit products to add to or update in a Buy More Save More
                (BMSM) or Buy X Get Y (BXGY) activity. Omitting this field or passing an empty array leaves the activity's
                existing benefit products unchanged; it does not remove them. After the update, the activity can contain at most
                100 benefit products.
            exclude_product_ids (list[str] | Unset): For a SHOP-level Buy More Save More (BMSM) or Buy X Get Y (BXGY)
                activity, these are the IDs of products to add to or update in the exclusion list. Omitting this field or
                passing an empty array leaves existing excluded products unchanged; it does not remove them. Maximum: 100 IDs
                per request.
     """

    activity_id: str
    products: list[UpdatePromotionActivityProductsRequestProduct] | Unset = UNSET
    benefit_product_ids: list[str] | Unset = UNSET
    exclude_product_ids: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.update_promotion_activity_products_request_product import UpdatePromotionActivityProductsRequestProduct # noqa: PLC0415
        activity_id = self.activity_id

        products: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.products, Unset):
            products = []
            for products_item_data in self.products:
                products_item = products_item_data.to_dict()
                products.append(products_item)



        benefit_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.benefit_product_ids, Unset):
            benefit_product_ids = self.benefit_product_ids



        exclude_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.exclude_product_ids, Unset):
            exclude_product_ids = self.exclude_product_ids




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "activity_id": activity_id,
        })
        if products is not UNSET:
            field_dict["products"] = products
        if benefit_product_ids is not UNSET:
            field_dict["benefit_product_ids"] = benefit_product_ids
        if exclude_product_ids is not UNSET:
            field_dict["exclude_product_ids"] = exclude_product_ids

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.update_promotion_activity_products_request_product import UpdatePromotionActivityProductsRequestProduct # noqa: PLC0415
        d = dict(src_dict)
        activity_id = d.pop("activity_id")

        _products = d.pop("products", UNSET)
        products: list[UpdatePromotionActivityProductsRequestProduct] | Unset = UNSET
        if _products is not UNSET:
            products = []
            for products_item_data in _products:
                products_item = UpdatePromotionActivityProductsRequestProduct.from_dict(products_item_data)



                products.append(products_item)


        benefit_product_ids = cast(list[str], d.pop("benefit_product_ids", UNSET))


        exclude_product_ids = cast(list[str], d.pop("exclude_product_ids", UNSET))


        update_promotion_activity_products_request = cls(
            activity_id=activity_id,
            products=products,
            benefit_product_ids=benefit_product_ids,
            exclude_product_ids=exclude_product_ids,
        )


        update_promotion_activity_products_request.additional_properties = d
        return update_promotion_activity_products_request

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
