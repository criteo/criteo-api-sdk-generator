import re

import pytest

from shared.utils import VERSION_BUMP_PATTERN

# VERSION_BUMP_PATTERN is consumed by `git ... | grep -Ev '<pattern>'` in
# GitClient.diff_count. grep -E matches unanchored, per-line, so we test the
# pattern with re.search (also unanchored)
_PATTERN = re.compile(VERSION_BUMP_PATTERN)

test_data = [
    # --- SHOULD be filtered ---
    ('0.0.260924',                True),  # preview/experimental tag
    ('0.1.260924',                True),  # preview tag, generator_version=1
    ('2026.01.0.260924',          True),  # dated tag
    ('Released version 0.0.260924 today', True),

    # --- should NOT be filtered ---
    ('version=1.2.3',             False),
    ('0.0.0',                     False),
    ('260924',                    False),
    ('+    public void foo() {}', False),
    ('+def bar():',               False),
]

@pytest.mark.parametrize('line, expected_match', test_data)
def test_version_bump_pattern(line, expected_match):
    matched = _PATTERN.search(line) is not None
    assert matched == expected_match
