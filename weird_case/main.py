# even is upper
# odd is lower
def to_weird_case(words):
    weird_string = ""
    index = 0
    for l in words:
        if l == ' ':
            index = 0
            weird_string += " " 
        elif index % 2 == 0: # even
            weird_string += l.upper()
            index += 1
        elif index % 2 == 1:
            weird_string += l.lower()
            index += 1
    return weird_string



# print(to_weird_case("String"))
print(to_weird_case('THIs iS a TEST'))
# 'ThIs Is A TeSt'
