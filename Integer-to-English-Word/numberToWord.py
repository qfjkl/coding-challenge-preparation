import time

class Solution:
    def numberToWords(self, num: int) -> str:
        if(not hasattr(self, "digits")):
            self.digits = {0:"Zero", 1:"One", 2:"Two", 3:"Three", 4:"Four",
                            5:"Five", 6:"Six",7:"Seven",8:"Eight",9:"Nine",10:"Ten",11:"Eleven",12:"Twelve",13:"Thirteen",14:"Fourteen",
                            15:"Fifteen",16:"Sixteen",17:"Seventeen",18:"Eighteen",19:"Nineteen",20:"Twenty",30:"Thirty",
                            40:"Forty",50:"Fifty",60:"Sixty",70:"Seventy",80:"Eighty",90:"Ninety",100:"Hundred",
                            1000:"Thousand",1000_000:"Million",1000_000_000:"Billion",
                            "max_digits": [10, 100, 1000, 1000_000, 1000_000_000]   
                        }
        
        if(num>0):
            
            if(num in self.digits and num not in range(self.digits["max_digits"][1], self.digits["max_digits"][-1]+1)):
                return self.digits[num]
            else:
                interval = []
                for digit in self.digits["max_digits"]:
                    if(num>digit):
                        interval = [digit]
                    elif(num<digit):
                        interval.append(digit)
                        break
                    else:
                        interval = [digit, digit]
                        break

                div = num // interval[0]
                mod = num % interval[0]
                witness = False
                if(interval[0] in self.digits["max_digits"][1:]):
                    word = self.numberToWords(div) 
                    witness = True
                else:
                    interval[0] *= div
                    word = ''  
                word += f" {self.digits[interval[0]]}" if witness else f"{self.numberToWords(interval[0])}"
                word += f" {self.numberToWords(mod)}" if mod > 0 else ""
                
                return word
        else:
            return self.digits[0]
    
    def WordToNumber(self, num:str) -> int:
        num = num.strip().split(' ')
        c = 0
        while(c<len(num)):
            if(c+1 < len(num)):

                pass


solution = Solution()
start = time.time()
with open('numberWord.txt', 'w+') as file:
    for i in range(0, 11000):
        file.write(f"{i} => {solution.numberToWords(i)}\n")

end = time.time()
f = end - start
print(f)
print(solution.numberToWords(4_000_000_014))