from Operations import Operations
import random

class Language(Operations):
    def __init__(self, lista):
        super().__init__(lista)

    def create_language(lista, cantidad):
        cerradura = [] 
        alphabets = []
        len_Alphabets = len(lista)

        for _ in range(len_Alphabets):
            alphabets.extend(lista[_])
               
        for _ in range(cantidad):
            letra = random.choice(alphabets)
            letra2 = random.choice(alphabets)
            elemento = f"{letra}{letra2}"
            cerradura.append(elemento)

        return cerradura
        
    def cardinality_language(language):
        return len(language)   
        
    def concatenate_languages(self, language1, language2):
        concatenate_language=[]
        element=''
        for i in language1:
            for j in language2:
                element=f"{i}{j}"
                element=element.replace('#', '')
                if element != '':
                    concatenate_language.append(element)
        return concatenate_language    
    
    def inverse_language(self,language):
        inverse_laguage = list(reversed(language))

        return inverse_laguage
    
    
    def pow(self, language, potencia):
        listaPow=[]
        pow={}
        if potencia > 0:
            listaPow.extend(language)
            for num in range(potencia-1):
                listaPow.extend(self.concatenate_languages(listaPow,language))
                
        return listaPow        
    
    
# lista=[]
# a1=['ab','cd', 'dc'] 
# a2=[3, 4, 5]
# a3=[3,4, 6, 7]
# lista.append(a1)
# lista.append(a2)
# lista.append(a3)
# print(lista)
# conjunto = Language
# print(conjunto.create_language(lista,10))