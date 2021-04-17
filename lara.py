class Persona:
    def __init__(self, nome, cognome, anni):
        self.Nome = nome
        self.Cognome = cognome
        self.Anni = anni
        self.In_Amore = False

    def Stampa_info(self):
        print("La persona si chiama: ", self.Nome, " ", self.Cognome)
        print("e ha ", self.Anni, " anni.")
        if(self.In_Amore == True):
            print('questa persona ama:', self.Persona.Nome, '!! e nessun altro')

        print('\n')

    def Ama(self, persona):
        self.In_Amore = True
        self.Persona = persona

persona1 = Persona('Lara', 'Baudracco', 21)
persona2 = Persona('Edoardo', 'Vay', 22)

persona1.Stampa_info()
persona2.Stampa_info()

persona1.Ama(persona2)
persona2.Ama(persona1)

for i in range(1):
    persona1.Stampa_info()
    persona2.Stampa_info()