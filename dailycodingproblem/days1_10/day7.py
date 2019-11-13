'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

input = '111'

def decode(input):
    def checkones(inp, count = 0):
        if int(inp[0]) in range(1,27):
            if len(inp) == 1:
                count += 1
            else:
                if len(inp) > 1:
                    inp = inp[1:]
                    count += checkones(inp)
                    if len(inp) > 2:
                        count += checktwos(inp)
        return count

    def checktwos(inp, count = 0):
        if int(inp[0:2]) in range(1,27):
            if len(inp) == 2:
                count += 1
            else:
                if len(inp) > 2:
                    inp = inp[2:]
                    count += checkones(inp)
                    if len(inp) > 2:
                        count += checktwos(inp)
        return count

    count = 0
    count += checkones(input, count)
    count += checktwos(input, count)

    return count

print(decode(input))
