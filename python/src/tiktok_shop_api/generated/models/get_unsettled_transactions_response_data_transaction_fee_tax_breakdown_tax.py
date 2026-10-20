from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset






T = TypeVar("T", bound="GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdownTax")



@_attrs_define
class GetUnsettledTransactionsResponseDataTransactionFeeTaxBreakdownTax:
    """ 
        Attributes:
            sales_tax_amount (str | Unset): The final sales tax to be paid by the customer for the product and delivery.
                Formula: sales_tax_payment_amount - sales_tax_refund_amount
            sales_tax_payment_amount (str | Unset): The expected sales tax to be paid by the customer for the product and
                delivery.
            sales_tax_refund_amount (str | Unset): The sales tax amount returned to the customer in the event of a refund.
            vat_amount (str | Unset): The VAT paid by the platform on the seller's behalf.
                Applicable only for cross-border shop orders.
            import_vat_amount (str | Unset): The import VAT, a tax paid on goods bought in one country and imported into
                another.
                Applicable only for cross-border shop orders.
            customs_duty_amount (str | Unset): The customs duties, a type of tax on cross-border goods collected by
                governments.
                Applicable only for cross-border shop orders.
            customs_clearance_amount (str | Unset): The fees charged by logistic suppliers for customs clearance services.
                Applicable only for cross-border shop orders.
            sst_amount (str | Unset): The sales and service tax (SST) collected and remitted to the tax authority by the
                platform for low-value goods imported into Malaysia, effective January 1, 2024.
            gst_amount (str | Unset): The goods and services tax (GST) collected and remitted to the tax authority by the
                platform for low-value goods imported into Singapore, effective January 1, 2023.
            sales_tax_referral_fee_amount (str | Unset): Some U.S. states consider referral fees taxable. To comply with
                state tax laws, TikTok Inc. collects and remits applicable sales tax when a taxable fee is charged.
            smart_promotion_fee_tax_amount (str | Unset): The sales tax applied to the Smart Promotion fee.
            cedular_tax (str | Unset): The Mexican Guanajuato cedular tax
            new_customer_growth_package_fee_tax (str | Unset): The sales tax applied to the New Customer Growth Package fee.
            store_gmv_growth_package_fee_sales_tax (str | Unset): The sales tax applied to the Shop GMV Growth Package fee.
            target_product_gmv_growth_package_tax (str | Unset): The sales tax applied to the Product GMV Growth Package
                fee.
            auto_post_shoppable_video_sales_tax (str | Unset): The sales tax applied to the auto-post shoppable video
                commission fee.
     """

    sales_tax_amount: str | Unset = UNSET
    sales_tax_payment_amount: str | Unset = UNSET
    sales_tax_refund_amount: str | Unset = UNSET
    vat_amount: str | Unset = UNSET
    import_vat_amount: str | Unset = UNSET
    customs_duty_amount: str | Unset = UNSET
    customs_clearance_amount: str | Unset = UNSET
    sst_amount: str | Unset = UNSET
    gst_amount: str | Unset = UNSET
    sales_tax_referral_fee_amount: str | Unset = UNSET
    smart_promotion_fee_tax_amount: str | Unset = UNSET
    cedular_tax: str | Unset = UNSET
    new_customer_growth_package_fee_tax: str | Unset = UNSET
    store_gmv_growth_package_fee_sales_tax: str | Unset = UNSET
    target_product_gmv_growth_package_tax: str | Unset = UNSET
    auto_post_shoppable_video_sales_tax: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        sales_tax_amount = self.sales_tax_amount

        sales_tax_payment_amount = self.sales_tax_payment_amount

        sales_tax_refund_amount = self.sales_tax_refund_amount

        vat_amount = self.vat_amount

        import_vat_amount = self.import_vat_amount

        customs_duty_amount = self.customs_duty_amount

        customs_clearance_amount = self.customs_clearance_amount

        sst_amount = self.sst_amount

        gst_amount = self.gst_amount

        sales_tax_referral_fee_amount = self.sales_tax_referral_fee_amount

        smart_promotion_fee_tax_amount = self.smart_promotion_fee_tax_amount

        cedular_tax = self.cedular_tax

        new_customer_growth_package_fee_tax = self.new_customer_growth_package_fee_tax

        store_gmv_growth_package_fee_sales_tax = self.store_gmv_growth_package_fee_sales_tax

        target_product_gmv_growth_package_tax = self.target_product_gmv_growth_package_tax

        auto_post_shoppable_video_sales_tax = self.auto_post_shoppable_video_sales_tax


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if sales_tax_amount is not UNSET:
            field_dict["sales_tax_amount"] = sales_tax_amount
        if sales_tax_payment_amount is not UNSET:
            field_dict["sales_tax_payment_amount"] = sales_tax_payment_amount
        if sales_tax_refund_amount is not UNSET:
            field_dict["sales_tax_refund_amount"] = sales_tax_refund_amount
        if vat_amount is not UNSET:
            field_dict["vat_amount"] = vat_amount
        if import_vat_amount is not UNSET:
            field_dict["import_vat_amount"] = import_vat_amount
        if customs_duty_amount is not UNSET:
            field_dict["customs_duty_amount"] = customs_duty_amount
        if customs_clearance_amount is not UNSET:
            field_dict["customs_clearance_amount"] = customs_clearance_amount
        if sst_amount is not UNSET:
            field_dict["sst_amount"] = sst_amount
        if gst_amount is not UNSET:
            field_dict["gst_amount"] = gst_amount
        if sales_tax_referral_fee_amount is not UNSET:
            field_dict["sales_tax_referral_fee_amount"] = sales_tax_referral_fee_amount
        if smart_promotion_fee_tax_amount is not UNSET:
            field_dict["smart_promotion_fee_tax_amount"] = smart_promotion_fee_tax_amount
        if cedular_tax is not UNSET:
            field_dict["cedular_tax"] = cedular_tax
        if new_customer_growth_package_fee_tax is not UNSET:
            field_dict["new_customer_growth_package_fee_tax"] = new_customer_growth_package_fee_tax
        if store_gmv_growth_package_fee_sales_tax is not UNSET:
            field_dict["store_gmv_growth_package_fee_sales_tax"] = store_gmv_growth_package_fee_sales_tax
        if target_product_gmv_growth_package_tax is not UNSET:
            field_dict["target_product_gmv_growth_package_tax"] = target_product_gmv_growth_package_tax
        if auto_post_shoppable_video_sales_tax is not UNSET:
            field_dict["auto_post_shoppable_video_sales_tax"] = auto_post_shoppable_video_sales_tax

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        sales_tax_amount = d.pop("sales_tax_amount", UNSET)

        sales_tax_payment_amount = d.pop("sales_tax_payment_amount", UNSET)

        sales_tax_refund_amount = d.pop("sales_tax_refund_amount", UNSET)

        vat_amount = d.pop("vat_amount", UNSET)

        import_vat_amount = d.pop("import_vat_amount", UNSET)

        customs_duty_amount = d.pop("customs_duty_amount", UNSET)

        customs_clearance_amount = d.pop("customs_clearance_amount", UNSET)

        sst_amount = d.pop("sst_amount", UNSET)

        gst_amount = d.pop("gst_amount", UNSET)

        sales_tax_referral_fee_amount = d.pop("sales_tax_referral_fee_amount", UNSET)

        smart_promotion_fee_tax_amount = d.pop("smart_promotion_fee_tax_amount", UNSET)

        cedular_tax = d.pop("cedular_tax", UNSET)

        new_customer_growth_package_fee_tax = d.pop("new_customer_growth_package_fee_tax", UNSET)

        store_gmv_growth_package_fee_sales_tax = d.pop("store_gmv_growth_package_fee_sales_tax", UNSET)

        target_product_gmv_growth_package_tax = d.pop("target_product_gmv_growth_package_tax", UNSET)

        auto_post_shoppable_video_sales_tax = d.pop("auto_post_shoppable_video_sales_tax", UNSET)

        get_unsettled_transactions_response_data_transaction_fee_tax_breakdown_tax = cls(
            sales_tax_amount=sales_tax_amount,
            sales_tax_payment_amount=sales_tax_payment_amount,
            sales_tax_refund_amount=sales_tax_refund_amount,
            vat_amount=vat_amount,
            import_vat_amount=import_vat_amount,
            customs_duty_amount=customs_duty_amount,
            customs_clearance_amount=customs_clearance_amount,
            sst_amount=sst_amount,
            gst_amount=gst_amount,
            sales_tax_referral_fee_amount=sales_tax_referral_fee_amount,
            smart_promotion_fee_tax_amount=smart_promotion_fee_tax_amount,
            cedular_tax=cedular_tax,
            new_customer_growth_package_fee_tax=new_customer_growth_package_fee_tax,
            store_gmv_growth_package_fee_sales_tax=store_gmv_growth_package_fee_sales_tax,
            target_product_gmv_growth_package_tax=target_product_gmv_growth_package_tax,
            auto_post_shoppable_video_sales_tax=auto_post_shoppable_video_sales_tax,
        )


        get_unsettled_transactions_response_data_transaction_fee_tax_breakdown_tax.additional_properties = d
        return get_unsettled_transactions_response_data_transaction_fee_tax_breakdown_tax

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
