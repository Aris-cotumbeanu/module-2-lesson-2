# ================================
# POWER CALCULATOR
# ================================

print("=== Power Calculator ===")

# ---------- PART 1: ask the two questions ----------
# Ask for the base number and store it in base
# Ask for the power and store it in exponent
# Wrap both in int() — you cannot multiply text.
base = int(input("Enter the base number: "))
exponent = int(input("Enter the exponent: "))

# ---------- PART 2: the running total ----------
# Create a variable called result and start it at 1.
# We start at 1 because multiplying by 0 would always give 0.
result = 1

# ---------- PART 3 + 4: the loop that multiplies ----------
# Multiply result by base repeatedly
for i in range(1, exponent + 1):
    result = result * base
    print(f"Step {i}: result is now {result}")

# ---------- PART 5: the answer ----------
# After the loop, print the base, the exponent, and the final result
print(f"\n{base} to the power of {exponent} is {result}")