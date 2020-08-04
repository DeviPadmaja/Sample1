print("How many kilometers did you run today?")
kms = input()

total = float(kms)/1.609344
total = round(total , 2)

print(" your {} km run was {} miles " .format(kms , total))

