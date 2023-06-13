from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.user_read import UserRead
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: AuthenticatedClient,
    pattern: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    order: Union[Unset, None, str] = UNSET,
    descending: Union[Unset, None, bool] = False,
    is_active: Union[Unset, None, bool] = UNSET,
    is_verified: Union[Unset, None, bool] = UNSET,
    is_employee: Union[Unset, None, bool] = UNSET,
    is_admin: Union[Unset, None, bool] = UNSET,
) -> Dict[str, Any]:
    url = "{}/v1/users/".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["pattern"] = pattern

    params["limit"] = limit

    params["offset"] = offset

    params["order"] = order

    params["descending"] = descending

    params["is_active"] = is_active

    params["is_verified"] = is_verified

    params["is_employee"] = is_employee

    params["is_admin"] = is_admin

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
) -> Optional[Union[Any, HTTPValidationError, List["UserRead"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = UserRead.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == HTTPStatus.FORBIDDEN:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, HTTPValidationError, List["UserRead"]]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    pattern: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    order: Union[Unset, None, str] = UNSET,
    descending: Union[Unset, None, bool] = False,
    is_active: Union[Unset, None, bool] = UNSET,
    is_verified: Union[Unset, None, bool] = UNSET,
    is_employee: Union[Unset, None, bool] = UNSET,
    is_admin: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, HTTPValidationError, List["UserRead"]]]:
    """Users:List Users

    Args:
        pattern (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 100.
        offset (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        descending (Union[Unset, None, bool]):
        is_active (Union[Unset, None, bool]):
        is_verified (Union[Unset, None, bool]):
        is_employee (Union[Unset, None, bool]):
        is_admin (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['UserRead']]]
    """

    kwargs = _get_kwargs(
        client=client,
        pattern=pattern,
        limit=limit,
        offset=offset,
        order=order,
        descending=descending,
        is_active=is_active,
        is_verified=is_verified,
        is_employee=is_employee,
        is_admin=is_admin,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    pattern: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    order: Union[Unset, None, str] = UNSET,
    descending: Union[Unset, None, bool] = False,
    is_active: Union[Unset, None, bool] = UNSET,
    is_verified: Union[Unset, None, bool] = UNSET,
    is_employee: Union[Unset, None, bool] = UNSET,
    is_admin: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, List["UserRead"]]]:
    """Users:List Users

    Args:
        pattern (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 100.
        offset (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        descending (Union[Unset, None, bool]):
        is_active (Union[Unset, None, bool]):
        is_verified (Union[Unset, None, bool]):
        is_employee (Union[Unset, None, bool]):
        is_admin (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['UserRead']]]
    """

    return sync_detailed(
        client=client,
        pattern=pattern,
        limit=limit,
        offset=offset,
        order=order,
        descending=descending,
        is_active=is_active,
        is_verified=is_verified,
        is_employee=is_employee,
        is_admin=is_admin,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    pattern: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    order: Union[Unset, None, str] = UNSET,
    descending: Union[Unset, None, bool] = False,
    is_active: Union[Unset, None, bool] = UNSET,
    is_verified: Union[Unset, None, bool] = UNSET,
    is_employee: Union[Unset, None, bool] = UNSET,
    is_admin: Union[Unset, None, bool] = UNSET,
) -> Response[Union[Any, HTTPValidationError, List["UserRead"]]]:
    """Users:List Users

    Args:
        pattern (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 100.
        offset (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        descending (Union[Unset, None, bool]):
        is_active (Union[Unset, None, bool]):
        is_verified (Union[Unset, None, bool]):
        is_employee (Union[Unset, None, bool]):
        is_admin (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['UserRead']]]
    """

    kwargs = _get_kwargs(
        client=client,
        pattern=pattern,
        limit=limit,
        offset=offset,
        order=order,
        descending=descending,
        is_active=is_active,
        is_verified=is_verified,
        is_employee=is_employee,
        is_admin=is_admin,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    pattern: Union[Unset, None, str] = UNSET,
    limit: Union[Unset, None, int] = 100,
    offset: Union[Unset, None, int] = 0,
    order: Union[Unset, None, str] = UNSET,
    descending: Union[Unset, None, bool] = False,
    is_active: Union[Unset, None, bool] = UNSET,
    is_verified: Union[Unset, None, bool] = UNSET,
    is_employee: Union[Unset, None, bool] = UNSET,
    is_admin: Union[Unset, None, bool] = UNSET,
) -> Optional[Union[Any, HTTPValidationError, List["UserRead"]]]:
    """Users:List Users

    Args:
        pattern (Union[Unset, None, str]):
        limit (Union[Unset, None, int]):  Default: 100.
        offset (Union[Unset, None, int]):
        order (Union[Unset, None, str]):
        descending (Union[Unset, None, bool]):
        is_active (Union[Unset, None, bool]):
        is_verified (Union[Unset, None, bool]):
        is_employee (Union[Unset, None, bool]):
        is_admin (Union[Unset, None, bool]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError, List['UserRead']]]
    """

    return (
        await asyncio_detailed(
            client=client,
            pattern=pattern,
            limit=limit,
            offset=offset,
            order=order,
            descending=descending,
            is_active=is_active,
            is_verified=is_verified,
            is_employee=is_employee,
            is_admin=is_admin,
        )
    ).parsed
