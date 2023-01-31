# Stock Returns Plotter

A simple CLI tool to calculate and plot returns for a stock.

## Usage

The CLI can be run from the command line with the following options:

```Bash
> init.py [-h] -s SYMBOLS [SYMBOLS ...] [-f {monthly,quarterly,yearly}] [-b BEGIN] [-e END] [-p {Open,High,Low,Close}]
````

Where:
- `-s` or `--symbols` is a list of stock symbols to plot.
- `-f` or `--frequency` is the frequency for the resampling of daily returns (monthly, quarterly, yearly).
- `-b` or `--begin` is the start date in `YYYY-MM-DD` format.
- `-e` or `--end` is the end date in `YYYY-MM-DD` format.
- `-p` or `--price-type` is the price type (Open, High, Low, or Close).

## Example

### 1.
To plot the monthly returns of Apple (AAPL) from 2020-01-01 to 2022-01-01 using the close price:

```Bash
> init.py -s AAPL -f monthly -b 2020-01-01 -e 2022-01-01 -p Close
````

This will lead to the follwing output in the terminal:

```Bash
                               AAPL
Date                               
2020-01-02 00:00:00-05:00       NaN
2020-01-03 00:00:00-05:00 -0.009770
2020-01-06 00:00:00-05:00  0.007937
2020-01-07 00:00:00-05:00 -0.004714
2020-01-08 00:00:00-05:00  0.015958
...                             ...
2021-12-27 00:00:00-05:00  0.022715
2021-12-28 00:00:00-05:00 -0.005784
2021-12-29 00:00:00-05:00  0.000502
2021-12-30 00:00:00-05:00 -0.006600
2021-12-31 00:00:00-05:00 -0.003542

[505 rows x 1 columns]
Save graph to the current folder? (y/n)
````

By answering with `y` the .png and .html file will get saved in subfolder `output/`. 

If output-folder does not exist, it will get created in your current working directory.

![Example 1 - Output (.png and .html available)](/AAPL_log-return_monthly_Close_2020-01-01-2022-01-01.png)

### 2.
To plot the quarterly returns of Apple (AAPL), Google (GOOG), Tesla (TSLA) from 2010-01-01 to 2022-12-31 using the Open price:

```Bash
> init.py -s AAPL GOOG TSLA -f quarterly -b 2010-01-01 -e 2022-12-31 -p Open
````

![Example 2 - Output (.png and .html available)](/AAPLGOOGTSLA_log-return_quarterly_Open_2010-01-01-2022-12-31.png)

## Interactivity

Since the function also exports the .html, you can embed the interactive chart within your desired platform.


## PlottingModule

The `plottingModule` module contains the function `plot_returns` which takes in the following parameters:
- `symbols`: List of stock symbols to plot.
- `frequency`: Frequency for the resampling of daily returns (monthly, quarterly, yearly).
- `begin`: Start date in `YYYY-MM-DD` format.
- `end`: End date in `YYYY-MM-DD` format.
- `price_type`: Price type (Open, High, Low, or Close).

This function calculates the returns of the specified stocks and plots them using matplotlib.



## Requirements

This tool requires the following libraries:
- argparse
- matplotlib
- pandas
- numpy

Make sure these are installed before running the tool.
