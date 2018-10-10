import pytest
from pathlib import Path

from zenodoclient.util import md5


@pytest.fixture(scope='session')
def test_file(tmpdir_factory):
    s = "Some string to test md5sum."
    fn = str(tmpdir_factory.mktemp('test').join('test_md5.txt'))

    with open(fn, 'w') as f:
        f.write(s)

    return Path(fn)


def test_md5(test_file):
    assert md5(test_file) == '9a9d595f500c823df5555e77c8c7398d'
