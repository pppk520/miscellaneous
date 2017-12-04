class Solution:
    # @param start : string
    # @param end : string
    # @param dictV : list of strings
    # @return an integer
    def ladderLength(self, start, end, dictV):
        if start == end:
            return 1

        queue = [start]

        count = 1
        visited = set()

        while len(queue) > 0:
            tmp_queue = []

            while len(queue) > 0:
                word = queue.pop(0)

                if self.word_diff(word, end) == 1:
                    return count + 1

                visited.add(word)
                for neighbor in self.adj(word, dictV):
                    if neighbor in visited:
                        continue

                    tmp_queue.append(neighbor)

            queue = tmp_queue
            count += 1

        return 0

    def word_diff(self, w1, w2):
        diff = 0

        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1

        return diff

    def adj(self, word, d):
        ll = []

        for w in d:
            if self.word_diff(word, w) == 1:
                ll.append(w)

        return ll
            

print(Solution().ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))
