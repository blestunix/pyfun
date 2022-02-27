# Author: Saud Kadiri

class PlayFair:
    def __init__(self, keyword=None):
        '''
        Constructor: Constructs the matrix on the basis of the keyword
        '''
        if keyword:
            line = list(keyword.lower()) + [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) != 'j' and chr(i) not in keyword]
        else:
            line = [chr(i) for i in range(ord('a'), ord('z') + 1) if chr(i) != 'j']
        self.matrix = [line[0:5], line[5:10], line[10:15], line[15:20], line[20:25]]

    def remove_special_chars(self):
        '''
        Removes any special (non-alphabetical) symbol
        '''
        res = ""
        for char in self.text:
            if char.isalpha():
                res += char
        self.text = res

    def replace_doubles(self):
        '''
        If a letter is repeated; it is replace by 'x' on its second occurrence:
        e.g:
            hammer  ->  hamxer
            hammmer ->  hamxmer
        '''
        res = self.text[0]
        for char in self.text[1:]:
            if char == res[-1]:
                res += 'x'
            else:
                res += char
        self.text = res

    def to_even_on_odd(self):
        '''
        If the length of the string is odd; this function appends an 'x' to make it even in length
        '''
        self.text += 'x' * (len(self.text) % 2)

    def pairs(self):
        '''
        This function is used to generate pairs based on the text
        '''
        for a, b in zip(self.text[::2], self.text[1::2]):
            yield (a,b)

    def position(self, char):
        '''
        This method determines the position of the given char in the matrix and returns the position
        '''
        if char == 'j': # j is to be treated as i
            char = 'i'
        for i, row in enumerate(self.matrix):
            if char in row:
                return(i, row.index(char))

    def encode(self, pos1, pos2):
        '''
        Encodes self.text
        '''
        matrix = self.matrix
        if pos1[0] == pos2[0]:      # same row
            return (matrix[pos1[0]][(pos1[1] + 1) % 5], matrix[pos2[0]][(pos2[1] + 1) % 5])
        elif pos1[1] == pos2[1]:    # same column
            return (matrix[(pos1[0] + 1) % 5][pos1[1]], matrix[(pos2[0] + 1) % 5][pos2[1]])
        else:                       # forming rectangle i.e. edge
            return (matrix[pos1[0]][pos2[1]], matrix[pos2[0]][pos1[1]])

    def decode(self, pos1, pos2):
        '''
        Decodes self.text
        '''
        matrix = self.matrix
        if pos1[0] == pos2[0]:      # same row
            return (matrix[pos1[0]][(pos1[1] - 1) % 5], matrix[pos2[0]][(pos2[1] - 1) % 5])
        elif pos1[1] == pos2[1]:    # same column
            return (matrix[(pos1[0] - 1) % 5][pos1[1]], matrix[(pos2[0] - 1) % 5][pos2[1]])
        else:                       # forming rectangle i.e. edge
            return (matrix[pos1[0]][pos2[1]], matrix[pos2[0]][pos1[1]])

    def iterate(self, f):
        '''
        iterate pair-wise over the text
        '''
        ans = ""
        for pair in self.pairs():
            new_chars = f(self.position(pair[0]), self.position(pair[1]))
            ans += new_chars[0] + new_chars[1]
        return ans

    def solve(self, text, decode=False):
        '''
        Acts as the main method of the class
        '''
        self.text = text.lower()
        self.remove_special_chars()
        self.replace_doubles()
        self.to_even_on_odd()
        return self.iterate(self.encode if not decode else self.decode)

text = input("Enter the text to be encypted: ")
key = "11"
while len(key) != len(set(key)):
    key = input("Enter the keyword: ")


pf = PlayFair(keyword=key)
ans = pf.solve(text)
print(f"`{text}` is encrypted as `{ans}`")
ans = pf.solve(ans, decode=True)
print(f"Decrypted text: {ans}")
