
class node:
    def __init__(self, value):
        self.value = value
        self.left = -1 
        self.right = -1
        self.symbol = ""
    # value = -1 cho node rỗng
    
    
class PrefixCodeTree:

    def __init__(self):
        self.root = node(2) # value = 2 cho node
        self.codebook = {}
    
    def add(self, symbol, code): 
        self.codebook[symbol] = code 

    def insert(self, codeword, symbol):
        # 1 nằm bên nhánh phải
        # 0 nằm bên nhánh trái
        current = self.root
        for word in codeword:
            if (word == "1"): 
                if(current.right == -1): # chưa tồn tại node bên phải thì tạo mới
                    current.right = node(1)
                current = current.right
            else: # word = 0 
                if ( current.left == -1): # chưa tồn tại node bên trái thì tạo mới
                    current.left = node(0)
                current = current.left
        current.symbol = symbol
        current = self.root
        
        self.add(symbol,codeword) # thêm symbol vào codebook
        
    
    def decode(self, encodedData): # duyệt cây
        result=""
        current = self.root
        for char in encodedData:
            if (char == "1"):
                current = current.right
            else: # char = "0"
                current = current.left
            
            if(current.symbol != ""):
                result += current.symbol
                current = self.root
                
        if (current != self.root):
            return "cant decode"
        else:
            return result

trie = PrefixCodeTree()
trie.insert("0","x1")
trie.insert("100","x2")
trie.insert("101","x3")
trie.insert("11","x4")
print(trie.decode("10011010010111"))