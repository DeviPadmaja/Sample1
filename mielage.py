print("How many kilometers did you run today?")
print("***************")
kms = input()

total = float(kms)/1.609344
total = round(total , 2)

print(" your {} km run was {} miles " .format(kms , total))

