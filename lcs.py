'''
Implementing longest common sequence using Dynamic programming.
Take two file as an input and will find longest common sequence of
words in that.
'''

def LCS(text1, text2):
    '''
    text1, text2 : two string or list of strings.
    return: list of similar characters of strings.
    '''
    n = len(text1)
    m = len(text2)

    # create (n+1)*(m+1) table
    table = [[[]]*(m+1)]*(n+1)

    # map index of texts to table
    indx = lambda i: i+1 
    
    for i in range(n):
        for j in range(m):
            if text1[i] == text2[j]:
                # LCS(i,j) = LCS(i-1, j-1) + 1
                table[indx(i)][indx(j)] = table[indx(i-1)][indx(j-1)] + [text1[i]]
            else:
                # LCS(i, j) = max(LCS(i, j-1), LCS(i-1, j))
                table[indx(i)][indx(j)] = max(table[indx(i)][indx(j-1)], table[indx(i-1)][indx(j)], key= lambda x:len(x))
    # s = set()
    # for i in range(n + 1):
    #     for j in range(m + 1):
    #         s.add(id(table[i][j]))
    # print("number of distint lists: %s" % len(s))
    # print(len(s)/(len(text1)* len(text2)))
    
    return table[n][m]

def dist_finder(text, words):
    counter = 0
    dist_list = []
    for i, word in enumerate(text):
        if len(words) == counter:
            break
        if words[counter] == word:
            dist_list.append(i)
            counter += 1
    return dist_list

def sim_score(t1, t2, lcs):
    '''
    t1: list of words
    t2: list of words
    lcs: longest common sequence of t1 and t2
    return: similarity rate and including rate.'''
    rate = len(lcs)/(len(t1)+len(t2)-len(lcs))

    return rate


def depend_score(t1, t2, lcs):
    '''
    t1: list of words
    t2: list of words
    lcs: longest common sequence of t1 and t2
    return: dependency socore of t1 on t2'''
    return len(lcs)/len(t1)

