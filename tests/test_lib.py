from bbquote716.lib import get_quote

def test_get_quote():
    assert len(get_quote()) != 0
