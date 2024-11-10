

from main import findSmallestAppealing, getSmallerItems



def test_find_smalles_appealing():
    assert findSmallestAppealing(old_code="1234", k=2) == "1313"
    assert findSmallestAppealing(old_code="41242", k=4) == "41244"


def test_find_smaller_items():
    # Example usage:
    items = [1, 2, 3, 2, 4, 1]
    start = [2, 0]
    end = [4, 0]
    query = [5, 3]
    assert getSmallerItems(items=items, start=start, end=end, query=query) == [4, 2]