# coding: utf8
from __future__ import unicode_literals, print_function, division
import os
import warnings

from urllib3.exceptions import InsecurePlatformWarning, SNIMissingWarning
import pytest

import zenodoclient
from zenodoclient.api import Zenodo, API_URL_SANDBOX

warnings.simplefilter('ignore', SNIMissingWarning)
warnings.simplefilter('ignore', InsecurePlatformWarning)


@pytest.mark.sandbox
def test_api():
    api = Zenodo(
        api_url=API_URL_SANDBOX, access_token=os.environ['ZENODO_SANDBOX_ACCESS_TOKEN'])
    dep = api.create(title='title', creators=[{'name': 'Doe, John'}], description='desc')
    assert dep.metadata.title == 'title'
    dep = api.update(dep, title='other')
    assert dep.metadata.title == 'other'
    with pytest.raises(ValueError):
        api.publish(dep)
    files = list(api.create_files(dep, __file__, zenodoclient.api.__file__))
    f = api.retrieve_file(dep, files[0])
    assert len(api.list_files(dep)) == 2
    api.sort_files(dep, [files[1], files[0]])
    assert dep.files[-1].filename.startswith('test_integration')
    api.update_file(dep, f, 'fname')
    api.delete_file(dep, f)
    assert len(api.list_files(dep)) == 1
    dep = api.publish(dep)
    api.update(dep, title='abc other')
    dep = api.edit(dep)
    with pytest.raises(ValueError):
        api.create_file(dep, zenodoclient.__file__)
    api.update(dep, title='abc other')
