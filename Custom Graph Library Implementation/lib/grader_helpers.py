def assert_equal(actual, expected) -> None:
    if actual != expected:
        raise AssertionError(f"Expected {expected}, but got {actual}")

def assert_true(condition: bool) -> None:
    if not condition:
        raise AssertionError("Expected True, but got False")

def assert_false(condition: bool) -> None:
    if condition:
        raise AssertionError("Expected False, but got True")
