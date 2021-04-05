from hashlib import sha256
import time
MAX_NONCE = 100000000000              #Max nonce number which we will use to iterate too.

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()      #.hexdigest to convert the hash value into a hexadecimal value.

def mine(block_number, transactions, previous_hash, prefix_zeros):      #this function will do the actual work, this will contain four parameters.block_number is the block number since data in ledger is stored in various blocks,transactions will represent transaction,previous_hash represents hash of the previous block,prefix_zeros represents number of zeros as the prefix in the final hash value.
    prefix_str = '0'*prefix_zeros
    for nonce in range(MAX_NONCE):
        text = str(block_number) + transactions + previous_hash + str(nonce)  #Creating a string which we will be passing as a parameter in the hash function
        new_hash = SHA256(text)
        if new_hash.startswith(prefix_str):                                      #Here we are checking that the output hash has that many prefix_zeros as defined in prefix_str
            print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
            return new_hash

    raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")   #Here we are raising as exception that we have not found our nonce value.

if __name__=='__main__':
    transactions='''
    Dhaval->Bhavin->20,
    Mando->Cara->45
    '''
    difficulty=6 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
    start = time.time()              #start time for bitcoin mining
    print("start mining")             
    new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))                     #Time it took for the process to complete
    print(f"end mining. Mining took: {total_time} seconds") 
    print(new_hash)

# from hashlib import sha256
# MAX_NONCE = 100000000000

# def SHA256(text):
#     return sha256(text.encode("ascii")).hexdigest()

# def mine(block_number, transactions, previous_hash, prefix_zeros):
#     prefix_str = '0'*prefix_zeros
#     for nonce in range(MAX_NONCE):
#         text = str(block_number) + transactions + previous_hash + str(nonce)
#         new_hash = SHA256(text)
#         if new_hash.startswith(prefix_str):
#             print(f"Yay! Successfully mined bitcoins with nonce value:{nonce}")
#             return new_hash

#     raise BaseException(f"Couldn't find correct has after trying {MAX_NONCE} times")

# if __name__=='__main__':
#     transactions='''
#     Dhaval->Bhavin->20,
#     Mando->Cara->45
#     '''
#     difficulty=4 # try changing this to higher number and you will see it will take more time for mining as difficulty increases
#     import time
#     start = time.time()
#     print("start mining")
#     new_hash = mine(5,transactions,'0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
#     total_time = str((time.time() - start))
#     print(f"end mining. Mining took: {total_time} seconds")
#     print(new_hash)