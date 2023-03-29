from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="UserPermissions")


@attr.s(auto_attribs=True)
class UserPermissions:
    """
    Attributes:
        guest (Union[Unset, bool]):
        basic (Union[Unset, bool]):
        employee (Union[Unset, bool]):
        admin (Union[Unset, bool]):
    """

    guest: Union[Unset, bool] = False
    basic: Union[Unset, bool] = False
    employee: Union[Unset, bool] = False
    admin: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        guest = self.guest
        basic = self.basic
        employee = self.employee
        admin = self.admin

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if guest is not UNSET:
            field_dict["guest"] = guest
        if basic is not UNSET:
            field_dict["basic"] = basic
        if employee is not UNSET:
            field_dict["employee"] = employee
        if admin is not UNSET:
            field_dict["admin"] = admin

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        guest = d.pop("guest", UNSET)

        basic = d.pop("basic", UNSET)

        employee = d.pop("employee", UNSET)

        admin = d.pop("admin", UNSET)

        user_permissions = cls(
            guest=guest,
            basic=basic,
            employee=employee,
            admin=admin,
        )

        user_permissions.additional_properties = d
        return user_permissions

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
