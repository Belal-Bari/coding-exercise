# Implement a function that receives two IPv4 addresses, and 
# returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. 
# The last address will always be greater than the first one.

# Examples
# * With input "10.0.0.0", "10.0.0.50"  => return   50 
# * With input "10.0.0.0", "10.0.1.0"   => return  256 
# * With input "20.0.0.10", "20.0.1.0"  => return  246

def ips_between(start, end):
    end_ary = end.split('.')
    start_ary = start.split('.')
    total_ip = 0
    for i,n in enumerate(end_ary[::-1]):
        if(i != 0):
            total_ip = (int(n) + 1) * (256 ** i) + total_ip
        else:
            total_ip = int(n) + total_ip
    used_ip = 0
    for i,n in enumerate(start_ary[::-1]):
        if(i != 0):
            used_ip = (int(n) + 1) * (256 ** i) + used_ip
        else:
            used_ip = int(n) + used_ip
    return total_ip - used_ip

print(ips_between("189.21.86.130", "230.13.188.172"))
#189.21.86.130 and 230.13.188.172 -> 687367722