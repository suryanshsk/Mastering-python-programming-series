from flask import app


def moving_average_strategy(symbol, short_window=40, long_window=100):
    barset = app.get_barset(symbol, 'day', limit=long_window)
    bars = barset[symbol]

    short_ma = sum([bar.c for bar in bars[-short_window:]]) / short_window
    long_ma = sum([bar.c for bar in bars]) / long_window

    if short_ma > long_ma:
        print(f"Buy signal for {symbol}")
        app.submit_order(
            symbol=symbol,
            qty=1,
            side='buy',
            type='market',
            time_in_force='gtc'
        )
    elif short_ma < long_ma:
        print(f"Sell signal for {symbol}")
        app.submit_order(
            symbol=symbol,
            qty=1,
            side='sell',
            type='market',
            time_in_force='gtc'
        )

# Example usage
moving_average_strategy('AAPL')
