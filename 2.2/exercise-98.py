age = int(input('Enter your age:'))
restingHeartRate = float(input('Enter your resting heart rate:'))
print(f'Training heart rate: {int(.7 * (220 - age) + .3 * restingHeartRate)} beats/min.')