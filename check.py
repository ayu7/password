#Angela Yu
#SoftDev2 pd8
#HW10 -- How Strong?
#2017-04-24

lower="qwertyuiopasdfghjklzxcvbnm"
upper="QWERTYUIOPASDFGHJKLZXCVBNM"
number="1234567890"
symbol=".?!&#,;:-_*"

def mix(password):
    low=[x for x in password if x in lower]
    up=[x for x in password if x in upper]
    num=[x for x in password if x in number]
    if len(low)>0 and len(up)>0 and len(num)>0:
        return True
    return False

print mix("aB1")
print mix("ab1")


def strength(password):
    rating=0
    if len(password)>8:
        rating+=2
    if mix(password):
        rating+=4
    sym=[x for x in password if x in symbol]
    if len(sym)>0:
        rating+=4
    return rating

print strength("abcDEf123:") #10
print strength("abDEF:f")#4
