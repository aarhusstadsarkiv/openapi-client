import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr
from dateutil.parser import isoparse

if TYPE_CHECKING:
    from ..models.schema_read_data import SchemaReadData


T = TypeVar("T", bound="SchemaRead")


@attr.s(auto_attribs=True)
class SchemaRead:
    """
    Attributes:
        type (str):
        data (SchemaReadData):
        name (str):
        version (int):
        created_by_id (str):
        timestamp (datetime.datetime):
    """

    type: str
    data: "SchemaReadData"
    name: str
    version: int
    created_by_id: str
    timestamp: datetime.datetime
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        data = self.data.to_dict()

        name = self.name
        version = self.version
        created_by_id = self.created_by_id
        timestamp = self.timestamp.isoformat()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "data": data,
                "name": name,
                "version": version,
                "created_by_id": created_by_id,
                "timestamp": timestamp,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_read_data import SchemaReadData

        d = src_dict.copy()
        type = d.pop("type")

        data = SchemaReadData.from_dict(d.pop("data"))

        name = d.pop("name")

        version = d.pop("version")

        created_by_id = d.pop("created_by_id")

        timestamp = isoparse(d.pop("timestamp"))

        schema_read = cls(
            type=type,
            data=data,
            name=name,
            version=version,
            created_by_id=created_by_id,
            timestamp=timestamp,
        )

        schema_read.additional_properties = d
        return schema_read

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
