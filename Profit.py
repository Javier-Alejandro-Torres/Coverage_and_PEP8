

def static_profit():

    profit1 = ({"cost_price": 32.67, "sell_price": 45.00, "inventory": 1200})
    profit2 = ({"cost_price": 225.89, "sellprice": 550.00, "inventory": 100})
    profit3 = ({"cost_price": 2.77, "sell_price": 7.95, "inventory": 8500})
    print("Press 1 to display all" + "\n\nProfit 1: ", profit1, "\n\nProfit 2:", profit2, "\n\nProfit 3: ", profit3)
    x = input("You selected: ")
    if(x == "1"):
        cost = profit1.get("cost_price")
        sell = profit1.get("sell_price")
        inventory = profit1.get("inventory")
        operaciones(cost, sell, inventory, profit1)

        cost = profit2.get("cost_price")
        sell = profit2.get("sell_price")
        inventory = profit2.get("inventory")
        operaciones(cost, sell, inventory, profit2)

        cost = profit3.get("cost_price")
        sell = profit3.get("sell_price")
        inventory = profit3.get("inventory")
        operaciones(cost, sell, inventory, profit3)


def operaciones(cost, sell, inventory, profit1):
    Total_sales = inventory * sell
    Total_cost = inventory * cost
    Profit = round(Total_sales - Total_cost)
    print("\nResult is:\n")
    print(profit1, "->", Profit)


if __name__ == '__main__':
    static_profit()
