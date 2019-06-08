'''
Write an algorithm to justify text. Given a sequence of words and an integer line length k, return a list of strings which represents each line, fully justified.

More specifically, you should have as many words as possible in each line. There should be at least one space between each word. Pad extra spaces when necessary so that each line has exactly length k. Spaces should be distributed as equally as possible, with the extra spaces, if any, distributed starting from the left.

If you can only fit one word on a line, then you should pad the right-hand side with spaces.

Each word is guaranteed not to be longer than k.

For example, given the list of words ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"] and k = 16, you should return the following:

["the  quick brown", # 1 extra space on the left
"fox  jumps  over", # 2 extra spaces distributed evenly
"the   lazy   dog"] # 4 extra spaces distributed evenly
'''

lwords = ["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"]
k = 16

def line2string(arr, k):
    avail = len(arr) - 1
    spaces_to_dist = k - sum(len(x) for x in arr)
    spaces = [(spaces_to_dist - avail) / avail] * avail

    for x in range(spaces_to_dist % avail):
        spaces[x] += 1

    string = ""

    for x in range(len(arr)-1):
        string += arr[x] + " "
        string += " " * spaces[x]
    string += arr[-1]

    return string

def day28(lwords, k):
    running_count = 0
    lines = []
    line = []
    running_ind = 0

    for i in range(len(lwords)):
        if running_count + len(lwords[i]) + (running_ind - 1) > k:
            lines.append(line)
            line = []
            running_count = 0
            running_ind = 0
        running_count += len(lwords[i])
        line.append(lwords[i])
        running_ind += 1
    lines.append(line)

    _lines = []
    for x in lines:
        _lines.append(line2string(x,k))
    return _lines

print(day28(lwords, k))
