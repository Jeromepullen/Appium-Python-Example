# conftest.py

import pytest

def pytest_html_report_title(report):
    report.title = "iOS App Test Report"
