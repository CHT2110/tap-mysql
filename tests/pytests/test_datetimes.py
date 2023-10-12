"""
    Test dates and datetimes are handled correctly.
    The timezone environment variable, TZ, somehow affects the behaviour of to_utc_datetime_str,
    and TZ is set on
"""

from tap_mysql.sync_strategies.common import to_utc_datetime_str
from datetime import datetime
from unittest import mock
import pytest
import os


@pytest.mark.parametrize(
    ("TZ", "expected", "the_datetime"),
    [
        ("", "2000-01-01T22:00:00.000000Z", datetime(2000, 1, 1)),
        ("UTC", "2000-01-01T00:00:00.000000Z", datetime(2000, 1, 1)),
        ("", "0001-01-01T22:00:00.000000Z", datetime(1, 1, 1)),
        ("UTC", "0001-01-01T22:00:00.000000Z", datetime(1, 1, 1)),
    ]
)
def test_to_utc_datetime_str(TZ, expected, the_datetime):
    with mock.patch.dict(os.environ, {"TZ": TZ}):
        # within this context manager the environment variable is TZ is set
        
        assert expected == to_utc_datetime_str(the_datetime)