import pytest

# ========================================================================
# PYTEST + PLAYWRIGHT TEST CONFIGURATION FILE
# ========================================================================


def pytest_addoption(parser):
    parser.addoption(
        "--framework-video",
        dest="framework_video",
        default="retain-on-failure",
        help="Record video: on, off, retain-on-failure",
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    setattr(item, f"rep_{report.when}", report)
