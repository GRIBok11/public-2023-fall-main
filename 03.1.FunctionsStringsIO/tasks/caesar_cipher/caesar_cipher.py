def caesar_encrypt(message: str, n: int) -> str:
    """Encrypt message using caesar cipher

    :param message: message to encrypt
    :param n: shift
    :return: encrypted message
    """
    alf_lower = "abcdefghijklmnopqrstuvwxyz"
    alf_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    shifr = []
    
    for char in message:
        if char in alf_lower:
            j = alf_lower.index(char)
            shifr.append(alf_lower[(j + n) % len(alf_lower)])
        elif char in alf_upper:
            j = alf_upper.index(char)
            shifr.append(alf_upper[(j + n) % len(alf_upper)])
        else:
            shifr.append(char)
    
    return ''.join(shifr)

message='Veni vidi vici'
print(caesar_encrypt(message,52))
