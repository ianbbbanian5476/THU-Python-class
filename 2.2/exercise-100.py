wattageOfDevice = int(input('Enter wattage:'))
hoursUsed = int(input('Enter number of hours uesd:'))
kWhPerCost = float(input('Enter price per kWh in cents:'))
print(f'Cost of electricity: ${round((wattageOfDevice * hoursUsed)/(1000 * kWhPerCost),2)}')