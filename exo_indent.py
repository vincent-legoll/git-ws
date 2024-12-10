#!/usr/bin/env python3

# on peut avoir des commentaires moisis

def affiche(message):
    print('Vous avez reçu un message...')
    print('  Voici le contenu:')
    print('  ' + message)

def main():
    affiche('Salut Jules!')
    affiche("Comment qu'c'est, gros ?")

if __name__ == '__main__':
    main()

