# ============================================================
#           STOCK MARKET DATA ANALYZER (NumPy Project)
# ============================================================
# Author  : Kirtikumar Prajapati
# Purpose : Analyze stock prices of multiple companies using NumPy.
# Dataset : 365 Days × 10 Companies
# Concepts Used:
#   • NumPy Arrays
#   • Vectorization
#   • Broadcasting
#   • np.mean()
#   • np.std()
#   • np.where()
#   • np.argsort()
#   • File Handling (.npy)
# ============================================================

import numpy as np

# ------------------------------------------------------------
# Load Dataset
# ------------------------------------------------------------
# stock_prices.npy  -> 365 x 10 matrix
# companies.npy     -> Company Names
# ------------------------------------------------------------

stock_prices = np.load("stock_prices.npy")
companies = np.load("companies.npy")


# ============================================================
# Helper Function
# ============================================================
def get_day():
    """
    Ask the user for a valid day number.
    Returns zero-based index.
    """

    while True:

        day = int(input("Enter Day (1-365): "))

        if 1 <= day <= len(stock_prices):
            return day - 1

        print("Invalid Day! Please try again.")


# ============================================================
# 1. Daily Return
# ============================================================
def daily_return():

    # Select today's day
    day = get_day()

    # Calculate today's profit/loss compared to yesterday
    returns = stock_prices[day] - stock_prices[day - 1]

    print("\n========== DAILY RETURN ==========\n")

    for company, value in zip(companies, returns):
        print(f"{company:<15} {value:8.2f}")


# ============================================================
# 2. Daily Percentage Return
# ============================================================
def percentage_return():

    day = get_day()

    today = stock_prices[day]
    yesterday = stock_prices[day - 1]

    # Percentage Return Formula
    percentage = ((today - yesterday) / yesterday) * 100

    print("\n======= DAILY PERCENTAGE RETURN =======\n")

    for company, value in zip(companies, percentage):
        print(f"{company:<15} {value:8.2f} %")


# ============================================================
# 3. Compare Two Days
# ============================================================
def compare_days():

    print("\nSelect First Day")
    day1 = get_day()

    print("\nSelect Second Day")
    day2 = get_day()

    comparison = ((stock_prices[day1] - stock_prices[day2])
                  / stock_prices[day2]) * 100

    print("\n========== COMPARISON ==========\n")

    for company, value in zip(companies, comparison):
        print(f"{company:<15}{value:8.2f} %")


# ============================================================
# 4. Moving Average
# ============================================================
def moving_average(window):

    day = get_day()

    # Check whether enough previous data exists
    if day < window - 1:
        print(f"\nNeed at least {window} days of data.")
        return

    # Calculate Moving Average
    average = np.mean(stock_prices[day-window+1:day+1], axis=0)

    print(f"\n======= {window}-DAY MOVING AVERAGE =======\n")

    for company, value in zip(companies, average):
        print(f"{company:<15}{value:8.2f}")


# ============================================================
# 5. Price Statistics
# ============================================================
def price_statistics():

    highest = np.max(stock_prices, axis=0)
    lowest = np.min(stock_prices, axis=0)
    average = np.mean(stock_prices, axis=0)

    print("\n========== PRICE STATISTICS ==========\n")

    for company, high, low, avg in zip(companies,
                                       highest,
                                       lowest,
                                       average):

        print(f"""
Company : {company}
Highest : {high:.2f}
Lowest  : {low:.2f}
Average : {avg:.2f}
""")


# ============================================================
# 6. Volatility
# ============================================================
def volatility():

    # Standard Deviation represents volatility
    std = np.std(stock_prices, axis=0)

    print("\n========== VOLATILITY ==========\n")

    for company, value in zip(companies, std):
        print(f"{company:<15}{value:8.2f}")


# ============================================================
# 7. Best Performing Companies
# ============================================================
def best_performance():

    # Calculate yearly percentage return
    yearly_return = ((stock_prices[-1] - stock_prices[0])
                     / stock_prices[0]) * 100

    # Rank companies from highest return to lowest
    ranking = np.argsort(yearly_return)[::-1]

    print("\n======= BEST PERFORMING COMPANIES =======\n")

    for i in ranking:
        print(f"{companies[i]:<15}{yearly_return[i]:8.2f} %")


# ============================================================
# 8. Buy / Sell Signal
# ============================================================
def signal():

    day = get_day()

    if day < 29:
        print("Need at least 30 days of data.")
        return

    # Today's stock price
    today = stock_prices[day]

    # Calculate 30-Day Moving Average
    ma30 = np.mean(stock_prices[day-29:day+1], axis=0)

    # Generate Buy / Sell / Hold Signal
    recommendation = np.where(
        today < ma30 * 0.95,
        "BUY",
        np.where(
            today > ma30 * 1.05,
            "SELL",
            "HOLD"
        )
    )

    print("\n========== SIGNAL ==========\n")

    print(f"{'Company':<15}{'Price':<12}{'MA30':<12}{'Signal'}")

    for company, price, avg, sig in zip(companies,
                                        today,
                                        ma30,
                                        recommendation):

        print(f"{company:<15}{price:<12.2f}{avg:<12.2f}{sig}")


# ============================================================
# 9. Risk Analysis
# ============================================================
def risk_analysis():

    std = np.std(stock_prices, axis=0)

    risk = np.where(
        std < 20,
        "Low Risk",
        np.where(
            std < 40,
            "Medium Risk",
            "High Risk"
        )
    )

    print("\n========== RISK ANALYSIS ==========\n")

    for company, vol, r in zip(companies, std, risk):
        print(f"{company:<15}{vol:<10.2f}{r}")


# ============================================================
# 10. Save Portfolio
# ============================================================
def save_portfolio():

    # Save as Normal NumPy file
    np.save("updated_stock_prices.npy", stock_prices)

    # Save as Compressed File
    np.savez_compressed(
        "portfolio.npz",
        companies=companies,
        prices=stock_prices
    )

    print("\nPortfolio Saved Successfully!")


# ============================================================
# Main Menu
# ============================================================
while True:

    print("""
==================================================
        STOCK MARKET DATA ANALYZER
==================================================
1. Daily Return
2. Daily Percentage Return
3. Compare Two Days
4. 7-Day Moving Average
5. 30-Day Moving Average
6. 90-Day Moving Average
7. Price Statistics
8. Volatility
9. Best Performing Companies
10. Buy/Sell Signal
11. Risk Analysis
12. Save Portfolio
0. Exit
==================================================
""")

    choice = int(input("Enter Your Choice: "))

    match choice:

        case 1:
            daily_return()

        case 2:
            percentage_return()

        case 3:
            compare_days()

        case 4:
            moving_average(7)

        case 5:
            moving_average(30)

        case 6:
            moving_average(90)

        case 7:
            price_statistics()

        case 8:
            volatility()

        case 9:
            best_performance()

        case 10:
            signal()

        case 11:
            risk_analysis()

        case 12:
            save_portfolio()

        case 0:
            print("Thank You for Using Stock Market Analyzer!")
            break

        case _:
            print("Invalid Choice!")