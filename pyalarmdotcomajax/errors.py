"""Exceptions."""
from __future__ import annotations


class UnsupportedDevice(Exception):
    """pyalarmdotcomajax encountered a device not currently supported by the package."""


class AuthenticationFailed(Exception):
    """Alarm.com authentication failure."""


class DataFetchFailed(Exception):
    """General or connection error encountered when fetching data."""


class UnexpectedDataStructure(Exception):
    """Successfully received JSON object, but format is not as expected."""


class BadAccount(Exception):
    """Account can't lock in or major permissions issue."""


class DeviceTypeNotAuthorized(Exception):
    """Account does not have access to a specific device type."""
