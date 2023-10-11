test:
	SINGER_TAP_MYSQL_TEST_DB_HOST=localhost SINGER_TAP_MYSQL_TEST_DB_PORT=3306 SINGER_TAP_MYSQL_TEST_DB_USER=root SINGER_TAP_MYSQL_TEST_DB_PASSWORD=password nosetests

# many test require the closed source dependency 'tap_tester', this excludes those
pytest:
	pytest --ignore=tests tests/pytests/test_datetimes.py
