from sys import stdin
rl = stdin.readline


N = int(rl())

base = ord('A')
empty = ord('.') - ord('A')

leftChildren = [-1] * N
rightChildren = [-1] * N
for _ in range(N):
    parent, leftChild, rightChild = map(lambda x : ord(x) - base, rl().split())
    leftChildren[parent] = leftChild
    rightChildren[parent] = rightChild

def preorder(node, result):
    if node != empty:
        result.append(chr(node + base))
        preorder(leftChildren[node], result)    
        preorder(rightChildren[node], result)

preorderResult = []
preorder(0, result=preorderResult)
print(''.join(preorderResult))

def inorder(node, result):
    if node != empty:
        inorder(leftChildren[node], result)    
        result.append(chr(node + base))
        inorder(rightChildren[node], result)

inorderResult = []
inorder(0, result=inorderResult)
print(''.join(inorderResult))

def postorder(node, result):
    if node != empty:
        postorder(leftChildren[node], result)    
        postorder(rightChildren[node], result)
        result.append(chr(node + base))

postorderResult = []
postorder(0, result=postorderResult)
print(''.join(postorderResult))