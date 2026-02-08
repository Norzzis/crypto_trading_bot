import pandas as pd
import numpy as np

def calculate_indicators(df):
    # Calculate moving averages
    df['SMA_50'] = df['Close'].rolling(window=50).mean()
    df['SMA_200'] = df['Close'].rolling(window=200).mean()
    
    # Calculate RSI
    delta = df['Close'].diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
    rs = gain / loss
    df['RSI'] = 100 - (100 / (1 + rs))

def generate_signal(df):
    if df['SMA_50'].iloc[-1] > df['SMA_200'].iloc[-1] and df['RSI'].iloc[-1] < 30:
        return "Buy"
    elif df['SMA_50'].iloc[-1] < df['SMA_200'].iloc[-1] and df['RSI'].iloc[-1] > 70:
        return "Sell"
    else:
        return "Hold"

def main():
    # Example DataFrame
    data = {
        'Close': [100, 102, 101, 103, 104, 106, 105, 107, 108, 110]  # Example closing prices
    }
    
    df = pd.DataFrame(data)
    calculate_indicators(df)
    signal = generate_signal(df)
    print(f"Generated Signal: {signal}")

if __name__ == "__main__":
    main()