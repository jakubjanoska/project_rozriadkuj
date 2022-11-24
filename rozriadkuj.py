"""
Cvičný program. 
Zoberie vstupný text (text vykopírovaný z PDF https://programmingwithmosh.com/wp-content/uploads/2020/09/Git-Cheat-Sheet.pdf)
a vytvorí z neho tabulku v dokumente  (v predpotopnom) .html
Tabulka nie je dokonalá, bol som zvedavý, či to zvádnem roztriediť. 
Následne test (a hladanie chýb) pri printe do .html
"""

with open('git_codes.txt', encoding='utf-8') as soubor:
    vstup = soubor.read()

    ssplit = vstup.split()
    zoznam = []  #bude zoznam dvojic (prikaz, popis)
    prikaz = ''
    popis = ''
    text = ''
    for slovo in ssplit:
        if '#' in slovo:
            prikaz = text
            text = slovo + ' '
        elif 'git' in slovo:
            prikaz = '<tr> <td>' +prikaz + '</td>'
            text = '<td>' + text + '</td></tr>'
            zoznam.append((prikaz, text))
            prikaz = " "
            text = slovo + ' '   
        else:
            text = text + slovo + " "

with open('tab3.html', mode='w', encoding='utf-8') as vysledok:
    print('<!DOCTYPE html> <head> <title> Tabulka prikazu </title> </head> <body> Tu snad mozem nieco napisat', file=vysledok)
    print('<table border="1">', file=vysledok)
    for radek in zoznam:
        for blok in radek:
            print(blok, sep='', file=vysledok)
    print('</table> </body> </html>', file=vysledok)
