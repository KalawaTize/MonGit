#import pandas as pd
#import numpy as np
import os
import pickle


class Livre:
    def __init__(self, titre, auteur, disponible=True):
        self.__titre = titre
        self.__auteur = auteur
        self.__disponible = disponible

    @property
    def titre(self):
        return self.__titre

    @property
    def auteur(self):
        return self.__auteur

    @property
    def disponible(self):
        return self.__disponible

    def changer_disponibilite(self, etat):
        self.__disponible = etat

    def afficher_info(self):
        statut = "Disponible" if self.__disponible else "Emprunté"
        return f"'{self.__titre}' par {self.__auteur} [{statut}]"

    def __str__(self):
        return self.afficher_info()
