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
            self.subs_aliment(chosen_aliment, category)
            subs_aliment = self.subs_aliment(chosen_aliment, category)
            # mettre un if : proposer la substitution si y a un produit, sinon retour au début
            print("Voulez-vous enregister votre produit de substitution ? O/N")
            get_input = input()
            if get_input == "O" or get_input == "o":
                self.database.add_favorite(subs_aliment, category)
            self.main()
        else:
            self.show_substitutes()
            self.main()

    def main_question(self):
        try:
            print("1 - Quel aliment souhaitez-vous remplacer ?")
            print("2 - Retrouver mes aliments substitués.")
            get_input = input()
            int_input = int(get_input)
            if int_input == 1 or int_input == 2:
                return int_input
            else:
                print("Cette valeur n'est pas un choix valable. Recommencez.")
                return self.main_question()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Un chiffre est attendu, merci. Recommencez")
            return self.main_question()

    def display_category(self):
        to_print = self.database.get_category()
        for i in range(0, len(to_print)):
            print(i + 1, to_print[i])

    def display_aliments(self, category):
        to_print = self.database.get_aliments(category)
        for i in range(0, len(to_print)):
            print(i + 1, to_print[i])

    def choose_category(self):
        try:
            print("Choissez votre catégorie")
            get_input = input()
            int_input = int(get_input) - 1
            if 0 <= int_input <= 4:  # pas oublier de mettre au nb de catégorie
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
            int_input = int(get_input)
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

    def subs_aliment(self, aliment, category):
        list_alim = self.database.list_aliments(category)
        nutriscore = aliment[3]
        save_id = -1
        good = False
        for subs in list_alim:
            if subs[3] < nutriscore:
                nutriscore = subs[3]
                save_id = subs[0] - 1  # index liste commence à 0, id table à 1
            else:
                if aliment[3] == "a":
                    good = True
        if save_id == -1:
            print("Il n'y a pas d'aliment plus sain à proposer.")
        if good:
            print("Votre aliment est le plus sain.")
            for subs in list_alim:
                if subs[3] == "a" and subs != aliment:
                    print("mais voici un aliment équivalent à substituer :",
                          subs)
                    save_id = subs[0] - 1  # index lst commence à 0, id tbl à 1
        else:
            print("Voici l'aliment le plus sains à substituer :",
                  list_alim[save_id])
        return list_alim[save_id]


cli = Cli()
cli.main()

# empecher de refill
#
# arranger la visualisation
