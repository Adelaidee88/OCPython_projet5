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
            chosen_aliment = self.database.show_aliment(aliment, category)
            print("Voulez-vous enregister votre produit de substitution ? O/N")
            get_input = input()
            if get_input == "O" or get_input == "o":
                self.database.add_favorite(chosen_aliment)
            self.main()
        else:
            self.show_substitutes()
            self.main()

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

    def show_substitutes(self):
        to_print = self.database.show_favorites()
        for i in range(0, len(to_print)):
            print(i + 1, to_print[i])



cli = Cli()
cli.main()

# trouver comment ne pas afficher les favoris quand choix
# finir show substitutes (pas besoin d'input dedans, on veut juste la montrer)
