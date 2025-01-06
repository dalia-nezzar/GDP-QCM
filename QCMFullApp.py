import random
import streamlit as st


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
        self.total_questions = len(self.questions)


def initialiser_session():
    if 'current_question' not in st.session_state:
        st.session_state.current_question = 0
    if 'score' not in st.session_state:
        st.session_state.score = 0
    if 'questions_melangees' not in st.session_state:
        questions = list(range(len(quiz.questions)))
        random.shuffle(questions)
        st.session_state.questions_melangees = questions  # On prend toutes les questions
    if 'reponses_donnees' not in st.session_state:
        st.session_state.reponses_donnees = False


def reset_quiz():
    for key in st.session_state.keys():
        del st.session_state[key]


quiz = QuizGestionProjet()

st.title('Quiz de Gestion de Projet')

# Initialisation
initialiser_session()

# Si on n'a pas encore répondu à toutes les questions
if st.session_state.current_question < quiz.total_questions:
    question_idx = st.session_state.questions_melangees[st.session_state.current_question]
    question = quiz.questions[question_idx]

    # Affichage de la question
    st.header(f"Question {st.session_state.current_question + 1}/{quiz.total_questions}")
    st.write(question["question"])

    # Barre de progression
    progress = st.session_state.current_question / quiz.total_questions
    st.progress(progress)

    # Type de question
    st.write(f"*Type: {'Choix multiple' if question['type'] == 'multiple' else 'Choix unique'}*")

    # Création des options de réponse
    if not st.session_state.reponses_donnees:
        if question["type"] == "unique":
            reponse = st.radio("Choisissez votre réponse:",
                               options=range(len(question["choices"])),
                               format_func=lambda x: question["choices"][x])
        else:
            reponses = []
            for i, choix in enumerate(question["choices"]):
                reponses.append(st.checkbox(choix))

        # Bouton de validation
        if st.button('Valider'):
            st.session_state.reponses_donnees = True
            if question["type"] == "unique":
                if reponse == question["correct"][0]:
                    st.success("✅ Correct !")
                    st.session_state.score += 1
                else:
                    st.error("❌ Incorrect")
                    st.write(f"La bonne réponse était : {question['choices'][question['correct'][0]]}")
            else:
                reponses_utilisateur = [i for i, rep in enumerate(reponses) if rep]
                if sorted(reponses_utilisateur) == sorted(question["correct"]):
                    st.success("✅ Parfait ! Toutes les réponses sont correctes !")
                    st.session_state.score += 1
                else:
                    st.error("❌ Incorrect")
                    bonnes_reponses = [question['choices'][i] for i in question["correct"]]
                    st.write("Les bonnes réponses étaient : " + ", ".join(bonnes_reponses))

    # Bouton suivant
    if st.session_state.reponses_donnees:
        col1, col2 = st.columns([1, 5])
        with col1:
            if st.button('Question suivante ➡️'):
                st.session_state.current_question += 1
                st.session_state.reponses_donnees = False
                st.rerun()

# Affichage des résultats finaux
else:
    st.header("Quiz terminé ! 🎉")
    score_percentage = (st.session_state.score / quiz.total_questions) * 100

    # Création de colonnes pour un affichage plus élégant
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Score final", f"{st.session_state.score}/{quiz.total_questions}")
    with col2:
        st.metric("Pourcentage", f"{score_percentage:.1f}%")

    # Message personnalisé basé sur le score
    if score_percentage >= 80:
        st.success("🌟 Bien vu, t'es prêt :)")
    elif score_percentage >= 60:
        st.warning("👍 Pas mal ! Continue tes révisions.")
    else:
        st.error("📚 Oof, force. Revois tes cours.")

    if st.button('Recommencer le quiz 🔄'):
        reset_quiz()
        st.rerun()

# Ajout d'un compteur de progression en bas de page
st.sidebar.write(f"Progression: {st.session_state.current_question}/{quiz.total_questions}")
st.sidebar.write(f"Score actuel: {st.session_state.score}")