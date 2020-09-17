from subprocess import check_call


def mypy_task():
    check_call(["mypy", "--ignore-missing-imports", "src/"])


def bp_tests():
    check_call(["pytest", "tests/bptest/"])


def endpoint_tests():
    check_call(["pytest", "tests/endpoints/"])


def coverage_task():
    check_call(["coverage", "run", "-m", "--source", "src/", "pytest", "-s"])
    check_call(["coverage", "html"])
