

class LetterCounter():
    letters_pos_1 = {0: 0, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3,
                     11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}
    letters_pos_2 = {0:0, 2:6, 3:6, 4:5, 5:5, 6:5, 7:7, 8:6, 9:6}
    letters_total = 0

    def __init__(self, n):
        self.n = str(n)
        self.find_total()
        return

    def __str__(self):
        return(str(self.letters_total))

    def find_total(self):
        if len(self.n) <= 2:
            self.letters_total = self.count_letters(self.n)
        elif len(self.n) == 3:
            self.letters_total = self.count_letters(self.n[-3])
            self.letters_total += 7  ##hundred
            if not int(self.n[-2:]) == 0: ## test for 'and'
                self.letters_total += self.count_letters(self.n[-2:])
                self.letters_total += 3
        elif len(self.n) == 4:
            self.letters_total = 11
        return

    def total(self):
        return(self.letters_total)


    def count_letters(self, n):
        tmp_val = 0
        if len(n) == 1:
            n = "0"+n
        if n[-2] == "1":
            tmp_val = self.letters_pos_1[int(n)]
        else:
            tmp_val = self.letters_pos_1[int(n[-1])]
            tmp_val += self.letters_pos_2[int(n[-2])]
        return(tmp_val)

print(LetterCounter(342).total())

final = 0
for v in range(1, 1001):
    final += LetterCounter(v).total()
print(final)
