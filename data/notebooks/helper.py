def SMA( data, windows):
    # Simple Moving Average (SMA)
    # Equation: SMA = (sum of the last 'windows' data points) / 'windows'
    res = data.rolling(window=windows).mean()
    res = data.rolling(window = windows).mean()
    return res

def EMA( data, windows):
    # Exponential Moving Average (EMA)
    # Equation: EMA_t = (Price_t * (1 - α)) + (EMA_(t-1) * α), where α = 2 / (windows + 1)
    res = data.ewm(span = windows).mean()
    return res

def MACD( data, long, short, windows):
    # Moving Average Convergence Divergence (MACD)
    # Equation:
    # MACD = EMA(short) - EMA(long)
    # Signal = EMA(MACD)

    short_ = data.ewm(span = short).mean()
    long_ = data.ewm(span = long).mean()
    macd_ = short_ - long_
    res = macd_.ewm(span = windows).mean()
    return res

def RSI( data, windows):

    # Relative Strength Index (RSI)
    # Equation:
    # RSI = 100 - (100 / (1 + RS)), where RS = (average gain) / (average loss)


    delta = data.diff(1)
    up = delta.copy()
    down = delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    avg_up = up.rolling(window = windows).mean()
    avg_down = down.rolling(window = windows).mean()
    rs = avg_up/ avg_down
    rsi = 100. -(100./ (1. + rs))
    return rsi

def atr(data_high, data_low, windows):
    # Average True Range (ATR)
    # Equation: ATR = (high - low) for each period, then average over 'windows' periods

    range_ = data_high - data_low
    res = range_.rolling(window = windows).mean()
    return res

def bollinger_band( data, windows):
    # Bollinger Bands
    # Equation:
    # Upper Band = SMA + (2 * std)
    # Lower Band = SMA - (2 * std)


    sma = data.rolling(window = windows).mean()
    std = data.rolling(window = windows).std()
    upper = sma + 2 * std
    lower = sma - 2 * std
    return upper, lower

def rsv( data, windows):
    # Raw Stochastic Value (RSV)
    # Equation: RSV = ((price - min) / (max - min)) * 100

    min_ = data.rolling(window = windows).min()
    max_ = data.rolling(window = windows).max()
    res = (data - min_)/ (max_ - min_) * 100
    return res