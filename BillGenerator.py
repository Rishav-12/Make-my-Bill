bill_amt = 0

print("Enter the price of the items. Press q when done")

while True:
    inp = input()

    if inp == 'q':
        break
    if inp.isdigit():
        price = int(inp)
        bill_amt += price
        print("Total so far: " + str(bill_amt))
    else:
        print("The input is not a valid price.")

print("Amount payable: Rs. " + str(bill_amt) + ". Thanks for shopping with us.")
input()
