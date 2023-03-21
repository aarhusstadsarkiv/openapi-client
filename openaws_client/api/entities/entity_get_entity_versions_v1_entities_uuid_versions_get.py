from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.entity_version_read import EntityVersionRead
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/v1/entities/{uuid}/versions".format(client.base_url, uuid=uuid)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["limit"] = limit

    params["offset"] = offset

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError, List["EntityVersionRead"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = EntityVersionRead.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[Any, HTTPValidationError, List["EntityVersionRead"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Response[Union[Any, HTTPValidationError, List["EntityVersionRead"]]]:
    """Entity:Get Entity Versions

    Args:
        uuid (str):
        limit (Union[Unset, None, int]):  Default: 10.
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['EntityVersionRead']]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        limit=limit,
        offset=offset,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, HTTPValidationError, List["EntityVersionRead"]]]:
    """Entity:Get Entity Versions

    Args:
        uuid (str):
        limit (Union[Unset, None, int]):  Default: 10.
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['EntityVersionRead']]]
    """

    return sync_detailed(
        uuid=uuid,
        client=client,
        limit=limit,
        offset=offset,
    ).parsed


async def asyncio_detailed(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Response[Union[Any, HTTPValidationError, List["EntityVersionRead"]]]:
    """Entity:Get Entity Versions

    Args:
        uuid (str):
        limit (Union[Unset, None, int]):  Default: 10.
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['EntityVersionRead']]]
    """

    kwargs = _get_kwargs(
        uuid=uuid,
        client=client,
        limit=limit,
        offset=offset,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    uuid: str,
    *,
    client: AuthenticatedClient,
    limit: Union[Unset, None, int] = 10,
    offset: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, HTTPValidationError, List["EntityVersionRead"]]]:
    """Entity:Get Entity Versions

    Args:
        uuid (str):
        limit (Union[Unset, None, int]):  Default: 10.
        offset (Union[Unset, None, int]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['EntityVersionRead']]]
    """

    return (
        await asyncio_detailed(
            uuid=uuid,
            client=client,
            limit=limit,
            offset=offset,
        )
    ).parsed
