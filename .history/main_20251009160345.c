#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

typedef struct tree tree;
struct tree
{
    short valeurs[100];
    int binaire[100], taille_valeurs, taille_binaire;
};


typedef struct save save;
struct save
{
    char valeur, valeur_calculs;
    int frequence, binaire[100], taille_binaire, decimal;
};

typedef struct noeud noeud;
struct noeud
{
    save pere, fils_gauche, fils_droit;
};


void sauvegarde(char *chaine, save S[100], int *niveau)
{
    int taille = strlen(chaine);
    int cpt1, cpt2;

    for (int i = 0; i < taille; i++)
    {
        cpt1 = 0;

        for (int j = i; j >= 0; j--)
        {
            if (chaine[i] == chaine[j])
                cpt1++;
        }

        if (cpt1 == 1)
        {
            cpt2 = 0;

            for (int k = 0; k < taille; k++)
            {
                if (chaine[i] == chaine[k])
                    cpt2++;

            }
            S[*niveau].valeur = chaine[i];
            S[*niveau].valeur_calculs = chaine[i];
            S[*niveau].frequence = cpt2;
            (*niveau)++;
            printf("Caractere %c repeter %d fois\n", chaine[i], cpt2);
        }
    }
}


void tri_frequence_croissante(int niveau,  save S[100])
{
    int c;
    for (int i = 0; i < niveau - 1; i++)
    {
        c = 0;
        for (int j = 0; j < niveau - i - 1; j++)
        {
            if (S[j].frequence > S[j + 1].frequence)
            {
                save temp = S[j];
                S[j] = S[j + 1];
                S[j + 1] = temp;
                c = 1;
            }
        }

        if (c == 0)
            break;
    }

}


void construction_arbre(noeud *arbre, int taille_S, save *S, int *niveau)
{
    while(taille_S != 1)
    {
        tri_frequence_croissante(taille_S, S);
        arbre[*niveau].pere.frequence = S[0].frequence + S[1].frequence;
        arbre[*niveau].pere.valeur_calculs = '#' + (*niveau);
        arbre[*niveau].pere.valeur = '$' ;
        arbre[*niveau].fils_droit = S[0];
        arbre[*niveau].fils_gauche = S[1];
        S[1] = arbre[*niveau].pere;
        (*niveau)++;
        for(int i = 0; i < taille_S - 1; i++) S[i] = S[i+1];
        taille_S--;
    }
}

void afficher_Noeud(noeud N)
{
    printf("\n\t[ '%c' : %d ]", N.pere.valeur, N.pere.frequence);
    printf("\n[ '%c' : %d ]\t", N.fils_gauche.valeur, N.fils_gauche.frequence);
    printf("[ '%c' : %d ]", N.fils_droit.valeur, N.fils_droit.frequence);
}


void binarisation(noeud *arbre, save *S, int taille_arbre)
{
    int index = 0;
    save elmt_de_comparaison = *S;
    for(int i = 0; i < taille_arbre; i++)
    {
        if(arbre[i].fils_gauche.valeur_calculs == elmt_de_comparaison.valeur_calculs && arbre[i].fils_gauche.frequence == elmt_de_comparaison.frequence)
        {
            S -> binaire[index] = 0;
            index++;
            elmt_de_comparaison = arbre[i].pere;
        }
        else if(arbre[i].fils_droit.valeur_calculs == elmt_de_comparaison.valeur_calculs && arbre[i].fils_droit.frequence == elmt_de_comparaison.frequence)
        {
            S -> binaire[index] = 1;
            index++;
            elmt_de_comparaison = arbre[i].pere;
        }
    }
    S -> taille_binaire = index;
}



