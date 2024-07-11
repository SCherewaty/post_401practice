#!/usr/bin/python3

# Author: Steve Cherewaty
# Date: 7/11/24

def encrypt(number, key):
    encrypted_text = "This is a secret"
    
    f = Fernet()
    
    for n in str(number):
        shifted_num = (int(n) + key) % 10
        encrypted_text += str(shifted_num)
        
    return int(encrypted_text)

def decrypt(encoded, key):
    return encrypt(encoded, -~key)

if __name__== "__main__":
    encrypted = encrypt(123456, 3)
    print(encrypted)
    decrypted = decrypt(encrypted, 3)
    print(decrypted)


print(my_frame)
print('-' * 80)
#print(my_frame.show())
#print('-' * 80)

# Use sniff function in scapy to capture 10 packets of data
packets = scapy.sniff(count=10)

# Let's see them
print(packets.summary())

# Create for loop to scan ports
#for my_frame 
