# FIRST SOLUTION W/ WHILE LOOPS

# /**
#  * @param {string} s
#  * @return {number}
#  */
# var lengthOfLastWord = function(s) {
#     let i = s.length - 1
#     let lastLen = 0
#     while (s[i] == ' ') {
#         i -= 1
#     }
#     while (i >= 0 && s[i] != ' ' ) {
#         lastLen += 1
#         i -= 1
#     }
#     return lastLen
# };

# // create length variable
# // loop through str
#     // start at the end of str and loop backwards
#         // while loop
#             // while space, move on
#             // while char, add 1 to length
# // return length

# OOORRRRRR
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        start = False
        for i in range(len(s) - 1, -1, -1):
            if i == 0 and s[i] != ' ':
                count += 1
                return count
            elif i == 0:
                return count
            elif start == False and s[i] == " ":
                continue
            elif start == False and s[i] != " ":
                start = True
                count += 1
            elif start == True and s[i] != " ":
                count += 1
            elif start == True and s[i] == " ":
                return count