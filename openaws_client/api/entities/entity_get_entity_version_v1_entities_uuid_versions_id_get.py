from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_read import EntityRead
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Dict[str, Any]:
    url = "{}/v1/entities/{uuid}/versions/{id}".format(client.base_url, uuid=uuid, id=id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, EntityRead, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = EntityRead.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.NOT_FOUND:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, EntityRead, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, EntityRead, HTTPValidationError]]:
    """Entity:Get Entity Version

    Args:
        uuid (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntityRead, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, EntityRead, HTTPValidationError]]:
    """Entity:Get Entity Version

    Args:
        uuid (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntityRead, HTTPValidationError]]
    """

    return sync_detailed(
        uuid=uuid,
        id=id,
        client=client,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Response[Union[Any, EntityRead, HTTPValidationError]]:
    """Entity:Get Entity Version

    Args:
        uuid (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntityRead, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        id=id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    id: int,
    *,
    client: AuthenticatedClient,
) -> Optional[Union[Any, EntityRead, HTTPValidationError]]:
    """Entity:Get Entity Version

    Args:
        uuid (str):
        id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, EntityRead, HTTPValidationError]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            id=id,
            client=client,
        )
    ).parsed
