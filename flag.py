for i in range(15):
    for j in range(30):
        if (i - 7)**2 + (j - 15)**2 <= 16:
            print("🔴", end="")
        else:
            print("🟩", end="")
    print()
