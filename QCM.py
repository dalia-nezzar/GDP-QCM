import random
from colorama import init, Fore, Back, Style


class QuizGestionProjet:
    def __init__(self):
        self.questions = [
            {
                "question": "Selon l'ISO, qu'est-ce qu'un projet ?",
                "choices": [
                    "Un ensemble d'actions récurrentes",
                    "Un processus unique avec des activités coordonnées et maîtrisées avec dates de début et fin",
                    "Une série de tâches sans contrainte de temps",
                    "Un ensemble de ressources dédiées"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "D'après le Standish Group, quel est le pourcentage de projets qui sont un succès total ?",
                "choices": [
                    "21%",
                    "42%",
                    "37%",
                    "50%"
                ],
                "correct": [2],
                "type": "unique"
            },
            {
                "question": "Quelles sont les deux principales causes d'échec d'un projet ?",
                "choices": [
                    "Manque de budget et manque de temps",
                    "Défaut de préparation et défaut de pilotage",
                    "Manque de ressources et problèmes techniques",
                    "Mauvaise communication et conflits d'équipe"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Qu'est-ce qu'un macroplanning ?",
                "choices": [
                    "Une liste détaillée de toutes les tâches",
                    "Un diagramme de Gantt simplifié montrant la trajectoire du projet",
                    "Un tableau des ressources disponibles",
                    "Un document de spécifications techniques"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Les ressources projet se divisent en combien de catégories ?",
                "choices": [
                    "3",
                    "4",
                    "2",
                    "5"
                ],
                "correct": [2],
                "type": "unique"
            },
            {
                "question": "Qu'est-ce qui donne du sens au projet ?",
                "choices": [
                    "Le budget",
                    "Les délais",
                    "Les enjeux",
                    "Les ressources"
                ],
                "correct": [2],
                "type": "unique"
            },
            {
                "question": "Pour définir la trajectoire d'un projet, quelle est la première étape dans la construction d'un macroplanning ?",
                "choices": [
                    "Poser les jalons connus",
                    "Poser la grille temporelle",
                    "Identifier les événements externes",
                    "Poser les différentes phases"
                ],
                "correct": [1],
                "type": "unique"
            },
            {
                "question": "Quels sont les éléments qu'il faut définir au début d'un projet selon le cours ?",
                "choices": [
                    "La Cible",
                    "Le Budget",
                    "Une Organisation",
                    "Une Trajectoire"
                ],
                "correct": [0, 1, 2, 3],
                "type": "multiple"
            },
            {
                "question": "Quelles sont les utilisations principales du macroplanning ?",
                "choices": [
                    "Préparer le projet et planifier les chantiers",
                    "Poser les jalons et communiquer",
                    "Analyser les risques",
                    "Gérer les congés des employés"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Quelles sont les caractéristiques des ressources dédiées dans un projet ?",
                "choices": [
                    "100% affectées au projet",
                    "Sous autorité hiérarchique ou matricielle du CdP",
                    "Affectation variable",
                    "Cas rare dans les projets"
                ],
                "correct": [0, 1, 3],
                "type": "multiple"
            },
            {
                "question": "Dans la construction d'un macroplanning, quelles sont les étapes correctes ?",
                "choices": [
                    "Poser la grille temporelle",
                    "Identifier les événements externes impactants",
                    "Définir le budget détaillé",
                    "Poser les jalons connus"
                ],
                "correct": [0, 1, 3],
                "type": "multiple"
            },
            {
                "question": "Quels sont les rôles essentiels dans une structuration classique d'équipe projet ?",
                "choices": [
                    "Sponsor",
                    "Chef de projet",
                    "Responsable de chantier",
                    "Responsable marketing"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Qu'est-ce qui caractérise un projet par rapport à une production récurrente ?",
                "choices": [
                    "Organisation transversale et temporaire",
                    "Résultat unique",
                    "Risques spécifiques et variables",
                    "Coûts fixes et maîtrisés"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Quels sont les pourcentages corrects concernant les projets selon le Standish Group ?",
                "choices": [
                    "37% de réussite",
                    "42% d'échec partiel",
                    "21% d'échec total",
                    "50% de réussite"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Quels sont les objectifs du cadrage d'un projet ?",
                "choices": [
                    "Définir les enjeux et objectifs",
                    "Identifier les livrables à produire",
                    "Identifier les chantiers",
                    "Organiser les vacances de l'équipe"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "D'après le cours, quelle est la meilleure définition d'un projet selon l'auteur ?",
                "choices": [
                    "Un ensemble d'actions à réaliser",
                    "Un processus unique d'activités",
                    "Un joli tas d'emmerdes",
                    "Une mission avec un début et une fin"
                ],
                "correct": [2],
                "type": "unique"
            },
            {
                "question": "Quels éléments caractérisent les ressources non dédiées d'un projet ?",
                "choices": [
                    "Affectées partiellement au projet",
                    "Pourcentage d'affectation peut être flou ou variable",
                    "Sous autorité matricielle",
                    "100% affectées au projet"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Les enjeux d'un projet sont essentiels car ils permettent de :",
                "choices": [
                    "Assurer que l'ensemble des galériens rament dans le même sens",
                    "Conserver la motivation quand le projet est difficile",
                    "Permettre de challenger les objectifs",
                    "Définir le salaire des employés"
                ],
                "correct": [0, 1, 2],
                "type": "multiple"
            },
            {
                "question": "Dans une structuration classique d'équipe projet, le sponsor est :",
                "choices": [
                    "Le gardien des enjeux",
                    "Le gardien des objectifs",
                    "Responsable d'un des sujets du projet",
                    "Chef de projet"
                ],
                "correct": [0],
                "type": "unique"
            },
            {
                "question": "Dans la construction d'un macroplanning, après avoir posé la grille temporelle, que faut-il identifier ?",
                "choices": [
                    "Les événements externes pouvant avoir un impact fort sur la disponibilité des ressources",
                    "Le budget détaillé du projet",
                    "Les technologies à utiliser",
                    "La composition de l'équipe"
                ],
                "correct": [0],
                "type": "unique"
            },
            {
                "question": "Un projet en opposition à une production récurrente est caractérisé par :",
                "choices": [
                    "Une organisation transversale",
                    "Une organisation temporaire",
                    "Des risques maîtrisés",
                    "Un résultat multiple"
                ],
                "correct": [0, 1],
                "type": "multiple"
            },
            {
                "question": "Le macroplanning doit servir à :",
                "choices": [
                    "Vérifier en permanence qu'on peut franchir les jalons",
                    "Vérifier qu'on peut atteindre l'objectif",
                    "Gérer les congés des équipes",
                    "Définir les salaires"
                ],
                "correct": [0, 1],
                "type": "multiple"
            },
            {
                "question": "Pourquoi est-il important de bien identifier les enjeux d'un projet ?",
                "choices": [
                    "Pour permettre l'adhésion",
                    "Pour assurer que les objectifs répondent aux enjeux",
                    "Pour définir les salaires",
                    "Pour planifier les congés"
                ],
                "correct": [0, 1],
                "type": "multiple"
            }
        ]
        self.score = 0
        self.questions_posees = 0

    def afficher_titre(self):
        print(f"\n{Back.BLUE}{Fore.BLACK}{'=' * 60}{Style.RESET_ALL}")
        print(f"{Back.BLUE}{Fore.BLACK}{'QUIZ DE GESTION DE PROJET':^60}{Style.RESET_ALL}")
        print(f"{Back.BLUE}{Fore.BLACK}{'=' * 60}{Style.RESET_ALL}\n")

    def afficher_question(self, numero, question):
        print(f"\n{Fore.CYAN}Question {numero + 1}:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{question['question']}{Style.RESET_ALL}")
        print(
            f"{Fore.MAGENTA}Type: {question['type'] == 'multiple' and 'Choix multiple' or 'Choix unique'}{Style.RESET_ALL}")
        for i, choix in enumerate(question["choices"]):
            print(f"{Fore.GREEN}{i + 1}.{Style.RESET_ALL} {choix}")

    def afficher_feedback_correct(self, message="Correct !"):
        print(f"\n{Back.GREEN}{Fore.BLACK} ✅ {message} {Style.RESET_ALL}")

    def afficher_feedback_incorrect(self, message="Incorrect."):
        print(f"\n{Back.RED}{Fore.BLACK} ❌ {message} {Style.RESET_ALL}")

    def afficher_reponses_correctes(self, question):
        print(f"{Fore.YELLOW}Les bonnes réponses étaient:{Style.RESET_ALL}", end=" ")
        reponses = [question['choices'][i] for i in question["correct"]]
        print(f"{Fore.GREEN}{', '.join(reponses)}{Style.RESET_ALL}")

    def poser_question(self, num_question):
        question = self.questions[num_question]
        self.afficher_question(self.questions_posees, question)

        if question["type"] == "unique":
            reponse = self.obtenir_reponse_unique()
            if [reponse - 1] == question["correct"]:
                self.afficher_feedback_correct()
                self.score += 1
            else:
                self.afficher_feedback_incorrect()
                self.afficher_reponses_correctes(question)
        else:
            reponses = self.obtenir_reponses_multiples()
            reponses_correctes = [i + 1 for i in question["correct"]]
            if sorted(reponses) == sorted(reponses_correctes):
                self.afficher_feedback_correct("Parfait ! Toutes les réponses sont correctes !")
                self.score += 1
            else:
                self.afficher_feedback_incorrect()
                self.afficher_reponses_correctes(question)

        self.questions_posees += 1

    def obtenir_reponse_unique(self):
        while True:
            try:
                print(f"\n{Fore.CYAN}Votre réponse (1-4):{Style.RESET_ALL}", end=" ")
                reponse = int(input())
                if 1 <= reponse <= 4:
                    return reponse
                print(f"{Fore.RED}Veuillez entrer un nombre entre 1 et 4.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Veuillez entrer un nombre valide.{Style.RESET_ALL}")

    def obtenir_reponses_multiples(self):
        while True:
            try:
                print(f"\n{Fore.CYAN}Vos réponses (séparées par des espaces, ex: 1 3 4):{Style.RESET_ALL}", end=" ")
                reponse = input()
                reponses = [int(x) for x in reponse.split()]
                if all(1 <= r <= 4 for r in reponses):
                    return reponses
                print(f"{Fore.RED}Veuillez entrer des nombres entre 1 et 4.{Style.RESET_ALL}")
            except ValueError:
                print(f"{Fore.RED}Veuillez entrer des nombres valides séparés par des espaces.{Style.RESET_ALL}")

    def afficher_resultats(self):
        print(f"\n{Back.BLUE}{Fore.BLACK}{'=' * 60}{Style.RESET_ALL}")
        print(f"{Fore.CYAN}Quiz terminé !{Style.RESET_ALL}")
        print(f"Score: {Fore.GREEN}{self.score}{Style.RESET_ALL}/{Fore.YELLOW}{self.questions_posees}{Style.RESET_ALL}")
        pourcentage = (self.score / self.questions_posees) * 100

        # Couleur du pourcentage basée sur le score
        couleur = Fore.RED
        if pourcentage >= 80:
            couleur = Fore.GREEN
        elif pourcentage >= 60:
            couleur = Fore.YELLOW

        print(f"Pourcentage de réussite: {couleur}{pourcentage:.1f}%{Style.RESET_ALL}")
        if pourcentage == 100:
            print(f"{Fore.GREEN}🎉🎉🎉 Parfait ! 🎉🎉🎉{Style.RESET_ALL}")
        elif pourcentage >= 60:
            print(f"{Fore.YELLOW}👍 Pas mal ! 👍{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}👎 Peut mieux faire... 👎{Style.RESET_ALL}")
        print(f"{Back.BLUE}{Fore.BLACK}{'=' * 60}{Style.RESET_ALL}\n")
        # print commentaire si le score est parfait, s'il est moyen ou mauvais


    def lancer_quiz(self):
        self.afficher_titre()
        print(f"{Fore.YELLOW}Instructions :{Style.RESET_ALL}")
        print(
            f"{Fore.CYAN}• Pour les questions à choix multiple : entrez tous les numéros corrects séparés par des espaces")
        print(f"• Pour les questions à choix unique : entrez simplement le numéro de la réponse{Style.RESET_ALL}\n")

        questions_melangees = list(range(len(self.questions)))
        random.shuffle(questions_melangees)

        for i in range(len(self.questions)):
            self.poser_question(questions_melangees[i])

        self.afficher_resultats()

if __name__ == "__main__":
    quiz = QuizGestionProjet()
    quiz.lancer_quiz()