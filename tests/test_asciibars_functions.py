def test_get_sign():
    from asciibars import _get_sign

    assert _get_sign(10) == +1
    assert _get_sign(-5) == -1
    assert _get_sign(0) == 0


def test_plot():
    import asciibars

    data_p = [
        ("Gigi", 64),
        ("Carletto", 12),
        ("Silvio", 0),
        ("Priscilla", 30),
        ("Rodolfo", 57),
        ("Sigismondo", 70),
    ]

    data_pn = [("One", 64), ("Two", 38), ("Three", 0), ("Four", -18), ("Five", -30)]

    asciibars.plot(data_p, print_bar=True)
    print("")
    asciibars.plot(data_p, sep_lc=" -> ", unit="▓", max_length=40, print_bar=True)
    print("")
    asciibars.plot(data_p, unit="▓", neg_unit="░", print_bar=True)
    print("")
    asciibars.plot(
        data_p, unit="▓", neg_unit="░", neg_max=100, count_pf="%", print_bar=True
    )
    print("")
    asciibars.plot(data_pn, sep_lc=" ", count_pf="%", print_bar=True)
    print("")
