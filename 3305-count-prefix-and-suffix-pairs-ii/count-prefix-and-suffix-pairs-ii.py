class Node:
    def __init__(self):
        self.children = {}
        self.count = 0


class Solution:
    def countPrefixSuffixPairs(self, words):
        root = Node()
        ans = 0

        for word in words:
            node = root

            for i in range(len(word)):
                pair = (word[i], word[-1 - i])

                if pair not in node.children:
                    node.children[pair] = Node()

                node = node.children[pair]

                # Previous words ending here
                ans += node.count

            # Current word insert
            node.count += 1

        return ans