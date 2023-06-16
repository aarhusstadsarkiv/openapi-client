from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.bearer_response import BearerResponse
from ...models.body_auth_db_bearer_login_v1_auth_jwt_login_post import BodyAuthDbBearerLoginV1AuthJwtLoginPost
from ...models.error_model import ErrorModel
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    form_data: BodyAuthDbBearerLoginV1AuthJwtLoginPost,
) -> Dict[str, Any]:
    url = "{}/v1/auth/jwt/login".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "follow_redirects": client.follow_redirects,
        "data": form_data.to_dict(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[BearerResponse, ErrorModel, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = BearerResponse.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = ErrorModel.from_dict(response.json())

        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[BearerResponse, ErrorModel, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    form_data: BodyAuthDbBearerLoginV1AuthJwtLoginPost,
) -> Response[Union[BearerResponse, ErrorModel, HTTPValidationError]]:
    """Auth:Db Bearer.Login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BearerResponse, ErrorModel, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    form_data: BodyAuthDbBearerLoginV1AuthJwtLoginPost,
) -> Optional[Union[BearerResponse, ErrorModel, HTTPValidationError]]:
    """Auth:Db Bearer.Login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BearerResponse, ErrorModel, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        form_data=form_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    form_data: BodyAuthDbBearerLoginV1AuthJwtLoginPost,
) -> Response[Union[BearerResponse, ErrorModel, HTTPValidationError]]:
    """Auth:Db Bearer.Login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[BearerResponse, ErrorModel, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        client=client,
        form_data=form_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    form_data: BodyAuthDbBearerLoginV1AuthJwtLoginPost,
) -> Optional[Union[BearerResponse, ErrorModel, HTTPValidationError]]:
    """Auth:Db Bearer.Login

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[BearerResponse, ErrorModel, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            form_data=form_data,
        )
    ).parsed
