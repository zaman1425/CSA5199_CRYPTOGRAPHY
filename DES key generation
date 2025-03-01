from Crypto.Cipher import DES
from Crypto.Util.Padding import unpad
import binascii

def des_decrypt(ciphertext, key):
    """Decrypts a ciphertext using DES in ECB mode."""
    cipher = DES.new(key, DES.MODE_ECB)  # Initialize DES cipher
    decrypted_data = unpad(cipher.decrypt(ciphertext), DES.block_size)  # Decrypt and remove padding
    return decrypted_data

if __name__ == "__main__":
    key = b'abcdefgh'  # DES requires an 8-byte key
    ciphertext_hex = "8d20e5056a8d24d0"  # Example encrypted hex string
    ciphertext = binascii.unhexlify(ciphertext_hex)  # Convert hex string to bytes

    try:
        decrypted_text = des_decrypt(ciphertext, key)
        print("Decrypted Text:", decrypted_text.decode('utf-8'))
    except ValueError:
        print("Decryption failed: Incorrect padding or key.")
