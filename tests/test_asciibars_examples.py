def test_example_positive_bars():
    from examples import example_positive_bars

    plot_dict = example_positive_bars.main()

    assert plot_dict['vect_str_bar'][0] == '▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓'
    assert plot_dict['vect_str_neg'][0] == '░░'
    assert 'Gigi' in plot_dict['bars_list'][0]
    assert '64' in plot_dict['bars_list'][0]
    assert 'Sigismondo' in plot_dict['bars_list'][-1]
    assert '70' in plot_dict['bars_list'][-1]

