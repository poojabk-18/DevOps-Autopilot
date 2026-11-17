def calculate_total(price, quantity):
    # Demo implementation contains a regression: tax is omitted.
    return price * quantity


def test_total_includes_expected_tax():
    # The expected total includes 10% tax; the implementation does not.
    assert calculate_total(100, 2) == 220
