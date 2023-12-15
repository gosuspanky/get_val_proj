import pytest

from utils.dicts import get_val


@pytest.mark.parametrize("dict_, key, default, expected",
                         [
                             ({"vcs": "mercurial"}, "vcs", "", 'mercurial'),
                             ({"vcs": "mercurial"}, "vcs", "git", 'mercurial'),
                             ({}, "vcs", "git", "git"),
                             ({}, "vcs", "bazaar", 'bazaar')
                         ]
                         )
def test_get_val(dict_, key, default, expected):
    assert get_val(dict_, key, default) == expected
