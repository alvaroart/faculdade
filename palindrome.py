palavra = input('Palavra: ')

palavra = palavra.casefold()

rev = palavra.casefold()[::-1]

palavra = palavra.replace(' ', '')
rev = rev.replace(' ', '')

#print ("\n\n", rev, "\n\n")

#print ("\n\n", rev, "\n\n")
#print (palavra. (' ', '')())

if palavra == rev:
    print('%s é Palíndrome' %palavra)
else:
    print('%s não é Palíndrome' %rev)
