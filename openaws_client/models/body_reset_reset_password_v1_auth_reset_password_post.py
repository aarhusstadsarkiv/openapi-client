from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BodyResetResetPasswordV1AuthResetPasswordPost")


@attr.s(auto_attribs=True)
class BodyResetResetPasswordV1AuthResetPasswordPost:
    """
    Attributes:
        token (str):
        password (str):
    """

    token: str
    password: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        token = self.token
        password = self.password

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "token": token,
                "password": password,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        token = d.pop("token")

        password = d.pop("password")

        body_reset_reset_password_v1_auth_reset_password_post = cls(
            token=token,
            password=password,
        )

        body_reset_reset_password_v1_auth_reset_password_post.additional_properties = d
        return body_reset_reset_password_v1_auth_reset_password_post

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
