


class RomanNumbers:

    def toInt(self, s:str)->int:
        
        if( not hasattr(self, "symbols")):
            self.symbols = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        s = list(s) if not isinstance(s, list) else s
        lenOfString = len(s)
        if lenOfString == 1:
            return self.symbols[s[0]]
        else:
            leftPart = s[:lenOfString//2]
            rightPart = s[lenOfString//2:]

            memory = 0
            if(self.symbols[leftPart[-1]] < self.symbols[rightPart[0]] and lenOfString > 2):
                memory = self.symbols[rightPart[0]] - self.symbols[leftPart[-1]]
                leftPart.pop(-1)
                rightPart.pop(0)

            romanToIntLeft = self.toInt(leftPart) + memory if (len(leftPart)>0) else memory
            romanToIntRigth = self.toInt(rightPart)

            if(romanToIntLeft < romanToIntRigth and len(rightPart) == 1):
                return romanToIntRigth - romanToIntLeft
            else:
                return romanToIntLeft + romanToIntRigth


    def IntTo(self, num:int)->str:

        if(num > 0):

            if( not hasattr(self, "datas")):
                self.datas = {
                    'symbols': ["I", "V", "X", "L", "C", "D", "M"],
                    'intToRoman': {1:"I", 5:"V", 10:"X", 50:"L", 100:"C", 500:"D", 1000:"M"},
                    'romanToInt': {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000},
                    'intervals': [[0, 1], [1, 5], [2, 10], [3, 50], [4, 100], [5, 500], [6, 1000]]
                }
                self.witness = False

            interval = []
            for val in self.datas["intervals"]:
                if(num < val[1]):
                    interval.append(val)
                    break
                elif(num == val[1]):
                    return self.datas["intToRoman"][val[1]]
                else:
                    interval = [val]
                    
            if len(interval) == 1:
                interval.append(self.datas["intervals"][-1])

            div = num // interval[0][1]
            rest = num % interval[0][1]

            if(div==4):
                self.witness = True
                if(interval[0][1] == self.datas["intervals"][-1][1]):
                    romanNumber = div * self.datas["symbols"][interval[0][0]]
                else:
                    item = interval[1][0] + 1 if interval[1][0] + 1 < len(self.datas["symbols"]) and not self.witness else interval[1][0]
                    romanNumber = self.datas["symbols"][interval[0][0]] + self.datas["symbols"][item]

                romanNumber += self.IntTo(rest)
                self.witness = True
            else:
                romanNumber = (div * self.datas["symbols"][interval[0][0]]) + self.IntTo(rest)

                if(self.witness and len(romanNumber) >= 3):
                    if(romanNumber[0] == romanNumber[2] and self.datas["romanToInt"][romanNumber[2]] * 2 in self.datas["intToRoman"]):
                        romanNumber = romanNumber[1:]
                        romanNumber = romanNumber.replace(romanNumber[1], self.datas["intToRoman"][self.datas["romanToInt"][romanNumber[1]] * 2])
                    elif(self.datas["romanToInt"][romanNumber[0]] < self.datas["romanToInt"][romanNumber[2]]):
                        romanNumber = romanNumber[1:]
                        
                    self.witness = False
            
            return romanNumber
        else:
            return ''


roman = RomanNumbers()

# with open("romanToInt.txt", "w+") as file:
#     for i in range(1, 40000):
#         file.write(f"{i} => {roman.IntTo(i)}\n")

# print(f"9 => {roman.IntTo(9)}")
# print(f"90 => {roman.IntTo(90)}")
# print(f"900 => {roman.IntTo(900)}")
# print(f"9015 => {roman.IntTo(9015)}")
# print(f"44 => {roman.IntTo(44)}")
# print(f"40 => {roman.IntTo(40)}")
# print(f"400 => {roman.IntTo(400)}")
# print(f"4225 => {roman.IntTo(4225)}")
# print(f"225 => {roman.IntTo(225)}")
# print(f"2425 => {roman.IntTo(2425)}")
# print(f"425 => {roman.IntTo(425)}")
# print(f"1994 => {roman.IntTo(1994)}")
# print(f"92 => {roman.IntTo(92)}")
# print(f"3129 => {roman.IntTo(3129)}")
# print(f"58 => {roman.IntTo(58)}")
# print(f"95 => {roman.IntTo(95)}")


# assert(roman.IntTo(1994) == "MCMXCIV")
# assert(roman.IntTo(92) == "XCII")
# assert(roman.IntTo(3129) == "MMMCXXIX")
# assert(roman.IntTo(53) == "LIII")
# assert(roman.IntTo(97) == "XCVII")

# print(roman.toInt("DCDV"))
# print(roman.toInt("LXLV"))
# print(roman.toInt("CMV"))

assert(roman.toInt("DCDV") == 905), "Error"
assert(roman.toInt("DLXXXI") == 581), "Error"
assert(roman.toInt("MMMMMCDXXV") == 5425), "Error"
assert(roman.toInt("MMDXV") == 2515), "Error"
assert(roman.toInt("MMDCV") == 2605), "Error"
assert(roman.toInt("MMDCVI") == 2606), "Error"
assert(roman.toInt("MMCCCXCIX") == 2399), "Error"
assert(roman.toInt("MMCDXXV") == 2425), "Error"
assert(roman.toInt("MCMXCIV") == 1994), "Error"
assert(roman.toInt("MCMXCI") == 1991), "Error"
assert(roman.toInt("XCIV") == 94), "Error"
assert(roman.toInt("XCI") == 91), "Error"
assert(roman.toInt("DXCI") == 591), "Error"
assert(roman.toInt("LVI") == 56), "Error"
assert(roman.toInt("LVIII") == 58), "Error"
assert(roman.toInt("III") == 3), "Error"
assert(roman.toInt("I") == 1), "Error"
assert(roman.toInt("II") == 2), "Error"
assert(roman.toInt("IV") == 4), "Error"

