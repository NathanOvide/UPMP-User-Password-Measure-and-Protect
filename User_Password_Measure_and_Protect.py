                                      #Importation des modules nécéssaires
from tkinter.filedialog import *
import webbrowser
from tkinter.messagebox import *
from tkinter import ttk
import time

# ------------------------------Création de toutes les listes------------------------------


LePrenomI = []                    # Prénom individu
LeNom = []                        # nom individu
LeSurnom = []                     # Surnom individu
MotDePasseI = []

LeJourDeNaissance = []          # naissance individu
LeMoisDeNaissance = []
LAnneeDeNaissance = []
MotDePasseDNI = []
LeLieuDeNaissance = []
LeDLieuDeNaissance = []


    # Parent 1

LePrenomP1 = []                   # Prénom parent 1
LeNomP1 = []                      # Nom parent 1
LeSurnomP1 = []                   # Surnom parent 1
MotDePasseP1 = []

LeJourDeNaissanceP1 = []        # Naissance parent 1
LeMoisDeNaissanceP1 = []
LAnneeDeNaissanceP1 = []
MotDePasseDNP1 = []
LeLieuDeNaissanceP1 = []
LeDLieuDeNaissanceP1 = []


    # Parent 2

LePrenomP2 = []                   # Prénom parent 1
LeNomP2 = []                      # Nom parent 1
LeSurnomP2 = []                   # Surnom parent 1
MotDePasseP2 = []

LeJourDeNaissanceP2 = []        # Naissance parent 1
LeMoisDeNaissanceP2 = []
LAnneeDeNaissanceP2 = []
MotDePasseDNP2 = []
LeLieuDeNaissanceP2 = []
LeDLieuDeNaissanceP2 = []


    # Freres et soeurs

LePrenomF = []
LeNomF = []
LeSurnomF = []
LeJourDeNaissanceF = []
LeMoisDeNaissanceF = []
LAnneeDeNaissanceF = []
LeLieuDeNaissanceF = []
LeDLieuDeNaissanceF = []
MotDePasseF = []


    # Animauix de compagnie

LePrenomA=[]
MotDePasseA = []


    # conjoint/conjointe

LePrenomC = []
LeNomC = []
LeSurnomC = []
LeJourDeNaissanceC = []
LeMoisDeNaissanceC = []
LAnneeDeNaissanceC = []
LeLieuDeNaissanceC = []
LeDLieuDeNaissanceC = []
MotDePasseC=[]


MotDePasse = []
Trie = []
MotDePasse_final = []

# ------------------------------Création de la fenetre principale------------------------------


fenetre = Tk()                                                                                                          # Création de la fenêtre
fenetre.title("User Password Measure and Protect : UPMP")                                                               # Titre de la fenêtre
fenetre.iconbitmap('icon.ico')                                                                                          # Icone de la fenêtre
w = 635                                                                                                                 #Taille souhaitée de la fenetre
h = 240
ws = fenetre.winfo_screenwidth()                                                                                        #Centrage de la fenêtre
hs = fenetre.winfo_screenheight()                                                                                       #Ratio de l'écran
x = (ws/2) - (w/2)                                                                                                      #Calcul position fenêtre
y = (hs/2) - (h/2)
fenetre.geometry('%dx%d+%d+%d' % (w, h, x, y))                                                                          # Taille fenêtre
fenetre.configure(bg="gray15")                                                                                           # Couleur Background fenêtre
fenetre.resizable(width=False, height=False)                                                                            # Fenetre non redimensionnable
Banhschrift = "{Banhschrift} 12 roman italic"                                                                           # Police Banhschrift
Slashsfont = "{Banhschrift} 16 roman italic"

texte_accueil = Label(fenetre, text="Lors de la saisie de vos données merci de ne pas entrer  : \n     - d\'espaces                                                               \n     - de carractères spéciaux (¨, ^, -)                                \n     - d\'accents                                                               ", font='Helvetica, 10')
texte_accueil.pack(anchor="w") 
texte_accueil.place(x=290, y=45)
texte_accueil.configure(bg="gray15", fg="DarkGoldenrod1", relief="groove")

# Def de selection et affichage de la ligne sélectionnée : (selection) car argument nécessaire pour plusieurs opérations

def selection(selection):
    index = listbox.curselection()[0]                                                                                   # Sélection de la ligne de la liste
    selecttext = listbox.get(index)                                                                                     # Récupère le n° d'index de la ligne sélectionnée
    entrylist.delete(0, 100)                                                                                            # Supprime le texte déja présent dans l'entry
    entrylist.insert(0, selecttext)                                                                                     # Entre le texte de la ligne sélectionnée dans l'entry


# ------------------------------Création de la fenetre secondaire concernant l'individu------------------------------

