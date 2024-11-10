

from main import findSmallestAppealing



def test_find_smalles_appealing():
    assert findSmallestAppealing(old_code="1234", k=2) == "1313"
    assert findSmallestAppealing(old_code="41242", k=4) == "41244"