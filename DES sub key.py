
from Crypto.Cipher import DES
import binascii

def left_shift(bits, n):
    """Perform a left shift of n positions on the bits."""
    return bits[n:] + bits[:n]

def generate_subkeys(key):
    """Generate 16 DES-like subkeys using a modified rule."""
    # Convert key into binary format (without parity bits)
    key_bin = bin(int(binascii.hexlify(key).decode(), 16))[2:].zfill(64)  # 64-bit key
    
    # Remove parity bits (every 8th bit)
    key_56 = "".join([key_bin[i] for i in range(64) if (i + 1) % 8 != 0])

    # Split into two 28-bit halves
    C = key_56[:28]
    D = key_56[28:]

    # Generate subkeys
    subkeys = []
    for round in range(16):
        # Perform a left shift on C and D
        C = left_shift(C, 1)
        D = left_shift(D, 1)

        # Select first 24 bits from C and next 24 bits from D
        subkey = C[:24] + D[:24]

        # Append the subkey
        subkeys.append(subkey)

    return subkeys

def display_subkeys(subkeys):
    """Display subkeys as hex strings."""
    for i, subkey in enumerate(subkeys):
        hex_subkey = hex(int(subkey, 2))[2:].zfill(6)  # 6 hex characters (24 bits)
        print(f"Subkey {i+1}: {hex_subkey}")

# Example usage
if __name__ == "__main__":
    key = binascii.unhexlify("133457799BBCDFF1")  # Corrected 8-byte key
    subkeys = generate_subkeys(key)
    display_subkeys(subkeys)
