import yfinance as yf

# Define the user's stock portfolio with stock ticker symbols and the number of shares
portfolio = {
    "AAPL": 10,  # 10 shares of Apple
    "GOOGL": 5,  # 5 shares of Google
    "TSLA": 2,   # 2 shares of Tesla
    "MSFT": 7,   # 7 shares of Microsoft
}

def get_stock_price(ticker):
    """Get the current price of the stock using Yahoo Finance."""
    stock = yf.Ticker(ticker)
    stock_info = stock.history(period="1d")  # Get the most recent day's data
    return stock_info['Close'][0]  # Return the closing price of the stock

def calculate_portfolio_value(portfolio):
    """Calculate the total value of the portfolio."""
    total_value = 0
    for ticker, shares in portfolio.items():
        stock_price = get_stock_price(ticker)
        stock_value = stock_price * shares
        print(f"{ticker}: {shares} shares at ${stock_price:.2f} = ${stock_value:.2f}")
        total_value += stock_value
    return total_value

def display_portfolio_value(portfolio):
    """Display the total value of the portfolio."""
    print("\nStock Portfolio Overview:")
    total_value = calculate_portfolio_value(portfolio)
    print(f"\nTotal Portfolio Value: ${total_value:.2f}")

# Run the portfolio tracker
display_portfolio_value(portfolio)
