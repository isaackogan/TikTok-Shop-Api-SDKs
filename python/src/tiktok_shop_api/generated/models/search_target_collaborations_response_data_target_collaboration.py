from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar, BinaryIO, TextIO, TYPE_CHECKING, Generator

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

from ..types import UNSET, Unset
from typing import cast

if TYPE_CHECKING:
  from ..models.query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule import QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule





T = TypeVar("T", bound="SearchTargetCollaborationsResponseDataTargetCollaboration")



@_attrs_define
class SearchTargetCollaborationsResponseDataTargetCollaboration:
    """ 
        Attributes:
            id (str | Unset): Target collaboration ID.
            name (str | Unset): Target collaboration name.
            message (str | Unset): Message seller has sent to creators about seller's  introduction and why excited to
                collaborate.
            start_time (int | Unset): Unix timestamp, in seconds, when the target collaboration starts.
            end_time (int | Unset): Unix timestamp, in seconds, when the target collaboration ends.
            create_time (int | Unset): Unix timestamp, in seconds, when the target collaboration was created.
            update_time (int | Unset): Unix timestamp, in seconds, when the target collaboration was last updated.
            creator_inivited_count (int | Unset): The count of creators invited in the target collaboration.
            showcase_creator_count (int | Unset): The number of creators in the target collaboration who added at least one
                of its products to their showcase.
            content_creator_count (int | Unset): The number of creators who posted content featuring products from target
                collaboration.
            product_count (int | Unset): The count of products added in the target collaboration.
            free_sample_rule (QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule | Unset):
            type_ (str | Unset): The type of target collaboration.
                Field values:
                - STANDARD: The target collaboration is created by sellers manually selecting products and creators.
                - TOP_CREATOR_PROGRAM: The target collaboration created by seller joining TikTok Shop Top Creator Program,
                requiring only product submission.
     """

    id: str | Unset = UNSET
    name: str | Unset = UNSET
    message: str | Unset = UNSET
    start_time: int | Unset = UNSET
    end_time: int | Unset = UNSET
    create_time: int | Unset = UNSET
    update_time: int | Unset = UNSET
    creator_inivited_count: int | Unset = UNSET
    showcase_creator_count: int | Unset = UNSET
    content_creator_count: int | Unset = UNSET
    product_count: int | Unset = UNSET
    free_sample_rule: QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule | Unset = UNSET
    type_: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)





    def to_dict(self) -> dict[str, Any]:
        from ..models.query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule import QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule # noqa: PLC0415
        id = self.id

        name = self.name

        message = self.message

        start_time = self.start_time

        end_time = self.end_time

        create_time = self.create_time

        update_time = self.update_time

        creator_inivited_count = self.creator_inivited_count

        showcase_creator_count = self.showcase_creator_count

        content_creator_count = self.content_creator_count

        product_count = self.product_count

        free_sample_rule: dict[str, Any] | Unset = UNSET
        if not isinstance(self.free_sample_rule, Unset):
            free_sample_rule = self.free_sample_rule.to_dict()

        type_ = self.type_


        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({
        })
        if id is not UNSET:
            field_dict["id"] = id
        if name is not UNSET:
            field_dict["name"] = name
        if message is not UNSET:
            field_dict["message"] = message
        if start_time is not UNSET:
            field_dict["start_time"] = start_time
        if end_time is not UNSET:
            field_dict["end_time"] = end_time
        if create_time is not UNSET:
            field_dict["create_time"] = create_time
        if update_time is not UNSET:
            field_dict["update_time"] = update_time
        if creator_inivited_count is not UNSET:
            field_dict["creator_inivited_count"] = creator_inivited_count
        if showcase_creator_count is not UNSET:
            field_dict["showcase_creator_count"] = showcase_creator_count
        if content_creator_count is not UNSET:
            field_dict["content_creator_count"] = content_creator_count
        if product_count is not UNSET:
            field_dict["product_count"] = product_count
        if free_sample_rule is not UNSET:
            field_dict["free_sample_rule"] = free_sample_rule
        if type_ is not UNSET:
            field_dict["type"] = type_

        return field_dict



    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.query_target_collaboration_detail_response_data_target_collaboration_free_sample_rule import QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule # noqa: PLC0415
        d = dict(src_dict)
        id = d.pop("id", UNSET)

        name = d.pop("name", UNSET)

        message = d.pop("message", UNSET)

        start_time = d.pop("start_time", UNSET)

        end_time = d.pop("end_time", UNSET)

        create_time = d.pop("create_time", UNSET)

        update_time = d.pop("update_time", UNSET)

        creator_inivited_count = d.pop("creator_inivited_count", UNSET)

        showcase_creator_count = d.pop("showcase_creator_count", UNSET)

        content_creator_count = d.pop("content_creator_count", UNSET)

        product_count = d.pop("product_count", UNSET)

        _free_sample_rule = d.pop("free_sample_rule", UNSET)
        free_sample_rule: QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule | Unset
        if isinstance(_free_sample_rule,  Unset):
            free_sample_rule = UNSET
        else:
            free_sample_rule = QueryTargetCollaborationDetailResponseDataTargetCollaborationFreeSampleRule.from_dict(_free_sample_rule)




        type_ = d.pop("type", UNSET)

        search_target_collaborations_response_data_target_collaboration = cls(
            id=id,
            name=name,
            message=message,
            start_time=start_time,
            end_time=end_time,
            create_time=create_time,
            update_time=update_time,
            creator_inivited_count=creator_inivited_count,
            showcase_creator_count=showcase_creator_count,
            content_creator_count=content_creator_count,
            product_count=product_count,
            free_sample_rule=free_sample_rule,
            type_=type_,
        )


        search_target_collaborations_response_data_target_collaboration.additional_properties = d
        return search_target_collaborations_response_data_target_collaboration

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
