from h5dantic import HDFModel


class _TestModel(HDFModel):
    a: int


def _test_constructability() -> None:
    m = _TestModel(a=1)
    assert m is not None
