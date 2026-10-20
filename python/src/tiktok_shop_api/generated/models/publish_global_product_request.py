from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from typing import cast

if TYPE_CHECKING:
  from ..models.publish_global_product_request_publish_target import PublishGlobalProductRequestPublishTarget





T = TypeVar("T", bound="PublishGlobalProductRequest")



@_attrs_define
class PublishGlobalProductRequest:
    """ 
        Attributes:
            publish_target (list[PublishGlobalProductRequestPublishTarget]): Target markets for publishing global products.
     """

    publish_target: list[PublishGlobalProductRequestPublishTarget]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.publish_global_product_request_publish_target import PublishGlobalProductRequestPublishTarget # noqa: PLC0415
        publish_target = []
        for publish_target_item_data in self.publish_target:
            publish_target_item = publish_target_item_data.to_dict()
            publish_target.append(publish_target_item)




        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
            "publish_target": publish_target,
        })

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.publish_global_product_request_publish_target import PublishGlobalProductRequestPublishTarget # noqa: PLC0415
        d = dict(src_dict)
        publish_target = []
        _publish_target = d.pop("publish_target")
        for publish_target_item_data in (_publish_target):
            publish_target_item = PublishGlobalProductRequestPublishTarget.from_dict(publish_target_item_data)



            publish_target.append(publish_target_item)


        publish_global_product_request = cls(
            publish_target=publish_target,
        )


        publish_global_product_request.additional_properties = d
        return publish_global_product_request

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
