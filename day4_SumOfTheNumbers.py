total = 0   # ✅ Step 1 (before loop)

while True:
    numbers = int(input("Enter numbers: "))

    if numbers == 0:   # ✅ Step 2 (check first)
        break

    total = total + numbers   # ✅ Step 3 (add after check)

print("Total =", total)   # ✅ Step 4 (after loop)