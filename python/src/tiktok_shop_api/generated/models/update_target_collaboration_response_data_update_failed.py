from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.seller_contact_info import SellerContactInfo
  from ..models.update_target_collaboration_response_data_update_failed_add_product import UpdateTargetCollaborationResponseDataUpdateFailedAddProduct
  from ..models.update_target_collaboration_response_data_update_failed_change_commission import UpdateTargetCollaborationResponseDataUpdateFailedChangeCommission





T = TypeVar("T", bound="UpdateTargetCollaborationResponseDataUpdateFailed")



@_attrs_define
class UpdateTargetCollaborationResponseDataUpdateFailed:
    """ 
        Attributes:
            remove_creator_open_ids (list[str] | Unset): The list of creators' TikTok User Open IDs that have not been
                successfully removed. More details:https://partner.tiktokshop.com/docv2/page/3obfokj6
            remove_product_ids (list[str] | Unset): The list of product ids that have not been successfully removed.
            add_creator_open_ids (list[str] | Unset): The list of creators' TikTok User Open IDs that have not been
                successfully added. More details:https://partner.tiktokshop.com/docv2/page/3obfokj6
            add_products (UpdateTargetCollaborationResponseDataUpdateFailedAddProduct | Unset):
            change_commissions (UpdateTargetCollaborationResponseDataUpdateFailedChangeCommission | Unset):
            end_time (int | Unset): The end time of the target collaboration, which has not been successfully updated.
            seller_contact_info (SellerContactInfo | Unset):
            name (str | Unset): The name of the target collaboration.
            invalid_product_id_list (list[str] | Unset): The list of product id that caused the update to fail.
            invalid_open_id_list (list[str] | Unset): The list of open id that caused the update to fail.
     """

    remove_creator_open_ids: list[str] | Unset = UNSET
    remove_product_ids: list[str] | Unset = UNSET
    add_creator_open_ids: list[str] | Unset = UNSET
    add_products: UpdateTargetCollaborationResponseDataUpdateFailedAddProduct | Unset = UNSET
    change_commissions: UpdateTargetCollaborationResponseDataUpdateFailedChangeCommission | Unset = UNSET
    end_time: int | Unset = UNSET
    seller_contact_info: SellerContactInfo | Unset = UNSET
    name: str | Unset = UNSET
    invalid_product_id_list: list[str] | Unset = UNSET
    invalid_open_id_list: list[str] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.seller_contact_info import SellerContactInfo # noqa: PLC0415
        from ..models.update_target_collaboration_response_data_update_failed_add_product import UpdateTargetCollaborationResponseDataUpdateFailedAddProduct # noqa: PLC0415
        from ..models.update_target_collaboration_response_data_update_failed_change_commission import UpdateTargetCollaborationResponseDataUpdateFailedChangeCommission # noqa: PLC0415
        remove_creator_open_ids: list[str] | Unset = UNSET
        if not isinstance(self.remove_creator_open_ids, Unset):
            remove_creator_open_ids = self.remove_creator_open_ids



        remove_product_ids: list[str] | Unset = UNSET
        if not isinstance(self.remove_product_ids, Unset):
            remove_product_ids = self.remove_product_ids



        add_creator_open_ids: list[str] | Unset = UNSET
        if not isinstance(self.add_creator_open_ids, Unset):
            add_creator_open_ids = self.add_creator_open_ids



        add_products: dict[str, Any] | Unset = UNSET
        if not isinstance(self.add_products, Unset):
            add_products = self.add_products.to_dict()

        change_commissions: dict[str, Any] | Unset = UNSET
        if not isinstance(self.change_commissions, Unset):
            change_commissions = self.change_commissions.to_dict()

        end_time = self.end_time

        seller_contact_info: dict[str, Any] | Unset = UNSET
        if not isinstance(self.seller_contact_info, Unset):
            seller_contact_info = self.seller_contact_info.to_dict()

        name = self.name

        invalid_product_id_list: list[str] | Unset = UNSET
        if not isinstance(self.invalid_product_id_list, Unset):
            invalid_product_id_list = self.invalid_product_id_list



        invalid_open_id_list: list[str] | Unset = UNSET
        if not isinstance(self.invalid_open_id_list, Unset):
            invalid_open_id_list = self.invalid_open_id_list




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if remove_creator_open_ids is not UNSET:
            field_dict["remove_creator_open_ids"] = remove_creator_open_ids
        if remove_product_ids is not UNSET:
            field_dict["remove_product_ids"] = remove_product_ids
        if add_creator_open_ids is not UNSET:
            field_dict["add_creator_open_ids"] = add_creator_open_ids
        if add_products is not UNSET:
            field_dict["add_products"] = add_products
        if change_commissions is not UNSET:
            field_dict["change_commissions"] = change_commissions
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if seller_contact_info is not UNSET:
            field_dict["seller_contact_info"] = seller_contact_info
        if name is not UNSET:
            field_dict["name"] = name
        if invalid_product_id_list is not UNSET:
            field_dict["invalid_product_id_list"] = invalid_product_id_list
        if invalid_open_id_list is not UNSET:
            field_dict["invalid_open_id_list"] = invalid_open_id_list

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.seller_contact_info import SellerContactInfo # noqa: PLC0415
        from ..models.update_target_collaboration_response_data_update_failed_add_product import UpdateTargetCollaborationResponseDataUpdateFailedAddProduct # noqa: PLC0415
        from ..models.update_target_collaboration_response_data_update_failed_change_commission import UpdateTargetCollaborationResponseDataUpdateFailedChangeCommission # noqa: PLC0415
        d = dict(src_dict)
        remove_creator_open_ids = cast(list[str], d.pop("remove_creator_open_ids", UNSET))


        remove_product_ids = cast(list[str], d.pop("remove_product_ids", UNSET))


        add_creator_open_ids = cast(list[str], d.pop("add_creator_open_ids", UNSET))


        _add_products = d.pop("add_products", UNSET)
        add_products: UpdateTargetCollaborationResponseDataUpdateFailedAddProduct | Unset
        if isinstance(_add_products,  Unset):
            add_products = UNSET
        else:
            add_products = UpdateTargetCollaborationResponseDataUpdateFailedAddProduct.from_dict(_add_products)




        _change_commissions = d.pop("change_commissions", UNSET)
        change_commissions: UpdateTargetCollaborationResponseDataUpdateFailedChangeCommission | Unset
        if isinstance(_change_commissions,  Unset):
            change_commissions = UNSET
        else:
            change_commissions = UpdateTargetCollaborationResponseDataUpdateFailedChangeCommission.from_dict(_change_commissions)




        end_time = d.pop("end_time", UNSET)

        _seller_contact_info = d.pop("seller_contact_info", UNSET)
        seller_contact_info: SellerContactInfo | Unset
        if isinstance(_seller_contact_info,  Unset):
            seller_contact_info = UNSET
        else:
            seller_contact_info = SellerContactInfo.from_dict(_seller_contact_info)




        name = d.pop("name", UNSET)

        invalid_product_id_list = cast(list[str], d.pop("invalid_product_id_list", UNSET))


        invalid_open_id_list = cast(list[str], d.pop("invalid_open_id_list", UNSET))


        update_target_collaboration_response_data_update_failed = cls(
            remove_creator_open_ids=remove_creator_open_ids,
            remove_product_ids=remove_product_ids,
            add_creator_open_ids=add_creator_open_ids,
            add_products=add_products,
            change_commissions=change_commissions,
            end_time=end_time,
            seller_contact_info=seller_contact_info,
            name=name,
            invalid_product_id_list=invalid_product_id_list,
            invalid_open_id_list=invalid_open_id_list,
        )


        update_target_collaboration_response_data_update_failed.additional_properties = d
        return update_target_collaboration_response_data_update_failed

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
