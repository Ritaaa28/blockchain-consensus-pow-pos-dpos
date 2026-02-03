import hashlib
import time

def HASH(data):
    """Implémente HASH(header || nonce) du pseudo-code"""
    return hashlib.sha256(data).hexdigest()

def BUILD_HEADER(prev_hash, tx_list):
    """Construit l'en-tête comme spécifié dans MINE_BLOCK"""
    timestamp = str(time.time())
    tx_string = ";".join(tx_list)
    return f"{prev_hash}|{tx_string}|{timestamp}".encode()

def MINE_BLOCK(prev_hash, tx_list, difficulty_target):
    """
    Implémentation fidèle du pseudo-code MINE_BLOCK
    Input: prev_hash, tx_list, difficulty_target
    Output: (header, nonce) tel que Hash(header || nonce) < difficulty_target
    """
    # header ← BUILD_HEADER(prev_hash, tx_list, timestamp=NOW())
    header = BUILD_HEADER(prev_hash, tx_list)
    
    # nonce ← 0
    nonce = 0
    
    # while True do
    while True:
        # h ← HASH(header || nonce)
        # Note: '||' signifie concaténation
        data = header + str(nonce).encode()
        h_hex = HASH(data)
        h_int = int(h_hex, 16)  # Convertir hexadécimal en entier
        
        # if h < difficulty_target then
        if h_int < difficulty_target:
            # return (header, nonce)
            return header, nonce, h_hex
        
        # nonce ← nonce + 1
        nonce += 1

def VERIFY_BLOCK(header, nonce, difficulty_target):
    """
    Implémentation fidèle du pseudo-code VERIFY_BLOCK
    return (HASH(header || nonce) < difficulty_target)
    """
    # HASH(header || nonce)
    data = header + str(nonce).encode()
    h_hex = HASH(data)
    h_int = int(h_hex, 16)
    
    # return (HASH(header || nonce) < difficulty_target)
    return h_int < difficulty_target