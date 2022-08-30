

def trie_fusion(tab):
    L = len(tab)
    if(L > 2):
        left = trie_fusion(tab[:L//2])
        right = trie_fusion(tab[L//2:])

        result = []
        i = 0
        while(i < len(left)):
            j = 0
            while(j < len(right)):
                if(left[i] < right[j]):
                    result.append(left[i])
                    left.pop(i)
                    i -= 1
                    break
                elif(left[i] > right[j]):
                    result.append(right[j])
                    right.pop(j)
                    j -= 1
                j += 1
            i += 1

        return result + left + right
    else:
        if(len(tab) == 2):
            if(tab[0] > tab[1]):
                memory = tab[0]
                tab[0] = tab[1]
                tab[1] = memory            
        return tab

t = [102, 25, 3, 3, 5, 8, 11, 16, 22, 2, 15, 1, 12, 6, 10, 1, 4, 7, 9, 0, 20, 17, 90]
print(trie_fusion(t))     
