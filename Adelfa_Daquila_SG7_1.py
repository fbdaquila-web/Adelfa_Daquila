# [FRANZ ROBERT B. DAQUILA / 8-ADELFA ]

# [ P1: INPUT AND DATA ]
accepted_payment_methods = ["GCash", "Cash", "Card"]
payment_method = str(input("Enter payment method: "))

# [ P2: PROCESS AND OUTPUT ]
if payment_method in accepted_payment_methods:
    print("Valid payment method.")
else:
    print("Invalid payment method.")
