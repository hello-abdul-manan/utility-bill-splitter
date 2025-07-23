print('\nUtility Bill Splitter')

# Get inputs
total_bill = float(input('Enter the total utility bill amount $: '))
people = int(input('Enter number of people sharing the bill: '))

# Calculate per person cost
per_person = total_bill / people

# Print the result
print('\nSplit Summary:')
print('------------------------')
print('Total Bill: $', total_bill)
print('People:', people)
print('Each person pays: $', round(per_person, 2))
