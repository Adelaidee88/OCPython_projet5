import sys
from database import *


class Cli(object):

    def __init__(self):
        self.database = Database()

    def main(self):
        response = self.main_question()
        if response == 1:
            self.display_category()
            category = self.choose_category()
            self.display_aliments(category)
            aliment = self.choose_aliment()
            self.database.show_aliment(aliment, category)
            # voulez vous ajouter l'aliment à votre liste personnelle ?
        else:
            self.show_category()

    def main_question(self):
        # self.display_subs_aliment()
        try:
            print("1 - Quel aliment souhaitez-vous remplacer ?")
            print("2 - Retrouver mes aliments substitués.")
            get_input = input()
            int_input = int(get_input)
            if int_input == 1 or int_input == 2:
                return int_input
            else:
                return self.main_question()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            return self.main_question()

    def display_category(self):
        to_print = self.database.get_category()
        for i in range(0, len(to_print)):
            print(i + 1, to_print[i])

    def display_aliments(self, category):
        to_print = self.database.get_aliments(category)  # récupérer la catégorie de l'input du choix de catégorie
        for i in range(0, len(to_print)):
            print(i + 1, to_print[i])

    def choose_category(self):
        try:
            print("Choissez votre catégorie")
            get_input = input()
            int_input = int(get_input) - 1
            if 0 <= int_input <= 3:
                return self.database.get_category()[int_input][0]
            else:
                return self.choose_category()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            return self.choose_category()

    def choose_aliment(self):
        try:
            print("Choissez votre aliment")
            get_input = input()
            int_input = int(get_input) - 1
            if 0 <= int_input <= 19:
                return int_input
            else:
                return self.choose_category()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            return self.choose_category()

    def show_substitutes(self, category, aliment):
        try:
            # appel BDD pour liste des catégories : noms des tables
            # affichées avec 1, 2, 3 etc
            get_input = input()
            int_input = int(get_input)
            if int_input >= 1 and int_input <=10:
                # changer selon le nombre d'aliments
                return self.show_substitutes()
            self.add_favorite(int_input)
            #  rechercher le nom de l'aliment dans la table
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
