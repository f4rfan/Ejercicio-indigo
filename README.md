# Ejercicios Indigo

Aplicaciones creadas en base a los requerimientos especificos de los ejercicios que me enviaron. 

## Getting Started

Los ejercicios fueron realizados en python 3, para utilizar las aplicaciones cree un archivo main, en el esta el menu
para utilizar cualquier ejercicio, en el archivo "Pruebas Unitarias" realize un pequeno test con valores especificos para
cada ejercicio, el codigo de cada uno esta en el respectivo archivo.

### Prerequisitos

Instalar Python 3, se puede obtener de la pagina https://www.python.org/downloads/, para windows y mac, en el caso de estar trabajando en linux
utilizar la instruccion "sudo apt-get install python3"

## Pruebas

Teniendo Python 3 instalado, para correr las pruebas para ambos ejercicos solo se debe hacer doble click en el archivo "Pruebas" (en windows)

### Explicacion de las pruebas

Las pruebas las realize con un modulo de Python llamado "unittest", creando 2 clases, una para cada ejercicio y utilizando la funcion "assertEqual" del modulo
"unittest", en esta funcion se toman dos valores y se comprueba que los valores sean igual, en este caso especifico prueba que la funcion devuelva el valor
deseado.

```
mymodule.py

 def sum(a, b):
    for n in (a, b):
        if not isinstance(n, int) and not isinstance(n, float):
            raise TypeError
    return a + b

	
import unittest
import mymodule
class TestMyModule(unittest.TestCase):
    
    def test_sum(self):
        self.assertEqual(mymodule.sum(5, 7), 12)

if __name__ == "__main__":
    unittest.main()
```

## Creado con

* [Python 3, IDLE]( https://www.python.org/downloads/) - Lenguaje, IDE
* [Git](https://git-scm.com) - Control de versiones


## Autor

* **Sergio Manuel Farfán Pérez** 