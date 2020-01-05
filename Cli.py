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
            aliment = self.choose_aliment(category)
            chosen_aliment = self.database.show_aliment(aliment, category)
            subs_aliment = self.subs_aliment(chosen_aliment, category)
            print("Voulez-vous enregister ce produit et son substitut dans "
                  "vos favoris ? O/N")
            get_input = str(input())
            if get_input == "O" or get_input == "o":
                self.database.add_favorite(aliment, str(subs_aliment[0]))
            self.main()
        else:
            self.show_substitutes()
            self.main()

    def main_question(self):
        try:
            print("Bienvenue chez Pur Beurre !")
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
            print("Un nombre est attendu, merci. Recommencez")
            return self.main_question()

    def display_category(self):
        to_print = self.database.get_category()
        for i in range(0, len(to_print)):
            print(i + 1, "-", str(to_print[i])[2:-3])

    def display_aliments(self, category):
        to_print = self.database.get_aliments(category)
        for i in range(0, len(to_print)):
            print("{} - {}".format(to_print[i][0], to_print[i][1]))

    def choose_category(self):
        try:
            print("Choissez votre catégorie.")
            get_input = input()
            int_input = int(get_input) - 1
            if 0 <= int_input <= 7:
                return self.database.get_category()[int_input][0]
            else:
                print("Ce n'est pas une catégorie valable")
                self.display_category()
                category = self.choose_category()
                self.display_aliments(category)
                aliment = self.choose_aliment(category)
                chosen_aliment = self.database.show_aliment(aliment, category)
                subs_aliment = self.subs_aliment(chosen_aliment, category)
                print("Voulez-vous enregister ce produit et son substitut dans "
                      "vos favoris ? O/N")
                get_input = str(input())
                if get_input == "O" or get_input == "o":
                    self.database.add_favorite(aliment, str(subs_aliment[0]))
                self.main()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            self.display_category()
            category = self.choose_category()
            self.display_aliments(category)
            aliment = self.choose_aliment(category)
            chosen_aliment = self.database.show_aliment(aliment, category)
            subs_aliment = self.subs_aliment(chosen_aliment, category)
            print("Voulez-vous enregister ce produit ? O/N")
            get_input = str(input())
            if get_input == "O" or get_input == "o":
                self.database.add_favorite(aliment, str(subs_aliment[0]))
            self.main()

    def choose_aliment(self, category):
        try:
            print("Choissez l'aliment que vous aimeriez remplacer.")
            get_input = input()
            int_input = int(get_input)
            id_cat = self.database.get_id_cat(category)
            if id_cat[0][0] <= int_input <= id_cat[len(id_cat) - 1][0]:
                return int_input
            else:
                print("l'input n'est pas bon.")
                self.display_aliments(category)
                aliment = self.choose_aliment(category)
                chosen_aliment = self.database.show_aliment(aliment, category)
                subs_aliment = self.subs_aliment(chosen_aliment, category)
                print("Voulez-vous enregister ce produit  et son substitut "
                      "dans vos favoris ? O/N")
                get_input = str(input())
                if get_input == "O" or get_input == "o":
                    self.database.add_favorite(aliment, str(subs_aliment[0]))
                self.main()
        except EOFError:
            print("C'est pas ça qu'il faut faire !!!")
            sys.exit()
        except:
            print("Une erreur est survenue, l'input n'est pas bon.")
            self.display_aliments(category)
            aliment = self.choose_aliment(category)
            chosen_aliment = self.database.show_aliment(aliment, category)
            subs_aliment = self.subs_aliment(chosen_aliment, category)
            print("Voulez-vous enregister ce produit ? O/N")
            get_input = str(input())
            if get_input == "O" or get_input == "o":
                self.database.add_favorite(aliment, str(subs_aliment[0]))
            self.main()

    def show_substitutes(self):
        to_print = self.database.show_favorites()
        for cle, valeur in to_print.items():
            print("{} est substitué par {}, dont le nutriscore est {}. \n On "
                  "peut le trouver dans ces magasins : {}. \n Pour plus "
                  "d'informations, son lien vers "
                  "OpenFoodFacts : {} \n".format(cle, valeur[1], valeur[4],
                                                 valeur[3][1:-1], valeur[5]))

    def subs_aliment(self, aliment, category):
        list_alim = self.database.list_aliments(category)
        nutriscore = aliment[4]
        save_id = -1
        good = False
        for subs in list_alim:
            if subs[4] < nutriscore:
                nutriscore = subs[4]
                save_id = subs[0]
            else:
                if aliment[4] == "a":
                    good = True
        if good:
            print("Votre aliment est le plus sain.")
            for subs in list_alim:
                if subs[4] == "a" and subs != aliment:
                    print("mais voici un aliment équivalent à "
                          "substituer : {}".format(subs[1]))
                    save_id = subs[0]
                    return self.database.my_aliment(save_id)
        if save_id == -1:
            print("Il n'y a pas d'aliment plus sain à proposer.")
            return aliment
        elif save_id != -1:
            print("Voici l'aliment le plus sain : {}, "
                  "avec un nutriscore de "
                  "{}".format(self.database.my_aliment(save_id)[1],
                              self.database.my_aliment(save_id)[4]))
        return self.database.my_aliment(save_id)


cli = Cli()
cli.main()
