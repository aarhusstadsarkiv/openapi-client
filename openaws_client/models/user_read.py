from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.user_flag import UserFlag
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.user_permissions import UserPermissions
    from ..models.user_read_data import UserReadData


T = TypeVar("T", bound="UserRead")


@attr.s(auto_attribs=True)
class UserRead:
    """Base User model.

    Attributes:
        id (str):
        email (str):
        data (UserReadData):
        permissions (UserPermissions):
        flags (UserFlag): To check if a user has a flag, use bitmasking:
            >>> assert user.flags & UserFlag.EMPLOYEE
            Add a flag:
            >>> user.flags |= UserFlag.EMPLOYEE
            Remove a flag:
            >>> user.flags &= ~UserFlag.EMPLOYEE.

            Maximum 64 bit because BigInt = 8 bytes, so we can only have 64 distinct flags.
        is_active (Union[Unset, bool]):  Default: True.
        is_superuser (Union[Unset, bool]):
        is_verified (Union[Unset, bool]):
    """

    id: str
    email: str
    data: "UserReadData"
    permissions: "UserPermissions"
    flags: UserFlag
    is_active: Union[Unset, bool] = True
    is_superuser: Union[Unset, bool] = False
    is_verified: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id
        email = self.email
        data = self.data.to_dict()

        permissions = self.permissions.to_dict()

        flags = self.flags.value

        is_active = self.is_active
        is_superuser = self.is_superuser
        is_verified = self.is_verified

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "email": email,
                "data": data,
                "permissions": permissions,
                "flags": flags,
            }
        )
        if is_active is not UNSET:
            field_dict["is_active"] = is_active
        if is_superuser is not UNSET:
            field_dict["is_superuser"] = is_superuser
        if is_verified is not UNSET:
            field_dict["is_verified"] = is_verified

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_permissions import UserPermissions
        from ..models.user_read_data import UserReadData

        d = src_dict.copy()
        id = d.pop("id")

        email = d.pop("email")

        data = UserReadData.from_dict(d.pop("data"))

        permissions = UserPermissions.from_dict(d.pop("permissions"))

        flags = UserFlag(d.pop("flags"))

        is_active = d.pop("is_active", UNSET)

        is_superuser = d.pop("is_superuser", UNSET)

        is_verified = d.pop("is_verified", UNSET)

        user_read = cls(
            id=id,
            email=email,
            data=data,
            permissions=permissions,
            flags=flags,
            is_active=is_active,
            is_superuser=is_superuser,
            is_verified=is_verified,
        )

        user_read.additional_properties = d
        return user_read

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
