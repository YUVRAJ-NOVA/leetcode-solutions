class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        n = len(words)
        record = dict()
        result = []
        for word in words:
            if word not in record:
                record[word] = 1
            else:
                record[word] = record[word] +1
        for i in range(k):
            max_count = max(record.values())
            best_word = min(w for w, c in record.items() if c == max_count)
            result.append(best_word)
            del record[best_word]
        return result