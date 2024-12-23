# %%
from typing import List

# %%
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        letters, digits = [], []
        for log in logs:
            # print(log.split())
            # print(log.split()[1])
            # print()
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)

        letters.sort(key=lambda x: (x.split()[1:], x.split()[0]))
        return letters + digits

# %%
if __name__ == "__main__":
    logs: List[str] = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(logs)
    soln = Solution()
    reordered_logs: List[str] = soln.reorderLogFiles(logs)
    print(reordered_logs)


