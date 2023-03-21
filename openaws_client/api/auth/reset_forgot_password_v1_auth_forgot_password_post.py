from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.body_reset_forgot_password_v1_auth_forgot_password_post import (
    BodyResetForgotPasswordV1AuthForgotPasswordPost,
)
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: BodyResetForgotPasswordV1AuthForgotPasswordPost,
) -> Dict[str, Any]:
    url = "{}/v1/auth/forgot-password".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.ACCEPTED:
        response_202 = cast(Any, response.json())
        return response_202
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: BodyResetForgotPasswordV1AuthForgotPasswordPost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Reset:Forgot Password

    Args:
        json_body (BodyResetForgotPasswordV1AuthForgotPasswordPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: BodyResetForgotPasswordV1AuthForgotPasswordPost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Reset:Forgot Password

    Args:
        json_body (BodyResetForgotPasswordV1AuthForgotPasswordPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: BodyResetForgotPasswordV1AuthForgotPasswordPost,
) -> Response[Union[Any, HTTPValidationError]]:
    """Reset:Forgot Password

    Args:
        json_body (BodyResetForgotPasswordV1AuthForgotPasswordPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: BodyResetForgotPasswordV1AuthForgotPasswordPost,
) -> Optional[Union[Any, HTTPValidationError]]:
    """Reset:Forgot Password

    Args:
        json_body (BodyResetForgotPasswordV1AuthForgotPasswordPost):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
