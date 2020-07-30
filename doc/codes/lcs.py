def LCS(text1, text2):
    '''
    text1, text2 : two string or list of strings.
    return: list of similar characters or strings.
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
                # LCS(i,j) = LCS(i-1, j-1) ^ text1[i]
                table[indx(i)][indx(j)] = table[indx(i-1)][indx(j-1)] + [text1[i]]
            else:
                # LCS(i, j) = max(LCS(i, j-1), LCS(i-1, j))
                table[indx(i)][indx(j)] = max(table[indx(i)][indx(j-1)], table[indx(i-1)][indx(j)], key= lambda x:len(x))
    
    return table[n][m]
