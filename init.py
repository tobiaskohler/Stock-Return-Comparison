import argparse
from plottingModule import plot_returns


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Calculate and plot returns for a stock')
    parser.add_argument("-s", "--symbols", type=str, nargs='+', help="List of stock symbols to plot")    
    parser.add_argument('-f', '--frequency', type=str, choices=['monthly', 'quarterly', 'yearly'], help='Frequency for the resampling of daily returns (monthly, quarterly, yearly)')
    parser.add_argument('-b', '--begin', type=str, help='Start date in YYYY-MM-DD format', default=None)
    parser.add_argument('-e', '--end', type=str, help='End date in YYYY-MM-DD format', default=None)
    parser.add_argument('-p', '--price-type', type=str, help='Price type (Open, High, Low, or Close)', default='Close', choices=['Open', 'High', 'Low', 'Close'])
    args = parser.parse_args()
    
    plot_returns(args.symbols, args.frequency, args.begin, args.end, args.price_type)
