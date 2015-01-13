n, m = map(int, input().split())


def affiche_nombres(n, m):
    if n > m:
        return None
    else:
        print(n, end=" ")
        return affiche_nombres(n+1, m)

affiche_nombres(n, m)
