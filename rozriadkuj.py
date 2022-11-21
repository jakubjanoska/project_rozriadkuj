with open('git_codes.txt', encoding='utf-8') as soubor:
    text = soubor.read()

    ssplit = text.split()
    for word in ssplit:
        if 'git' in word:
            print ('\n', 'git', end=' ')
        else:
            #word.rstrip()
            print (word, end=' ')

    
    

    
