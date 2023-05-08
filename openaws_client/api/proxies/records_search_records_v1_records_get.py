from http import HTTPStatus
from typing import Any, Dict, Optional, Union, cast

import httpx

from ... import errors
from ...client import Client
from ...models.records_search_records_v1_records_get_response_records_search_records_v1_records_get import (
    RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet,
)
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/v1/records".format(client.base_url)

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
) -> Optional[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet.from_dict(
            response.json()
        )

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = cast(Any, None)
        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]:
    """Records:Search Records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]:
    """Records:Search Records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]:
    """Records:Search Records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]:
    """Records:Search Records

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, RecordsSearchRecordsV1RecordsGetResponseRecordsSearchRecordsV1RecordsGet]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
