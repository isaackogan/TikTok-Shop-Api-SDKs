from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.shipping_provider import ShippingProvider





T = TypeVar("T", bound="GetShippingProvidersResponseData")



@_attrs_define
class GetShippingProvidersResponseData:
    """ 
        Attributes:
            shipping_providers (list[ShippingProvider] | Unset): The shipping providers available for the specified delivery
                option.
     """

    shipping_providers: list[ShippingProvider] | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.shipping_provider import ShippingProvider # noqa: PLC0415
        shipping_providers: list[dict[str, Any]] | Unset = UNSET
        if not isinstance(self.shipping_providers, Unset):
            shipping_providers = []
            for shipping_providers_item_data in self.shipping_providers:
                shipping_providers_item = shipping_providers_item_data.to_dict()
                shipping_providers.append(shipping_providers_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if shipping_providers is not UNSET:
            field_dict["shipping_providers"] = shipping_providers

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.shipping_provider import ShippingProvider # noqa: PLC0415
        d = dict(src_dict)
        _shipping_providers = d.pop("shipping_providers", UNSET)
        shipping_providers: list[ShippingProvider] | Unset = UNSET
        if _shipping_providers is not UNSET:
            shipping_providers = []
            for shipping_providers_item_data in _shipping_providers:
                shipping_providers_item = ShippingProvider.from_dict(shipping_providers_item_data)



                shipping_providers.append(shipping_providers_item)


        get_shipping_providers_response_data = cls(
            shipping_providers=shipping_providers,
        )


        get_shipping_providers_response_data.additional_properties = d
        return get_shipping_providers_response_data

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
