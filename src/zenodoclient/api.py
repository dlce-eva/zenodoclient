"""
http://developers.zenodo.org/
"""
import json
import os
import pathlib
import requests
import warnings
from http.client import responses as http_status
from urllib3.exceptions import InsecurePlatformWarning, SNIMissingWarning

from zenodoclient.models import Deposition, DepositionFile, PUBLISHED, \
    UNSUBMITTED
from zenodoclient.util import md5

warnings.simplefilter('once', SNIMissingWarning)
warnings.simplefilter('once', InsecurePlatformWarning)

API_URL = 'https://zenodo.org/api/'
API_URL_SANDBOX = 'https://sandbox.zenodo.org/api/'
ACCESS_TOKEN = os.environ.get('ZENODO_ACCESS_TOKEN')


class ApiError(Exception):
    def __init__(self, status, details=None):
        msg = '{0} {1}'.format(status, http_status[status])
        if details and 'message' in details:
            msg += ': {0}'.format(details['message'])
        self.errors = details.get('errors') if details else None
        Exception.__init__(self, msg)


class Zenodo(object):
    def __init__(self, access_token=ACCESS_TOKEN, api_url=API_URL):
        self._access_token = access_token
        self._api_url = api_url

    def _req(self, method, path='', prefix='deposit/depositions', expected=200, **kw):
        """
        http://developers.zenodo.org/#requests
        http://developers.zenodo.org/#responses
        """
        if path and not path.startswith('/'):
            path = '/' + path
        params = kw.pop('params', {})
        if method == 'get':
            params['access_token'] = self._access_token
        else:
            assert '?' not in path
            path += '?access_token={0}'.format(self._access_token)

        # All POST and PUT request bodies must be JSON encoded, and must have content
        # type of application/json [...]
        if method in ['post', 'put'] and 'data' in kw and 'files' not in kw:
            kw['headers'] = {"Content-Type": "application/json"}
            kw['data'] = json.dumps(kw['data'])

        response = getattr(requests, method)(
            '{0}{1}{2}'.format(self._api_url, prefix, path), params=params, **kw)
        if response.status_code == expected:
            if expected != 204:
                return response.json()
            return  # 204 No Content
        # See http://developers.zenodo.org/#errors
        raise ApiError(
            response.status_code,
            response.json() if 400 <= response.status_code < 500 else None)

    #
    # Records API
    #
    def search(self, keywords=None, limit=None, **kw):
        """
        "https://zenodo.org/api/records/?sort=mostrecent&page=2&keywords=cldf&size=2",
{
    "hits": {
        "total": 4,
        "hits": [
            {
                "files": [
                    {
                        "key": "dictionaria/nen-v1.0.zip",
                        "size": 421044,
                        "type": "zip",
                        "checksum": "md5:df25dbca677de8aa31bb728cb012116a",
                        "bucket": "d8bbe7e9-cdcc-4972-a415-dd56667cf7d7",
                        "links": {
                            "self": "https://zenodo.org/api/files/d8bbe7e9-cdcc-4972-a415-dd56667cf7d7/dictionaria/nen-v1.0.zip"
                        }
                    }
                ],
                "created": "2019-07-22T14:04:43.573452+00:00",
                "conceptdoi": "10.5281/zenodo.3345804",
                "metadata": {
                    "keywords": [
                        "linguistics",
                        "CLDF"
                    ],
                    "related_identifiers": [
                        {
                            "scheme": "url",
                            "relation": "isSupplementTo",
                            "identifier": "https://github.com/dictionaria/nen/tree/v1.0"
                        },
                        {
                            "scheme": "doi",
                            "relation": "isVersionOf",
                            "identifier": "10.5281/zenodo.3345804"
                        }
                    ],
                    "relations": {
                        "version": [
                            {
                                "count": 1,
                                "last_child": {
                                    "pid_value": "3345805",
                                    "pid_type": "recid"
                                },
                                "index": 0,
                                "is_last": true,
                                "parent": {
                                    "pid_value": "3345804",
                                    "pid_type": "recid"
                                }
                            }
                        ]
                    },
                    "description": "<p>Evans, Nicholas. 2019. Nen dictionary. Dictionaria 8. 1-5005 (Available online at <a href=\"https://matthew.clld.org/dictionaria/contributions/nen\">https://dictionaria.clld.org/contributions/nen</a>)</p>",
                    "resource_type": {
                        "title": "Dataset",
                        "type": "dataset"
                    },
                    "creators": [
                        {
                            "name": "Nicholas Evans",
                            "affiliation": "Australian National University"
                        }
                    ],
                    "publication_date": "2019-07-22",
                    "access_right_category": "success",
                    "license": {
                        "id": "CC-BY-4.0"
                    },
                    "version": "v1.0",
                    "communities": [
                        {
                            "id": "cldf-datasets"
                        },
                        {
                            "id": "clld"
                        },
                        {
                            "id": "dictionaria"
                        }
                    ],
                    "doi": "10.5281/zenodo.3345805",
                    "title": "dictionaria/nen: Nen Dictionary",
                    "access_right": "open"
                },
                "id": 3345805,
                "owners": [
                    46881
                ],
                "conceptrecid": "3345804",
                "stats": {
                    "views": 3.0,
                    "version_unique_downloads": 3.0,
                    "volume": 1263132.0,
                    "version_views": 3.0,
                    "unique_views": 1.0,
                    "unique_downloads": 3.0,
                    "version_unique_views": 1.0,
                    "version_volume": 1263132.0,
                    "downloads": 3.0,
                    "version_downloads": 3.0
                },
                "revision": 6,
                "updated": "2019-07-22T19:05:49.975603+00:00",
                "links": {
                    "conceptdoi": "https://doi.org/10.5281/zenodo.3345804",
                    "html": "https://zenodo.org/record/3345805",
                    "badge": "https://zenodo.org/badge/doi/10.5281/zenodo.3345805.svg",
                    "bucket": "https://zenodo.org/api/files/d8bbe7e9-cdcc-4972-a415-dd56667cf7d7",
                    "latest": "https://zenodo.org/api/records/3345805",
                    "doi": "https://doi.org/10.5281/zenodo.3345805",
                    "latest_html": "https://zenodo.org/record/3345805",
                    "conceptbadge": "https://zenodo.org/badge/doi/10.5281/zenodo.3345804.svg",
                    "self": "https://zenodo.org/api/records/3345805"
                },
                "doi": "10.5281/zenodo.3345805"
            }
        ],


           "links": {
        "next": "https://zenodo.org/api/records/?sort=mostrecent&page=2&keywords=cldf&size=2",
        "self": "https://zenodo.org/api/records/?sort=mostrecent&page=1&keywords=cldf&size=2"
    },

        :return:
        """
        recs = []
        res = self._req('get', prefix='records', path='/', params=dict(keywords=keywords))
        recs.extend(res['hits']['hits'])
        while ('next' in res['links']) and len(recs) < limit:
            res = requests.get(res['links']['next']).json()
            recs.extend(res['hits']['hits'])
        return recs[:limit]

    #
    # Deposition API
    #
    def list(self, q=None, status=None, sort=None, page=None, size=10):
        params = {k: v for k, v in locals().items() if k != 'self' and v}
        return [Deposition.from_dict(d) for d in self._req('get', params=params)]

    def iter(self, q=None, status=None, sort=None):
        page, size, i = 1, 10, 0
        for i, d in enumerate(self.list(
                q=q, status=status, sort=sort, page=page, size=size)):
            yield d
        while i:
            page += 1
            i = 0
            for i, d in enumerate(self.list(
                    q=q, status=status, sort=sort, page=page, size=size)):
                yield d

    def _dep(self, method, **kw):
        return Deposition.from_dict(self._req(method, **kw))

    def create(self, **md):
        res = self._dep('post', expected=201, data={})
        # FIXME: Should we immediately discard the deposition if updating fails?
        return self.update(res, **md) if md else res

    def _update(self, dep):
        dep.validate_update()
        return self._dep(
            'put', path='{0}'.format(dep), data={'metadata': dep.metadata.asdict()})

    def retrieve(self, dep):
        return self._dep('get', path='{0}'.format(dep))

    def delete(self, dep):
        self._req('delete', path='{0}'.format(dep), expected=201)

    def publish(self, dep):
        dep.validate_publish()
        return self._dep('post', path='{0}/actions/publish'.format(dep), expected=202)

    def edit(self, dep):
        return self._dep('post', path='{0}/actions/edit'.format(dep), expected=201)

    def discard(self, dep):
        return self._dep('post', path='{0}/actions/discard'.format(dep), expected=201)

    def newversion(self, dep):
        return self._dep('post', path='{0}/actions/newversion'.format(dep), expected=201)

    def update(self, dep, **kw):
        if not isinstance(dep, Deposition):
            dep = self.retrieve(dep)

        # We automatically unlock published Depositions for editing:
        published = dep.state == PUBLISHED
        if published:
            print('unlock for editing')
            dep = self.edit(dep)

        for k, v in kw.items():
            # Set the metadata attributes, thereby triggering validators:
            setattr(dep.metadata, k, v)

        dep = self._update(dep)
        if published:
            print('publish changes')
            dep = self.publish(dep)
        return dep

    #
    # Deposition File API
    #
    def create_files(self, dep, *paths, **kw):
        for path in paths:
            yield self.create_file(dep, path, verify=kw.get('verify', True))

    def create_file(self, dep, path, verify=True):
        if dep.state != UNSUBMITTED:
            raise ValueError('files can only be uploaded for unsubmitted depositions')
        path = pathlib.Path(path)
        if not path.exists():
            raise ValueError('file to be uploaded does not exist')
        with path.open('rb') as fp:
            res = DepositionFile.from_dict(self._req(
                'post',
                path='{0}/files'.format(dep),
                expected=201,
                data={'filename': path.name},
                files={'file': fp}))
        if verify and res.checksum != md5(path):
            # We delete the deposition file immediately:
            self.delete_file(dep, res)
            raise ValueError('invalid file upload')
        dep.files.append(res)
        return res

    def list_files(self, dep):
        return [
            DepositionFile.from_dict(d) for d in
            self._req('get', path='{0}/files'.format(dep))]

    def sort_files(self, dep, sorted_):
        res = self._req(
            'put',
            path='{0}/files'.format(dep),
            data=[{'id': "{0}".format(d)} for d in sorted_])
        dep.files = [DepositionFile.from_dict(d) for d in res]
        return dep.files

    def retrieve_file(self, dep, depfile):
        return DepositionFile.from_dict(
            self._req('get', path='{0}/files/{1}'.format(dep, depfile)))

    def update_file(self, dep, depfile, filename):
        return DepositionFile.from_dict(self._req(
            'put', path='{0}/files/{1}'.format(dep, depfile), data={'filename': filename}
        ))

    def delete_file(self, dep, depfile):
        self._req('delete', path='{0}/files/{1}'.format(dep, depfile), expected=204)
