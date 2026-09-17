# [FRANZ ROBERT B. DAQUILA / 8-ADELFA ]

# [ P1: INPUT AND DATA ]
PIN = int(input("Create a 6-digit PIN: "))

# [ P2: PROCESS AND OUTPUT ]
PIN = str(PIN)
if len(PIN) == 6:
    print("Valid PIN.")
else:
    print("Invalid PIN. Enter exactly 6 digits.")