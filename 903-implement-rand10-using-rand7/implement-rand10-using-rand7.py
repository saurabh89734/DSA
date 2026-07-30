class Solution:
    def rand10(self):
        while True:
            num = (rand7() - 1) * 7 + rand7()   # 1 to 49

            if num <= 40:
                return (num - 1) % 10 + 1