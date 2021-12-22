pi_string = "0.0008"

pi_float = float(pi_string)

#print(pi_float)


st2 = 0.0008
st = str(st2)
sr = st.split(sep=".",maxsplit=-1)
print(sr[0])
print(sr[1])

weight = float(sr[0]) + (float(sr[1]) / 10000.0)
print(weight)


index = 0
for s in st:
    if (index == 2):
        a = float(s)
    elif (index == 4):
        b = float(s)
    index = index + 1

#print(a)
#print(b)

#weight = a + (b / 10000.0)

#print(weight)

# r = float(a)
# print(b)

#weight = float(a) + (float(b) / 10000.0)





