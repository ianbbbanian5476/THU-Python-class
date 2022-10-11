purchase = float(input('Enter purchase price:'))
selling = float(input('Enter selling price:'))
markup = selling - purchase
print(f'Markup: ${markup}\nPercentage markup: {round(markup / purchase * 100,2)}%\nProfit margin: {round(markup / selling *100,2)}%')