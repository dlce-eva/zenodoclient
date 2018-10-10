import pytest
from mock import Mock

from zenodoclient.models import check_controlled_vocabulary, \
    PUBLICATION_TYPES, \
    IMAGE_TYPES, ACCESS_RIGHTS, RELATION_TYPES, CONTRIBUTOR_TYPES, \
    check_regex, \
    check_list_of_objects, check_persons, check_access_right, check_iso639_3, \
    Metadata


def test_validators():
    with pytest.raises(ValueError):
        check_regex(r'[a-z]+', None, Mock(), '')

    check_regex(r'[a-z]+', None, Mock(), 'abc')

    with pytest.raises(ValueError):
        check_controlled_vocabulary(PUBLICATION_TYPES, lambda i: i is True,
                                    True, Mock(), 'abc')

    check_controlled_vocabulary(PUBLICATION_TYPES, lambda i: i is True, True,
                                Mock(), 'book')

    check_controlled_vocabulary(IMAGE_TYPES, lambda i: i is True, True, Mock(),
                                'photo')

    check_controlled_vocabulary(ACCESS_RIGHTS, lambda i: i is True, True,
                                Mock(), 'closed')

    check_controlled_vocabulary(RELATION_TYPES, lambda i: i is True, True,
                                Mock(), 'cites')

    check_controlled_vocabulary(CONTRIBUTOR_TYPES, lambda i: i is True, True,
                                Mock(), 'Sponsor')

    with pytest.raises(ValueError):
        check_list_of_objects(None, None, Mock(), 'not a list')

    with pytest.raises(ValueError):
        check_list_of_objects({'a': 1}, None, None, [dict()])

    with pytest.raises(ValueError):
        check_list_of_objects('', None, Mock(), [''])

    check_list_of_objects('', None, Mock(), [])

    with pytest.raises(ValueError):
        check_persons(None, None, None, with_type=None)

    with pytest.raises(ValueError):
        check_persons(None, None, None, with_type=True)

    with pytest.raises(ValueError):
        check_access_right('open', Metadata(), None, '')

    with pytest.raises(ValueError):
        check_iso639_3(None, None, 'abfa')

    check_iso639_3(None, None, 'abf')


def test_metadata():
    pass
