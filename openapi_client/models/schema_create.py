from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.schema_create_data import SchemaCreateData


T = TypeVar("T", bound="SchemaCreate")


@attr.s(auto_attribs=True)
class SchemaCreate:
    """
    Attributes:
        type (str):
        data (SchemaCreateData):
    """

    type: str
    data: "SchemaCreateData"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        type = self.type
        data = self.data.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type,
                "data": data,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.schema_create_data import SchemaCreateData

        d = src_dict.copy()
        type = d.pop("type")

        data = SchemaCreateData.from_dict(d.pop("data"))

        schema_create = cls(
            type=type,
            data=data,
        )

        schema_create.additional_properties = d
        return schema_create

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
