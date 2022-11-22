with open('git_codes.txt', encoding='utf-8') as soubor:
    text = soubor.read()

    ssplit = text.split()
    zoznam = []
    riadok = ""
    for word in ssplit:
        if 'git' not in word:
            riadok = riadok + word + " "
        elif 'git' in word:
            zoznam.append(riadok)
            riadok = word + " "
            
            
    print(*zoznam, sep='\n')

    """    if 'git' in word:
            print ('\n', 'git', end=' ')
        else:
            #word.rstrip()
            print (word, end=' ')
    """
