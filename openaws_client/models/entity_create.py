from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

if TYPE_CHECKING:
    from ..models.entity_create_data_type_0 import EntityCreateDataType0


T = TypeVar("T", bound="EntityCreate")


@attr.s(auto_attribs=True)
class EntityCreate:
    """
    Example:
        {'data': {'label': 'My entity', 'title': 'My entity title', 'from_date': '2020-01-01', 'to_date': '2020-01-01'},
            'schema_name': 'person_1'}

    Attributes:
        data (Union['EntityCreateDataType0', List[Any]]):
        schema_name (str):
    """

    data: Union["EntityCreateDataType0", List[Any]]
    schema_name: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.entity_create_data_type_0 import EntityCreateDataType0

        data: Union[Dict[str, Any], List[Any]]

        if isinstance(self.data, EntityCreateDataType0):
            data = self.data.to_dict()

        else:
            data = self.data

        schema_name = self.schema_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "data": data,
                "schema_name": schema_name,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_create_data_type_0 import EntityCreateDataType0

        d = src_dict.copy()

        def _parse_data(data: object) -> Union["EntityCreateDataType0", List[Any]]:
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                data_type_0 = EntityCreateDataType0.from_dict(data)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = cast(List[Any], data)

            return data_type_1

        data = _parse_data(d.pop("data"))

        schema_name = d.pop("schema_name")

        entity_create = cls(
            data=data,
            schema_name=schema_name,
        )

        entity_create.additional_properties = d
        return entity_create

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
