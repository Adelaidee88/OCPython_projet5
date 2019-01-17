import sys


class Cli(object):

    def __init__(self):
        pass

    def main(self):
        response = self.main_question()
        if response == 1:
            category = self.choose_category()
            self.show_category(category)
        else:
            self.display_subs_aliment()

    def main_question(self):
        try:
            print("1 - Quel aliment souhaitez-vous remplacer ?")
            print("2 - Retrouver mes aliments substitués.")
            get_input = input()
            int_input = int(get_input)
            if int_input != 1 and int_input != 2:
                return self.main_question()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            return self.main_question()
        return int_input

    def display_subs_aliment(self):
        # appel à la BDD
        print("Affichage de l'appel à la BDD")

    def choose_category(self):
        try:
            # appel BDD pour liste des catégories : noms des tables
            # affichées avec 1, 2, 3 etc
            get_input = input()
            int_input = int(get_input)
            if int_input >= 1 and int_input <=6:
                return self.choose_category()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            return self.choose_category()
        return int_input  # retourner la valeur du champ (pas une table)

    def show_category(self, category):
        try:
            # appel BDD pour liste des catégories : noms des tables
            # affichées avec 1, 2, 3 etc
            get_input = input()
            int_input = int(get_input)
            if int_input >= 1 and int_input <=10: # changer selon le nombre d'aliments
                return self.show_category()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            return self.show_category()
        return int_input  # retourner la valeur du champ selectionné

    def show_substitutes(self, category, aliment):
        try:
            # appel BDD pour liste des catégories : noms des tables
            # affichées avec 1, 2, 3 etc
            get_input = input()
            int_input = int(get_input)
            if int_input >= 1 and int_input <=10: # changer selon le nombre d'aliments
                return self.show_substitutes()
            self.add_favorite(int_input) #  rechercher le nom de l'aliment dans la table
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            return self.show_substitutes()
        return int_input  # retourner la valeur du champ selectionné

    def add_favorite(self):
        sql = "INSERT INTO IF NOT EXISTE favoris (name) VALUES (%s)"
        val = ("patate")

cli = Cli()
cli.main()
