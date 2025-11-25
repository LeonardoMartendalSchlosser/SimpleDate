from simpledate import today, parse_date, format_date, days_between

def test_today():
    assert today() is not None

def test_parse_and_format():
    d = parse_date("01/01/2025")
    assert format_date(d) == "01/01/2025"

def test_days_between():
    d1 = parse_date("01/01/2025")
    d2 = parse_date("05/01/2025")
    assert days_between(d1, d2) == 4
