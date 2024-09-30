class trie_node:
    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


class Solution:
    def __init__(self):
        # Initialize the root node of the trie.
        self.root = trie_node()

    # Insert function for the word.
    def insert(self, word):
        node = self.root
        for c in word:
            # If new prefix, create a new trie node.
            if node.next[ord(c) - ord("a")] is None:
                node.next[ord(c) - ord("a")] = trie_node()
            # Increment the count of the current prefix.
            node.next[ord(c) - ord("a")].cnt += 1
            node = node.next[ord(c) - ord("a")]

    # Calculate the prefix count using this function.
    def count(self, s):
        node = self.root
        ans = 0
        # The ans would store the total sum of counts.
        for c in s:
            ans += node.next[ord(c) - ord("a")].cnt
            node = node.next[ord(c) - ord("a")]
        return ans

    def sumPrefixScores(self, words):
        N = len(words)
        # Insert words in trie.
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            # Get the count of all prefixes of given string.
            scores[i] = self.count(words[i])
        return scores