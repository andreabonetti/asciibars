# ======================================================
# import
# ======================================================

import asciibars

# ======================================================
# init
# ======================================================

data_p = [
    ('Gigi',        64  ),
    ('Carletto',    12  ),
    ('Silvio',      0   ),
    ('Priscilla',   30  ),
    ('Rodolfo',     57  ),
    ('Sigismondo',  70  )
]

data_pn = [
    ('One',     64  ),
    ('Two',     38  ),
    ('Three',   0   ),
    ('Four',    -18 ),
    ('Five',    -30 )
]


# ======================================================
# plot
# ======================================================

def test_plot():
    asciibars.plot(data_p)
    print("")
    asciibars.plot(data_p,sep_lc=' -> ',unit='▓',max_length=40)
    print("")
    asciibars.plot(data_p,unit='▓',neg_unit='░')
    print("")
    asciibars.plot(data_p,unit='▓',neg_unit='░',neg_max=100,count_pf='%')
    print("")
    asciibars.plot(data_pn,sep_lc=' ',count_pf='%')
    print("")
