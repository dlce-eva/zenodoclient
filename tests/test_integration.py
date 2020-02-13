import os
import pytest
import warnings
from urllib3.exceptions import InsecurePlatformWarning, SNIMissingWarning

import zenodoclient
from zenodoclient.api import Zenodo, API_URL_SANDBOX

warnings.simplefilter('ignore', SNIMissingWarning)
warnings.simplefilter('ignore', InsecurePlatformWarning)


def test_api():
    at = os.environ.get('ZENODO_SANDBOX_ACCESS_TOKEN')
    if not at:
        return
    api = Zenodo(api_url=API_URL_SANDBOX, access_token=at)
    dep = api.create(title='title', creators=[{'name': 'Doe, John'}],
                     description='desc')
    assert dep.metadata.title == 'title'
    dep = api.update(dep, title='other')
    assert dep.metadata.title == 'other'
    with pytest.raises(ValueError):
        api.publish(dep)
    files = list(api.create_files(dep, __file__, zenodoclient.api.__file__))
    dep = api.publish(dep)
    api.update(dep, title='abc other')
    dep = api.edit(dep)
    with pytest.raises(ValueError):
        api.create_file(dep, zenodoclient.__file__)
    api.update(dep, title='abc other')
