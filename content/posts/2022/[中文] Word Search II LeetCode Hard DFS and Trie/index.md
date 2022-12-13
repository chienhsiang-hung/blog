---
title: "[中文] Word Search II LeetCode Hard | DFS and Trie"
date: 2022-12-13T10:11:00+08:00
lastmod: 2022-12-13T10:11:00+08:00
draft: false
author: "Hsiang"
authorLink: "https://chienhsiang-hung.github.io/"
description: "I’m developing a News Board in Powerapps. I utilize RSS Connector to retrieve Google News for the following effect."
resources:
- name: "featured-image"
  src: "featured-image.jpg"
tags: [""]
toc:
  enable: true
zhtw: true
---
## 題目
### 文字接龍
![Word Search II](featured-image.jpg "Word Search II")
LeetCode這題Hard要求找出Graph中存在於Input `words` List 中的字，為 [Word Search - LeetCode](https://leetcode.com/problems/word-search/description/) 的進階版。

`words`從一個變成數個，main loop一樣採用**DFS**，差別在如何*有效率地*在words中依據`n-chr`來進行搜索。這裡採用 <b>Trie</b>* 的文字樹結構，先手刻**Trie**，內建`insert()`跟`search()`。接著整體**iteration流程**跟 [Word Search - LeetCode](https://leetcode.com/problems/word-search/description/) 差不多。

**Trie implimentation 練習: [Implement Trie (Prefix Tree) - LeetCode](https://leetcode.com/problems/implement-trie-prefix-tree/description/)*
```python
# impliment trie
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(bool)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root
        for _chr in key:
            if current.children[_chr]:
                current = current.children[_chr]
            else:
                current.children[_chr] = TrieNode()
                current = current.children[_chr]
        current.isEnd = True

    def search(self, key):
        current = self.root
        for _chr in key:
            if current.children[_chr]:
                current = current.children[_chr]
            else:
                return False
        return current.isEnd

    def word_in_trie(self, key):
        current = self.root
        for _chr in key:
            current = current.children[_chr]
            if not current:
                return False
        return True
    
    def list_words(self):
        current = self.root
        
        def dfs(current, word_snake):
            if not current: return
            
            for k, v in current.items():
                if v:
                    if current[k].isEnd:
                        output.append(
                            ''.join(word_snake+[k])
                        )
                    if current[k].children:
                        dfs(current[k].children, word_snake+[k])        
        
        output = []
        dfs(current.children, [])
        
        return output
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(r, c, word_snake=[], visited=defaultdict(), current=TrieNode().children):
            if visited[(r,c)]:
                return
            visited[(r,c)] = True
            
            word_snake.append(board[r][c])
            current_word = ''.join(word_snake)

            if current[board[r][c]]:
                if current[board[r][c]].isEnd:
                    output.add(current_word)

            # if trie.word_in_trie(current_word):
            #     if trie.search(current_word):
            #         output.add(current_word)

                for new_r, new_c in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0<=new_r<len(board) and 0<=new_c<len(board[0]):
                        dfs(new_r, new_c, [current_word], visited.copy(), current[board[r][c]].children)

        output = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                print(r,c,board[r][c])
                current = trie.root
                dfs(r, c, [], defaultdict(bool), current.children)
        
        return output
```

## Time Limit Exceeded
然而此解會遭遇**Time Limit Exceeded**，當遇到大量重複再重複的`chr`時。
```
graph = [["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"],["a","a","a","a","a","a","a","a","a","a","a","a"]]
words = ["lllllll","fffffff","ssss","s","rr","xxxx","ttt","eee","ppppppp","iiiiiiiii","xxxxxxxxxx","pppppp","xxxxxx","yy","jj","ccc","zzz","ffffffff","r","mmmmmmmmm","tttttttt","mm","ttttt","qqqqqqqqqq","z","aaaaaaaa","nnnnnnnnn","v","g","ddddddd","eeeeeeeee","aaaaaaa","ee","n","kkkkkkkkk","ff","qq","vvvvv","kkkk","e","nnn","ooo","kkkkk","o","ooooooo","jjj","lll","ssssssss","mmmm","qqqqq","gggggg","rrrrrrrrrr","iiii","bbbbbbbbb","aaaaaa","hhhh","qqq","zzzzzzzzz","xxxxxxxxx","ww","iiiiiii","pp","vvvvvvvvvv","eeeee","nnnnnnn","nnnnnn","nn","nnnnnnnn","wwwwwwww","vvvvvvvv","fffffffff","aaa","p","ddd","ppppppppp","fffff","aaaaaaaaa","oooooooo","jjjj","xxx","zz","hhhhh","uuuuu","f","ddddddddd","zzzzzz","cccccc","kkkkkk","bbbbbbbb","hhhhhhhhhh","uuuuuuu","cccccccccc","jjjjj","gg","ppp","ccccccccc","rrrrrr","c","cccccccc","yyyyy","uuuu","jjjjjjjj","bb","hhh","l","u","yyyyyy","vvv","mmm","ffffff","eeeeeee","qqqqqqq","zzzzzzzzzz","ggg","zzzzzzz","dddddddddd","jjjjjjj","bbbbb","ttttttt","dddddddd","wwwwwww","vvvvvv","iii","ttttttttt","ggggggg","xx","oooooo","cc","rrrr","qqqq","sssssss","oooo","lllllllll","ii","tttttttttt","uuuuuu","kkkkkkkk","wwwwwwwwww","pppppppppp","uuuuuuuu","yyyyyyy","cccc","ggggg","ddddd","llllllllll","tttt","pppppppp","rrrrrrr","nnnn","x","yyy","iiiiiiiiii","iiiiii","llll","nnnnnnnnnn","aaaaaaaaaa","eeeeeeeeee","m","uuu","rrrrrrrr","h","b","vvvvvvv","ll","vv","mmmmmmm","zzzzz","uu","ccccccc","xxxxxxx","ss","eeeeeeee","llllllll","eeee","y","ppppp","qqqqqq","mmmmmm","gggg","yyyyyyyyy","jjjjjj","rrrrr","a","bbbb","ssssss","sss","ooooo","ffffffffff","kkk","xxxxxxxx","wwwwwwwww","w","iiiiiiii","ffff","dddddd","bbbbbb","uuuuuuuuu","kkkkkkk","gggggggggg","qqqqqqqq","vvvvvvvvv","bbbbbbbbbb","nnnnn","tt","wwww","iiiii","hhhhhhh","zzzzzzzz","ssssssssss","j","fff","bbbbbbb","aaaa","mmmmmmmmmm","jjjjjjjjjj","sssss","yyyyyyyy","hh","q","rrrrrrrrr","mmmmmmmm","wwwww","www","rrr","lllll","uuuuuuuuuu","oo","jjjjjjjjj","dddd","pppp","hhhhhhhhh","kk","gggggggg","xxxxx","vvvv","d","qqqqqqqqq","dd","ggggggggg","t","yyyy","bbb","yyyyyyyyyy","tttttt","ccccc","aa","eeeeee","llllll","kkkkkkkkkk","sssssssss","i","hhhhhh","oooooooooo","wwwwww","ooooooooo","zzzz","k","hhhhhhhh","aaaaa","mmmmm"]
```
原因在於我們重複查找樹內文字，而已查過的文字其實可以從樹中移除，來讓後續查找越來越快。
### 刪除已成功查找
加入`Trie().remove()`後顯著改善運行效率。
```python
from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(bool)
        self.isEnd = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, key):
        current = self.root
        for _chr in key:
            if current.children[_chr]:
                current = current.children[_chr]
            else:
                current.children[_chr] = TrieNode()
                current = current.children[_chr]
        current.isEnd = True

    def search(self, key):
        current = self.root
        for _chr in key:
            if current.children[_chr]:
                current = current.children[_chr]
            else:
                return False
        return current.isEnd

    def word_in_trie(self, key):
        current = self.root
        for _chr in key:
            current = current.children[_chr]
            if not current:
                return False
        return True
    
    def list_words(self):
        current = self.root
        
        def dfs(current, word_snake):
            if not current: return
            
            for k, v in current.items():
                if v:
                    if current[k].isEnd:
                        output.append(
                            ''.join(word_snake+[k])
                        )
                    if current[k].children:
                        dfs(current[k].children, word_snake+[k])        
        
        output = []
        dfs(current.children, [])
        
        return output
    
    def remove(self, key):

        def recursive_down(current, i, key):
            if i == len(key):
                if all(v==False for v in current.children.values()):
                    return False
                else:
                    return current

            current.children[key[i]] = recursive_down(
                current.children[key[i]], i+1, key
            )
            return current

        current = self.root
        current.children[key[0]] = recursive_down(
            current.children[key[0]], 1, key
        )
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        def dfs(r, c, word_snake=[], visited=defaultdict(), current=TrieNode().children):
            if visited[(r,c)]:
                return
            visited[(r,c)] = True
            
            word_snake.append(board[r][c])
            current_word = ''.join(word_snake)

            if current[board[r][c]]:
                if current[board[r][c]].isEnd:
                    output.add(current_word)
                    trie.remove(current_word)

            # if trie.word_in_trie(current_word):
            #     if trie.search(current_word):
            #         output.add(current_word)

                for new_r, new_c in [(r+1,c), (r-1,c), (r,c+1), (r,c-1)]:
                    if 0<=new_r<len(board) and 0<=new_c<len(board[0]) and current[board[r][c]]:
                        dfs(new_r, new_c, [current_word], visited.copy(), current[board[r][c]].children)

        output = set()
        for r in range(len(board)):
            for c in range(len(board[0])):
                current = trie.root
                dfs(r, c, [], defaultdict(bool), current.children)
        
        return output
```