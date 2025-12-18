import asciibars


def main():
    data = [
        ("Gigi", 64),
        ("Carletto", 12),
        ("Silvio", 0),
        ("Priscilla", 30),
        ("Rodolfo", 57),
        ("Sigismondo", 70),
    ]

    print("")
    plot_dict = asciibars.plot(data, print_bar=True, unit="▓", neg_unit="░")
    print("")

    print("List of bars:")
    print(plot_dict["vect_str_bar"])
    print("")

    print("List of *negated* bars:")
    print(plot_dict["vect_str_neg"])
    print("")

    return plot_dict  # for testing


if __name__ == "__main__":
    _ = main()
