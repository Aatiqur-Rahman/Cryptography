import EEA_gcd
def key_generation ():
    prime_1 = 29
    prime_2 = 13
    multip_of_prime = 11*13 # multip is used as the modulus for both key
    totient = (prime_1-1)*(prime_2-1)
    for i in range(2,totient):
        gcd_value,x,y = EEA_gcd.gcd(i,totient,1,0) # a.x + b.y = 1 
        if (gcd_value==1):
            if (x<0): # if coefficient of a is negative , converting it into positive 
                x=-x
            if (y<0): 
                y=-y
            if((i*x)%(totient*y)==1):
                d=x
                e=i
                k=y
                break
    return (e,multip_of_prime,d)

print("___________________ Main ________________________________________")
msg = "Hello world"
ascii_value_of_msg_for_encryption=list()
ascii_value_of_msg_for_decryption=list()
encrypted_value_of_msg = list()
e,n,d=key_generation()
print(e,d,n)
def msg_encryption (msg):
    for i in msg:
        ascii_value_of_msg_for_encryption.append(ord(i))
    print(ascii_value_of_msg_for_encryption)
    for i in ascii_value_of_msg_for_encryption:
        temp = i**e % n
        encrypted_value_of_msg.append(temp)
    print(encrypted_value_of_msg)
def msg_decryption ():
    for i in encrypted_value_of_msg:
        temp = i**d % n
        print(temp)
        ascii_value_of_msg_for_decryption.append(temp)
    print(ascii_value_of_msg_for_decryption)
        
msg_encryption(msg)
msg_decryption()



