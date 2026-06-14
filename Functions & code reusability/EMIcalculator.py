def emi_calculator(principal, rate, tenure):
    monthly_rate = rate / (12 * 100)
    emi = (principal * monthly_rate * (1 + monthly_rate) ** tenure) / ((1 + monthly_rate) ** tenure - 1)
    return emi

p = float(input("Loan Amount: "))
r = float(input("Annual Interest Rate (%): "))
t = int(input("Tenure (months): "))
print(f"Monthly EMI: {emi_calculator(p, r, t):.2f}")
