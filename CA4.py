# Addressing Modes - Effective Address Calculation

address = 200
R1 = 40

memory = {
    200: 500,
    240: 900
}

# 1. Immediate Addressing
print("Immediate Addressing:")
print("Operand Value =", 25)
print("Effective Address = Not Applicable")

# 2. Direct Addressing
print("\nDirect Addressing:")
EA = address
print("Effective Address =", EA)
print("Operand Value =", memory[EA])

# 3. Indirect Addressing
print("\nIndirect Addressing:")
EA = memory[address]
print("Effective Address =", EA)

if EA in memory:
    print("Operand Value =", memory[EA])
else:
    print("Operand Value = Not Available")

# 4. Indexed Addressing
print("\nIndexed Addressing:")
EA = address + R1
print("Effective Address =", EA)
print("Operand Value =", memory[EA])
