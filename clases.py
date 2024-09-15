class persona():
    nom=""
    edad=0;
    doc=0

    def __init__(self, nom, edad, doc):
      self.nom=nom
      self.edad=edad
      self.doc=doc

    def imprimir(self):
       print("El nombre es:",self.nom)


person = persona("juan",24,234) 
person.imprimir()     