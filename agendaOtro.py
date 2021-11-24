#otro de agenda
#-*-coding:utf-8-*-
#modulos
import csv
import itertools #conteo del identificador
import re #expresiones regulares

#clases

class Contacto:
	nuevoId = itertools.count()
	def __init__(self,nombre,apellidos,empresa,fijo,movil):
		self.codigo = next(self.nuevoId) #Añado identificador usando la clase itertools
		self.nombre = nombre
		self.apellidos = apellidos
		self.empresa = empresa
		self.fijo = fijo
		self.movil = movil

class Agenda:
	def  __init__(self):
		self.contactos = []

	def ordenarNombre(self):
		self.contactos.sort(key = lambda contacto: contacto.nombre)#Lambda(es palabra clave) funcion anonima carece de nombre, se guarda en la variable key. Escribo p1 y p2 como parámetros 1 y 2 de la función.
                                                                   #lambda p1, p2: expresión 

	def ordenarApellidos(self):
		self.contactos.sort(key = lambda contacto: contacto.apellidos)

	def añadir(self,nombre,apellidos,empresa,fijo,movil):
		contacto = Contacto(nombre,apellidos,empresa,fijo,movil)
		self.contactos.append(contacto)

	def mostraTodos(self):
		self.submenuOrden()
		for contacto in self.contactos:
			self.imprimeContacto(contacto)

	def buscar(self,textoBuscar):
		encontrado = 0
		for contacto in self.contactos:
			#Expresiones regulares
			if(re.findall(textoBuscar,contacto.nombre)) or (re.findall(textoBuscar,contacto.apellido)):
				self.imprimeContacto(contacto)
				encontrado = encontrado + 1
				self.submenuBuscar(contacto.codigo)

		if encontrado == 0:
			self.noEncontrado()

	def borrar(self,codigo):
		for contacto in self.contactos:
			if contacto.codigo == codigo:
				print("---*---*---*---*---*---*---*")
				print("Quieres borrar? (s/n)")
				print("---*---*---*---*---*---*---*")
				opcion = str(input(""))
				if opcion == 's' or opcion == 'S':
					print("Borrando contacto")
					del self.contactos[codigo]
				elif opcion == 'n' or opcion == 'N':
					break

	def modificar(self,codigo):
		for contacto in self.contactos:
			if contacto.codigo == codigo:
				del self.contactos[codigo]
				nombre = str(input("Escribe el nombre: "))
				apellidos = str(input("Escribe los apellidos: "))
				empresa = str(input("Escribe la empresa: "))
				fijo = str(input("Escribe el fijo: "))
				movil = str(input("Escribe el movil: "))
				contacto = contacto(nombre.capitalize(),apellidos.capitalize(),fijo,movil)
				self.contactos.append(contacto)
				break

	def submenuBuscar(self,codigo):
		print("---*---*---*---*---*---*---*")
		print("Quiere (m)odificarlo o (b)orrarlo: ")
		print("---*---*---*---*---*---*---*")
		opcion = str(input(""))
		if opcion == 'm' or 'M':
			self.modificar(codigo)

		elif opcion == 'b' or opcion == 'B':
			self.borrar(codigo)

		else:
			print("Continumos sin realizar ninguna modificacion")

	def submenuOrden(self):
		print("---*---*---*---*---*---*---*")
		print("Quieres ordenar por (n)ombre o por (a)pellido ")
		print("---*---*---*---*---*---*---*")
		opcion = str(input(""))
		if opcion=="n" or opcion=="N":
			self.ordenarNombre()
		elif opcion=="a" or opcion=="A":
			self.ordenarApellidos()
		

	def grabar(self):
		with open('Agenda.csv','w') as fichero:
			escribir = csv.writer(fichero)
			escribir.writerow(('codigo', 'apellidos','empresa','fijo','movil'))
			for contacto in self.contactos:
				escribir.writerow((contacto.codigo, contacto.nombre, contacto.apellidos, contacto.empresa, contacto.fijo, contacto.movil))

	def imprimeContacto(self,contacto):
		print("---*---*---*---*---*---*---*")
		print("---*---*---*---*---*---*---*")
		print('Codigo {}'.format(contacto.codigo))
		print('Nombre {}'.format(contacto.nombre))
		print('Apellido {}'.format(contacto.apellidos))
		print("Empresa {}"	.format(contacto.empresa))
		print("Fijo {}".format(contacto.fijo))
		print("Movil {}".format(contacto.movil))
		print("---*---*---*---*---*---*---*")
		print("---*---*---*---*---*---*---*")

	def noEncontrado(self):
		print("---*---*---*---*---*---*---*")
		print("---*---*---*---*---*---*---*")
		print("---Contacto no Encontrado---")
		print("---*---*---*---*---*---*---*")
		print("---*---*---*---*---*---*---*")


#Cuerpo del programa
def ejecutar():
		agenda = Agenda()
		try:
			with open('agenda.csv','r') as fichero:
				lector = csv.DictReader(fichero,delimiter=',')
				for fila in lector:
					agenda.añadir(fila['nombre'].capitalize,fila['apellido'].capitalize,fila['empresa'].capitalize,fila['fijo'],fila['movil'])
		except:
			print('Error al abrir el archivo o todavia no se ha creado')

		while True:
			menu=str(input('''

				\nSelecciona una opción\n
				1-Mostrar lista de Contactos
				2-Buscar Contacto
				3-Añadir Contacto
				0-Salir\n\n


				'''))

			if menu == '1':
				agenda.mostraTodos()
			elif menu == '2':
				texto = str(input("Ingrese el texto para realizar la busqueda: "))
				agenda.buscar(texto.capitalize())
				agenda.grabar()
			elif menu == '3':

				nombre = str(input("Escribe el nombre: "))
				apellidos = str(input("Escribe los apellidos: "))
				empresa = str(input("Escribe la empresa: "))
				fijo = str(input("Escribe el fijo: "))
				movil = str(input("Escribe el movil: "))
				#contacto = contacto(nombre.capitalize(),apellidos.capitalize(),fijo,movil)
				agenda.añadir(nombre.capitalize,apellidos.capitalize,empresa.capitalize,fijo,movil)
				agenda.grabar()

			elif menu=='0':
				print("Hasta pronto")
				agenda.grabar()	
				break
			else:
				print("Opción no valida")

if __name__=='__main__':
	ejecutar()

#Funcion lambda
"""
#Aquí tenemos una función creada para sumar.
def suma(x,y):
    return(x + y)
#Aquí tenemos una función Lambda que también suma.
lambda x,y : x + y
#Para poder utilizarla necesitamos guardarla en una variable.
suma_dos = lambda x,y : x + y	

"""