#listing 1.15
from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    # generate length random bytes
    tb: bytes = token_bytes(length)
    # convert those bytes into a bit string and return it
    return int.from_bytes(tb, "big")

#listing 1.16
def encrypt(original: str) -> Tuple[int, int]:
    original_bytes: bytes = original.encode()
    dummy_Key: int = random_key(len(original_bytes))
    original_Key: int = int.from_bytes(original_bytes, "big")
    encrypted_Key: int = original_Key ^ dummy_Key  # XOR
    return dummy_Key, encrypted_Key

  
  
  
#listing 1.17

def decrypt(key1: int, key2: int) -> str:
    decrypted_Key: int = key1 ^ key2  # XOR
    temp: bytes = decrypted_Key.to_bytes((decrypted_Key.bit_length()+ 7) // 8, "big")
    return temp.decode()


  
  
 #listing 1.18

if __name__ == "__main__":
    key1, key2 = encrypt("One Time Execution!")
    result: str = decrypt(key1, key2)
    print(result) ## RESULT is One Time Execution!
