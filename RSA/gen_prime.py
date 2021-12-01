import EEA_gcd
prime_1 = 29
prime_2 = 13
multip_of_prime = 11*13 # multip is used as the modulus for both key
totient = (prime_1-1)*(prime_2-1)
for i in range(2,totient):
    gcd_value,x,y = EEA_gcd.gcd(i,totient,1,0)
    if (gcd_value==1):
        if (x<0):
            x=-x
        if (y<0):
            y=-y
        if((i*x)%(totient*y)==1):
            d=x
            e=i
            k=y
            break
print (d,e,k)
msg = "Hello world"
ascii_value_of_msg=list()
encrypted_value_of_msg = list()
def msg_encryption (msg):
    for i in msg:
        ascii_value_of_msg.append(ord(i))
    print(ascii_value_of_msg)
    for i in ascii_value_of_msg:
        temp = i**e % multip_of_prime
        encrypted_value_of_msg.append(temp)
    print(encrypted_value_of_msg)
msg_encryption(msg)



