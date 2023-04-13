import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr
from dateutil.parser import isoparse

from ..models.status_flag import StatusFlag

if TYPE_CHECKING:
    from ..models.entity_read_data_type_0 import EntityReadDataType0


T = TypeVar("T", bound="EntityRead")


@attr.s(auto_attribs=True)
class EntityRead:
    """
    Example:
        {'data': {'label': 'My entity', 'title': 'My entity title', 'from_date': '2020-01-01', 'to_date': '2020-01-01'},
            'schema_name': 'person_1'}

    Attributes:
        data (Union['EntityReadDataType0', List[Any]]):
        schema_name (str):
        id (int):
        uuid (str):
        status (StatusFlag): To check if a user has a flag, use bitmasking:

            Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.
        timestamp (datetime.datetime):
        created_by_id (str):
        updated_by_id (str):
        is_soft_deleted (bool):
        is_hard_deleted (bool):
    """

    data: Union["EntityReadDataType0", List[Any]]
    schema_name: str
    id: int
    uuid: str
    status: StatusFlag
    timestamp: datetime.datetime
    created_by_id: str
    updated_by_id: str
    is_soft_deleted: bool
    is_hard_deleted: bool
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.entity_read_data_type_0 import EntityReadDataType0

        data: Union[Dict[str, Any], List[Any]]

        if isinstance(self.data, EntityReadDataType0):
            data = self.data.to_dict()

        else:
            data = self.data

        schema_name = self.schema_name
        id = self.id
        uuid = self.uuid
        status = self.status.value

        timestamp = self.timestamp.isoformat()

        created_by_id = self.created_by_id
        updated_by_id = self.updated_by_id
        is_soft_deleted = self.is_soft_deleted
        is_hard_deleted = self.is_hard_deleted

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "schema_name": schema_name,
                "id": id,
                "uuid": uuid,
                "status": status,
                "timestamp": timestamp,
                "created_by_id": created_by_id,
                "updated_by_id": updated_by_id,
                "is_soft_deleted": is_soft_deleted,
                "is_hard_deleted": is_hard_deleted,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_read_data_type_0 import EntityReadDataType0

        d = src_dict.copy()

        def _parse_data(data: object) -> Union["EntityReadDataType0", List[Any]]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = EntityReadDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = cast(List[Any], data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        schema_name = d.pop("schema_name")

        id = d.pop("id")

        uuid = d.pop("uuid")

        status = StatusFlag(d.pop("status"))

        timestamp = isoparse(d.pop("timestamp"))

        created_by_id = d.pop("created_by_id")

        updated_by_id = d.pop("updated_by_id")

        is_soft_deleted = d.pop("is_soft_deleted")

        is_hard_deleted = d.pop("is_hard_deleted")

        entity_read = cls(
            data=data,
            schema_name=schema_name,
            id=id,
            uuid=uuid,
            status=status,
            timestamp=timestamp,
            created_by_id=created_by_id,
            updated_by_id=updated_by_id,
            is_soft_deleted=is_soft_deleted,
            is_hard_deleted=is_hard_deleted,
        )

        entity_read.additional_properties = d
        return entity_read

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
