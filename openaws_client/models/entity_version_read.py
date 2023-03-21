import datetime
from typing import Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

from ..models.status_flag import StatusFlag

T = TypeVar("T", bound="EntityVersionRead")


@attr.s(auto_attribs=True)
class EntityVersionRead:
    """
    Attributes:
        id (int):
        uuid (str):
        status (StatusFlag): To check if a user has a flag, use bitmasking:

            Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.
        schema (str):
        timestamp (datetime.datetime):
        updated_by_id (str):
        is_soft_deleted (bool):
        is_hard_deleted (bool):
    """

    id: int
    uuid: str
    status: StatusFlag
    schema: str
    timestamp: datetime.datetime
    updated_by_id: str
    is_soft_deleted: bool
    is_hard_deleted: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        uuid = self.uuid
        status = self.status.value

        schema = self.schema
        timestamp = self.timestamp.isoformat()

        updated_by_id = self.updated_by_id
        is_soft_deleted = self.is_soft_deleted
        is_hard_deleted = self.is_hard_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "uuid": uuid,
                "status": status,
                "schema": schema,
                "timestamp": timestamp,
                "updated_by_id": updated_by_id,
                "is_soft_deleted": is_soft_deleted,
                "is_hard_deleted": is_hard_deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        uuid = d.pop("uuid")

        status = StatusFlag(d.pop("status"))

        schema = d.pop("schema")

        timestamp = isoparse(d.pop("timestamp"))

        updated_by_id = d.pop("updated_by_id")

        is_soft_deleted = d.pop("is_soft_deleted")

        is_hard_deleted = d.pop("is_hard_deleted")

        entity_version_read = cls(
            id=id,
            uuid=uuid,
            status=status,
            schema=schema,
            timestamp=timestamp,
            updated_by_id=updated_by_id,
            is_soft_deleted=is_soft_deleted,
            is_hard_deleted=is_hard_deleted,
        )

        entity_version_read.additional_properties = d
        return entity_version_read

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
