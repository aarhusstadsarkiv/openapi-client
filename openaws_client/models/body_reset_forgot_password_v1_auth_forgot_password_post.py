from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="BodyResetForgotPasswordV1AuthForgotPasswordPost")


@attr.s(auto_attribs=True)
class BodyResetForgotPasswordV1AuthForgotPasswordPost:
    """
    Attributes:
        email (str):
    """

    email: str
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        email = self.email

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "email": email,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        email = d.pop("email")

        body_reset_forgot_password_v1_auth_forgot_password_post = cls(
            email=email,
        )

        body_reset_forgot_password_v1_auth_forgot_password_post.additional_properties = d
        return body_reset_forgot_password_v1_auth_forgot_password_post

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
