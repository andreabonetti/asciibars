__author__ = "Andrea Bonetti"
__author_email__ = ""

"""
======================================================
ascii bars
======================================================

author: Andrea Bonetti
github: https://github.com/andreabonetti

inspired by:
https://alexwlchan.net/2018/05/ascii-bar-charts/

block elements:
https://en.wikipedia.org/wiki/Block_Elements

selection of useful block elements:
U+2587  ▇   Lower seven eighths block
U+2588  █   Full block
U+2591  ░   Light shade
U+2592  ▒   Medium shade
U+2593  ▓   Dark shade

"""


def _get_sign(x):
    """
    Get sign of a number:
        -1  : negative
        0  : zero
        +1  : positive
    """
    if x > 0:
        sign = +1
    elif x < 0:
        sign = -1
    else:
        sign = 0
    return sign


def _generate_enables_for_negated_bars(neg_unit: str, neg_max: int) -> tuple[bool, bool]:
    """Determine enable flags for negated bar rendering."""
    neg_e = False
    neg_max_e = False

    if neg_unit != "":
        neg_e = True

    if neg_max > 0:
        neg_max_e = True

    return neg_e, neg_max_e


def _get_min_max_values(data: list[tuple[str, int]]) -> tuple[int, int]:
    """Get min and max values from data."""

    max_value = max(count for _label, count in data)
    min_value = min(count for _label, count in data)

    return max_value, min_value


def _get_max_len_str_count(data: list[tuple[str, int]]) -> int:
    """Get maximum length of string representation of counts."""

    max_len_str_count = 0

    for _label, count in data:
        len_str_count = len(str(count))
        
        if len_str_count > max_len_str_count:
            max_len_str_count = len_str_count
    
    return max_len_str_count


def _get_signs_vector(data: list[tuple[str, int]]) -> list[int]:
    """Get vector of signs for data counts."""

    vect_sign = []

    for _, count in data:
        vect_sign.append(_get_sign(count))

    return vect_sign


def _check_data_non_negative(vect_sign: list[int], neg_e: bool, neg_max_e: bool) -> None:
    """Check data counts are non-negative if neg_unit or neg_max are specified."""

    if neg_e or neg_max_e:
        for sign in vect_sign:
            if sign == (-1):
                raise Exception("Data contains negative values, but neg_unit or neg_max is specified.")



def _get_bars_strings(
    data: list[tuple[str, int]],
    unit: str,
    neg_unit: str,
    max_length: int,
    range_of_values: float
    ) -> tuple[list[str], list[str], int, int]:

    vect_str_bar = []
    vect_str_neg = []
    max_pos_length = 0
    max_neg_length = 0

    for label, count in data:
        sign = _get_sign(count) # get sign of count
        length = round(abs(count) / range_of_values * max_length) # get bar length (absolute value)
        neg_length = max_length - length # get negated bar length (absolute value)

        # longest positive/negative bar
        if sign == (+1):
            if length > max_pos_length:
                max_pos_length = length
        elif sign == (-1):
            if length > max_neg_length:
                max_neg_length = length

        # bar
        bar = unit * length
        neg = neg_unit * neg_length
        vect_str_bar.append(bar)
        vect_str_neg.append(neg)
    
    return vect_str_bar, vect_str_neg, max_pos_length, max_neg_length




def _generate_bars(
    max_length: int,
    sep_lc: str,
    count_pf: str,
    print_bar: bool,
    data: list[tuple[str, int]],
    max_label_length: int,
    max_len_str_count: int,
    vect_str_bar: list[str],
    vect_str_neg: list[str],
    max_neg_length: int,
    neg_e: bool,
    neg_unit: str,
    zero: str,
) -> list[str]:
    """ Generate bars strings for plotting."""

    i = 0
    bars_list = []
    for label, count in data:
        # get sign of count
        sign = _get_sign(count)

        # strings
        str_label = label.ljust(max_label_length)
        str_count = str(count).rjust(max_len_str_count)

        # str_bar
        if sign == (+1):
            str_spaces = " " * max_neg_length
            str_bar = str_spaces + vect_str_bar[i]
            if neg_e:
                str_bar = str_bar + vect_str_neg[i]
        elif sign == (-1):
            str_bar = vect_str_bar[i].rjust(max_neg_length)
        else:
            str_spaces = " " * max_neg_length
            if neg_e:
                str_negated = neg_unit * (max_length)
                str_bar = str_negated
            else:
                str_bar = str_spaces + zero

        # bars
        bar_to_print = str_label + sep_lc + str_count + count_pf + " " + str_bar
        bars_list.append(bar_to_print)

        if print_bar:
            print(bar_to_print)
            
        i += 1

    return bars_list




def _get_max_value_line(
    max_label_length: int,
    sep_lc: str,
    count_pf: str,
    print_bar: bool,
    neg_e: bool,
    neg_max_e: bool,
    neg_max: int,
    max_length: int,
    max_len_str_count: int,
    ):
    """Generate and print the maximum value line if applicable."""

    str_max_val_with_spaces = ""
    if neg_e and neg_max_e:
        str_spaces = " " * (
            max_label_length + len(sep_lc) + max_len_str_count + len(count_pf) + 1
        )
        str_max_val = (str(neg_max) + str(count_pf)).rjust(max_length)
        str_max_val_with_spaces = str_spaces + str_max_val

        if print_bar:
            print(str_max_val_with_spaces)
    
    return str_max_val_with_spaces



def plot(
    data: list[tuple[str, int]],  # input data (label, count)
    sep_lc: str =" | ",  # label-count separator
    unit: str="█",  # string unit for bar
    zero: str="▏",  # string for bar when equal to zero
    max_length: int=20,  # maximum bar length in plot
    neg_unit: str="",  # negated bar unit (e.g., '░')
    neg_max: int=0,  # maximum value when negated bar is used
    count_pf: str="",  # count postfix (e.g., '%')
    print_bar: bool=False,
) -> dict:
    """Plot ascii bars."""

    # get useful values
    neg_e, neg_max_e = _generate_enables_for_negated_bars(neg_unit, neg_max)
    max_value, min_value = _get_min_max_values(data)
    max_len_str_count = _get_max_len_str_count(data)
    range_of_values = neg_max if (neg_e and neg_max_e) else (max_value - min_value)
    max_label_length = max(len(label) for label, _count in data)
    vect_sign = _get_signs_vector(data)
    
    # checks
    _check_data_non_negative(vect_sign, neg_e, neg_max_e)

    # bars
    vect_str_bar, vect_str_neg, max_pos_length, max_neg_length = _get_bars_strings(
        data,
        unit,
        neg_unit,
        max_length,
        range_of_values
    )

    bars_list = _generate_bars(
        max_length,
        sep_lc,
        count_pf,
        print_bar,
        data,
        max_label_length,
        max_len_str_count,
        vect_str_bar,
        vect_str_neg,
        max_neg_length,
        neg_e,
        neg_unit,
        zero,
    )

    str_max_val_with_spaces = _get_max_value_line(
        max_label_length,
        sep_lc,
        count_pf,
        print_bar,
        neg_e,
        neg_max_e,
        neg_max,
        max_length,
        max_len_str_count,
    )


    # return
    return {
        "bars_list": bars_list,
        "str_max_val_with_spaces": str_max_val_with_spaces,
    }
