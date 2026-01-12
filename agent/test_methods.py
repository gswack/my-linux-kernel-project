from unittest.mock import patch, mock_open

from monitor import read_state, get_pids, read_rss


def test_get_pids(mock_file):
    pids = get_pids()
    assert isinstance(pids, list)
    assert all(isinstance(pid, int) for pid in pids)
    assert len(pids) > 0


@patch("builtins.open", new_callable=mock_open, read_data="123 (test) R ...")
def test_read_stat(mock_file):
    stat = read_state(123)
    assert stat is not None


def test_read_rss(mock_file):
    rss = read_rss(123)
    assert rss is not None
    assert isinstance(rss, int)
    assert rss >= 0