def window_personal_info(window_personal_info):

    window_personal_info = Toplevel()                                                                                   # Nouvelle fenetre1 au dessus de la précédente
    window_personal_info.focus_set()                                                                                    # S'affiche comme fenêtre principale (Déja sélectionée en Bleu)
    window_personal_info.geometry("410x370+250+240")                                                                    # Dimension de la fenêtre1
    window_personal_info.resizable(width=False, height=False)                                                           # La fenetre n'est pas redimensionnable
    window_personal_info.iconbitmap('icon.ico')
    window_personal_info.title("Vous")                                                                                  # Titre de la nouvelle fenêtre1

    # ------------------------------

    texte_prenom = Label(window_personal_info, text="Prénom :", font=Banhschrift)
    texte_prenom.pack(anchor="w")
    texte_prenom.place(x=20, y=10)

    entry_prenom = Entry(window_personal_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_prenom.place(x=180, y=14)

    # -----

    def prenom_individu():
        global LePrenomI                                                                                                # Modifications apportés soit valable partout
        global MotDePasseI
        prenomi = entry_prenom.get()                                                                                    # Demande du prénom de l'individu qui s'enregistre dans une variable plus simple à manipuler
        var = str.lower(prenomi)                                                                                        # utilisation d'une autre variable qui enregistre la précédente en minuscule pour palier au problème de majuscule
        LePrenomI.append(var)                                                                                           # On intègre la variable dans la liste
        MotDePasseI.append(str.upper(prenomi))                                                                          # La liste des mot de passes intègre la variable en majuscules
        MotDePasseI.append(str.lower(prenomi))                                                                          # La liste des mot de passes intègre la variable en minuscules

        for a in range(len(prenomi)):                                                                                   # Création de Mot de passe avec 1 lettre majuscule constament
            LePrenomI = [elt for elt in var]                                                                            # On sépare chaque lettre du mot
            LePrenomI[a] = ord(LePrenomI[a])                                                                            # On met la variable a (lettre) sous forme de nombre
            if LePrenomI[a] >= 97 and LePrenomI[a] <= 122:                                                              # Si le nombre de la variable a est comprise entre 97 et 122 inclus alors
                LePrenomI[a] = chr(LePrenomI[a] - 32)                                                                   # Elle est transformé en majuscule
                MotDePasseI.append("".join(LePrenomI))                                                                  # Le mot de passe intègre le résultat avec seulement a en majuscule
                for z in range(len(prenomi)):
                    if z != a:                                                                                          # Lorsque z est différent de la valeur a
                        LePrenomI[z] = ord(LePrenomI[z])                                                                # on met au fur et à mesure les autres lettres en majuscule
                        if LePrenomI[z] >= 97 and LePrenomI[z] <= 122:                                                  # Tout en gardant la variable a en majuscule
                            LePrenomI[z] = chr(LePrenomI[z] - 32)
                            MotDePasseI.append("".join(LePrenomI))                                                      # on les intègre au fur et à mesure à la liste des mots de passes concernant le prénom
                            LePrenomI[z] = ord(LePrenomI[z])                                                            # a reste toujours en majuscule, en revanche toutes les autres redeviennent en minuscule
                            LePrenomI[z] = chr(LePrenomI[z] + 32)

        for a in range((len(prenomi))-1):                                                                               # Création de Mot de passe avec 2 lettres majuscule constament
            b = a + 1                                                                                                   # d'où le b qui correspond à la deuxième majuscule qui suit a, elle aussi une majuscule
            LePrenomI = [elt for elt in var]                                                                            # On sépare chaque lettre du mot
            LePrenomI[a] = ord(LePrenomI[a])                                                                            # On met les variable a et b (lettre) sous forme de nombres
            LePrenomI[b] = ord(LePrenomI[b])
            if LePrenomI[a] >= 97 and LePrenomI[a] <= 122 and LePrenomI[b] >= 97 and LePrenomI[b] <= 122:               # Si le nombre des variables a et b sont compris entre 97 et 122 inclus alors
                LePrenomI[a] = chr(LePrenomI[a] - 32)                                                                   # Elles sont transformés en majuscule
                LePrenomI[b] = chr(LePrenomI[b] - 32)
                MotDePasseI.append("".join(LePrenomI))                                                                  # Le mot de passe intègre le résultat avec seulement a et b en majuscule
                for z in range(len(prenomi)):
                    if z != a and z != b:                                                                               # Lorsque z est différent de la valeur a et b
                        LePrenomI[z] = ord(LePrenomI[z])                                                                # on met au fur et à mesure les autres lettres en majuscule
                        if LePrenomI[z] >= 97 and LePrenomI[z] <= 122:                                                  # Tout en gardant les variables a et b en majuscule
                            LePrenomI[z] = chr(LePrenomI[z] - 32)
                            MotDePasseI.append("".join(LePrenomI))                                                      # on les intègre au fur et à mesure à la liste des mots de passes concernant le prénom
                            LePrenomI[z] = ord(LePrenomI[z])                                                            # a et b restent toujours en majuscule, en revanche toutes les autres redeviennent en minuscule
                            LePrenomI[z] = chr(LePrenomI[z] + 32)

        for a in range((len(prenomi)) - 2):                                                                             # Création de Mot de passe avec 3 lettres majuscule constament
            b = a + 1                                                                                                   # d'où le b qui correspond à la deuxième majuscule qui suit a, elle aussi une majuscule
            c = a + 2                                                                                                   # d'où le c qui correspond à la troisième majuscule qui suit b, elle aussi une majuscule
            LePrenomI = [elt for elt in var]                                                                            # On sépare chaque lettre du mot
            LePrenomI[a] = ord(LePrenomI[a])                                                                            # On met les variable a, b et c (lettre) sous forme de nombres
            LePrenomI[b] = ord(LePrenomI[b])
            LePrenomI[c] = ord(LePrenomI[c])
            if LePrenomI[a] >= 97 and LePrenomI[a] <= 122 and LePrenomI[b] >= 97 and LePrenomI[b] <= 122 and LePrenomI[c] >= 97 and LePrenomI[c] <=122:# Si le nombre des variables a, b et c sont compris entre 97 et 122 inclus alors
                LePrenomI[a] = chr(LePrenomI[a] - 32)                                                                   # Elles sont transformés en majuscule
                LePrenomI[b] = chr(LePrenomI[b] - 32)
                LePrenomI[c] = chr(LePrenomI[c] - 32)
                MotDePasseI.append("".join(LePrenomI))                                                                  # Le mot de passe intègre le résultat avec seulement a, b et c en majuscule
                for z in range(len(prenomi)):
                    if z != a and z != b and z != c:                                                                    # Lorsque z est différent de la valeur a, b et c
                        LePrenomI[z] = ord(LePrenomI[z])                                                                # on met au fur et à mesure les autres lettres en majuscule
                        if LePrenomI[z] >= 97 and LePrenomI[z] <= 122:                                                  # Tout en gardant les variables a, b et c en majuscule
                            LePrenomI[z] = chr(LePrenomI[z]-32)
                            MotDePasseI.append("".join(LePrenomI))                                                      # on les intègre au fur et à mesure à la liste des mots de passes concernant le prénom
                            LePrenomI[z] = ord(LePrenomI[z])                                                            # a , b et c restent toujours en majuscule, en revanche toutes les autres redeviennent en minuscule
                            LePrenomI[z] = chr(LePrenomI[z]+32)

        for a in range((len(prenomi)) - 3):                                                                             # Création de Mot de passe avec 3 lettres majuscule constament
            b = a + 1                                                                                                   # d'où le b qui correspond à la deuxième majuscule qui suit a, elle aussi une majuscule
            c = a + 2                                                                                                   # d'où le c qui correspond à la troisième majuscule qui suit b, elle aussi une majuscule
            d = a + 3                                                                                                   # d'où le d qui correspond à la quatrième majuscule qui suit c, elle aussi une majuscule
            LePrenomI = [elt for elt in var]                                                                            # On sépare chaque lettre du mot
            LePrenomI[a] = ord(LePrenomI[a])                                                                            # On met les variable a, b, c et d (lettre) sous forme de nombres
            LePrenomI[b] = ord(LePrenomI[b])
            LePrenomI[c] = ord(LePrenomI[c])
            LePrenomI[d] = ord(LePrenomI[d])
            if LePrenomI[a] >= 97 and LePrenomI[a] <= 122 and LePrenomI[b] >= 97 and LePrenomI[b] <= 122 and LePrenomI[c] >= 97 and LePrenomI[c] <= 122 and LePrenomI[d] >= 97 and LePrenomI[d] <= 122:# Si le nombre des variables a, b, c et d sont compris entre 97 et 122 inclus alors
                LePrenomI[a] = chr(LePrenomI[a] - 32)                                                                   # Elles sont transformés en majuscule
                LePrenomI[b] = chr(LePrenomI[b] - 32)
                LePrenomI[c] = chr(LePrenomI[c] - 32)
                LePrenomI[d] = chr(LePrenomI[d] - 32)
                MotDePasseI.append("".join(LePrenomI))                                                                  # Le mot de passe intègre le résultat avec seulement a, b, c et d en majuscule
                for z in range(len(prenomi)):
                    if z != a and z != b and z != c and z != d:                                                         # Lorsque z est différent de la valeur a, b, c et d
                        LePrenomI[z] = ord(LePrenomI[z])                                                                # on met au fur et à mesure les autres lettres en majuscule
                        if LePrenomI[z] >= 97 and LePrenomI[z] <= 122:                                                  # Tout en gardant les variables a, b, c et d en majuscule
                            LePrenomI[z] = chr(LePrenomI[z] - 32)
                            MotDePasseI.append("".join(LePrenomI))                                                      # on les intègre au fur et à mesure à la liste des mots de passes concernant le prénom
                            LePrenomI[z] = ord(LePrenomI[z])                                                            # a , b, c et d restent toujours en majuscule, en revanche toutes les autres redeviennent en minuscule
                            LePrenomI[z] = chr(LePrenomI[z] + 32)

    # ------------------------------

    texte_nom = Label(window_personal_info, text="Nom :", font=Banhschrift)                                             # zone de texte
    texte_nom.place(x=20, y=60)

    entry_nom = Entry(window_personal_info, width=30, bg='white', fg="black", justify="center")                         # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_nom.place(x=180, y=64)

    # -----

    def nom_individu():
        global LeNom
        global MotDePasseI
        nomi = entry_nom.get()
        var = str.lower(nomi)
        LeNom.append(var)
        MotDePasseI.append(str.upper(nomi))
        MotDePasseI.append(str.lower(nomi))

        for a in range(len(nomi)):
            LeNom = [elt for elt in var]
            LeNom[a] = ord(LeNom[a])
            if LeNom[a] >= 97 and LeNom[a] <= 122:
                LeNom[a] = chr(LeNom[a] - 32)
                MotDePasseI.append("".join(LeNom))
                for z in range(len(nomi)):
                    if z != a:
                        LeNom[z] = ord(LeNom[z])
                        if LeNom[z] >= 97 and LeNom[z] <= 122:
                            LeNom[z] = chr(LeNom[z] - 32)
                            MotDePasseI.append("".join(LeNom))
                            LeNom[z] = ord(LeNom[z])
                            LeNom[z] = chr(LeNom[z] + 32)

        for a in range((len(nomi)) - 1):
            b = a + 1
            LeNom = [elt for elt in var]
            LeNom[a] = ord(LeNom[a])
            LeNom[b] = ord(LeNom[b])
            if LeNom[a] >= 97 and LeNom[a] <= 122 and LeNom[b] >= 97 and LeNom[b] <= 122:
                LeNom[a] = chr(LeNom[a] - 32)
                LeNom[b] = chr(LeNom[b] - 32)
                MotDePasseI.append("".join(LeNom))
                for z in range(len(nomi)):
                    if z != a and z != b:
                        LeNom[z] = ord(LeNom[z])
                        if LeNom[z] >= 97 and LeNom[z] <= 122:
                            LeNom[z] = chr(LeNom[z] - 32)
                            MotDePasseI.append("".join(LeNom))
                            LeNom[z] = ord(LeNom[z])
                            LeNom[z] = chr(LeNom[z] + 32)

        for a in range((len(nomi)) - 2):
            b = a + 1
            c = a + 2
            LeNom = [elt for elt in var]
            LeNom[a] = ord(LeNom[a])
            LeNom[b] = ord(LeNom[b])
            LeNom[c] = ord(LeNom[c])
            if LeNom[a] >= 97 and LeNom[a] <= 122 and LeNom[b] >= 97 and LeNom[b] <= 122 and LeNom[c] >= 97 and LeNom[c] <= 122:
                LeNom[a] = chr(LeNom[a] - 32)
                LeNom[b] = chr(LeNom[b] - 32)
                LeNom[c] = chr(LeNom[c] - 32)
                MotDePasseI.append("".join(LeNom))
                for z in range(len(nomi)):
                    if z != a and z != b and z != c:
                        LeNom[z] = ord(LeNom[z])
                        if LeNom[z] >= 97 and LeNom[z] <= 122:
                            LeNom[z] = chr(LeNom[z] - 32)
                            MotDePasseI.append("".join(LeNom))
                            LeNom[z] = ord(LeNom[z])
                            LeNom[z] = chr(LeNom[z] + 32)

        for a in range((len(nomi)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeNom = [elt for elt in var]
            LeNom[a] = ord(LeNom[a])
            LeNom[b] = ord(LeNom[b])
            LeNom[c] = ord(LeNom[c])
            LeNom[d] = ord(LeNom[d])
            if LeNom[a] >= 97 and LeNom[a] <= 122 and LeNom[b] >= 97 and LeNom[b] <= 122 and LeNom[c] >= 97 and LeNom[c] <= 122 and LeNom[d] >= 97 and LeNom[d] <= 122:
                LeNom[a] = chr(LeNom[a] - 32)
                LeNom[b] = chr(LeNom[b] - 32)
                LeNom[c] = chr(LeNom[c] - 32)
                LeNom[d] = chr(LeNom[d] - 32)
                MotDePasseI.append("".join(LeNom))
                for z in range(len(nomi)):
                    if z != a and z != b and z != c and z != d:
                        LeNom[z] = ord(LeNom[z])
                        if LeNom[z] >= 97 and LeNom[z] <= 122:
                            LeNom[z] = chr(LeNom[z] - 32)
                            MotDePasseI.append("".join(LeNom))
                            LeNom[z] = ord(LeNom[z])
                            LeNom[z] = chr(LeNom[z] + 32)

    # ------------------------------

    texte_pseudo = Label(window_personal_info, text="Surnom - Pseudo :", font=Banhschrift)
    texte_pseudo.place(x=20, y=110)

    entry_pseudo = Entry(window_personal_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_pseudo.place(x=180, y=114)

    # -----

    def surnom_individu():
        global LeSurnom
        global MotDePasseI
        surnomi = entry_pseudo.get()
        var = str.lower(surnomi)
        LeSurnom.append(var)
        MotDePasseI.append(str.lower(surnomi))
        MotDePasseI.append(str.upper(surnomi))

        for a in range(len(surnomi)):
            LeSurnom = [elt for elt in var]
            LeSurnom[a] = ord(LeSurnom[a])
            if LeSurnom[a] >= 97 and LeSurnom[a] <= 122:
                LeSurnom[a] = chr(LeSurnom[a] - 32)
                MotDePasseI.append("".join(LeSurnom))
                for z in range(len(surnomi)):
                    if z != a:
                        LeSurnom[z] = ord(LeSurnom[z])
                        if LeSurnom[z] >= 97 and LeSurnom[z] <= 122:
                            LeSurnom[z] = chr(LeSurnom[z] - 32)
                            MotDePasseI.append("".join(LeSurnom))
                            LeSurnom[z] = ord(LeSurnom[z])
                            LeSurnom[z] = chr(LeSurnom[z] + 32)

        for a in range((len(surnomi)) - 1):
            b = a + 1
            LeSurnom = [elt for elt in var]
            LeSurnom[a] = ord(LeSurnom[a])
            LeSurnom[b] = ord(LeSurnom[b])
            if LeSurnom[a] >= 97 and LeSurnom[a] <= 122 and LeSurnom[b] >= 97 and LeSurnom[b] <= 122:
                LeSurnom[a] = chr(LeSurnom[a] - 32)
                LeSurnom[b] = chr(LeSurnom[b] - 32)
                MotDePasseI.append("".join(LeSurnom))
                for z in range(len(surnomi)):
                    if z != a and z != b:
                        LeSurnom[z] = ord(LeSurnom[z])
                        if LeSurnom[z] >= 97 and LeSurnom[z] <= 122:
                            LeSurnom[z] = chr(LeSurnom[z] - 32)
                            MotDePasseI.append("".join(LeSurnom))
                            LeSurnom[z] = ord(LeSurnom[z])
                            LeSurnom[z] = chr(LeSurnom[z] + 32)

        for a in range((len(surnomi)) - 2):
            b = a + 1
            c = a + 2
            LeSurnom = [elt for elt in var]
            LeSurnom[a] = ord(LeSurnom[a])
            LeSurnom[b] = ord(LeSurnom[b])
            LeSurnom[c] = ord(LeSurnom[c])
            if LeSurnom[a] >= 97 and LeSurnom[a] <= 122 and LeSurnom[b] >= 97 and LeSurnom[b] <= 122 and LeSurnom[
                c] >= 97 and LeSurnom[c] <= 122:
                LeSurnom[a] = chr(LeSurnom[a] - 32)
                LeSurnom[b] = chr(LeSurnom[b] - 32)
                LeSurnom[c] = chr(LeSurnom[c] - 32)
                MotDePasseI.append("".join(LeSurnom))
                for z in range(len(surnomi)):
                    if z != a and z != b and z != c:
                        LeSurnom[z] = ord(LeSurnom[z])
                        if LeSurnom[z] >= 97 and LeSurnom[z] <= 122:
                            LeSurnom[z] = chr(LeSurnom[z] - 32)
                            MotDePasseI.append("".join(LeSurnom))
                            LeSurnom[z] = ord(LeSurnom[z])
                            LeSurnom[z] = chr(LeSurnom[z] + 32)

        for a in range((len(surnomi)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeSurnom = [elt for elt in var]
            LeSurnom[a] = ord(LeSurnom[a])
            LeSurnom[b] = ord(LeSurnom[b])
            LeSurnom[c] = ord(LeSurnom[c])
            LeSurnom[d] = ord(LeSurnom[d])
            if LeSurnom[a] >= 97 and LeSurnom[a] <= 122 and LeSurnom[b] >= 97 and LeSurnom[b] <= 122 and LeSurnom[c] >= 97 and LeSurnom[c] <= 122 and LeSurnom[d] >= 97 and LeSurnom[d] <= 122:
                LeSurnom[a] = chr(LeSurnom[a] - 32)
                LeSurnom[b] = chr(LeSurnom[b] - 32)
                LeSurnom[c] = chr(LeSurnom[c] - 32)
                LeSurnom[d] = chr(LeSurnom[d] - 32)
                MotDePasseI.append("".join(LeSurnom))
                for z in range(len(surnomi)):
                    if z != a and z != b and z != c and z != d:
                        LeSurnom[z] = ord(LeSurnom[z])
                        if LeSurnom[z] >= 97 and LeSurnom[z] <= 122:
                            LeSurnom[z] = chr(LeSurnom[z] - 32)
                            MotDePasseI.append("".join(LeSurnom))
                            LeSurnom[z] = ord(LeSurnom[z])
                            LeSurnom[z] = chr(LeSurnom[z] + 32)

    # ------------------------------

    texte_datenaissance = Label(window_personal_info, text="Date de Naissance :", font=Banhschrift)                     # Zone de texte
    texte_datenaissance.pack(anchor="w")
    texte_datenaissance.place(x=20, y=160)                                                                              # Position

    # ----------

    jourMenu = ttk.Combobox(window_personal_info)                                                                       # Menu déroulant concernant les jours de naissance possible
    jourMenu.place(x=180, y=165, width=45)                                                                              # Position
    jourMenu['values'] = (                                                                                              # Liste des valeurs possibles
    "Jour", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "15", "16", "17", "18",
    "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    jourMenu.current(0)

    def jour_individu():
        global MotDePasseDNI
        JourNaissance = jourMenu.get()                                                                                  # Variable qui récupère la valeur du menu déroulant
        MotDePasseDNI.append(JourNaissance)                                                                             # Mot de passe qui l'intègre

    # ----------

    slash1 = Label(window_personal_info, text="/", font=Slashsfont)
    slash1.place(x=225, y=162)

    # ----------

    moisMenu = ttk.Combobox(window_personal_info)                                                                       # Menu déroulant concernant les mois de naissance possible
    moisMenu.place(x=238, y=165, width=50)                                                                              # Position
    moisMenu["values"] = ("Mois", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")               # Liste des valeurs possibles
    moisMenu.current(0)

    def mois_individu():
        global MotDePasseDNI
        MoisNaissance = moisMenu.get()                                                                                  # Variable qui récupère la valeur du menu déroulant
        MotDePasseDNI.append(MoisNaissance)                                                                             # Mot de passe qui l'intègre

    # ----------

    slash2 = Label(window_personal_info, text="/", font=Slashsfont)
    slash2.place(x=288, y=162)

    # ----------

    anneeMenu = ttk.Combobox(window_personal_info)                                                                      # Menu déroulant concernant les années de naissance possible
    anneeMenu.place(x=301, y=165, width=62)                                                                             # Position
    anneeMenu["values"] = (                                                                                             # Liste des valeurs possibles
    "Année", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
    "1992", "1991", "1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979",
    "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965",
    "1964", "1963", "1962", "1961", "1960", "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951",
    "1950", "1949", "1948", "1947", "1946", "1945", "1944", "1943", "1942", "1941", "1940", "1939", "1938", "1937",
    "1936", "1935", "1934", "1933", "1932", "1931", "1930", "1929", "1928", "1927", "1926", "1925", "1924", "1923",
    "1922", "1921", "1920", "1919")
    anneeMenu.current(0)

    def annee_individu():
        global MotDePasseDNI
        AnneeNaissance = anneeMenu.get()                                                                                # Variable qui récupère la valeur du menu déroulant
        MotDePasseDNI.append(AnneeNaissance)                                                                            # Mot de passe qu'y l'intègre

    # ------------------------------

    texte_lieunaissance = Label(window_personal_info, text="Ville Natale :", font=Banhschrift)                          # Zone de texte
    texte_lieunaissance.pack(anchor="w")
    texte_lieunaissance.place(x=20, y=210)                                                                              # Postition

    lieunaissanceMenu = Entry(window_personal_info, width=30, bg='white', fg="black", justify="center")                 # Zone de saisie pour l'utilisateur
    lieunaissanceMenu.place(x=180, y=215)                                                                               # Emplacement

    def lieu_individu():
        global LeLieuDeNaissance
        LieuNaissance = lieunaissanceMenu.get()                                                                         # Variable qui récupère la valeur du menu déroulant
        LeLieuDeNaissance.append(LieuNaissance)                                                                         # Mot de passe qu'y l'intègre

    # ------------------------------

    texte_departementnaissance = Label(window_personal_info, text="Département de Naissance :", font=Banhschrift)       # Zone de texte
    texte_departementnaissance.pack(anchor="w")
    texte_departementnaissance.place(x=20, y=260)                                                                       # Position

    numdepartementMenu = ttk.Combobox(window_personal_info)                                                             # menu déroulant concernant les numéros de département possibles
    numdepartementMenu.place(x=239, y=263, width=125)                                                                   # emplacement
    numdepartementMenu["values"] = (
        "N° de département", "2A", "2B", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",  # liste des valeurs possibles
        "14", "15", "15",
        "16", "17", "18", "19", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34",
        "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",
        "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
        "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88",
        "89", "90", "91", "92", "93", "94", "95")
    numdepartementMenu.current(0)

    def dlieu_individu():
        global LeDLieuDeNaissance
        DLieuNaissance = numdepartementMenu.get()                                                                       # variable qui récupère la valeur du menu déroulant
        LeDLieuDeNaissance.append(DLieuNaissance)                                                                       # mot de passe qu'y l'intègre

    # ------------------------------

    def creation_MDP_individu():                                                                                        # fonction principale qui fait appel aux précédentes
        global MotDePasseI
        global MotDePasseDNI
        global LeLieuDeNaissance
        global LeDLieuDeNaissance
        global MotDePasse
        prenom_individu()                                                                                               # fonction qui concerne le prénom
        nom_individu()                                                                                                  # fonction qui concerne le nom
        surnom_individu()                                                                                               # fonction qui concerne le surnom
        jour_individu()                                                                                                 # fonction qui concerne le jour de naissance
        mois_individu()                                                                                                 # fonction qui concerne le mois de naissance
        annee_individu()                                                                                                # fonction qui concerne l'année de naissance
        lieu_individu()                                                                                                 # fonction qui concerne le lieu de naissance
        dlieu_individu()                                                                                                # fonction qui concerne le département de naissance
        for i in range(len(MotDePasseI)):                                                                               # mot de passe général qui intègre tous les mots de passe particuliers créés
            MotDePasse.append(MotDePasseI[i])
        for i in range(len(MotDePasseDNI)):
            MotDePasse.append(MotDePasseDNI[i])
        for i in range(len(LeLieuDeNaissance)):
            MotDePasse.append(LeLieuDeNaissance[i])
        for i in range(len(LeDLieuDeNaissance)):
            MotDePasse.append(LeDLieuDeNaissance[i])
        showinfobox_enregistrement()
        #print(MotDePasse)
        window_personal_info.destroy()

    # ------------------------------

    bouton_valider_window_personal_info = Button(window_personal_info, text="      Valider les     \n informations", relief="groove", command=creation_MDP_individu)    # Bouton avec texte + commande
    bouton_valider_window_personal_info.place(x=150, y=310)


# ------------------------------Création de la fenetre secondaire concernant le parent 1------------------------------

def window_parent1_info(window_parent1_info):

    window_parent1_info = Toplevel()                                                                                    # Nouvelle fenetre1 au dessus de la précédente
    window_parent1_info.focus_set()                                                                                     # S'affiche comme fenêtre principale (Déja sélectionée en Bleu)
    window_parent1_info.geometry("410x370+250+240")                                                                     # Dimension de la fenêtre1
    window_parent1_info.resizable(width=False, height=False)                                                            # La fenetre n'est pas redimensionnable
    window_parent1_info.iconbitmap('icon.ico')
    window_parent1_info.title("Parent 1")                                                                      # Titre de la nouvelle fenêtre1

    # ------------------------------

    texte_prenom = Label(window_parent1_info, text="Prénom :", font=Banhschrift)
    texte_prenom.pack(anchor="w")
    texte_prenom.place(x=20, y=10)

    entry_prenom1 = Entry(window_parent1_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_prenom1.place(x=180, y=14)

    # -----

    def prenom_p1():
        global LePrenomP1
        global MotDePasseP1
        prenomp1 = entry_prenom1.get()
        var = str.lower(prenomp1)
        LePrenomP1.append(var)
        MotDePasseP1.append(str.upper(prenomp1))
        MotDePasseP1.append(str.lower(prenomp1))

        for a in range(len(prenomp1)):
            LePrenomP1 = [elt for elt in var]
            LePrenomP1[a] = ord(LePrenomP1[a])
            if LePrenomP1[a] >= 97 and LePrenomP1[a] <= 122:
                LePrenomP1[a] = chr(LePrenomP1[a] - 32)
                MotDePasseP1.append("".join(LePrenomP1))
                for z in range(len(prenomp1)):
                    if z != a:
                        LePrenomP1[z] = ord(LePrenomP1[z])
                        if LePrenomP1[z] >= 97 and LePrenomP1[z] <= 122:
                            LePrenomP1[z] = chr(LePrenomP1[z] - 32)
                            MotDePasseP1.append("".join(LePrenomP1))
                            LePrenomP1[z] = ord(LePrenomP1[z])
                            LePrenomP1[z] = chr(LePrenomP1[z] + 32)

        for a in range((len(prenomp1)) - 1):
            b = a + 1
            LePrenomP1 = [elt for elt in var]
            LePrenomP1[a] = ord(LePrenomP1[a])
            LePrenomP1[b] = ord(LePrenomP1[b])
            if LePrenomP1[a] >= 97 and LePrenomP1[a] <= 122 and LePrenomP1[b] >= 97 and LePrenomP1[b] <= 122:
                LePrenomP1[a] = chr(LePrenomP1[a] - 32)
                LePrenomP1[b] = chr(LePrenomP1[b] - 32)
                MotDePasseP1.append("".join(LePrenomP1))
                for z in range(len(prenomp1)):
                    if z != a and z != b:
                        LePrenomP1[z] = ord(LePrenomP1[z])
                        if LePrenomP1[z] >= 97 and LePrenomP1[z] <= 122:
                            LePrenomP1[z] = chr(LePrenomP1[z] - 32)
                            MotDePasseP1.append("".join(LePrenomP1))
                            LePrenomP1[z] = ord(LePrenomP1[z])
                            LePrenomP1[z] = chr(LePrenomP1[z] + 32)

        for a in range((len(prenomp1)) - 2):
            b = a + 1
            c = a + 2
            LePrenomP1 = [elt for elt in var]
            LePrenomP1[a] = ord(LePrenomP1[a])
            LePrenomP1[b] = ord(LePrenomP1[b])
            LePrenomP1[c] = ord(LePrenomP1[c])
            if LePrenomP1[a] >= 97 and LePrenomP1[a] <= 122 and LePrenomP1[b] >= 97 and LePrenomP1[b] <= 122 and LePrenomP1[c] >= 97 and LePrenomP1[c] <= 122:
                LePrenomP1[a] = chr(LePrenomP1[a] - 32)
                LePrenomP1[b] = chr(LePrenomP1[b] - 32)
                LePrenomP1[c] = chr(LePrenomP1[c] - 32)
                MotDePasseP1.append("".join(LePrenomP1))
                for z in range(len(prenomp1)):
                    if z != a and z != b and z != c:
                        LePrenomP1[z] = ord(LePrenomP1[z])
                        if LePrenomP1[z] >= 97 and LePrenomP1[z] <= 122:
                            LePrenomP1[z] = chr(LePrenomP1[z] - 32)
                            MotDePasseP1.append("".join(LePrenomP1))
                            LePrenomP1[z] = ord(LePrenomP1[z])
                            LePrenomP1[z] = chr(LePrenomP1[z] + 32)

        for a in range((len(prenomp1)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LePrenomP1 = [elt for elt in var]
            LePrenomP1[a] = ord(LePrenomP1[a])
            LePrenomP1[b] = ord(LePrenomP1[b])
            LePrenomP1[c] = ord(LePrenomP1[c])
            LePrenomP1[d] = ord(LePrenomP1[d])
            if LePrenomP1[a] >= 97 and LePrenomP1[a] <= 122 and LePrenomP1[b] >= 97 and LePrenomP1[b] <= 122 and LePrenomP1[c] >= 97 and LePrenomP1[c] <= 122 and LePrenomP1[d] >= 97 and LePrenomP1[d] <= 122:
                LePrenomP1[a] = chr(LePrenomP1[a] - 32)
                LePrenomP1[b] = chr(LePrenomP1[b] - 32)
                LePrenomP1[c] = chr(LePrenomP1[c] - 32)
                LePrenomP1[d] = chr(LePrenomP1[d] - 32)
                MotDePasseP1.append("".join(LePrenomP1))
                for z in range(len(prenomp1)):
                    if z != a and z != b and z != c and z != d:
                        LePrenomP1[z] = ord(LePrenomP1[z])
                        if LePrenomP1[z] >= 97 and LePrenomP1[z] <= 122:
                            LePrenomP1[z] = chr(LePrenomP1[z] - 32)
                            MotDePasseP1.append("".join(LePrenomP1))
                            LePrenomP1[z] = ord(LePrenomP1[z])
                            LePrenomP1[z] = chr(LePrenomP1[z] + 32)

    # ------------------------------

    texte_nom = Label(window_parent1_info, text="Nom :", font=Banhschrift)
    texte_nom.place(x=20, y=60)

    entry_nom1 = Entry(window_parent1_info, width=30, bg='white', fg="black", justify="center")                         # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_nom1.place(x=180, y=64)

    # -----

    def nom_p1():
        global LeNomP1
        global MotDePasseP1
        nomp1 = entry_nom1.get()
        var = str.lower(nomp1)
        LeNomP1.append(var)
        MotDePasseP1.append(str.upper(nomp1))
        MotDePasseP1.append(str.lower(nomp1))

        for a in range(len(nomp1)):
            LeNomP1 = [elt for elt in var]
            LeNomP1[a] = ord(LeNomP1[a])
            if LeNomP1[a] >= 97 and LeNomP1[a] <= 122:
                LeNomP1[a] = chr(LeNomP1[a] - 32)
                MotDePasseP1.append("".join(LeNomP1))
                for z in range(len(nomp1)):
                    if z != a:
                        LeNomP1[z] = ord(LeNomP1[z])
                        if LeNomP1[z] >= 97 and LeNomP1[z] <= 122:
                            LeNomP1[z] = chr(LeNomP1[z] - 32)
                            MotDePasseP1.append("".join(LeNomP1))
                            LeNomP1[z] = ord(LeNomP1[z])
                            LeNomP1[z] = chr(LeNomP1[z] + 32)

        for a in range((len(nomp1)) - 1):
            b = a + 1
            LeNomP1 = [elt for elt in var]
            LeNomP1[a] = ord(LeNomP1[a])
            LeNomP1[b] = ord(LeNomP1[b])
            if LeNomP1[a] >= 97 and LeNomP1[a] <= 122 and LeNomP1[b] >= 97 and LeNomP1[b] <= 122:
                LeNomP1[a] = chr(LeNomP1[a] - 32)
                LeNomP1[b] = chr(LeNomP1[b] - 32)
                MotDePasseP1.append("".join(LeNomP1))
                for z in range(len(nomp1)):
                    if z != a and z != b:
                        LeNomP1[z] = ord(LeNomP1[z])
                        if LeNomP1[z] >= 97 and LeNomP1[z] <= 122:
                            LeNomP1[z] = chr(LeNomP1[z] - 32)
                            MotDePasseP1.append("".join(LeNomP1))
                            LeNomP1[z] = ord(LeNomP1[z])
                            LeNomP1[z] = chr(LeNomP1[z] + 32)

        for a in range((len(nomp1)) - 2):
            b = a + 1
            c = a + 2
            LeNomP1 = [elt for elt in var]
            LeNomP1[a] = ord(LeNomP1[a])
            LeNomP1[b] = ord(LeNomP1[b])
            LeNomP1[c] = ord(LeNomP1[c])
            if LeNomP1[a] >= 97 and LeNomP1[a] <= 122 and LeNomP1[b] >= 97 and LeNomP1[b] <= 122 and LeNomP1[c] >= 97 and LeNomP1[c] <= 122:
                LeNomP1[a] = chr(LeNomP1[a] - 32)
                LeNomP1[b] = chr(LeNomP1[b] - 32)
                LeNomP1[c] = chr(LeNomP1[c] - 32)
                MotDePasseP1.append("".join(LeNomP1))
                for z in range((len(nomp1))):
                    if z != a and z != b and z != c:
                        LeNomP1[z] = ord(LeNomP1[z])
                        if LeNomP1[z] >= 97 and LeNomP1[z] <= 122:
                            LeNomP1[z] = chr(LeNomP1[z] - 32)
                            MotDePasseP1.append("".join(LeNomP1))
                            LeNomP1[z] = ord(LeNomP1[z])
                            LeNomP1[z] = chr(LeNomP1[z] + 32)

        for a in range((len(nomp1)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeNomP1 = [elt for elt in var]
            LeNomP1[a] = ord(LeNomP1[a])
            LeNomP1[b] = ord(LeNomP1[b])
            LeNomP1[c] = ord(LeNomP1[c])
            LeNomP1[d] = ord(LeNomP1[d])
            if LeNomP1[a] >= 97 and LeNomP1[a] <= 122 and LeNomP1[b] >= 97 and LeNomP1[b] <= 122 and LeNomP1[c] >= 97 and LeNomP1[c] <= 122 and LeNomP1[d] >= 97 and LeNomP1[d] <= 122:
                LeNomP1[a] = chr(LeNomP1[a] - 32)
                LeNomP1[b] = chr(LeNomP1[b] - 32)
                LeNomP1[c] = chr(LeNomP1[c] - 32)
                LeNomP1[d] = chr(LeNomP1[d] - 32)
                MotDePasseP1.append("".join(LeNomP1))
                for z in range(len(nomp1)):
                    if z != a and z != b and z != c and z != d:
                        LeNomP1[z] = ord(LeNomP1[z])
                        if LeNomP1[z] >= 97 and LeNomP1[z] <= 122:
                            LeNomP1[z] = chr(LeNomP1[z] - 32)
                            MotDePasseP1.append("".join(LeNomP1))
                            LeNomP1[z] = ord(LeNomP1[z])
                            LeNomP1[z] = chr(LeNomP1[z] + 32)

    # ------------------------------

    texte_pseudo = Label(window_parent1_info, text="Surnom - Pseudo :", font=Banhschrift)
    texte_pseudo.place(x=20, y=110)

    entry_pseudo1 = Entry(window_parent1_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_pseudo1.place(x=180, y=114)

    # -----

    def surnom_p1():
        global LeSurnomP1
        global MotDePasseP1
        surnomp1 = entry_pseudo1.get()
        var = str.lower(surnomp1)
        LeSurnomP1.append(var)
        MotDePasseP1.append(str.lower(surnomp1))
        MotDePasseP1.append(str.upper(surnomp1))

        for a in range(len(surnomp1)):
            LeSurnomP1 = [elt for elt in var]
            LeSurnomP1[a] = ord(LeSurnomP1[a])
            if LeSurnomP1[a] >= 97 and LeSurnomP1[a] <= 122:
                LeSurnomP1[a] = chr(LeSurnomP1[a] - 32)
                MotDePasseP1.append("".join(LeSurnomP1))
                for z in range(len(surnomp1)):
                    if z != a:
                        LeSurnomP1[z] = ord(LeSurnomP1[z])
                        if LeSurnomP1[z] >= 97 and LeSurnomP1[z] <= 122:
                            LeSurnomP1[z] = chr(LeSurnomP1[z] - 32)
                            MotDePasseP1.append("".join(LeSurnomP1))
                            LeSurnomP1[z] = ord(LeSurnomP1[z])
                            LeSurnomP1[z] = chr(LeSurnomP1[z] + 32)

        for a in range((len(surnomp1)) - 1):
            b = a + 1
            LeSurnomP1 = [elt for elt in var]
            LeSurnomP1[a] = ord(LeSurnomP1[a])
            LeSurnomP1[b] = ord(LeSurnomP1[b])
            if LeSurnomP1[a] >= 97 and LeSurnomP1[a] <= 122 and LeSurnomP1[b] >= 97 and LeSurnomP1[b] <= 122:
                LeSurnomP1[a] = chr(LeSurnomP1[a] - 32)
                LeSurnomP1[b] = chr(LeSurnomP1[b] - 32)
                MotDePasseP1.append("".join(LeSurnomP1))
                for z in range(len(surnomp1)):
                    if z != a and z != b:
                        LeSurnomP1[z] = ord(LeSurnomP1[z])
                        if LeSurnomP1[z] >= 97 and LeSurnomP1[z] <= 122:
                            LeSurnomP1[z] = chr(LeSurnomP1[z] - 32)
                            MotDePasseP1.append("".join(LeSurnomP1))
                            LeSurnomP1[z] = ord(LeSurnomP1[z])
                            LeSurnomP1[z] = chr(LeSurnomP1[z] + 32)

        for a in range((len(surnomp1)) - 2):
            b = a + 1
            c = a + 2
            LeSurnomP1 = [elt for elt in var]
            LeSurnomP1[a] = ord(LeSurnomP1[a])
            LeSurnomP1[b] = ord(LeSurnomP1[b])
            LeSurnomP1[c] = ord(LeSurnomP1[c])
            if LeSurnomP1[a] >= 97 and LeSurnomP1[a] <= 122 and LeSurnomP1[b] >= 97 and LeSurnomP1[b] <= 122 and LeSurnomP1[c] >= 97 and LeSurnomP1[c] <= 122:
                LeSurnomP1[a] = chr(LeSurnomP1[a] - 32)
                LeSurnomP1[b] = chr(LeSurnomP1[b] - 32)
                LeSurnomP1[c] = chr(LeSurnomP1[c] - 32)
                MotDePasseP1.append("".join(LeSurnomP1))
                for z in range(len(surnomp1)):
                    if z != a and z != b and z != c:
                        LeSurnomP1[z] = ord(LeSurnomP1[z])
                        if LeSurnomP1[z] >= 97 and LeSurnomP1[z] <= 122:
                            LeSurnomP1[z] = chr(LeSurnomP1[z] - 32)
                            MotDePasseP1.append("".join(LeSurnomP1))
                            LeSurnomP1[z] = ord(LeSurnomP1[z])
                            LeSurnomP1[z] = chr(LeSurnomP1[z] + 32)


        for a in range((len(surnomp1)) - 3):
            b = a+1
            c = a+2
            d = a+3
            LeSurnomP1 = [elt for elt in var]
            LeSurnomP1[a] = ord(LeSurnomP1[a])
            LeSurnomP1[b] = ord(LeSurnomP1[b])
            LeSurnomP1[c] = ord(LeSurnomP1[c])
            LeSurnomP1[d] = ord(LeSurnomP1[d])
            if LeSurnomP1[a] >= 97 and LeSurnomP1[a] <= 122 and LeSurnomP1[b] >= 97 and LeSurnomP1[b] <= 122 and LeSurnomP1[c] >= 97 and LeSurnomP1[c] <= 122 and LeSurnomP1[d] >= 97 and LeSurnomP1[d] <= 122:
                LeSurnomP1[a] = chr(LeSurnomP1[a] - 32)
                LeSurnomP1[b] = chr(LeSurnomP1[b] - 32)
                LeSurnomP1[c] = chr(LeSurnomP1[c] - 32)
                LeSurnomP1[d] = chr(LeSurnomP1[d] - 32)
                MotDePasseP1.append("".join(LeSurnomP1))
                for z in range(len(surnomp1)):
                    if z != a and z != b and z != c and z != d:
                        LeSurnomP1[z] = ord(LeSurnomP1[z])
                        if LeSurnomP1[z] >= 97 and LeSurnomP1[z] <= 122:
                            LeSurnomP1[z] = chr(LeSurnomP1[z] - 32)
                            MotDePasseP1.append("".join(LeSurnomP1))
                            LeSurnomP1[z] = ord(LeSurnomP1[z])
                            LeSurnomP1[z] = chr(LeSurnomP1[z] + 32)

    # ------------------------------

    texte_datenaissance = Label(window_parent1_info, text="Date de Naissance :", font=Banhschrift)
    texte_datenaissance.pack(anchor="w")
    texte_datenaissance.place(x=20, y=160)


    jourMenu1 = ttk.Combobox(window_parent1_info)
    jourMenu1.place(x=180, y=165, width=45)
    jourMenu1['values'] = (
    "Jour", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "15", "16", "17", "18",
    "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    jourMenu1.current(0)

    def jour_p1():
        global MotDePasseDNP1
        JourNaissanceP1 = jourMenu1.get()
        MotDePasseDNP1.append(JourNaissanceP1)

    # ----------

    slash1 = Label(window_parent1_info, text="/", font=Slashsfont)
    slash1.place(x=225, y=162)

    # ----------

    moisMenu1 = ttk.Combobox(window_parent1_info)
    moisMenu1.place(x=238, y=165, width=50)
    moisMenu1["values"] = ("Mois", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
    moisMenu1.current(0)

    def mois_p1():
        global MotDePasseDNP1
        MoisNaissanceP1 = moisMenu1.get()
        MotDePasseDNP1.append(MoisNaissanceP1)

    # ----------

    slash2 = Label(window_parent1_info, text="/", font=Slashsfont)
    slash2.place(x=288, y=162)

    # ----------

    anneeMenu1 = ttk.Combobox(window_parent1_info)
    anneeMenu1.place(x=301, y=165, width=62)
    anneeMenu1["values"] = (
    "Année", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
    "1992", "1991", "1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979",
    "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965",
    "1964", "1963", "1962", "1961", "1960", "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951",
    "1950", "1949", "1948", "1947", "1946", "1945", "1944", "1943", "1942", "1941", "1940", "1939", "1938", "1937",
    "1936", "1935", "1934", "1933", "1932", "1931", "1930", "1929", "1928", "1927", "1926", "1925", "1924", "1923",
    "1922", "1921", "1920", "1919")
    anneeMenu1.current(0)

    def annee_p1():
        global MotDePasseDNP1
        AnneeNaissanceP1 = anneeMenu1.get()
        MotDePasseDNP1.append(AnneeNaissanceP1)

    # ------------------------------

    texte_lieunaissance = Label(window_parent1_info, text="Ville Natale :", font=Banhschrift)
    texte_lieunaissance.pack(anchor="w")
    texte_lieunaissance.place(x=20, y=210)

    lieunaissanceMenu1 = Entry(window_parent1_info, width=30, bg='white', fg="black", justify="center")
    lieunaissanceMenu1.place(x=180, y=215)

    def lieu_p1():
        global LeLieuDeNaissanceP1
        LieuNaissanceP1 = lieunaissanceMenu1.get()
        LeLieuDeNaissanceP1.append(LieuNaissanceP1)

    # ------------------------------

    texte_departementnaissance = Label(window_parent1_info, text="Département de Naissance :", font=Banhschrift)
    texte_departementnaissance.pack(anchor="w")
    texte_departementnaissance.place(x=20, y=260)

    numdepartementMenu1 = ttk.Combobox(window_parent1_info)
    numdepartementMenu1.place(x=239, y=263, width=125)
    numdepartementMenu1["values"] = (
        "N° de département", "2A", "2B", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
        "14", "15", "15",
        "16", "17", "18", "19", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34",
        "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",
        "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
        "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88",
        "89", "90", "91", "92", "93", "94", "95")
    numdepartementMenu1.current(0)

    def dlieu_p1():
        global LeDLieuDeNaissanceP1
        DLieuNaissanceP1 = numdepartementMenu1.get()
        LeDLieuDeNaissanceP1.append(DLieuNaissanceP1)

    # ------------------------------

    def creation_MDP_parent1():
        global MotDePasseP1
        global MotDePasseDNP1
        global LeLieuDeNaissanceP1
        global LeDLieuDeNaissanceP1
        global MotDePasse
        prenom_p1()
        nom_p1()
        surnom_p1()
        jour_p1()
        mois_p1()
        annee_p1()
        lieu_p1()
        dlieu_p1()
        for i in range(len(MotDePasseP1)):
            MotDePasse.append(MotDePasseP1[i])
        for i in range(len(MotDePasseDNP1)):
            MotDePasse.append(MotDePasseDNP1[i])
        for i in range(len(LeLieuDeNaissanceP1)):
            MotDePasse.append(LeLieuDeNaissanceP1[i])
        for i in range(len(LeDLieuDeNaissanceP1)):
            MotDePasse.append(LeDLieuDeNaissanceP1[i])
        showinfobox_enregistrement()
        #print(MotDePasse)
        window_parent1_info.destroy()

    # ------------------------------


    bouton_valider_window_parent1_info = Button(window_parent1_info, text="      Valider les     \n informations", relief="groove", command=creation_MDP_parent1)  # Bouton avec texte + commande
    bouton_valider_window_parent1_info.place(x=150, y=310)


# ------------------------------Création de la fenetre secondaire concernant le parent 2------------------------------

def window_parent2_info(window_parent2_info):

    window_parent2_info = Toplevel()                                                                                    # Nouvelle fenetre1 au dessus de la précédente
    window_parent2_info.focus_set()                                                                                     # S'affiche comme fenêtre principale (Déja sélectionée en Bleu)
    window_parent2_info.geometry("410x370+250+240")                                                                     # Dimension de la fenêtre1
    window_parent2_info.resizable(width=False, height=False)                                                            # La fenetre n'est pas redimensionnable
    window_parent2_info.iconbitmap('icon.ico')
    window_parent2_info.title("Parent 2")                                                                      # Titre de la nouvelle fenêtre1

    # ------------------------------

    texte_prenom = Label(window_parent2_info, text="Prénom :", font=Banhschrift)
    texte_prenom.pack(anchor="w")
    texte_prenom.place(x=20, y=10)

    entry_prenom2 = Entry(window_parent2_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_prenom2.place(x=180, y=14)

    # -----

    def prenom_p2():
        global LePrenomP2
        global MotDePasseP2
        prenomp2 = entry_prenom2.get()
        var = str.lower(prenomp2)
        LePrenomP2.append(var)
        MotDePasseP2.append(str.upper(prenomp2))
        MotDePasseP2.append(str.lower(prenomp2))

        for a in range(len(prenomp2)):
            LePrenomP2 = [elt for elt in var]
            LePrenomP2[a] = ord(LePrenomP2[a])
            if LePrenomP2[a] >= 97 and LePrenomP2[a] <= 122:
                LePrenomP2[a] = chr(LePrenomP2[a] - 32)
                MotDePasseP2.append("".join(LePrenomP2))
                for z in range(len(prenomp2)):
                    if z != a:
                        LePrenomP2[z] = ord(LePrenomP2[z])
                        if LePrenomP2[z] >= 97 and LePrenomP2[z] <= 122:
                            LePrenomP2[z] = chr(LePrenomP2[z] - 32)
                            MotDePasseP2.append("".join(LePrenomP2))
                            LePrenomP2[z] = ord(LePrenomP2[z])
                            LePrenomP2[z] = chr(LePrenomP2[z] + 32)

        for a in range((len(prenomp2)) - 1):
            b = a + 1
            LePrenomP2 = [elt for elt in var]
            LePrenomP2[a] = ord(LePrenomP2[a])
            LePrenomP2[b] = ord(LePrenomP2[b])
            if LePrenomP2[a] >= 97 and LePrenomP2[a] <= 122 and LePrenomP2[b] >= 97 and LePrenomP2[b] <= 122:
                LePrenomP2[a] = chr(LePrenomP2[a] - 32)
                LePrenomP2[b] = chr(LePrenomP2[b] - 32)
                MotDePasseP2.append("".join(LePrenomP2))
                for z in range(len(prenomp2)):
                    if z != a and z != b:
                        LePrenomP2[z] = ord(LePrenomP2[z])
                        if LePrenomP2[z] >= 97 and LePrenomP2[z] <= 122:
                            LePrenomP2[z] = chr(LePrenomP2[z] - 32)
                            MotDePasseP2.append("".join(LePrenomP2))
                            LePrenomP2[z] = ord(LePrenomP2[z])
                            LePrenomP2[z] = chr(LePrenomP2[z] + 32)

        for a in range((len(prenomp2)) - 2):
            b = a + 1
            c = a + 2
            LePrenomP2 = [elt for elt in var]
            LePrenomP2[a] = ord(LePrenomP2[a])
            LePrenomP2[b] = ord(LePrenomP2[b])
            LePrenomP2[c] = ord(LePrenomP2[c])
            if LePrenomP2[a] >= 97 and LePrenomP2[a] <= 122 and LePrenomP2[b] >= 97 and LePrenomP2[b] <= 122 and LePrenomP2[c] >= 97 and LePrenomP2[c] <= 122:
                LePrenomP2[a] = chr(LePrenomP2[a] - 32)
                LePrenomP2[b] = chr(LePrenomP2[b] - 32)
                LePrenomP2[c] = chr(LePrenomP2[c] - 32)
                MotDePasseP2.append("".join(LePrenomP2))
                for z in range(len(prenomp2)):
                    if z != a and z != b and z != c:
                        LePrenomP2[z] = ord(LePrenomP2[z])
                        if LePrenomP2[z] >= 97 and LePrenomP2[z] <= 122:
                            LePrenomP2[z] = chr(LePrenomP2[z] - 32)
                            MotDePasseP2.append("".join(LePrenomP2))
                            LePrenomP2[z] = ord(LePrenomP2[z])
                            LePrenomP2[z] = chr(LePrenomP2[z] + 32)

        for a in range((len(prenomp2)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LePrenomP2 = [elt for elt in var]
            LePrenomP2[a] = ord(LePrenomP2[a])
            LePrenomP2[b] = ord(LePrenomP2[b])
            LePrenomP2[c] = ord(LePrenomP2[c])
            LePrenomP2[d] = ord(LePrenomP2[d])
            if LePrenomP2[a] >= 97 and LePrenomP2[a] <= 122 and LePrenomP2[b] >= 97 and LePrenomP2[b] <= 122 and LePrenomP2[c] >= 97 and LePrenomP2[c] <= 122 and LePrenomP2[d] >= 97 and LePrenomP2[d] <= 122:
                LePrenomP2[a] = chr(LePrenomP2[a] - 32)
                LePrenomP2[b] = chr(LePrenomP2[b] - 32)
                LePrenomP2[c] = chr(LePrenomP2[c] - 32)
                LePrenomP2[d] = chr(LePrenomP2[d] - 32)
                MotDePasseP2.append("".join(LePrenomP2))
                for z in range(len(prenomp2)):
                    if z != a and z != b and z != c and z != d:
                        LePrenomP2[z] = ord(LePrenomP2[z])
                        if LePrenomP2[z] >= 97 and LePrenomP2[z] <= 122:
                            LePrenomP2[z] = chr(LePrenomP2[z] - 32)
                            MotDePasseP2.append("".join(LePrenomP2))
                            LePrenomP2[z] = ord(LePrenomP2[z])
                            LePrenomP2[z] = chr(LePrenomP2[z] + 32)

    # ------------------------------

    texte_nom = Label(window_parent2_info, text="Nom :", font=Banhschrift)
    texte_nom.place(x=20, y=60)

    entry_nom2 = Entry(window_parent2_info, width=30, bg='white', fg="black", justify="center")                         # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_nom2.place(x=180, y=64)

    # -----

    def nom_p2():
        global LeNomP2
        global MotDePasseP2
        nomp2 = entry_nom2.get()
        var = str.lower(nomp2)
        LeNomP2.append(var)
        MotDePasseP2.append(str.upper(nomp2))
        MotDePasseP2.append(str.lower(nomp2))

        for a in range(len(nomp2)):
            LeNomP2 = [elt for elt in var]
            LeNomP2[a] = ord(LeNomP2[a])
            if LeNomP2[a] >= 97 and LeNomP2[a] <= 122:
                LeNomP2[a] = chr(LeNomP2[a] - 32)
                MotDePasseP2.append("".join(LeNomP2))
                for z in range(len(nomp2)):
                    if z != a:
                        LeNomP2[z] = ord(LeNomP2[z])
                        if LeNomP2[z] >= 97 and LeNomP2[z] <= 122:
                            LeNomP2[z] = chr(LeNomP2[z] - 32)
                            MotDePasseP2.append("".join(LeNomP2))
                            LeNomP2[z] = ord(LeNomP2[z])
                            LeNomP2[z] = chr(LeNomP2[z] + 32)

        for a in range((len(nomp2)) - 1):
            b = a + 1
            LeNomP2 = [elt for elt in var]
            LeNomP2[a] = ord(LeNomP2[a])
            LeNomP2[b] = ord(LeNomP2[b])
            if LeNomP2[a] >= 97 and LeNomP2[a] <= 122 and LeNomP2[b] >= 97 and LeNomP2[b] <= 122:
                LeNomP2[a] = chr(LeNomP2[a] - 32)
                LeNomP2[b] = chr(LeNomP2[b] - 32)
                MotDePasseP2.append("".join(LeNomP2))
                for z in range(len(nomp2)):
                    if z != a and z != b:
                        LeNomP2[z] = ord(LeNomP2[z])
                        if LeNomP2[z] >= 97 and LeNomP2[z] <= 122:
                            LeNomP2[z] = chr(LeNomP2[z] - 32)
                            MotDePasseP2.append("".join(LeNomP2))
                            LeNomP2[z] = ord(LeNomP2[z])
                            LeNomP2[z] = chr(LeNomP2[z] + 32)

        for a in range((len(nomp2)) - 2):
            b = a + 1
            c = a + 2
            LeNomP2 = [elt for elt in var]
            LeNomP2[a] = ord(LeNomP2[a])
            LeNomP2[b] = ord(LeNomP2[b])
            LeNomP2[c] = ord(LeNomP2[c])
            if LeNomP2[a] >= 97 and LeNomP2[a] <= 122 and LeNomP2[b] >= 97 and LeNomP2[b] <= 122 and LeNomP2[c] >= 97 and LeNomP2[c] <= 122:
                LeNomP2[a] = chr(LeNomP2[a] - 32)
                LeNomP2[b] = chr(LeNomP2[b] - 32)
                LeNomP2[c] = chr(LeNomP2[c] - 32)
                MotDePasseP2.append("".join(LeNomP2))
                for z in range(len(nomp2)):
                    if z != a and z != b and z != c:
                        LeNomP2[z] = ord(LeNomP2[z])
                        if LeNomP2[z] >= 97 and LeNomP2[z] <= 122:
                            LeNomP2[z] = chr(LeNomP2[z] - 32)
                            MotDePasseP2.append("".join(LeNomP2))
                            LeNomP2[z] = ord(LeNomP2[z])
                            LeNomP2[z] = chr(LeNomP2[z] + 32)

        for a in range((len(nomp2)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeNomP2 = [elt for elt in var]
            LeNomP2[a] = ord(LeNomP2[a])
            LeNomP2[b] = ord(LeNomP2[b])
            LeNomP2[c] = ord(LeNomP2[c])
            LeNomP2[d] = ord(LeNomP2[d])
            if LeNomP2[a] >= 97 and LeNomP2[a] <= 122 and LeNomP2[b] >= 97 and LeNomP2[b] <= 122 and LeNomP2[c] >= 97 and LeNomP2[c] <= 122 and LeNomP2[d] >= 97 and LeNomP2[d] <= 122:
                LeNomP2[a] = chr(LeNomP2[a] - 32)
                LeNomP2[b] = chr(LeNomP2[b] - 32)
                LeNomP2[c] = chr(LeNomP2[c] - 32)
                LeNomP2[d] = chr(LeNomP2[d] - 32)
                MotDePasseP2.append("".join(LeNomP2))
                for z in range(len(nomp2)):
                    if z != a and z != b and z != c and z != d:
                        LeNomP2[z] = ord(LeNomP2[z])
                        if LeNomP2[z] >= 97 and LeNomP2[z] <= 122:
                            LeNomP2[z] = chr(LeNomP2[z] - 32)
                            MotDePasseP2.append("".join(LeNomP2))
                            LeNomP2[z] = ord(LeNomP2[z])
                            LeNomP2[z] = chr(LeNomP2[z] + 32)

    # ------------------------------

    texte_pseudo = Label(window_parent2_info, text="Surnom, Pseudo :", font=Banhschrift)
    texte_pseudo.place(x=20, y=110)

    entry_pseudo2 = Entry(window_parent2_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_pseudo2.place(x=180, y=114)

    # -----

    def surnom_p2():
        global LeSurnomP2
        global MotDePasseP2
        surnomp2 = entry_pseudo2.get()
        var = str.lower(surnomp2)
        LeSurnomP2.append(var)
        MotDePasseP2.append(str.lower(surnomp2))
        MotDePasseP2.append(str.upper(surnomp2))

        for a in range(len(surnomp2)):
            LeSurnomP2 = [elt for elt in var]
            LeSurnomP2[a] = ord(LeSurnomP2[a])
            if LeSurnomP2[a] >= 97 and LeSurnomP2[a] <= 122:
                LeSurnomP2[a] = chr(LeSurnomP2[a] - 32)
                MotDePasseP2.append("".join(LeSurnomP2))
                for z in range(len(surnomp2)):
                    if z != a:
                        LeSurnomP2[z] = ord(LeSurnomP2[z])
                        if LeSurnomP2[z] >= 97 and LeSurnomP2[z] <= 122:
                            LeSurnomP2[z] = chr(LeSurnomP2[z] - 32)
                            MotDePasseP2.append("".join(LeSurnomP2))
                            LeSurnomP2[z] = ord(LeSurnomP2[z])
                            LeSurnomP2[z] = chr(LeSurnomP2[z] + 32)

        for a in range((len(surnomp2)) - 1):
            b = a + 1
            LeSurnomP2 = [elt for elt in var]
            LeSurnomP2[a] = ord(LeSurnomP2[a])
            LeSurnomP2[b] = ord(LeSurnomP2[b])
            if LeSurnomP2[a] >= 97 and LeSurnomP2[a] <= 122 and LeSurnomP2[b] >= 97 and LeSurnomP2[b] <= 122:
                LeSurnomP2[a] = chr(LeSurnomP2[a] - 32)
                LeSurnomP2[b] = chr(LeSurnomP2[b] - 32)
                MotDePasseP2.append("".join(LeSurnomP2))
                for z in range(len(surnomp2)):
                    if z != a and z != b:
                        LeSurnomP2[z] = ord(LeSurnomP2[z])
                        if LeSurnomP2[z] >= 97 and LeSurnomP2[z] <= 122:
                            LeSurnomP2[z] = chr(LeSurnomP2[z] - 32)
                            MotDePasseP2.append("".join(LeSurnomP2))
                            LeSurnomP2[z] = ord(LeSurnomP2[z])
                            LeSurnomP2[z] = chr(LeSurnomP2[z] + 32)

        for a in range((len(surnomp2)) - 2):
            b = a + 1
            c = a + 2
            LeSurnomP2 = [elt for elt in var]
            LeSurnomP2[a] = ord(LeSurnomP2[a])
            LeSurnomP2[b] = ord(LeSurnomP2[b])
            LeSurnomP2[c] = ord(LeSurnomP2[c])
            if LeSurnomP2[a] >= 97 and LeSurnomP2[a] <= 122 and LeSurnomP2[b] >= 97 and LeSurnomP2[b] <= 122 and LeSurnomP2[c] >= 97 and LeSurnomP2[c] <= 122:
                LeSurnomP2[a] = chr(LeSurnomP2[a] - 32)
                LeSurnomP2[b] = chr(LeSurnomP2[b] - 32)
                LeSurnomP2[c] = chr(LeSurnomP2[c] - 32)
                MotDePasseP2.append("".join(LeSurnomP2))
                for z in range(len(surnomp2)):
                    if z != a and z != b and z != c:
                        LeSurnomP2[z] = ord(LeSurnomP2[z])
                        if LeSurnomP2[z] >= 97 and LeSurnomP2[z] <= 122:
                            LeSurnomP2[z] = chr(LeSurnomP2[z] - 32)
                            MotDePasseP2.append("".join(LeSurnomP2))
                            LeSurnomP2[z] = ord(LeSurnomP2[z])
                            LeSurnomP2[z] = chr(LeSurnomP2[z] + 32)

        for a in range((len(surnomp2)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeSurnomP2 = [elt for elt in var]
            LeSurnomP2[a] = ord(LeSurnomP2[a])
            LeSurnomP2[b] = ord(LeSurnomP2[b])
            LeSurnomP2[c] = ord(LeSurnomP2[c])
            LeSurnomP2[d] = ord(LeSurnomP2[d])
            if LeSurnomP2[a] >= 97 and LeSurnomP2[a] <= 122 and LeSurnomP2[b] >= 97 and LeSurnomP2[b] <= 122 and LeSurnomP2[c] >= 97 and LeSurnomP2[c] <= 122 and LeSurnomP2[d] >= 97 and LeSurnomP2[d] <= 122:
                LeSurnomP2[a] = chr(LeSurnomP2[a] - 32)
                LeSurnomP2[b] = chr(LeSurnomP2[b] - 32)
                LeSurnomP2[c] = chr(LeSurnomP2[c] - 32)
                LeSurnomP2[d] = chr(LeSurnomP2[d] - 32)
                MotDePasseP2.append("".join(LeSurnomP2))
                for z in range(len(surnomp2)):
                    if z != a and z != b and z != c and z != d:
                        LeSurnomP2[z] = ord(LeSurnomP2[z])
                        if LeSurnomP2[z] >= 97 and LeSurnomP2[z] <= 122:
                            LeSurnomP2[z] = chr(LeSurnomP2[z] - 32)
                            MotDePasseP2.append("".join(LeSurnomP2))
                            LeSurnomP2[z] = ord(LeSurnomP2[z])
                            LeSurnomP2[z] = chr(LeSurnomP2[z] + 32)

    # ------------------------------

    texte_datenaissance = Label(window_parent2_info, text="Date de Naissance :", font=Banhschrift)
    texte_datenaissance.pack(anchor="w")
    texte_datenaissance.place(x=20, y=160)


    jourMenu2 = ttk.Combobox(window_parent2_info)
    jourMenu2.place(x=180, y=165, width=45)
    jourMenu2['values'] = (
    "Jour", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "15", "16", "17", "18",
    "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    jourMenu2.current(0)

    def jour_p2():
        global MotDePasseDNP2
        JourNaissanceP2 = jourMenu2.get()
        MotDePasseDNP2.append(JourNaissanceP2)

    # -----

    slash1 = Label(window_parent2_info, text="/", font=Slashsfont)
    slash1.place(x=225, y=162)

    # -----

    moisMenu2 = ttk.Combobox(window_parent2_info)
    moisMenu2.place(x=238, y=165, width=50)
    moisMenu2["values"] = ("Mois", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
    moisMenu2.current(0)

    def mois_p2():
        global MotDePasseDNP2
        MoisNaissanceP2 = moisMenu2.get()
        MotDePasseDNP2.append(MoisNaissanceP2)

    # -----

    slash2 = Label(window_parent2_info, text="/", font=Slashsfont)
    slash2.place(x=288, y=162)

    # -----

    anneeMenu2 = ttk.Combobox(window_parent2_info)
    anneeMenu2.place(x=301, y=165, width=62)
    anneeMenu2["values"] = (
    "Année", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
    "1992", "1991", "1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979",
    "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965",
    "1964", "1963", "1962", "1961", "1960", "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951",
    "1950", "1949", "1948", "1947", "1946", "1945", "1944", "1943", "1942", "1941", "1940", "1939", "1938", "1937",
    "1936", "1935", "1934", "1933", "1932", "1931", "1930", "1929", "1928", "1927", "1926", "1925", "1924", "1923",
    "1922", "1921", "1920", "1919")
    anneeMenu2.current(0)

    def annee_p2():
        global MotDePasseDNP2
        AnneeNaissanceP2 = anneeMenu2.get()
        MotDePasseDNP2.append(AnneeNaissanceP2)

    # ------------------------------

    texte_lieunaissance = Label(window_parent2_info, text="Ville Natale :", font=Banhschrift)
    texte_lieunaissance.pack(anchor="w")
    texte_lieunaissance.place(x=20, y=210)

    lieunaissanceMenu2 = Entry(window_parent2_info, width=30, bg='white', fg="black", justify="center")
    lieunaissanceMenu2.place(x=180, y=215)

    def lieu_p2():
        global LeDLieuDeNaissanceP2
        LieuNaissanceP2 = lieunaissanceMenu2.get()
        LeLieuDeNaissanceP2.append(LieuNaissanceP2)

    # ------------------------------

    texte_departementnaissance = Label(window_parent2_info, text="Département de Naissance :", font=Banhschrift)
    texte_departementnaissance.pack(anchor="w")
    texte_departementnaissance.place(x=20, y=260)

    numdepartementMenu2 = ttk.Combobox(window_parent2_info)
    numdepartementMenu2.place(x=239, y=263, width=125)
    numdepartementMenu2["values"] = (
        "N° de département", "2A", "2B", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
        "14", "15", "15",
        "16", "17", "18", "19", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34",
        "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",
        "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
        "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88",
        "89", "90", "91", "92", "93", "94", "95")
    numdepartementMenu2.current(0)

    def dlieu_p2():
        global LeDLieuDeNaissanceP2
        DLieuNaissanceP2 = numdepartementMenu2.get()
        LeDLieuDeNaissanceP2.append(DLieuNaissanceP2)

    # ------------------------------

    def creation_MDP_parent2():
        global MotDePasseP2
        global MotDePasseDNP2
        global LeLieuDeNaissanceP2
        global LeDLieuDeNaissanceP2
        global MotDePasse
        prenom_p2()
        nom_p2()
        surnom_p2()
        jour_p2()
        mois_p2()
        annee_p2()
        lieu_p2()
        dlieu_p2()
        for i in range(len(MotDePasseP2)):
            MotDePasse.append(MotDePasseP2[i])
        for i in range(len(MotDePasseDNP2)):
            MotDePasse.append(MotDePasseDNP2[i])
        for i in range(len(LeLieuDeNaissanceP2)):
            MotDePasse.append(LeLieuDeNaissanceP2[i])
        for i in range(len(LeDLieuDeNaissanceP2)):
            MotDePasse.append(LeDLieuDeNaissanceP2[i])
        showinfobox_enregistrement()
        #print(MotDePasse)
        window_parent2_info.destroy()

    # ------------------------------

    bouton_valider_window_parent2_info = Button(window_parent2_info, text="      Valider les     \n informations", relief="groove", command=creation_MDP_parent2)  # Bouton avec texte + commande
    bouton_valider_window_parent2_info.place(x=150, y=310)


# ------------------------------Création de la fenetre secondaire concernant le conjoint------------------------------

def window_conjoint_info(window_conjoint_info):

    window_conjoint_info = Toplevel()                                                                                   # Nouvelle fenetre1 au dessus de la précédente
    window_conjoint_info.focus_set()                                                                                    # S'affiche comme fenêtre principale (Déja sélectionée en Bleu)
    window_conjoint_info.geometry("410x370+250+240")                                                                    # Dimension de la fenêtre1
    window_conjoint_info.resizable(width=False, height=False)                                                           # La fenetre n'est pas redimensionnable
    window_conjoint_info.iconbitmap('icon.ico')
    window_conjoint_info.title("Conjoint")                                                                              # Titre de la nouvelle fenêtre1

    # ------------------------------

    texte_prenom = Label(window_conjoint_info, text="Prénom :", font=Banhschrift)
    texte_prenom.pack(anchor="w")
    texte_prenom.place(x=20, y=10)

    entry_prenomC = Entry(window_conjoint_info, width=30, bg='white', fg="black", justify="center")                     # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_prenomC.place(x=180, y=14)

    # -----

    def prenom_c():
        global LePrenomC
        global MotDePasseC
        PrenomC = entry_prenomC.get()
        var = str.lower(PrenomC)
        LePrenomC.append(var)
        MotDePasseC.append(str.upper(PrenomC))
        MotDePasseC.append(str.lower(PrenomC))

        for a in range(len(PrenomC)):
            LePrenomC = [elt for elt in var]
            LePrenomC[a] = ord(LePrenomC[a])
            if LePrenomC[a] >= 97 and LePrenomC[a] <= 122:
                LePrenomC[a] = chr(LePrenomC[a]-32)
                MotDePasseC.append("".join(LePrenomC))
                for z in range(len(PrenomC)):
                    if z != a:
                        LePrenomC[z] = ord(LePrenomC[z])
                        if LePrenomC[z] >= 97 and LePrenomC[z] <= 122:
                            LePrenomC[z] = chr(LePrenomC[z]-32)
                            MotDePasseC.append("".join(LePrenomC))
                            LePrenomC[z] = ord(LePrenomC[z])
                            LePrenomC[z] = chr(LePrenomC[z]+32)

        for a in range((len(PrenomC))-1):
            b = a + 1
            LePrenomC = [elt for elt in var]
            LePrenomC[a] = ord(LePrenomC[a])
            LePrenomC[b] = ord(LePrenomC[b])
            if LePrenomC[a]>=97 and LePrenomC[a]<=122 and LePrenomC[b]>=97 and LePrenomC[b]<=122:
                LePrenomC[a] = chr(LePrenomC[a]-32)
                LePrenomC[b] = chr(LePrenomC[b]-32)
                MotDePasseC.append("".join(LePrenomC))
                for z in range(len(PrenomC)):
                    if z != a and z !=b:
                        LePrenomC[z] = ord(LePrenomC[z])
                        if LePrenomC[z] >= 97 and LePrenomC[z] <= 122:
                            LePrenomC[z] = chr(LePrenomC[z]-32)
                            MotDePasseC.append("".join(LePrenomC))
                            LePrenomC[z] = ord(LePrenomC[z])
                            LePrenomC[z] = chr(LePrenomC[z]+32)

        for a in range((len(PrenomC))-2):
            b = a + 1
            c = a + 2
            LePrenomC = [elt for elt in var]
            LePrenomC[a] = ord(LePrenomC[a])
            LePrenomC[b] = ord(LePrenomC[b])
            LePrenomC[c] = ord(LePrenomC[c])
            if LePrenomC[a]>=97 and LePrenomC[a]<=122 and LePrenomC[b]>=97 and LePrenomC[b]<=122 and LePrenomC[c]>=97 and LePrenomC[c]<=122:
                LePrenomC[a] = chr(LePrenomC[a]-32)
                LePrenomC[b] = chr(LePrenomC[b]-32)
                LePrenomC[c] = chr(LePrenomC[c]-32)
                MotDePasseC.append("".join(LePrenomC))
                for z in range(len(PrenomC)):
                    if z != a and z != b and z != c:
                        LePrenomC[z] = ord(LePrenomC[z])
                        if LePrenomC[z] >= 97 and LePrenomC[z] <= 122:
                            LePrenomC[z] = chr(LePrenomC[z]-32)
                            MotDePasseC.append("".join(LePrenomC))
                            LePrenomC[z] = ord(LePrenomC[z])
                            LePrenomC[z] = chr(LePrenomC[z]+32)

        for a in range((len(PrenomC))-3):
            b = a + 1
            c = a + 2
            d = a + 3
            LePrenomC= [elt for elt in var]
            LePrenomC[a] = ord(LePrenomC[a])
            LePrenomC[b] = ord(LePrenomC[b])
            LePrenomC[c] = ord(LePrenomC[c])
            LePrenomC[d] = ord(LePrenomC[d])
            if LePrenomC[a]>=97 and LePrenomC[a]<=122 and LePrenomC[b]>=97 and LePrenomC[b]<=122 and LePrenomC[c]>=97 and LePrenomC[c]<=122 and LePrenomC[d]>=97 and LePrenomC[d]<=122:
                LePrenomC[a] = chr(LePrenomC[a]-32)
                LePrenomC[b] = chr(LePrenomC[b]-32)
                LePrenomC[c] = chr(LePrenomC[c]-32)
                LePrenomC[d] = chr(LePrenomC[d]-32)
                MotDePasseC.append("".join(LePrenomC))
                for z in range(len(PrenomC)):
                    if z != a and z != b and z != c and z != d:
                        LePrenomC[z] = ord(LePrenomC[z])
                        if LePrenomC[z] >= 97 and LePrenomC[z] <= 122:
                            LePrenomC[z] = chr(LePrenomC[z]-32)
                            MotDePasseC.append("".join(LePrenomC))
                            LePrenomC[z] = ord(LePrenomC[z])
                            LePrenomC[z] = chr(LePrenomC[z]+32)

    # ------------------------------

    texte_nom = Label(window_conjoint_info, text="Nom :", font=Banhschrift)
    texte_nom.place(x=20, y=60)

    entry_nomC = Entry(window_conjoint_info, width=30, bg='white', fg="black", justify="center")                        # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_nomC.place(x=180, y=64)

    # -----

    def nom_c():
        global LeNomC
        global MotDePasseC
        NomC = entry_nomC.get()
        var = str.lower(NomC)
        LeNomC.append(var)
        MotDePasseC.append(str.upper(NomC))
        MotDePasseC.append(str.lower(NomC))

        for a in range(len(NomC)):
            LeNomC = [elt for elt in var]
            LeNomC[a] = ord(LeNomC[a])
            if LeNomC[a] >= 97 and LeNomC[a] <= 122:
                LeNomC[a] = chr(LeNomC[a] - 32)
                MotDePasseC.append("".join(LeNomC))
                for z in range(len(NomC)):
                    if z != a:
                        LeNomC[z] = ord(LeNomC[z])
                        if LeNomC[z] >= 97 and LeNomC[z] <= 122:
                            LeNomC[z] = chr(LeNomC[z] - 32)
                            MotDePasseC.append("".join(LeNomC))
                            LeNomC[z] = ord(LeNomC[z])
                            LeNomC[z] = chr(LeNomC[z] + 32)

        for a in range((len(NomC)) - 1):
            b = a + 1
            LeNomC = [elt for elt in var]
            LeNomC[a] = ord(LeNomC[a])
            LeNomC[b] = ord(LeNomC[b])
            if LeNomC[a] >= 97 and LeNomC[a] <= 122 and LeNomC[b] >= 97 and LeNomC[b] <= 122:
                LeNomC[a] = chr(LeNomC[a] - 32)
                LeNomC[b] = chr(LeNomC[b] - 32)
                MotDePasseC.append("".join(LeNomC))
                for z in range(len(NomC)):
                    if z != a and z != b:
                        LeNomC[z] = ord(LeNomC[z])
                        if LeNomC[z] >= 97 and LeNomC[z] <= 122:
                            LeNomC[z] = chr(LeNomC[z] - 32)
                            MotDePasseC.append("".join(LeNomC))
                            LeNomC[z] = ord(LeNomC[z])
                            LeNomC[z] = chr(LeNomC[z] + 32)

        for a in range((len(NomC)) - 2):
            b = a + 1
            c = a + 2
            LeNomC = [elt for elt in var]
            LeNomC[a] = ord(LeNomC[a])
            LeNomC[b] = ord(LeNomC[b])
            LeNomC[c] = ord(LeNomC[c])
            if LeNomC[a] >= 97 and LeNomC[a] <= 122 and LeNomC[b] >= 97 and LeNomC[b] <= 122 and LeNomC[c] >= 97 and LeNomC[c] <= 122:
                LeNomC[a] = chr(LeNomC[a] - 32)
                LeNomC[b] = chr(LeNomC[b] - 32)
                LeNomC[c] = chr(LeNomC[c] - 32)
                MotDePasseC.append("".join(LeNomC))
                for z in range(len(NomC)):
                    if z != a and z != b and z != c:
                        LeNomC[z] = ord(LeNomC[z])
                        if LeNomC[z] >= 97 and LeNomC[z] <= 122:
                            LeNomC[z] = chr(LeNomC[z] - 32)
                            MotDePasseC.append("".join(LeNomC))
                            LeNomC[z] = ord(LeNomC[z])
                            LeNomC[z] = chr(LeNomC[z] + 32)

        for a in range((len(NomC)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeNomC = [elt for elt in var]
            LeNomC[a] = ord(LeNomC[a])
            LeNomC[b] = ord(LeNomC[b])
            LeNomC[c] = ord(LeNomC[c])
            LeNomC[d] = ord(LeNomC[d])
            if LeNomC[a] >= 97 and LeNomC[a] <= 122 and LeNomC[b] >= 97 and LeNomC[b] <= 122 and LeNomC[c] >= 97 and LeNomC[c] <= 122 and LeNomC[d] >= 97 and LeNomC[d] <= 122:
                LeNomC[a] = chr(LeNomC[a] - 32)
                LeNomC[b] = chr(LeNomC[b] - 32)
                LeNomC[c] = chr(LeNomC[c] - 32)
                LeNomC[d] = chr(LeNomC[d] - 32)
                MotDePasseC.append("".join(LeNomC))
                for z in range(len(NomC)):
                    if z != a and z != b and z != c and z != d:
                        LeNomC[z] = ord(LeNomC[z])
                        if LeNomC[z] >= 97 and LeNomC[z] <= 122:
                            LeNomC[z] = chr(LeNomC[z] - 32)
                            MotDePasseC.append("".join(LeNomC))
                            LeNomC[z] = ord(LeNomC[z])
                            LeNomC[z] = chr(LeNomC[z] + 32)

    # ------------------------------

    texte_pseudo = Label(window_conjoint_info, text="Surnom - Pseudo :", font=Banhschrift)
    texte_pseudo.place(x=20, y=110)

    entry_pseudoC = Entry(window_conjoint_info, width=30, bg='white', fg="black", justify="center")                     # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_pseudoC.place(x=180, y=114)

    # -----

    def surnom_c():
        global LeSurnomC
        global MotDePasseC
        SurnomC = entry_pseudoC.get()
        var = str.lower(SurnomC)
        LeSurnomC.append(var)
        MotDePasseC.append(str.lower(SurnomC))
        MotDePasseC.append(str.upper(SurnomC))

        for a in range(len(SurnomC)):
            LeSurnomC = [elt for elt in var]
            LeSurnomC[a] = ord(LeSurnomC[a])
            if LeSurnomC[a] >= 97 and LeSurnomC[a] <= 122:
                LeSurnomC[a] = chr(LeSurnomC[a] - 32)
                MotDePasseC.append("".join(LeSurnomC))
                for z in range(len(SurnomC)):
                    if z != a:
                        LeSurnomC[z] = ord(LeSurnomC[z])
                        if LeSurnomC[z] >= 97 and LeSurnomC[z] <= 122:
                            LeSurnomC[z] = chr(LeSurnomC[z] - 32)
                            MotDePasseC.append("".join(LeSurnomC))
                            LeSurnomC[z] = ord(LeSurnomC[z])
                            LeSurnomC[z] = chr(LeSurnomC[z] + 32)

        for a in range((len(SurnomC)) - 1):
            b = a + 1
            LeSurnomC = [elt for elt in var]
            LeSurnomC[a] = ord(LeSurnomC[a])
            LeSurnomC[b] = ord(LeSurnomC[b])
            if LeSurnomC[a] >= 97 and LeSurnomC[a] <= 122 and LeSurnomC[b] >= 97 and LeSurnomC[b] <= 122:
                LeSurnomC[a] = chr(LeSurnomC[a] - 32)
                LeSurnomC[b] = chr(LeSurnomC[b] - 32)
                MotDePasseC.append("".join(LeSurnomC))
                for z in range(len(SurnomC)):
                    if z != a and z != b:
                        LeSurnomC[z] = ord(LeSurnomC[z])
                        if LeSurnomC[z] >= 97 and LeSurnomC[z] <= 122:
                            LeSurnomC[z] = chr(LeSurnomC[z] - 32)
                            MotDePasseC.append("".join(LeSurnomC))
                            LeSurnomC[z] = ord(LeSurnomC[z])
                            LeSurnomC[z] = chr(LeSurnomC[z] + 32)

        for a in range((len(SurnomC)) - 2):
            b = a + 1
            c = a + 2
            LeSurnomC = [elt for elt in var]
            LeSurnomC[a] = ord(LeSurnomC[a])
            LeSurnomC[b] = ord(LeSurnomC[b])
            LeSurnomC[c] = ord(LeSurnomC[c])
            if LeSurnomC[a] >= 97 and LeSurnomC[a] <= 122 and LeSurnomC[b] >= 97 and LeSurnomC[b] <= 122 and LeSurnomC[c] >= 97 and LeSurnomC[c] <= 122:
                LeSurnomC[a] = chr(LeSurnomC[a] - 32)
                LeSurnomC[b] = chr(LeSurnomC[b] - 32)
                LeSurnomC[c] = chr(LeSurnomC[c] - 32)
                MotDePasseC.append("".join(LeSurnomC))
                for z in range(len(SurnomC)):
                    if z != a and z != b and z != c:
                        LeSurnomC[z] = ord(LeSurnomC[z])
                        if LeSurnomC[z] >= 97 and LeSurnomC[z] <= 122:
                            LeSurnomC[z] = chr(LeSurnomC[z] - 32)
                            MotDePasseC.append("".join(LeSurnomC))
                            LeSurnomC[z] = ord(LeSurnomC[z])
                            LeSurnomC[z] = chr(LeSurnomC[z] + 32)

        for a in range((len(SurnomC)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeSurnomC = [elt for elt in var]
            LeSurnomC[a] = ord(LeSurnomC[a])
            LeSurnomC[b] = ord(LeSurnomC[b])
            LeSurnomC[c] = ord(LeSurnomC[c])
            LeSurnomC[d] = ord(LeSurnomC[d])
            if LeSurnomC[a] >= 97 and LeSurnomC[a] <= 122 and LeSurnomC[b] >= 97 and LeSurnomC[b] <= 122 and LeSurnomC[c] >= 97 and LeSurnomC[c] <= 122 and LeSurnomC[d] >= 97 and LeSurnomC[d] <= 122:
                LeSurnomC[a] = chr(LeSurnomC[a] - 32)
                LeSurnomC[b] = chr(LeSurnomC[b] - 32)
                LeSurnomC[c] = chr(LeSurnomC[c] - 32)
                LeSurnomC[d] = chr(LeSurnomC[d] - 32)
                MotDePasseC.append("".join(LeSurnomC))
                for z in range(len(SurnomC)):
                    if z != a and z != b and z != c and z != d:
                        LeSurnomC[z] = ord(LeSurnomC[z])
                        if LeSurnomC[z] >= 97 and LeSurnomC[z] <= 122:
                            LeSurnomC[z] = chr(LeSurnomC[z] - 32)
                            MotDePasseC.append("".join(LeSurnomC))
                            LeSurnomC[z] = ord(LeSurnomC[z])
                            LeSurnomC[z] = chr(LeSurnomC[z] + 32)

    # ------------------------------

    texte_datenaissance = Label(window_conjoint_info, text="Date de Naissance :", font=Banhschrift)
    texte_datenaissance.pack(anchor="w")
    texte_datenaissance.place(x=20, y=160)

    jourMenuC = ttk.Combobox(window_conjoint_info)
    jourMenuC.place(x=180, y=165, width=45)
    jourMenuC['values'] = (
    "Jour", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "15", "16", "17", "18",
    "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    jourMenuC.current(0)

    def jour_c():
        global MotDePasseC
        JourNaissanceC = jourMenuC.get()
        MotDePasseC.append(JourNaissanceC)

    # -----

    slash1 = Label(window_conjoint_info, text="/", font=Slashsfont)
    slash1.place(x=225, y=162)

    # -----

    moisMenuC = ttk.Combobox(window_conjoint_info)
    moisMenuC.place(x=238, y=165, width=50)
    moisMenuC["values"] = ("Mois", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
    moisMenuC.current(0)

    def mois_c():
        global MotDePasseC
        MoisNaissanceC = moisMenuC.get()
        MotDePasseC.append(MoisNaissanceC)

    # -----

    slash2 = Label(window_conjoint_info, text="/", font=Slashsfont)
    slash2.place(x=288, y=162)

    # -----

    anneeMenuC = ttk.Combobox(window_conjoint_info)
    anneeMenuC.place(x=301, y=165, width=62)
    anneeMenuC["values"] = (
    "Année", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
    "1992", "1991", "1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979",
    "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965",
    "1964", "1963", "1962", "1961", "1960", "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951",
    "1950", "1949", "1948", "1947", "1946", "1945", "1944", "1943", "1942", "1941", "1940", "1939", "1938", "1937",
    "1936", "1935", "1934", "1933", "1932", "1931", "1930", "1929", "1928", "1927", "1926", "1925", "1924", "1923",
    "1922", "1921", "1920", "1919")
    anneeMenuC.current(0)

    def annee_c():
        global MotDePasseC
        AnneeNaissanceC = anneeMenuC.get()
        MotDePasseC.append(AnneeNaissanceC)

    # ------------------------------

    texte_lieunaissance = Label(window_conjoint_info, text="Ville Natale :", font=Banhschrift)
    texte_lieunaissance.pack(anchor="w")
    texte_lieunaissance.place(x=20, y=210)

    lieunaissanceMenuC = Entry(window_conjoint_info, width=30, bg='white', fg="black", justify="center")
    lieunaissanceMenuC.place(x=180, y=215)

    def lieu_c():
        global LeLieuDeNaissanceC
        LieuNaissanceC = lieunaissanceMenuC.get()
        LeLieuDeNaissanceC.append(LieuNaissanceC)

    # ------------------------------

    texte_departementnaissance = Label(window_conjoint_info, text="Département de Naissance :", font=Banhschrift)
    texte_departementnaissance.pack(anchor="w")
    texte_departementnaissance.place(x=20, y=260)


    numdepartementMenuC = ttk.Combobox(window_conjoint_info)
    numdepartementMenuC.place(x=239, y=263, width=125)
    numdepartementMenuC["values"] = (
        "N° de département", "2A", "2B", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
        "14", "15", "15",
        "16", "17", "18", "19", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34",
        "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",
        "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
        "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88",
        "89", "90", "91", "92", "93", "94", "95")
    numdepartementMenuC.current(0)

    def dlieu_c():
        global LeDLieuDeNaissanceC
        DLieuNaissanceC = numdepartementMenuC.get()
        LeDLieuDeNaissanceC.append(DLieuNaissanceC)

    # ------------------------------

    def creation_MDP_conjoint():
        global MotDePasseC
        global LeLieuDeNaissanceC
        global LeDLieuDeNaissanceC
        global MotDePasse
        prenom_c()
        nom_c()
        surnom_c()
        jour_c()
        mois_c()
        annee_c()
        lieu_c()
        dlieu_c()
        for i in range(len(MotDePasseC)):
            MotDePasse.append(MotDePasseC[i])
        for i in range(len(LeLieuDeNaissanceC)):
            MotDePasse.append(LeLieuDeNaissanceC[i])
        for i in range(len(LeDLieuDeNaissanceC)):
            MotDePasse.append(LeDLieuDeNaissanceC[i])
        showinfobox_enregistrement()
        #print(MotDePasse)
        window_conjoint_info.destroy()

    # ------------------------------

    bouton_valider_window_conjoint_info = Button(window_conjoint_info, text="      Valider les     \n informations", relief="groove", command=creation_MDP_conjoint)  # Bouton avec texte + commande
    bouton_valider_window_conjoint_info.place(x=150, y=310)


# ------------------------------Création de la fenetre secondaire concernant les frères et soeurs------------------------------

def window_freresoeur_info(window_freresoeur_info):

    window_freresoeur_info = Toplevel()                                                                                 # Nouvelle fenetre1 au dessus de la précédente
    window_freresoeur_info.focus_set()                                                                                  # S'affiche comme fenêtre principale (Déja sélectionée en Bleu)
    window_freresoeur_info.geometry("410x370+250+240")                                                                  # Dimension de la fenêtre1
    window_freresoeur_info.resizable(width=False, height=False)                                                         # La fenetre n'est pas redimensionnable
    window_freresoeur_info.iconbitmap('icon.ico')
    window_freresoeur_info.title("Frères et sœurs")                                                                     # Titre de la nouvelle fenêtre1

    # ------------------------------

    texte_prenom = Label(window_freresoeur_info, text="Prénom :", font=Banhschrift)
    texte_prenom.pack(anchor="w")
    texte_prenom.place(x=20, y=10)

    entry_prenomF = Entry(window_freresoeur_info, width=30, bg='white', fg="black", justify="center")                   # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_prenomF.place(x=180, y=14)

    # -----

    def prenom_f():
        global LePrenomF
        global MotDePasseF
        PrenomF = entry_prenomF.get()
        var = str.lower(PrenomF)
        LePrenomF.append(var)
        MotDePasseF.append(str.upper(PrenomF))
        MotDePasseF.append(str.lower(PrenomF))

        for a in range(len(PrenomF)):
            LePrenomF = [elt for elt in var]
            LePrenomF[a] = ord(LePrenomF[a])
            if LePrenomF[a] >= 97 and LePrenomF[a] <= 122:
                LePrenomF[a] = chr(LePrenomF[a] - 32)
                MotDePasseF.append("".join(LePrenomF))
                for z in range(len(PrenomF)):
                    if z != a:
                        LePrenomF[z] = ord(LePrenomF[z])
                        if LePrenomF[z] >= 97 and LePrenomF[z] <= 122:
                            LePrenomF[z] = chr(LePrenomF[z] - 32)
                            MotDePasseF.append("".join(LePrenomF))
                            LePrenomF[z] = ord(LePrenomF[z])
                            LePrenomF[z] = chr(LePrenomF[z] + 32)

        for a in range((len(PrenomF)) - 1):
            b = a+1
            LePrenomF = [elt for elt in var]
            LePrenomF[a] = ord(LePrenomF[a])
            LePrenomF[b] = ord(LePrenomF[b])
            if LePrenomF[a] >= 97 and LePrenomF[a] <= 122 and LePrenomF[b] >= 97 and LePrenomF[b] <= 122:
                LePrenomF[a] = chr(LePrenomF[a] - 32)
                LePrenomF[b] = chr(LePrenomF[b] - 32)
                MotDePasseF.append("".join(LePrenomF))
                for z in range(len(PrenomF)):
                    if z != a and z != b:
                        LePrenomF[z] = ord(LePrenomF[z])
                        if LePrenomF[z] >= 97 and LePrenomF[z] <= 122:
                            LePrenomF[z] = chr(LePrenomF[z] - 32)
                            MotDePasseF.append("".join(LePrenomF))
                            LePrenomF[z] = ord(LePrenomF[z])
                            LePrenomF[z] = chr(LePrenomF[z] + 32)

        for a in range((len(PrenomF)) - 2):
            b = a + 1
            c = a + 2
            LePrenomF = [elt for elt in var]
            LePrenomF[a] = ord(LePrenomF[a])
            LePrenomF[b] = ord(LePrenomF[b])
            LePrenomF[c] = ord(LePrenomF[c])
            if LePrenomF[a] >= 97 and LePrenomF[a] <= 122 and LePrenomF[b] >= 97 and LePrenomF[b] <= 122 and LePrenomF[c] >= 97 and LePrenomF[c] <= 122:
                LePrenomF[a] = chr(LePrenomF[a] - 32)
                LePrenomF[b] = chr(LePrenomF[b] - 32)
                LePrenomF[c] = chr(LePrenomF[c] - 32)
                MotDePasseF.append("".join(LePrenomF))
                for z in range((len(PrenomF)) - 3):
                    if z != a and z != b and z != c:
                        LePrenomF[z] = ord(LePrenomF[z])
                        if LePrenomF[z] >= 97 and LePrenomF[z] <= 122:
                            LePrenomF[z] = chr(LePrenomF[z] - 32)
                            MotDePasseF.append("".join(LePrenomF))
                            LePrenomF[z] = ord(LePrenomF[z])
                            LePrenomF[z] = chr(LePrenomF[z] + 32)

        for a in range((len(PrenomF)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LePrenomF = [elt for elt in var]
            LePrenomF[a] = ord(LePrenomF[a])
            LePrenomF[b] = ord(LePrenomF[b])
            LePrenomF[c] = ord(LePrenomF[c])
            LePrenomF[d] = ord(LePrenomF[d])
            if LePrenomF[a] >= 97 and LePrenomF[a] <= 122 and LePrenomF[b] >= 97 and LePrenomF[b] <= 122 and LePrenomF[c] >= 97 and LePrenomF[c] <= 122 and LePrenomF[d] >= 97 and LePrenomF[d] <= 122:
                LePrenomF[a] = chr(LePrenomF[a] - 32)
                LePrenomF[b] = chr(LePrenomF[b] - 32)
                LePrenomF[c] = chr(LePrenomF[c] - 32)
                LePrenomF[d] = chr(LePrenomF[d] - 32)
                MotDePasseF.append("".join(LePrenomF))
                for z in range(len(PrenomF)):
                    if z != a and z != b and z != c and z != d:
                        LePrenomF[z] = ord(LePrenomF[z])
                        if LePrenomF[z] >= 97 and LePrenomF[z] <= 122:
                            LePrenomF[z] = chr(LePrenomF[z] - 32)
                            MotDePasseF.append("".join(LePrenomF))
                            LePrenomF[z] = ord(LePrenomF[z])
                            LePrenomF[z] = chr(LePrenomF[z] + 32)

    # ------------------------------

    texte_nom = Label(window_freresoeur_info, text="Nom :", font=Banhschrift)
    texte_nom.place(x=20, y=60)

    entry_nomF = Entry(window_freresoeur_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_nomF.place(x=180, y=64)

    # -----

    def nom_f():
        global LeNomF
        global MotDePasseF
        NomF = entry_nomF.get()
        var = str.lower(NomF)
        LeNomF.append(var)
        MotDePasseF.append(str.upper(NomF))
        MotDePasseF.append(str.lower(NomF))

        for a in range(len(NomF)):
            LeNomF = [elt for elt in var]
            LeNomF[a] = ord(LeNomF[a])
            if LeNomF[a] >= 97 and LeNomF[a] <= 122:
                LeNomF[a] = chr(LeNomF[a] - 32)
                MotDePasseF.append("".join(LeNomF))
                for z in range(len(NomF)):
                    if z != a:
                        LeNomF[z] = ord(LeNomF[z])
                        if LeNomF[z] >= 97 and LeNomF[z] <= 122:
                            LeNomF[z] = chr(LeNomF[z] - 32)
                            MotDePasseF.append("".join(LeNomF))
                            LeNomF[z] = ord(LeNomF[z])
                            LeNomF[z] = chr(LeNomF[z] + 32)

        for a in range((len(NomF)) - 1):
            b = a + 1
            LeNomF = [elt for elt in var]
            LeNomF[a] = ord(LeNomF[a])
            LeNomF[b] = ord(LeNomF[b])
            if LeNomF[a] >= 97 and LeNomF[a] <= 122 and LeNomF[b] >= 97 and LeNomF[b] <= 122:
                LeNomF[a] = chr(LeNomF[a] - 32)
                LeNomF[b] = chr(LeNomF[b] - 32)
                MotDePasseF.append("".join(LeNomF))
                for z in range(len(NomF)):
                    if z != a and z != b:
                        LeNomF[z] = ord(LeNomF[z])
                        if LeNomF[z] >= 97 and LeNomF[z] <= 122:
                            LeNomF[z] = chr(LeNomF[z] - 32)
                            MotDePasseF.append("".join(LeNomF))
                            LeNomF[z] = ord(LeNomF[z])
                            LeNomF[z] = chr(LeNomF[z] + 32)

        for a in range((len(NomF)) - 2):
            b = a + 1
            c = a + 2
            LeNomF = [elt for elt in var]
            LeNomF[a] = ord(LeNomF[a])
            LeNomF[b] = ord(LeNomF[b])
            LeNomF[c] = ord(LeNomF[c])
            if LeNomF[a] >= 97 and LeNomF[a] <= 122 and LeNomF[b] >= 97 and LeNomF[b] <= 122 and LeNomF[c] >= 97 and LeNomF[c] <= 122:
                LeNomF[a] = chr(LeNomF[a] - 32)
                LeNomF[b] = chr(LeNomF[b] - 32)
                LeNomF[c] = chr(LeNomF[c] - 32)
                MotDePasseF.append("".join(LeNomF))
                for z in range(len(NomF)):
                    if z != a and z != b and z != c:
                        LeNomF[z] = ord(LeNomF[z])
                        if LeNomF[z] >= 97 and LeNomF[z] <= 122:
                            LeNomF[z] = chr(LeNomF[z] - 32)
                            MotDePasseF.append("".join(LeNomF))
                            LeNomF[z] = ord(LeNomF[z])
                            LeNomF[z] = chr(LeNomF[z] + 32)

        for a in range((len(NomF)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeNomF = [elt for elt in var]
            LeNomF[a] = ord(LeNomF[a])
            LeNomF[b] = ord(LeNomF[b])
            LeNomF[c] = ord(LeNomF[c])
            LeNomF[d] = ord(LeNomF[d])
            if LeNomF[a] >= 97 and LeNomF[a] <= 122 and LeNomF[b] >= 97 and LeNomF[b] <= 122 and LeNomF[c] >= 97 and LeNomF[c] <= 122 and LeNomF[d] >= 97 and LeNomF[d] <= 122:
                LeNomF[a] = chr(LeNomF[a] - 32)
                LeNomF[b] = chr(LeNomF[b] - 32)
                LeNomF[c] = chr(LeNomF[c] - 32)
                LeNomF[d] = chr(LeNomF[d] - 32)
                MotDePasseF.append("".join(LeNomF))
                for z in range(len(NomF)):
                    if z != a and z != b and z != c and z != d:
                        LeNomF[z] = ord(LeNomF[z])
                        if LeNomF[z] >= 97 and LeNomF[z] <= 122:
                            LeNomF[z] = chr(LeNomF[z] - 32)
                            MotDePasseF.append("".join(LeNomF))
                            LeNomF[z] = ord(LeNomF[z])
                            LeNomF[z] = chr(LeNomF[z] + 32)

    # ------------------------------

    texte_pseudo = Label(window_freresoeur_info, text="Surnom - Pseudo :", font=Banhschrift)
    texte_pseudo.place(x=20, y=110)

    entry_pseudoF = Entry(window_freresoeur_info, width=30, bg='white', fg="black", justify="center")                   # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_pseudoF.place(x=180, y=114)

    # -----

    def surnom_f():
        global LeSurnomF
        global MotDePasseF
        SurnomF = entry_pseudoF.get()
        var = str.lower(SurnomF)
        LeSurnomF.append(var)
        MotDePasseF.append(str.lower(SurnomF))
        MotDePasseF.append(str.upper(SurnomF))

        for a in range(len(SurnomF)):
            LeSurnomF = [elt for elt in var]
            LeSurnomF[a] = ord(LeSurnomF[a])
            if LeSurnomF[a] >= 97 and LeSurnomF[a] <= 122:
                LeSurnomF[a] = chr(LeSurnomF[a] - 32)
                MotDePasseF.append("".join(LeSurnomF))
                for z in range(len(SurnomF)):
                    if z != a:
                        LeSurnomF[z] = ord(LeSurnomF[z])
                        if LeSurnomF[z] >= 97 and LeSurnomF[z] <= 122:
                            LeSurnomF[z] = chr(LeSurnomF[z] - 32)
                            MotDePasseF.append("".join(LeSurnomF))
                            LeSurnomF[z] = ord(LeSurnomF[z])
                            LeSurnomF[z] = chr(LeSurnomF[z] + 32)

        for a in range((len(SurnomF)) - 1):
            b = a + 1
            LeSurnomF = [elt for elt in var]
            LeSurnomF[a] = ord(LeSurnomF[a])
            LeSurnomF[b] = ord(LeSurnomF[b])
            if LeSurnomF[a] >= 97 and LeSurnomF[a] <= 122 and LeSurnomF[b] >= 97 and LeSurnomF[b] <= 122:
                LeSurnomF[a] = chr(LeSurnomF[a] - 32)
                LeSurnomF[b] = chr(LeSurnomF[b] - 32)
                MotDePasseF.append("".join(LeSurnomF))
                for z in range(len(SurnomF)):
                    if z != a and z != b:
                        LeSurnomF[z] = ord(LeSurnomF[z])
                        if LeSurnomF[z] >= 97 and LeSurnomF[z] <= 122:
                            LeSurnomF[z] = chr(LeSurnomF[z] - 32)
                            MotDePasseF.append("".join(LeSurnomF))
                            LeSurnomF[z] = ord(LeSurnomF[z])
                            LeSurnomF[z] = chr(LeSurnomF[z] + 32)

        for a in range((len(SurnomF)) - 2):
            b = a + 1
            c = a + 2
            LeSurnomF = [elt for elt in var]
            LeSurnomF[a] = ord(LeSurnomF[a])
            LeSurnomF[b] = ord(LeSurnomF[b])
            LeSurnomF[c] = ord(LeSurnomF[c])
            if LeSurnomF[a] >= 97 and LeSurnomF[a] <= 122 and LeSurnomF[b] >= 97 and LeSurnomF[b] <= 122 and LeSurnomF[c] >= 97 and LeSurnomF[c] <= 122:
                LeSurnomF[a] = chr(LeSurnomF[a] - 32)
                LeSurnomF[b] = chr(LeSurnomF[b] - 32)
                LeSurnomF[c] = chr(LeSurnomF[c] - 32)
                MotDePasseF.append("".join(LeSurnomF))
                for z in range(len(SurnomF)):
                    if z != a and z != b and z != c:
                        LeSurnomF[z] = ord(LeSurnomF[z])
                        if LeSurnomF[z] >= 97 and LeSurnomF[z] <= 122:
                            LeSurnomF[z] = chr(LeSurnomF[z] - 32)
                            MotDePasseF.append("".join(LeSurnomF))
                            LeSurnomF[z] = ord(LeSurnomF[z])
                            LeSurnomF[z] = chr(LeSurnomF[z] + 32)

        for a in range((len(SurnomF)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LeSurnomF = [elt for elt in var]
            LeSurnomF[a] = ord(LeSurnomF[a])
            LeSurnomF[b] = ord(LeSurnomF[b])
            LeSurnomF[c] = ord(LeSurnomF[c])
            LeSurnomF[d] = ord(LeSurnomF[d])
            if LeSurnomF[a] >= 97 and LeSurnomF[a] <= 122 and LeSurnomF[b] >= 97 and LeSurnomF[b] <= 122 and LeSurnomF[c] >= 97 and LeSurnomF[c] <= 122 and LeSurnomF[d] >= 97 and LeSurnomF[d] <= 122:
                LeSurnomF[a] = chr(LeSurnomF[a] - 32)
                LeSurnomF[b] = chr(LeSurnomF[b] - 32)
                LeSurnomF[c] = chr(LeSurnomF[c] - 32)
                LeSurnomF[d] = chr(LeSurnomF[d] - 32)
                MotDePasseF.append("".join(LeSurnomF))
                for z in range(len(SurnomF)):
                    if z != a and z != b and z != c and z != d:
                        LeSurnomF[z] = ord(LeSurnomF[z])
                        if LeSurnomF[z] >= 97 and LeSurnomF[z] <= 122:
                            LeSurnomF[z] = chr(LeSurnomF[z] - 32)
                            MotDePasseF.append("".join(LeSurnomF))
                            LeSurnomF[z] = ord(LeSurnomF[z])
                            LeSurnomF[z] = chr(LeSurnomF[z] + 32)

    # ------------------------------

    texte_datenaissance = Label(window_freresoeur_info, text="Date de Naissance :", font=Banhschrift)
    texte_datenaissance.pack(anchor="w")
    texte_datenaissance.place(x=20, y=160)

    jourMenuF = ttk.Combobox(window_freresoeur_info)
    jourMenuF.place(x=180, y=165, width=45)
    jourMenuF['values'] = (
    "Jour", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "15", "16", "17", "18",
    "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31")
    jourMenuF.current(0)

    def jour_f():
        global MotDePasseF
        JourNaissanceF = jourMenuF.get()
        MotDePasseF.append(JourNaissanceF)

    # -----

    slash1 = Label(window_freresoeur_info, text="/", font=Slashsfont)
    slash1.place(x=225, y=162)

    # -----

    moisMenuF = ttk.Combobox(window_freresoeur_info)
    moisMenuF.place(x=238, y=165, width=50)
    moisMenuF["values"] = ("Mois", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12")
    moisMenuF.current(0)

    def mois_f():
        global MotDePasseF
        MoisNaissanceF = moisMenuF.get()
        MotDePasseF.append(MoisNaissanceF)

    # -----

    slash2 = Label(window_freresoeur_info, text="/", font=Slashsfont)
    slash2.place(x=288, y=162)

    # -----

    anneeMenuF = ttk.Combobox(window_freresoeur_info)
    anneeMenuF.place(x=301, y=165, width=62)
    anneeMenuF["values"] = (
    "Année", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
    "1992", "1991", "1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979",
    "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965",
    "1964", "1963", "1962", "1961", "1960", "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951",
    "1950", "1949", "1948", "1947", "1946", "1945", "1944", "1943", "1942", "1941", "1940", "1939", "1938", "1937",
    "1936", "1935", "1934", "1933", "1932", "1931", "1930", "1929", "1928", "1927", "1926", "1925", "1924", "1923",
    "1922", "1921", "1920", "1919")
    anneeMenuF.current(0)

    def annee_f():
        global MotDePasseF
        AnneeNaissanceF = anneeMenuF.get()
        MotDePasseF.append(AnneeNaissanceF)

    # ------------------------------

    texte_lieunaissance = Label(window_freresoeur_info, text="Ville Natale :", font=Banhschrift)
    texte_lieunaissance.pack(anchor="w")
    texte_lieunaissance.place(x=20, y=210)

    lieunaissanceMenuF = Entry(window_freresoeur_info, width=30, bg='white', fg="black", justify="center")
    lieunaissanceMenuF.place(x=180, y=215)

    def lieu_f():
        global LeLieuDeNaissanceF
        LieuNaissanceF = lieunaissanceMenuF.get()
        LeLieuDeNaissanceF.append(LieuNaissanceF)

    # ------------------------------

    texte_departementnaissance = Label(window_freresoeur_info, text="Département de Naissance :", font=Banhschrift)
    texte_departementnaissance.pack(anchor="w")
    texte_departementnaissance.place(x=20, y=260)


    numdepartementMenuF = ttk.Combobox(window_freresoeur_info)
    numdepartementMenuF.place(x=239, y=263, width=125)
    numdepartementMenuF["values"] = (
        "N° de département", "2A", "2B", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13",
        "14", "15", "15",
        "16", "17", "18", "19", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34",
        "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52",
        "53", "54", "55", "56", "57", "58", "59", "60", "61", "62", "63", "64", "65", "66", "67", "68", "69", "70",
        "71", "72", "73", "74", "75", "76", "77", "78", "79", "80", "81", "82", "83", "84", "85", "86", "87", "88",
        "89", "90", "91", "92", "93", "94", "95")
    numdepartementMenuF.current(0)

    def dlieu_f():
        global LeDLieuDeNaissanceF
        DLieuNaissanceF = numdepartementMenuF.get()
        LeDLieuDeNaissanceF.append(DLieuNaissanceF)

    # ------------------------------

    def creation_MDP_freresoeur():
        global MotDePasseF
        global LeLieuDeNaissanceF
        global LeDLieuDeNaissanceF
        global MotDePasse
        prenom_f()
        nom_f()
        surnom_f()
        jour_f()
        mois_f()
        annee_f()
        lieu_f()
        dlieu_f()
        for i in range(len(MotDePasseF)):
            MotDePasse.append(MotDePasseF[i])
        for i in range(len(LeLieuDeNaissanceF)):
            MotDePasse.append(LeLieuDeNaissanceF[i])
        for i in range(len(LeDLieuDeNaissanceF)):
            MotDePasse.append(LeDLieuDeNaissanceF[i])
        showinfobox_enregistrement()
        #print(MotDePasse)
        window_freresoeur_info.destroy()

    # ------------------------------

    bouton_valider_window_freresoeur_info = Button(window_freresoeur_info, text="      Valider les     \n informations", relief="groove", command=creation_MDP_freresoeur)  # Bouton avec texte + commande
    bouton_valider_window_freresoeur_info.place(x=150, y=310)


# ------------------------------Création de la fenetre secondaire concernant les animaux------------------------------

def window_animaux_info(window_conjoint_info):

    window_animaux_info = Toplevel()                                                                                    # Nouvelle fenetre1 au dessus de la précédente
    window_animaux_info.focus_set()                                                                                     # S'affiche comme fenêtre principale (Déja sélectionée en Bleu)
    window_animaux_info.geometry("370x390+250+240")                                                                     # Dimension de la fenêtre1
    window_animaux_info.resizable(width=False, height=False)                                                            # La fenetre n'est pas redimensionnable
    window_animaux_info.iconbitmap('icon.ico')
    window_animaux_info.title("Animaux")                                                                         # Titre de la nouvelle fenêtre1

    # ------------------------------

    texte_espece = Label(window_animaux_info, text="Espèce : ", font=Banhschrift)
    texte_espece.pack(anchor="w")
    texte_espece.place(x=20, y=10)

    entry_espece = ttk.Combobox(window_animaux_info, value=["Espèce", "Chat", "Chien", "Cheval", "Lapin", "Oiseau", "Furet", "Rongeurs", "Poissons", "Serpent", "Iguane"])
    entry_espece.place(x=130, y=14, width=130)
    entry_espece.current(0)
    # -----

    def espece():
        global MotDePasseA
        Espece = entry_espece.get()
        MotDePasseA.append(Espece)
        MotDePasseA.append(str.upper(Espece))
        MotDePasseA.append(str.lower(Espece))

    # ------------------------------

    texte_race = Label(window_animaux_info, text="Race : ", font=Banhschrift)
    texte_race.pack(anchor="w")
    texte_race.place(x=20, y=50)

    # -----

    texte_chien = Label(window_animaux_info, text="Chien : ", font='Helvetica, 11 ')                                    # tout ce qui concerne les chiens
    texte_chien.pack(anchor="w")
    texte_chien.place(x=50, y=80)

    entry_chien = ttk.Combobox(window_animaux_info, value=["      Race de Chien", "Affenpinscher", "Airedale Terrier", "Akita Americain", "Akita Inu", "American Staffordshire Terrier", "Ancien chien d'arrêt danois", "Anglo-Français de Petite Vènerie", "Ariégeois", "Barbet", "Barbu Tchèque", "Barzoï", "Basenji", "Basset Artésien-Normand", "Basset Bleu de Gascogne", "Basset de Westphalie", "Basset des Alpes", "Basset Fauve de Bretagne", "Basset Hound", "Beagle", "Beagle-Harrier", "Bearded Collie", "Beauceron", "Bedlington Terrier", "Berger Allemand", "Berger", "Berger Australien", "Berger Belge Groenendael", "Berger Belge Laekenois", "Berger Belge Malinois", "Berger Belge Tervueren", "Berger Blanc Suisse", "Berger Catalan", "Berger d'Anatolie", "Berger d'Asie Centrale", "Berger de Bergame", "Berger de Bohême", "Berger de Brie", "Berger de l\'Atlas", "Berger de Maremme et Abruzzes", "Berger de Picardie", "Berger de Russie", "Berger des pyrénées", "Berger des Shetland", "Berger du Caucase", "Berger du Massif du Karst", "Berger finois de Laponie", "Berger Hollandais", "Berger Islandais", "Berger Plonais de Plaine", "Berger Polonais de Podhale", "Berger Potugais", "Berger Yougoslave"])
    entry_chien.place(x=130, y=82, width=200)
    entry_chien.current(0)

    # -----

    texte_chat = Label(window_animaux_info, text="Chat : ", font='Helvetica, 11 ')                                      # tout ce qui concerne les chats
    texte_chat.pack(anchor="w")
    texte_chat.place(x=50, y=106)

    entry_chat = ttk.Combobox(window_animaux_info, value=["      Race de Chat", "Abyssin", "American Bobtail", "American Curl",
                                      "Amerian Shortair", "American Wirehair", "Angora Turc", " Balinais", "Bengal",
                                      "Bleu russe", "Bombay", "British Shorthair", "Burmese", "Burmilla", "Ceylan",
                                      "Chartreux", "Chausie", "Cornish Rex", "Devon Rex", "Donskoy", "Européen",
                                      "Exotic", "German Rex", "Havana Brown", "Japanese Bobtail", "Javanais", "Korat",
                                      "Kurilian Bobtail", "LaPerm", "Maine coon", "Man", "Mau Egyptien", "Minchkin",
                                      "Norvégien", "Ocicat", "Oriental", "Persan", "Peterbald", "Pixie-Bob", "Ragdoll",
                                      "Sacré de Birmanie", "Savannah", "Scottish & Highland", "Scottish fold",
                                      "Siamois", "Sibérien", "Singapura", "Skogcatt", "Snowshoe", "Somali", "Sphynx",
                                      "Thaï", "Tiffany", "Tonkinois", "Toyger", "Turc de van"])
    entry_chat.place(x=130, y=107, width=200)
    entry_chat.current(0)

    # -----

    texte_cheval = Label(window_animaux_info, text="Cheval : ", font='Helvetica, 11 ')                                  # tout ce qui concerne les chevauxs
    texte_cheval.pack(anchor="w")
    texte_cheval.place(x=50, y=131)

    entry_cheval = ttk.Combobox(window_animaux_info,
                              value=["      Race de Cheval"])
    entry_cheval.place(x=130, y=133, width=200)
    entry_cheval.current(0)

    # -----

    texte_lapin = Label(window_animaux_info, text="Lapin : ", font='Helvetica, 11 ')                                    # tout ce qui concerne les lapins
    texte_lapin.pack(anchor="w")
    texte_lapin.place(x=50, y=158)

    entry_lapin = ttk.Combobox(window_animaux_info,
                              value=["      Race de Lapin"])
    entry_lapin.place(x=130, y=159, width=200)
    entry_lapin.current(0)

    # -----

    texte_oiseau = Label(window_animaux_info, text="Oiseau : ", font='Helvetica, 11 ')                                  # tout ce qui concerne les oiseaux
    texte_oiseau.pack(anchor="w")
    texte_oiseau.place(x=50, y=183)

    entry_oiseau = ttk.Combobox(window_animaux_info,
                               value=["      Race d'Oiseaux"])
    entry_oiseau.place(x=130, y=185, width=200)
    entry_oiseau.current(0)

    # -----

    texte_poisson = Label(window_animaux_info, text="Poisson : ", font='Helvetica, 11 ')                                # tout ce qui concerne les poissons
    texte_poisson.pack(anchor="w")
    texte_poisson.place(x=50, y=211)

    entry_poisson = ttk.Combobox(window_animaux_info,
                                value=["      Race de Poisson"])
    entry_poisson.place(x=130, y=211, width=200)
    entry_poisson.current(0)

    # ----------

    def race():
        global MotDePasseA
        Chat = entry_chat.get()                                                                                         # variable qui apprend la valeur du menu déroulant
        MotDePasseA.append(Chat)                                                                                        # le mot de passe dédié l'intègre tel quel
        MotDePasseA.append(str.upper(Chat))                                                                             # ainsi qu'en majuscule
        MotDePasseA.append(str.lower(Chat))                                                                             # et en minuscule

        Chien = entry_chien.get()
        MotDePasseA.append(Chien)
        MotDePasseA.append(str.upper(Chien))
        MotDePasseA.append(str.lower(Chien))

        Cheval = entry_cheval.get()
        MotDePasseA.append(Cheval)
        MotDePasseA.append(str.upper(Cheval))
        MotDePasseA.append(str.lower(Cheval))

        Lapin = entry_lapin.get()
        MotDePasseA.append(Lapin)
        MotDePasseA.append(str.upper(Lapin))
        MotDePasseA.append(str.lower(Lapin))

        Oiseau = entry_oiseau.get()
        MotDePasseA.append(Oiseau)
        MotDePasseA.append(str.upper(Oiseau))
        MotDePasseA.append(str.lower(Oiseau))

        Poisson = entry_poisson.get()
        MotDePasseA.append(Poisson)
        MotDePasseA.append(str.upper(Poisson))
        MotDePasseA.append(str.lower(Poisson))

    # ------------------------------

    texte_prenom = Label(window_animaux_info, text="Nom ou Surnom:", font=Banhschrift)
    texte_prenom.pack(anchor="w")
    texte_prenom.place(x=20, y=250)

    entry_prenomA = Entry(window_animaux_info, width=30, bg='white', fg="black", justify="center")                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_prenomA.place(x=200, y=255, width=130)

    # -----

    def prenomA():
        global LePrenomA
        global MotDePasseA
        PrenomA = entry_prenomA.get()
        var = str.lower(PrenomA)
        LePrenomA.append(var)
        MotDePasseA.append(str.upper(PrenomA))
        MotDePasseA.append(str.lower(PrenomA))

        for a in range(len(PrenomA)):
            LePrenomA = [elt for elt in var]
            LePrenomA[a] = ord(LePrenomA[a])
            if LePrenomA[a] >= 97 and LePrenomA[a] <= 122:
                LePrenomA[a] = chr(LePrenomA[a] - 32)
                MotDePasseA.append("".join(LePrenomA))
                for z in range(len(PrenomA)):
                    if z != a:
                        LePrenomA[z] = ord(LePrenomA[z])
                        if LePrenomA[z] >= 97 and LePrenomA[z] <= 122:
                            LePrenomA[z] = chr(LePrenomA[z] - 32)
                            MotDePasseA.append("".join(LePrenomA))
                            LePrenomA[z] = ord(LePrenomA[z])
                            LePrenomA[z] = chr(LePrenomA[z] + 32)

        for a in range((len(PrenomA)) - 1):
            b = a + 1
            LePrenomA = [elt for elt in var]
            LePrenomA[a] = ord(LePrenomA[a])
            LePrenomA[b] = ord(LePrenomA[b])
            if LePrenomA[a] >= 97 and LePrenomA[a] <= 122 and LePrenomA[b] >= 97 and LePrenomA[b] <= 122:
                LePrenomA[a] = chr(LePrenomA[a] - 32)
                LePrenomA[b] = chr(LePrenomA[b] - 32)
                MotDePasseA.append("".join(LePrenomA))
                for z in range(len(PrenomA)):
                    if z != a and z != b:
                        LePrenomA[z] = ord(LePrenomA[z])
                        if LePrenomA[z] >= 97 and LePrenomA[z] <= 122:
                            LePrenomA[z] = chr(LePrenomA[z] - 32)
                            MotDePasseA.append("".join(LePrenomA))
                            LePrenomA[z] = ord(LePrenomA[z])
                            LePrenomA[z] = chr(LePrenomA[z] + 32)

        for a in range((len(PrenomA)) - 2):
            b = a + 1
            c = a + 2
            LePrenomA = [elt for elt in var]
            LePrenomA[a] = ord(LePrenomA[a])
            LePrenomA[b] = ord(LePrenomA[b])
            LePrenomA[c] = ord(LePrenomA[c])
            if LePrenomA[a] >= 97 and LePrenomA[a] <= 122 and LePrenomA[b] >= 97 and LePrenomA[b] <= 122 and LePrenomA[c] >= 97 and LePrenomA[c] <= 122:
                LePrenomA[a] = chr(LePrenomA[a] - 32)
                LePrenomA[b] = chr(LePrenomA[b] - 32)
                LePrenomA[c] = chr(LePrenomA[c] - 32)
                MotDePasseA.append("".join(LePrenomA))
                for z in range(len(PrenomA)):
                    if z != a and z != b and z != c:
                        LePrenomA[z] = ord(LePrenomA[z])
                        if LePrenomA[z] >= 97 and LePrenomA[z] <= 122:
                            LePrenomA[z] = chr(LePrenomA[z] - 32)
                            MotDePasseA.append("".join(LePrenomA))
                            LePrenomA[z] = ord(LePrenomA[z])
                            LePrenomA[z] = chr(LePrenomA[z] + 32)

        for a in range((len(PrenomA)) - 3):
            b = a + 1
            c = a + 2
            d = a + 3
            LePrenomA = [elt for elt in var]
            LePrenomA[a] = ord(LePrenomA[a])
            LePrenomA[b] = ord(LePrenomA[b])
            LePrenomA[c] = ord(LePrenomA[c])
            LePrenomA[d] = ord(LePrenomA[d])
            if LePrenomA[a] >= 97 and LePrenomA[a] <= 122 and LePrenomA[b] >= 97 and LePrenomA[b] <= 122 and LePrenomA[c] >= 97 and LePrenomA[c] <= 122 and LePrenomA[d] >= 97 and LePrenomA[d] <= 122:
                LePrenomA[a] = chr(LePrenomA[a] - 32)
                LePrenomA[b] = chr(LePrenomA[b] - 32)
                LePrenomA[c] = chr(LePrenomA[c] - 32)
                LePrenomA[d] = chr(LePrenomA[d] - 32)
                MotDePasseA.append("".join(LePrenomA))
                for z in range(len(PrenomA)):
                    if z != a and z != b and z != c and z != d:
                        LePrenomA[z] = ord(LePrenomA[z])
                        if LePrenomA[z] >= 97 and LePrenomA[z] <= 122:
                            LePrenomA[z] = chr(LePrenomA[z] - 32)
                            MotDePasseA.append("".join(LePrenomA))
                            LePrenomA[z] = ord(LePrenomA[z])
                            LePrenomA[z] = chr(LePrenomA[z] + 32)

    # ------------------------------

    texte_annee = Label(window_animaux_info, text="Année de naissance :", font=Banhschrift)
    texte_annee.pack(anchor="w")
    texte_annee.place(x=20, y=290)

    anneeMenuA = ttk.Combobox(window_animaux_info)
    anneeMenuA.place(x=200, y=295, width=130)
    anneeMenuA["values"] = (
    "Année", "2019", "2018", "2017", "2016", "2015", "2014", "2013", "2012", "2011", "2010", "2009", "2008", "2007",
    "2006", "2005", "2004", "2003", "2002", "2001", "2000", "1999", "1998", "1997", "1996", "1995", "1994", "1993",
    "1992", "1991", "1990", "1989", "1988", "1987", "1986", "1985", "1984", "1983", "1982", "1981", "1980", "1979",
    "1978", "1977", "1976", "1975", "1974", "1973", "1972", "1971", "1970", "1969", "1968", "1967", "1966", "1965",
    "1964", "1963", "1962", "1961", "1960", "1959", "1958", "1957", "1956", "1955", "1954", "1953", "1952", "1951",
    "1950", "1949", "1948", "1947", "1946", "1945", "1944", "1943", "1942", "1941", "1940", "1939", "1938", "1937",
    "1936", "1935", "1934", "1933", "1932", "1931", "1930", "1929", "1928", "1927", "1926", "1925", "1924", "1923",
    "1922", "1921", "1920", "1919")
    anneeMenuA.current(0)

    def annee_A():
        global MotDePasseA
        AnneeNaissanceA = anneeMenuA.get()
        MotDePasseA.append(AnneeNaissanceA)

    # ------------------------------

    def creation_MDP_animaux():
        global LePrenomA
        global MotDePasseA
        espece()
        race()
        prenomA()
        annee_A()

        for i in range(len(MotDePasseA)):
            MotDePasse.append(MotDePasseA[i])
        showinfobox_enregistrement()
        #print(MotDePasse)
        window_animaux_info.destroy()

    # ------------------------------

    bouton_valider_window_animaux_info = Button(window_animaux_info, text="      Valider les     \n informations", relief="groove", command=creation_MDP_animaux)  # Bouton avec texte + commande
    bouton_valider_window_animaux_info.place(x=150, y=335)

def window_mdp_fin():
    window_mdp_fin = Toplevel()                                                                                         # Nouvelle fenetre au dessus de la précédente
    window_mdp_fin.focus_set()                                                                                          # S'affiche comme fenêtre principale (Déja sélectionée en Bleu)
    window_mdp_fin.geometry("800x180+80+240")                                                                           # Dimension de la fenêtre1
    window_mdp_fin.resizable(width=False, height=False)                                                                 # La fenetre n'est pas redimensionnable
    window_mdp_fin.iconbitmap('icon.ico')
    window_mdp_fin.title("Création de votre mot de passe")

    # ------------------------------
    texte_info = Label(window_mdp_fin, text="Bravo ! Vous avez atteint la dernière étape du processus !", font='Helvetica, 12')
    texte_info.pack(anchor="w")
    texte_info.place(x=250, y=8)

    texte_info1 = Label(window_mdp_fin,
                       text="Elle consiste à l'évaluation du niveau de sécurité de votre mot de passe. \nPour cela, il vous faut entrer votre mot de passe dans la zone ci-dessous et sa fiabilité vous sera indiquée. \nDans un deuxième temps, un mot de passe plus sécurisé vous sera conseillé.",
                       font='Helvetica, 11')
    texte_info1.pack(anchor="w")
    texte_info1.place(x=55, y=50)

    # ----------

    texte_mdp = Label(window_mdp_fin, text="Entrez un mot de passe : ", font='Bahnschrift, 13')
    texte_mdp.pack(anchor="w")
    texte_mdp.place(x=150, y=120)

    entry_mdp = Entry(window_mdp_fin, width=30, bg='white', fg="black",justify="center", show='*')                      # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
    entry_mdp.place(x=400, y=123, width=160)

    def check():
        global MotDePasse
        global Trie
        global MotDePasse_final

        for element in MotDePasse:                                                                                      # trie les mots de passe et la liste Trie les intègre en un seul exemplaire
            if element not in Trie:
                Trie.append(element)


        for j in range(len(Trie)):                                                                                      # mutiplication des mots de passe composés de deux variables qui se suivent dans la liste MotDePasse_final
            for i in range(len(Trie)):
                MotDePasse_final.append(Trie[j] + Trie[i])
        #print(MotDePasse_final)

        Test = entry_mdp.get()
        Resultat = MotDePasse_final.count(Test)
        if Resultat > 0:                                                                                                # si la proposition de l'individu (resultat) est trouvé dans la liste
            showwarning('Résultat : ', 'Votre mot de passe n\'est pas assez fiable, il est facilement piratable. ')                                     # alors s'affiche ce message
        if Resultat == 0:                                                                                               # si la proposition de l'individu (résultat) n'est pas trouvé dans la liste
            showinfo('Résultat : ', 'Votre mot de passe est fiable ou assez fiable. Il semble sécurisé en vu des informations qui vous concernent. ')                                  # alors s'affiche ce message


    bouton_valider_window_mdp_fin = Button(window_mdp_fin, text=" Vérifier ", relief="groove", command=check)           # Bouton avec texte + commande
    bouton_valider_window_mdp_fin.place(x=600, y=120)

    bouton_fermer_window_mdp_fin = Button(window_mdp_fin, text=" Quitter ", relief="groove", command=fenetre.destroy)   # Bouton avec texte + commande
    bouton_fermer_window_mdp_fin.place(x=730, y=140)

#Déf Ouverture Notice-Utilisation

def web():

    url = 'https://upmp.000webhostapp.com/'                                                                                              #URL de requête
    webbrowser.open(url, new=2, autoraise=True)                                                                         #Ouverture du navigateur, (par défaut de l'utilisateur), se superposant aux autres






# Déf Fenêtre confirmation fermeture programme

def quit():

    if askyesno('Quitter ?', 'Êtes-vous sûr de vouloir quitter ?'):                                                     #Fenetre de dialogue (OUI-NON)
        fenetre.quit()                                                                                                  #Action de OUI






def filemanager():                                                                                                      #Déf Ouvertude de l'explorateur de fichiers

    filepath = askopenfilename(title="Sélection dictionnaire",filetypes=[('Fichier Texte','.txt'), ('Tous les fichiers', '.*')])

# Sélection de l'emplacement du fichier, types, extension, tri par extension

# ----------

def lheure():
    # on arrive ici toutes les 1000 ms
    heure.set(time.strftime('%H:%M:%S'))
    fenetre.after(1000, lheure)

heure = StringVar()                                                                                                     # on définit 'heure' comme variable
fenetre_heure = Label(fenetre, textvariable=heure)                                                                      # la variable 'heure' s'affiche dans l'interface fenêtre
fenetre_heure.place(x=295, y=185)                                                                                       # emplacement de l'heure dans la fenêtre
fenetre_heure.configure(bg="gray15",fg="white")                                                                                     # on met le fond en blanc pour mieux l'intégrer à l'interface

lheure()

# ----------

# Menu déroulant interactif au top de la fenêtre

menubar = Menu(fenetre)                                                                                                 # Création Widget Menu
menu1 = Menu(menubar, tearoff=0)                                                                                        # Menu non détachable de son emplacement
menubar.add_cascade(label="Fichier", menu=menu1)                                                                        # Ajout Bouton avec texte déroulant
menu1.add_command(label="Ajouter Dico", command=filemanager)                                                            # Ajout d'un bouton avec texte + une commande
menu1.add_separator()                                                                                                   # Séparateur esthétique entre les boutons
menu1.add_command(label="Quitter", command=quit)                                                                        # Ajout d'un bouton avec texte + une commande


# Deuxième Bouton déroulant

menu2 = Menu(menubar, tearoff=0)                                                                                        # Menu non détachable de son emplacement
menubar.add_cascade(label="Aide", menu=menu2)                                                                           # Ajout Bouton avec texte déroulant
menu2.add_command(label="Notice d'utilisation", command=web)                                                            # Ajout d'un bouton avec texte + une commande

fenetre.config(menu=menubar)                                                                                            # Fin configuration du menu déroulant




# Liste de Sélections

listbox = Listbox(fenetre, selectmode=SINGLE, width=45)                                                                 # Création widget liste avec une seule sélection possible



listbox.pack(side=LEFT, fill=Y,padx=8, pady=10)                                                                         # Postionnement Gauche + remplissage en Hauteur selon fenetre + espacement de 8 en largeur

listbox.config(bg="gray15", fg="white", relief="raised", bd=3, highlightcolor="green", highlightbackground="green")                                                                      # Couleur fond + relief éléments liste + marge intérieur + curseur souris

listbox.insert(1, ". Informations sur vous .")                                                                          # Elements sélectionnable de la liste
listbox.insert(2,"   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   ")
listbox.insert(3, ". Informations sur votre parent 1 .")
listbox.insert(4,"   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   ")
listbox.insert(5, ". Informations sur votre parent 2 .")
listbox.insert(6,"   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   ")
listbox.insert(7, ". Informations sur votre conjoint .")
listbox.insert(8,"   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   ")
listbox.insert(9, ". Informations sur vos frères et soeurs .")
listbox.insert(10,"   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   ")
listbox.insert(11, ". Informations sur vos animaux de compagnies .")

listbox.bind('<ButtonRelease-1>', selection)                                                                            #Action de sélection d'élement lors d'appui clique gauche






    # Entry de selection de la liste

entrylist = Entry(fenetre, width=50, bg='RoyalBlue3', fg="white", justify="center")                                           # Zone entrée qui récupère le choix utlisateur de l'élément dans la liste + taille + couleur fond
entrylist.insert(0, 'Sélectionnez un élément de la liste')                                                              # Texte entré de base dans la zone
entrylist.pack(anchor="nw", pady=10, padx=12)                                                                                    # Postionnement de la zone




def warningbox():                                                                                                       # Ouverture boîte de dialogue signalant erreur de sélection
    showwarning("Sélection Impossible", "Veuillez choisir une sélection valide dans l'encadré de gauche \npuis resélectionner le bouton \" saisir les informations \".")

def showinfobox_fraternite():                                                                                           # Ouverture boîte de dialogue signalant des informations sur la fraternité
    showinfo('Informations : ', 'Si vous avez plusieurs frères et/ou soeurs, merci d\'appuyer sur le bouton \"Valider les informations\" entre chaque frère et/ou soeur.')

def showinfobox_animaux():                                                                                              # Ouverture boîte de dialogue signalant des informations sur la fraternité
    showinfo('Informations : ', 'Si vous avez plusieurs animaux, merci d\'appuyer sur le bouton \"Valider les informations\" entre chaque animal.')

def showinfobox_enregistrement():                                                                                              # Ouverture boîte de dialogue signalant des informations sur la fraternité
    showinfo('Enregistrement : ', 'Les informations ont bien été enregistrés.')


def ouverture_fenetre(*args):                                                                                           # *args sert a prendre n'importe quel argument (pour éxécuter cette fonction en Clicking ou Pressing)

    lecture_entry_par_bouton = entrylist.get()                                                                          # récupère ce qui est lu dans l'entry

    selectionlistfalse = "   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   -   "                  # Variable quelconque
    selection_par_defaut = "Sélectionnez un élément de la liste"                                                        # #Variable quelconque

    selectionlist1 = ". Informations sur vous ."                                                                        # Variable liste
    selectionlist2 = ". Informations sur votre parent 1 ."                                                              # Variable liste
    selectionlist3 = ". Informations sur votre parent 2 ."                                                              # Variable liste
    selectionlist4 = ". Informations sur votre conjoint ."
    selectionlist5 = ". Informations sur vos frères et soeurs ."                                                        # Variable liste
    selectionlist6 = ". Informations sur vos animaux de compagnies ."                                                   # Variable liste

    if lecture_entry_par_bouton == selection_par_defaut:                                                                # Si variables de sélection fausses, ouverture boite de dialogue erreur
        warningbox()
    if lecture_entry_par_bouton == selectionlistfalse:                                                                  # Si variables de sélection fausses, ouverture boite de dialogue erreur
        warningbox()

    

    if lecture_entry_par_bouton == selectionlist1:                                                                      # Correspondance des variables de listes avec ouverture de la fenetre appropriée
        window_personal_info(open)
    if lecture_entry_par_bouton == selectionlist2:
        window_parent1_info(open)
    if lecture_entry_par_bouton == selectionlist3:
        window_parent2_info(open)
    if lecture_entry_par_bouton == selectionlist4:
        window_conjoint_info(open)
    if lecture_entry_par_bouton == selectionlist5:
        window_freresoeur_info(open)
        showinfobox_fraternite()
    if lecture_entry_par_bouton == selectionlist6:
        window_animaux_info(open)
        showinfobox_animaux()
        
    




# Bonton Remplir Sélection

bouton_valider = Button(fenetre, text= "      Saisir les      \n informations", command=ouverture_fenetre, relief="ridge", fg="chartreuse3")   # Bouton avec texte + commande qui permet l'ouverture d'autres fenêtre pour remplir ses données
bouton_valider.pack(anchor="sw")
bouton_valider.place(x=410, y=135)                                                                                       # emplacement du bouton dans la fenêtre
bouton_valider.configure(bg="gray40")
# Postion bouton Gauche + remplissage hauteur + distance par rapport aux autres élements

bouton_terminer = Button(fenetre, text=" Terminer ", command=window_mdp_fin, relief="raised")
bouton_terminer.pack(anchor="sw")
bouton_terminer.place(x=555, y=180)
bouton_terminer.configure(bg="gray40", fg="white")

listbox.bind('<KeyPress-Return>', ouverture_fenetre)                                                                    # Exécution de l'ouverture par pression du bouton entrée.





fenetre.mainloop()          #Fin Fenetre Principale TKINTER
