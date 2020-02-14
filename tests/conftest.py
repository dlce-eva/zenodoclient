import pytest


@pytest.fixture
def record():
    from zenodoclient.models import Record
    return Record(**{
        "files": [
            {
                "links": {
                    "self": "https://zenodo.org/api/files/f409690d-1538-45df-a285-9c485465b291/"
                            "cldf-datasets/normansinitic-v2.0.pdf"
                },
                "checksum": "md5:1",
                "bucket": "f409690d-1538-45df-a285-9c485465b291",
                "key": "cldf-datasets/normansinitic-v2.0.pdf",
                "type": "pdf",
                "size": 46470
            },
            {
                "links": {
                    "self": "https://zenodo.org/api/files/f409690d-1538-45df-a285-9c485465b291/"
                            "cldf-datasets/normansinitic-v2.0.zip"
                },
                "checksum": "md5:1",
                "bucket": "f409690d-1538-45df-a285-9c485465b291",
                "key": "cldf-datasets/normansinitic-v2.0.zip",
                "type": "zip",
                "size": 46470
            }
        ],
        "owners": [
            46881
        ],
        "doi": "10.5281/zenodo.3552559",
        "stats": {
            "version_unique_downloads": 7.0,
            "unique_views": 8.0,
            "views": 10.0,
            "version_views": 42.0,
            "unique_downloads": 1.0,
            "version_unique_views": 36.0,
            "volume": 46470.0,
            "version_downloads": 10.0,
            "downloads": 1.0,
            "version_volume": 215868.0
        },
        "links": {
            "doi": "https://doi.org/10.5281/zenodo.3552559",
            "conceptdoi": "https://doi.org/10.5281/zenodo.1405147",
            "bucket": "https://zenodo.org/api/files/f409690d-1538-45df-a285-9c485465b291",
            "conceptbadge": "https://zenodo.org/badge/doi/10.5281/zenodo.1405147.svg",
            "html": "https://zenodo.org/record/3552559",
            "latest_html": "https://zenodo.org/record/3552559",
            "badge": "https://zenodo.org/badge/doi/10.5281/zenodo.3552559.svg",
            "latest": "https://zenodo.org/api/records/3552559"
        },
        "conceptdoi": "10.5281/zenodo.1405147",
        "created": "2019-11-25T14:42:36.281493+00:00",
        "updated": "2020-02-13T16:29:04.932607+00:00",
        "conceptrecid": "1405147",
        "revision": 7,
        "id": 3552559,
        "metadata": {
            "access_right_category": "success",
            "doi": "10.5281/zenodo.3552559",
            "description": "<p>Original source of the data:</p>\n\n<blockquote>\n<p>"
                           "Norman, J. (2003): Chinese dialects. Phonology. In: Thurgood, "
                           "G. &amp; LaPolla, R.: The Sino-Tibetan Languages. Routledge: "
                           "London and New York. 72-83.</p>\n</blockquote>",
            "license": {
                "id": "CC-BY-4.0"
            },
            "title": "cldf-datasets/normansinitic: Structural and lexical data for the paper "
                     "by Norman (2013) on Chinese dialect classification",
            "relations": {
                "version": [
                    {
                        "count": 2,
                        "index": 1,
                        "parent": {
                            "pid_type": "recid",
                            "pid_value": "1405147"
                        },
                        "is_last": True,
                        "last_child": {
                            "pid_type": "recid",
                            "pid_value": "3552559"
                        }
                    }
                ]
            },
            "communities": [
                {
                    "id": "calc"
                },
                {
                    "id": "cldf-datasets"
                },
                {
                    "id": "lexibank"
                }
            ],
            "version": "v2.0",
            "keywords": [
                "cldf:StructureDataset",
                "cldf:Wordlist"
            ],
            "publication_date": "2019-11-25",
            "creators": [
                {
                    "affiliation": "Max Planck Institute for the Science of Human History",
                    "name": "Johann-Mattis List"
                },
                {
                    "affiliation": "Max Planck Institute for the Science of Human History",
                    "name": "Robert Forkel"
                }
            ],
            "access_right": "open",
            "resource_type": {
                "type": "dataset",
                "title": "Dataset"
            },
            "related_identifiers": [
                {
                    "scheme": "url",
                    "identifier": "https://github.com/cldf-datasets/normansinitic/tree/v2.0",
                    "relation": "isSupplementTo"
                },
                {
                    "scheme": "doi",
                    "identifier": "10.5281/zenodo.1405147",
                    "relation": "isVersionOf"
                }
            ]
        }
    })
