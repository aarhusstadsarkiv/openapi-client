from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar

import attr

if TYPE_CHECKING:
    from ..models.user_permissions import UserPermissions


T = TypeVar("T", bound="UserUpdatePermissions")


@attr.s(auto_attribs=True)
class UserUpdatePermissions:
    """Used to update user permissions.

    Attributes:
        permissions (UserPermissions):
    """

    permissions: "UserPermissions"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        permissions = self.permissions.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "permissions": permissions,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.user_permissions import UserPermissions

        d = src_dict.copy()
        permissions = UserPermissions.from_dict(d.pop("permissions"))

        user_update_permissions = cls(
            permissions=permissions,
        )

        user_update_permissions.additional_properties = d
        return user_update_permissions

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
