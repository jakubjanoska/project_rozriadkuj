with open('git_codes.txt', encoding='utf-8') as soubor:
    text = soubor.read()

    ssplit = text.split()
    zoznam = []  #bude zoznam dvojic (prikaz, popis)
    prikaz = ""
    popis = ''
    #PrikazPrazdny, PopisPrazdny = True
    for slovo in ssplit:
        if '#' in slovo:
            prikaz = text
            text = slovo + ' '
        #elif 'git' not in slovo:
        #    prikaz = prikaz + slovo + " "
        elif 'git' in slovo:
            zoznam.append((prikaz, text))
            prikaz = " "
            text = slovo + ' '   
        else:
            text = text + slovo + " "
            
    print(*zoznam, sep='\n')

