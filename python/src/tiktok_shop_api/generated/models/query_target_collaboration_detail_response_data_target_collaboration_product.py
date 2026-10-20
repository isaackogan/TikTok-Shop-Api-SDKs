from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.original_price import OriginalPrice
  from ..models.query_target_collaboration_detail_response_data_target_collaboration_product_commission import QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission





T = TypeVar("T", bound="QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct")



@_attrs_define
class QueryTargetCollaborationDetailResponseDataTargetCollaborationProduct:
    """ 
        Attributes:
            id (str | Unset): The product identifier.
            main_image_url (str | Unset): The product image url.
            title (str | Unset): The product name.
            original_price (OriginalPrice | Unset):
            commission (QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission | Unset):
            status (str | Unset): Product's status.
                Field values:
                - LIVE: When the product is normal for sale, return to the LIVE status
                - OUT_OF_STOCK: When the product is out of stock for the consumer, the OUT_OF_STOCK state is returned
                - SELLER_DEACTIVATE:  When the product is deactivated by the merchant, the SELLER_DEACTIVATE status is returned
                - PLATFORM_DEACTIVATE: When the product is deactivated by the platform or is not available for sale, the
                PLATFORM_DEACTIVATE status is returned
                - GNE_REJECT: When the product is governed or the target collaboration is dismissed, the GNE_REJECT state is
                returned
                - DELETE: When the product is deleted, the DELETE status is returned
                - OTHER: When the product is in an unsaleable state, such as draft, frozen, review, etc, the OTHER status is
                returned
            commission_effective_status (str | Unset): The effectiveness of this product's target collaboration commission
                across creators.
                Field values:
                - EFFECTIVE_ALL: The commission is effective for all creators.
                - EFFECTIVE_PARTIALLY: The commission is effective for some creators.
                - EFFECTIVE_NONE: The commission is not effective for any creators.
                Normally, the commission for a product will be the same for all creators.
                If the merchant participates in TOP_CREATOR_PROGRAM, and TOP_CREATOR_PROGRAM includes the current product and
                some creators, the commission rate will be based on TOP_CREATOR_PROGRAM. The product commission under the
                current Target Collaboration will be effective for some creators, corresponding to EFFECTIVE_PARTIALLY status.
            collaboration_status (str | Unset): The status of the product in the current target cooperation.
                Field values:
                - NORMAL: The status of the product in the current target collaboration is normal.
                - DELETING: The status of the product in the current target collaboration is deleting.Product in the DELETING
                state will end their delayed effectiveness state and move to the DELETED state at 00:00 the next day.
                - DELETED: The status of the product in the current target collaboration is deleted.
     """

    id: str | Unset = UNSET
    main_image_url: str | Unset = UNSET
    title: str | Unset = UNSET
    original_price: OriginalPrice | Unset = UNSET
    commission: QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission | Unset = UNSET
    status: str | Unset = UNSET
    commission_effective_status: str | Unset = UNSET
    collaboration_status: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.original_price import OriginalPrice # noqa: PLC0415
        from ..models.query_target_collaboration_detail_response_data_target_collaboration_product_commission import QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission # noqa: PLC0415
        id = self.id

        main_image_url = self.main_image_url

        title = self.title

        original_price: dict[str, Any] | Unset = UNSET
        if not isinstance(self.original_price, Unset):
            original_price = self.original_price.to_dict()

        commission: dict[str, Any] | Unset = UNSET
        if not isinstance(self.commission, Unset):
            commission = self.commission.to_dict()

        status = self.status

        commission_effective_status = self.commission_effective_status

        collaboration_status = self.collaboration_status


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if main_image_url is not UNSET:
            field_dict["main_image_url"] = main_image_url
        if title is not UNSET:
            field_dict["title"] = title
        if original_price is not UNSET:
            field_dict["original_price"] = original_price
        if commission is not UNSET:
            field_dict["commission"] = commission
        if status is not UNSET:
            field_dict["status"] = status
        if commission_effective_status is not UNSET:
            field_dict["commission_effective_status"] = commission_effective_status
        if collaboration_status is not UNSET:
            field_dict["collaboration_status"] = collaboration_status

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.original_price import OriginalPrice # noqa: PLC0415
        from ..models.query_target_collaboration_detail_response_data_target_collaboration_product_commission import QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        main_image_url = d.pop("main_image_url", UNSET)

        title = d.pop("title", UNSET)

        _original_price = d.pop("original_price", UNSET)
        original_price: OriginalPrice | Unset
        if isinstance(_original_price,  Unset):
            original_price = UNSET
        else:
            original_price = OriginalPrice.from_dict(_original_price)




        _commission = d.pop("commission", UNSET)
        commission: QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission | Unset
        if isinstance(_commission,  Unset):
            commission = UNSET
        else:
            commission = QueryTargetCollaborationDetailResponseDataTargetCollaborationProductCommission.from_dict(_commission)




        status = d.pop("status", UNSET)

        commission_effective_status = d.pop("commission_effective_status", UNSET)

        collaboration_status = d.pop("collaboration_status", UNSET)

        query_target_collaboration_detail_response_data_target_collaboration_product = cls(
            id=id,
            main_image_url=main_image_url,
            title=title,
            original_price=original_price,
            commission=commission,
            status=status,
            commission_effective_status=commission_effective_status,
            collaboration_status=collaboration_status,
        )


        query_target_collaboration_detail_response_data_target_collaboration_product.additional_properties = d
        return query_target_collaboration_detail_response_data_target_collaboration_product

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
