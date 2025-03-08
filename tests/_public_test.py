import h5dantic


def test_magic_string() -> None:
    assert h5dantic.hello() == "Hello from h5dantic!"
