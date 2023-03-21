from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.status_flag import StatusFlag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.entity_update_data_type_0 import EntityUpdateDataType0


T = TypeVar("T", bound="EntityUpdate")


@attr.s(auto_attribs=True)
class EntityUpdate:
    """
    Attributes:
        uuid (str):
        data (Union['EntityUpdateDataType0', List[Any], Unset]):
        status (Union[Unset, StatusFlag]): To check if a user has a flag, use bitmasking:

            Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.
        schema (Union[Unset, str]):
    """

    uuid: str
    data: Union["EntityUpdateDataType0", List[Any], Unset] = UNSET
    status: Union[Unset, StatusFlag] = UNSET
    schema: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.entity_update_data_type_0 import EntityUpdateDataType0

        uuid = self.uuid
        data: Union[Dict[str, Any], List[Any], Unset]
        if isinstance(self.data, Unset):
            data = UNSET

        elif isinstance(self.data, EntityUpdateDataType0):
            data = UNSET
            if not isinstance(self.data, Unset):
                data = self.data.to_dict()

        else:
            data = UNSET
            if not isinstance(self.data, Unset):
                data = self.data

        status: Union[Unset, int] = UNSET
        if not isinstance(self.status, Unset):
            status = self.status.value

        schema = self.schema

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "uuid": uuid,
            }
        )
        if data is not UNSET:
            field_dict["data"] = data
        if status is not UNSET:
            field_dict["status"] = status
        if schema is not UNSET:
            field_dict["schema"] = schema

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.entity_update_data_type_0 import EntityUpdateDataType0

        d = src_dict.copy()
        uuid = d.pop("uuid")

        def _parse_data(data: object) -> Union["EntityUpdateDataType0", List[Any], Unset]:
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                _data_type_0 = data
                data_type_0: Union[Unset, EntityUpdateDataType0]
                if isinstance(_data_type_0, Unset):
                    data_type_0 = UNSET
                else:
                    data_type_0 = EntityUpdateDataType0.from_dict(_data_type_0)

                return data_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, list):
                raise TypeError()
            data_type_1 = cast(List[Any], data)

            return data_type_1

        data = _parse_data(d.pop("data", UNSET))

        _status = d.pop("status", UNSET)
        status: Union[Unset, StatusFlag]
        if isinstance(_status, Unset):
            status = UNSET
        else:
            status = StatusFlag(_status)

        schema = d.pop("schema", UNSET)

        entity_update = cls(
            uuid=uuid,
            data=data,
            status=status,
            schema=schema,
        )

        entity_update.additional_properties = d
        return entity_update

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