void tri_ordre_arbre(save *S, char *tab, int taille_S)
{

    int max_tailles_binaires = S[0].taille_binaire;
    for(int i = 0; i < taille_S; i ++)
    {
        if(S[i].taille_binaire > max_tailles_binaires) max_tailles_binaires = S[i].taille_binaire;
    }
    //Rangement des valeurs decimales pour la comparaison
    int puissance = 0;
    for(int i = 0; i < taille_S; i ++)
    {
        S[i].decimal = 0;
    }
    for(int i = 0; i < taille_S; i ++)
    {
        puissance = max_tailles_binaires;
        for(int j = S[i].taille_binaire - 1; j >= 0; j --)
        {
            S[i].decimal += S[i].binaire[j] * pow(2, puissance);
            puissance --;
        }
    }

    //Tri en fonction des decimaux en recyclant le code du tri_frequence_croissantes
    for (int i = 0; i < taille_S - 1; i++)
    {
        int c = 0;
        for (int j = 0; j < taille_S - i - 1; j++)
        {
            if (S[j].decimal > S[j + 1].decimal)
            {
                save temp = S[j];
                S[j] = S[j + 1];
                S[j + 1] = temp;
                c = 1;
            }
        }

        if (c == 0)
            break;
    }

    for (int i = 0; i < taille_S; i++) printf(" %c : %d ", S[i].valeur, S[i].decimal);
}



short index_difference(save S1, save S2)
{
    int index_1 = S1.taille_binaire - 1;
    int index_2 = S2.taille_binaire - 1;
    if(S1.binaire[index_1] != S2.binaire[index_2]) return index_2;
    else
    {
        while(S1.binaire[index_1] == S2.binaire[index_2])
        {
            index_1 --;
            index_2 --;
        }
    }
    return index_2 ;
}


void init(noeud *N)
{
    N ->fils_gauche.valeur = N -> fils_gauche.valeur_calculs = 'K';
    N -> fils_droit.valeur = N -> fils_droit.valeur_calculs = 'K';
    N -> pere.valeur = '$';
    N -> pere.valeur_calculs = 'K';
    N -> fils_gauche.frequence = N -> fils_droit.frequence = N -> pere.frequence = 0;
}

void stockage_tableau(tree *stocke, noeud *arbre, int taille_arbre, save *S, int taille_S)
{

    //Rangement de S dans l'ordre de l'arbre
    char tab[taille_S];
    tri_ordre_arbre(S, tab, taille_S);

    //Rangement des caracteres dans l'arbre
    int index = 0;
    for(int i = 0; i < taille_S; i ++)
    {
        stocke -> valeurs[index] = S[i].valeur;
        index ++;
    }
    stocke -> taille_valeurs = index;


    //Rangement du code de l'arbre
    index = 0;
    int k = S[0].taille_binaire - 1;
    for(int i = 0; i < taille_S - 1; i++)
    {
        for(int j = k; j >= 0; j--)
        {
              stocke -> binaire[index] = S[i].binaire[j];
              printf("\n%c : %d.\nk : %d.\n",S[i].valeur_calculs, S[i].binaire[j], k);
              index ++;
        }
        k = index_difference(S[i], S[i + 1]);
    }
    stocke -> binaire[index] = 1;
    stocke -> binaire[index + 1] = 1;
    stocke -> taille_binaire = index + 2;
}

void decodage_chaine_codee(tree arbre_stocke, char *chaine_decodee, int *taille_chaine_decodee, int *chaine_binarisee)
{
    //Determination de la taille de l'arbre i.e le nombre de 1 dans le code de l'arbre - 1
    int taille_arbre = -1;
    for(int i = 0; i < arbre_stocke.taille_binaire; i ++)
    {
        if(arbre_stocke.binaire[i] == 1) taille_arbre ++;
    }


    //Initialisaion de l'arbre
    noeud arbre[taille_arbre];
    for(int i = 0; i < taille_arbre; i ++) init(&arbre[i]);


    //Placement des caracteres dans l'arbre
    int index = 0, k = taille_arbre - 1;
    for(int i = 0; i < arbre_stocke.taille_binaire - 2; i ++)
    {
        if(arbre_stocke.binaire[i] == 0 && arbre_stocke.binaire[i + 1] == 1)
        {
            if(arbre_stocke.binaire[i + 2] == 0)
            {
                printf("\nTonton");
                arbre[k].fils_gauche.valeur = arbre[k].fils_gauche.valeur_calculs = arbre_stocke.valeurs[index];
                index ++;
                k --;
            }
            else
            {
                printf("Tata");
                arbre[k].fils_gauche.valeur = arbre[k].fils_gauche.valeur_calculs = arbre_stocke.valeurs[index];
                printf(" %c ", arbre_stocke.valeurs[index]);
                index ++;
                arbre[k].fils_droit.valeur = arbre[k].fils_droit.valeur_calculs = arbre_stocke.valeurs[index];
                index ++;
                k -= 2;
            }
        }

    }

    index = 0;
    for(int i = taille_arbre - 1; i >= 0; i --) afficher_Noeud(arbre[i]);
}

