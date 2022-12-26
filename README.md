# asciibars

`asciibars` is a Python module for plotting bar charts in ASCII.

## How to install it

## How to use it

Import the module:
```
import asciibars
```

Define your data with both labels and counts:
```
data_p = [
    ('Gigi',        64  ),
    ('Carletto',    12  ),
    ('Silvio',      0   ),
    ('Priscilla',   30  ),
    ('Rodolfo',     57  ),
    ('Sigismondo',  70  )
]
```

Generate your bar chart in ASCII:
```
asciibars.plot(data_p)
```

The command above will print:
```
Gigi       | 64 ██████████████████
Carletto   | 12 ███
Silvio     |  0 ▏
Priscilla  | 30 █████████
Rodolfo    | 57 ████████████████
Sigismondo | 70 ████████████████████
```

## Arguments of asciibars.plot

| Input      | Type           | Description                            |
| ---------- | -------------- | -------------------------------------- |
| data       | [(str, float)] | data array with labels and count       |
| sep_lc     | str            | label-count separator                  |
| unit       | str            | string unit for bar                    |
| zero       | str            | string for bar when equal to zero      |
| max_length | int            | maximum bar length in plot             |
| neg_unit   | str            | negated bar unit (e.g., '░')           |
| neg_max    | int            | maximum value when negated bar is used |
| count_pf   | str            | count postfix (e.g., '%')              |


## Examples

Please find more examples below.


```
asciibars.plot(data_p,sep_lc=' -> ',unit='▓',max_length=40)

Gigi       -> 64 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
Carletto   -> 12 ▓▓▓▓▓▓▓
Silvio     ->  0 ▏
Priscilla  -> 30 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
Rodolfo    -> 57 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
Sigismondo -> 70 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

```
asciibars.plot(data_p,unit='▓',neg_unit='░')

Gigi       | 64 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░
Carletto   | 12 ▓▓▓░░░░░░░░░░░░░░░░░
Silvio     |  0 ░░░░░░░░░░░░░░░░░░░░
Priscilla  | 30 ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░
Rodolfo    | 57 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░
Sigismondo | 70 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
```

```
asciibars.plot(data_p,unit='▓',neg_unit='░',neg_max=100,count_pf='%')

Gigi       | 64% ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░
Carletto   | 12% ▓▓░░░░░░░░░░░░░░░░░░
Silvio     |  0% ░░░░░░░░░░░░░░░░░░░░
Priscilla  | 30% ▓▓▓▓▓▓░░░░░░░░░░░░░░
Rodolfo    | 57% ▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░
Sigismondo | 70% ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░
                                 100%
```

```
data_pn = [
    ('One',     64  ),
    ('Two',     38  ),
    ('Three',   0   ),
    ('Four',    -18 ),
    ('Five',    -30 )
]

asciibars.plot(data_pn,sep_lc=' ',count_pf='%')

One    64%       ██████████████
Two    38%       ████████
Three   0%       ▏
Four  -18%   ████
Five  -30% ██████
```

## Change log
Please find the change log [here](CHANGELOG.md).

## Acknowledgments
Thanks to:
- [Alex](https://alexwlchan.net/) for inspiring this work with [this blog post](https://alexwlchan.net/2018/05/ascii-bar-charts/).
- [Jinhang Jiang](https://www.linkedin.com/in/jinhangjiang/) for the tutorial on [how to publish your first Python package](https://towardsdatascience.com/an-end-to-end-guide-to-publish-your-python-package-bdb56639662c).