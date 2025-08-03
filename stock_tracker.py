print("Starting Stock Portfolio Tracker...\n")

stock_prices = {"AAPL": 180, "TSLA": 250, "GOOGL": 145, "NFLX": 410}
portfolio = {}

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock in stock_prices:
        try:
            quantity = int(input(f"Enter quantity for {stock}: "))
            portfolio[stock] = portfolio.get(stock, 0) + quantity
        except ValueError:
            print("Invalid input. Please enter a numeric value for quantity.")
    else:
        print("Stock not found in price list.")

total = sum(stock_prices[stk] * qty for stk, qty in portfolio.items())

print("\nInvestment Summary:")
for stk, qty in portfolio.items():
    value = stock_prices[stk] * qty
    print(f"{stk}: {qty} shares × ${stock_prices[stk]} = ${value}")
print(f"\nTotal Investment Value: ${total}")

save = input("Would you like to save this summary? (yes/no): ").lower()
if save in ["yes", "y"]:
    with open("portfolio_summary.txt", "w") as f:
        for stk, qty in portfolio.items():
            f.write(f"{stk},{qty},{stock_prices[stk] * qty}\n")
        f.write(f"\nTotal Investment: ${total}\n")
    print("Summary saved to 'portfolio_summary.txt'.")