chaine = input()

def reverse(chaine):

    if chaine == '':
        return ''  

    else:
        return chaine[-1] + reverse(chaine[:-1])


print(reverse(chaine))

