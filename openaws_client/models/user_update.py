from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_flag import UserFlag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_permissions import UserPermissions
    from ..models.user_update_data import UserUpdateData


T = TypeVar("T", bound="UserUpdate")


@attr.s(auto_attribs=True)
class UserUpdate:
    """
    Attributes:
        password (Union[Unset, str]):
        email (Union[Unset, str]):
        is_active (Union[Unset, bool]):
        is_superuser (Union[Unset, bool]):
        is_verified (Union[Unset, bool]):
        data (Union[Unset, UserUpdateData]):
        permissions (Union[Unset, UserPermissions]):
        flags (Union[Unset, UserFlag]): To check if a user has a flag, use bitmasking:
            >>> assert user.flags & UserFlag.EMPLOYEE
            Add a flag:
            >>> user.flags |= UserFlag.EMPLOYEE
            Remove a flag:
            >>> user.flags &= ~UserFlag.EMPLOYEE

            Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.
    """

    password: Union[Unset, str] = UNSET
    email: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = UNSET
    is_superuser: Union[Unset, bool] = UNSET
    is_verified: Union[Unset, bool] = UNSET
    data: Union[Unset, "UserUpdateData"] = UNSET
    permissions: Union[Unset, "UserPermissions"] = UNSET
    flags: Union[Unset, UserFlag] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        password = self.password
        email = self.email
        is_active = self.is_active
        is_superuser = self.is_superuser
        is_verified = self.is_verified
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        permissions: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.permissions, Unset):
            permissions = self.permissions.to_dict()

        flags: Union[Unset, int] = UNSET
        if not isinstance(self.flags, Unset):
            flags = self.flags.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if password is not UNSET:
            field_dict["password"] = password
        if email is not UNSET:
            field_dict["email"] = email
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified
        if data is not UNSET:
            field_dict["data"] = data
        if permissions is not UNSET:
            field_dict["permissions"] = permissions
        if flags is not UNSET:
            field_dict["flags"] = flags

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_permissions import UserPermissions
        from ..models.user_update_data import UserUpdateData

        d = src_dict.copy()
        password = d.pop("password", UNSET)

        email = d.pop("email", UNSET)

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        _data = d.pop("data", UNSET)
        data: Union[Unset, UserUpdateData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = UserUpdateData.from_dict(_data)

        _permissions = d.pop("permissions", UNSET)
        permissions: Union[Unset, UserPermissions]
        if isinstance(_permissions, Unset):
            permissions = UNSET
        else:
            permissions = UserPermissions.from_dict(_permissions)

        _flags = d.pop("flags", UNSET)
        flags: Union[Unset, UserFlag]
        if isinstance(_flags, Unset):
            flags = UNSET
        else:
            flags = UserFlag(_flags)

        user_update = cls(
            password=password,
            email=email,
            is_active=is_active,
            is_superuser=is_superuser,
            is_verified=is_verified,
            data=data,
            permissions=permissions,
            flags=flags,
        )

        user_update.additional_properties = d
        return user_update

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