int main()
{
    printf("\nBienvenue dans l'algorithme de compression.\n");
    printf("\nVeuillez entrer votre chaine de caractere : ");
    char chaine[100];
    scanf("%[^\n]s", chaine);
    int niveau = 0;
    save S[100];
    sauvegarde(chaine, S, &niveau);

  //Sauvegarde de la liste avec les valeurs et fréquences
    save copy_S[niveau];
    for(int i = 0; i < niveau; i++)
    {
        printf("\n[ '%c' : %d ]\n", S[i].valeur, S[i].frequence);
        copy_S[i] = S[i];
    }

  //Construction et affichage de l'arbre
    noeud arbre[100];
    int taille_S = niveau;
    niveau = 0;
    construction_arbre(arbre, taille_S, copy_S, &niveau);
    int taille_arbre = niveau;
    printf("\nAffichage de l'arbre : \n");
    for(int i = taille_arbre - 1; i >= 0; i--) afficher_Noeud(arbre[i]);

 //Binarisation
    printf("\n\nBinarisation : \n");

    int chaine_binarisee[100], taille_chaine_binarisee = 0;
    for(int i = 0; i < taille_S; i++) binarisation(arbre, &S[i], taille_arbre);

    for(int i = 0; i < taille_S; i++)
    {
        printf("\n [ '%c' : ", S[i].valeur);
        for(int j = S[i].taille_binaire-1; j >= 0; j--) printf("%d", S[i].binaire[j]);
        printf(" ]\n");
    }


    //Affichage de la chaine compresssée en binaire
    tree arbre_stocke;
    stockage_tableau(&arbre_stocke, arbre, taille_arbre, S, taille_S);

    for(int i = 0; i < strlen(chaine); i++)
    {
        for(int j = 0; j < taille_S; j++)
        {
            if(S[j].valeur == chaine[i])
            {
                for(int k = S[j].taille_binaire - 1; k >= 0; k--)
                {
                    chaine_binarisee[taille_chaine_binarisee] = S[j].binaire[k];
                    taille_chaine_binarisee ++;
                }
            }
        }
    }

    printf("\nValeur binaire de l'arbre : ");
    for(int i = 0; i < taille_chaine_binarisee; i++) printf("%d", chaine_binarisee[i]);


    //Affichage du code de l'arbre

    printf("\nCode de l'arbre : ");
    for(int i = 0; i < arbre_stocke.taille_binaire; i++) printf("%d", arbre_stocke.binaire[i]);
    printf("\n");

    //Affichage des valeurs dans l'arbre
    printf("\nEnsemble des valeurs dans l'arbre : ");
    for(int i = 0; i < arbre_stocke.taille_valeurs; i++) printf("%c", arbre_stocke.valeurs[i]);
    printf("\n");

    //Décodage de l'arbre
    char chaine_decodee[100];
    int taille_chaine_decodee = 0;
    decodage_chaine_codee(arbre_stocke, chaine_decodee, &taille_chaine_decodee, chaine_decodee);
    printf("\nChaine decodee : ");
    for(int i = 0; i < taille_chaine_decodee; i++) printf("%c", chaine_decodee[i]);
    printf("\nFin du projet Huffman tree.\n");

}
