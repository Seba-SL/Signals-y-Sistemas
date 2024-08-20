{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "source": [
        "# Jupyter Notebook"
      ],
      "metadata": {
        "id": "ScjK-T9YFzLR"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Los archivos `.ipynb` están divididos en celdas, en donde podemos escribir texto plano en estilo Markdown (como estamos haciendo acá) o código en lenguaje Python, como se hace a continuación:"
      ],
      "metadata": {
        "id": "hh3Fj4PAF5Ci"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "U_EIujM8ESn2"
      },
      "outputs": [],
      "source": [
        "# Esto es una celda de código, no de texto.\n",
        "# Puedo hacer comentarios empezando el renglón con un \"#\".\n",
        "\n",
        "print('Esta es una celda de código. Para ejecutar la celda, utilizo Crtl+Enter.')\n",
        "print('Lo único que tiene de interesante esta celda es la función print(arg1,arg2,...,argn)')\n",
        "print('que, como su nombre lo indica,','imprime lo que está entre paréntesis. No hay más misterio que eso.')"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "En el caso de una celda de código, al oprimir `Crtl+Enter`, las instrucciones se ejecutan una a continuación de la otra."
      ],
      "metadata": {
        "id": "g16oaQBgGAMc"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"Esto sale como output\"\n",
        "a"
      ],
      "metadata": {
        "id": "sRikWw-LF-G8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Para usuaries de Jupyter local: Para crear una celda nueva, hacemos click en el ícono +, que se encuentra en la barra de herramientas. Para eliminarla, el ícono es el de las tijeras. Con el botón dropdown de la misma barra se puede elegir si la celda es para uso de texto (opción Markdown) o de código (opción Code).\n",
        "\n",
        "Para usuaries de Google Colab: Para crear una nueva celda podemos hacer click en las opciones +Code y +Text que aparecen en la parte superior izquierda de la pestaña, o cuando pasamos el cursor por la parte inferior de cualquier celda. Para eliminar una celda busco el ícono \"tacho de basura\" que aparece en la parte superior derecha de la celda que estamos utilizando.\n",
        "\n",
        "En Jupyter se pueden usar los comandos de bash anteponiendo el signo ! antes de cada línea."
      ],
      "metadata": {
        "id": "LpQjVkSvGEh_"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "!wget https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Saturn_during_Equinox.jpg/300px-Saturn_during_Equinox.jpg -O img.jpg"
      ],
      "metadata": {
        "id": "2ybJz_0DHIHc"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Breve Introducción a Python"
      ],
      "metadata": {
        "id": "0Zz8Eh0FHLuK"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Python es un lenguaje de propósito general orientado a objetos. En lo que sigue se hará una breve introducción al tema y para profundizar en ello puede consultarse la bibliografía dada al final de este notebook."
      ],
      "metadata": {
        "id": "s_jQ5ecGHNva"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Tipos básicos en Python\n"
      ],
      "metadata": {
        "id": "xokhP9eAHP90"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "En Python existen muchos tipos de objetos, pero los más importantes para nosotres van a ser los siguientes:\n",
        "\n",
        "* Los números enteros (`int`), flotantes (`float`) y complejos (`complex`)\n",
        "* Las cadenas de caracteres (`str`)\n",
        "* Los booleanos (`bool`)\n",
        "* Las listas (`list`)\n",
        "* Los diccionarios (`dict`)\n",
        "* Los conjuntos (`set`)\n",
        "* El tipo nulo especial de Python (`None`)\n",
        "* Las funciones comunes (`function`) y las funciones lambda (`lambda function`)\n",
        "* Las clases definidas por el usuario"
      ],
      "metadata": {
        "id": "TDbeSQ1THSJj"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Números y strings"
      ],
      "metadata": {
        "id": "gAD6gnOHHj9h"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "i_int = 1\n",
        "i_float = 1.\n",
        "i_complex = 1+0j \n",
        "i_string = \"1\"\n",
        "i_string2 = '1'"
      ],
      "metadata": {
        "id": "qJiwvNYsHPIK"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "i = i_int\n",
        "print(i)\n",
        "print(type(i))"
      ],
      "metadata": {
        "id": "MfvRekaqHqo2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Algunas operaciones entre números"
      ],
      "metadata": {
        "id": "IZCrSDcZHqAW"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(4 + 3)"
      ],
      "metadata": {
        "id": "0Gz0Oi74Hv2W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(4 * 3)\n"
      ],
      "metadata": {
        "id": "_2bnaYcFH0LS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(4 / 3)\n"
      ],
      "metadata": {
        "id": "SA_I-gEFH1bV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(4 // 4)\n"
      ],
      "metadata": {
        "id": "_MjKz6P-H2Uo"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(4 % 3)\n"
      ],
      "metadata": {
        "id": "Kxd_yAM-H3GQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(4**3)"
      ],
      "metadata": {
        "id": "ovB3V1nlH3tI"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Comparamos tipos entre sí"
      ],
      "metadata": {
        "id": "aF5MUWZSH6NM"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "print(i_int == i_float)\n"
      ],
      "metadata": {
        "id": "PAFyRdjSH6u0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(i_int == i_complex)\n"
      ],
      "metadata": {
        "id": "IMAjjQj_H8Hm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(i_string == i_string2)\n"
      ],
      "metadata": {
        "id": "b2GZEJaVH9QH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(i_int == i_string)"
      ],
      "metadata": {
        "id": "_Muhr9LmH_Ba"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Booleanos y sus operadores"
      ],
      "metadata": {
        "id": "HiDjrCCKICkx"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "A, B, C, D, E = 1, 2, \"1\", \"2\", '3'"
      ],
      "metadata": {
        "id": "9R0HjOFKID_E"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(A == B)"
      ],
      "metadata": {
        "id": "tqWWuWlsIGQ7"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(A >= B)"
      ],
      "metadata": {
        "id": "Jez0YdIeILTX"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(B > A)"
      ],
      "metadata": {
        "id": "HRgaGPWSIMiY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(C == D)"
      ],
      "metadata": {
        "id": "ICpwehH7INnB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(C > D)"
      ],
      "metadata": {
        "id": "NATykb-gIPmw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(A > C)"
      ],
      "metadata": {
        "id": "hd-kRHMLIP34"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(C is D)"
      ],
      "metadata": {
        "id": "oHaYoU8oIRYs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(D == E)"
      ],
      "metadata": {
        "id": "hD29NGxrIULe"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(A < B and C == D)"
      ],
      "metadata": {
        "id": "BanvU2pLIVXz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(True or False)"
      ],
      "metadata": {
        "id": "GW8UAH4BIWmE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "El tipo `None` y el *keyword* `is`"
      ],
      "metadata": {
        "id": "cT66240QIYQf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a, b = 1, 1."
      ],
      "metadata": {
        "id": "XAqAsf6kIarv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(a is b)"
      ],
      "metadata": {
        "id": "eOdp1p_KIclD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(a == b)"
      ],
      "metadata": {
        "id": "IABY1FXsId59"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Contenedores básicos de datos: listas, diccionarios, tuplas y conjuntos"
      ],
      "metadata": {
        "id": "t82bSvuvIpE5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = [1,1,2,3] # Lista\n",
        "b = {1,1,2,3} # Set (conjunto)\n",
        "c = (1,2,3,4) # Tupla\n",
        "d = {\"perro\": \"guau\", \"gato\": \"miau\", \"vaca\": \"muuu\", \"vinchuca\": \"vinchuuu\"} # Diccionario\n",
        "\n",
        "print(a, b, c, d)"
      ],
      "metadata": {
        "id": "N8yU4YCcIgDW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Indexación de listas y tuplas"
      ],
      "metadata": {
        "id": "ch9ujCkZIvL7"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a[0]"
      ],
      "metadata": {
        "id": "YETcSen7Itok"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a[2:4]"
      ],
      "metadata": {
        "id": "DzDYza06IxV2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a[-1]"
      ],
      "metadata": {
        "id": "Y1_R5Z2WIy9Z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "**Precaución**: Las listas son objetos *mutables*!"
      ],
      "metadata": {
        "id": "jqAmWhIGI3N0"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "a = \"abcde\"\n",
        "a[0] = 3"
      ],
      "metadata": {
        "id": "NCYCrog9I1w0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "d[\"perro\"]"
      ],
      "metadata": {
        "id": "E94wMm_QI9K0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Funciones"
      ],
      "metadata": {
        "id": "o0VtPpQvI_eF"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def hola_mundo():\n",
        "    print(\"Hola mundo!\")\n",
        "\n",
        "hola_mundo()"
      ],
      "metadata": {
        "id": "vCIqHiV0JAqG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def saludar():\n",
        "    name = input(\"Ingrese su nombre: \")\n",
        "    print(\"\\nHola, \" + name + \"!\")\n",
        "    # print(\"\\nHola, {}!\".format(name))\n",
        "    # print(f\"\\nHola, {name}!\")\n",
        "    \n",
        "saludar()"
      ],
      "metadata": {
        "id": "VJhTPBuzJEye"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "def crear_saludo(nombre):\n",
        "    return f\"\\nHola, {nombre}!\"\n",
        "    \n",
        "def saludar_n_veces(n):\n",
        "    nombre = input(\"Ingrese su nombre: \")\n",
        "    saludo = crear_saludo(nombre)\n",
        "    saludo = saludo + \" \"\n",
        "    saludo = saludo * n\n",
        "    print(saludo)\n",
        "    \n",
        "saludar_n_veces(4)"
      ],
      "metadata": {
        "id": "5ahzHvryJJ2Z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Clases y Objetos"
      ],
      "metadata": {
        "id": "Dqx7bjkDJUzy"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "class AlumneFiuba:\n",
        "    \n",
        "    materias_por_carrera = {\n",
        "        \"electrónica\": [\"Álgebra 2\", \"AM2\", \"Adc\", \"Dispo\"],\n",
        "        \"informática\": [\"Álgebra 2\", \"AM2\", \"Orga\", \"Algoritmos2\"],\n",
        "    }\n",
        "    \n",
        "    def __init__(self,nombre,apellido,carrera):\n",
        "        self.nombre = nombre\n",
        "        self.apellido = apellido\n",
        "        self.correo = f\"{nombre[0].lower()}{apellido.lower()}@fi.uba.ar\"\n",
        "        self.carrera = carrera\n",
        "        self.materias_por_aprobar = self.materias_por_carrera[carrera]\n",
        "        \n",
        "    def imprimir_correo(self):\n",
        "        print(self.correo)\n",
        "        \n",
        "    def imprimir_materias_por_aprobar(self):\n",
        "        print(\"Todavía quedan por aprobar:\",self.materias_por_aprobar)\n",
        "        \n",
        "    def marcar_aprobada(self,materia):\n",
        "        self.materias_por_aprobar.remove(materia)\n",
        "        print(f\"Chau {materia}!\")\n",
        "        \n",
        "a1 = AlumneFiuba(\"Lautaro\",\"Estienne\",\"electrónica\")\n",
        "\n",
        "a1.imprimir_materias_por_aprobar()\n",
        "a1.marcar_aprobada(\"AM2\")\n",
        "a1.imprimir_materias_por_aprobar()"
      ],
      "metadata": {
        "id": "BE9X3pIpJTWN"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Condicionales y manejo de errores"
      ],
      "metadata": {
        "id": "n9Lb_mvuJ-l0"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "Ver [acá](https://docs.python.org/3/library/exceptions.html#concrete-exceptions) para una lista completa de los diferentes tipos de error en Python."
      ],
      "metadata": {
        "id": "iPXdcAgPT2PI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "d = {\n",
        "  \"Argentina\": \"Buenos Aires\",\n",
        "  \"Uruguay\": \"Montevideo\",\n",
        "  \"Paraguay\": \"Asunción\"\n",
        "}\n",
        "\n",
        "pais = \"Brasil\"\n",
        "if pais not in d:\n",
        "  raise KeyError(f\"{pais} not in dict\")"
      ],
      "metadata": {
        "id": "Whi2ZSYYTznj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "try:\n",
        "  capital = d[\"Brasil\"]\n",
        "except KeyError:\n",
        "  capital = \"Brasilia\""
      ],
      "metadata": {
        "id": "xldOEkKuVVnH"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Ciclos e iteradores"
      ],
      "metadata": {
        "id": "jsRCfIgxVbM-"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "for i in [1,2,3,4,5,6,7,8,9,10]:\n",
        "  if i % 2 == 0:\n",
        "    print(f\"{i} es par\")"
      ],
      "metadata": {
        "id": "lwAgBVBnVaQE"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "for i in range(1,20,3):\n",
        "  if i % 2 == 0:\n",
        "    print(f\"{i} es par\")"
      ],
      "metadata": {
        "id": "O_608EbUVvy5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "\n",
        "## Módulos y librerías\n",
        "\n"
      ],
      "metadata": {
        "id": "hgO_RMNsV91g"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "from itertools import product\n",
        "\n",
        "for (i, j) in product([1,2,3],[4,5,6]):\n",
        "  print(i,j)"
      ],
      "metadata": {
        "id": "-t_kdTyZV84q"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "import numpy as np\n",
        "\n",
        "x = np.array([1,2,3,4])\n",
        "x * 2"
      ],
      "metadata": {
        "id": "nURh5qGtWmWs"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Bibliografía\n"
      ],
      "metadata": {
        "id": "vt6ArOtIWvuL"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "* Youtube:\n",
        "\n",
        "  * Curso para principiantes de [Corey Schafer](https://www.youtube.com/watch?v=YYXdXT2l-Gg&list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7)\n",
        "  * Buscar según la aplicación que une quiera desarrollar (Machine Learning, procesamiento de señales, ecuaciones diferenciales, etc.)\n",
        "  * [Documentación oficial](https://www.python.org/)\n",
        "\n",
        "* [Towards Data Science](https://towardsdatascience.com/) y [Medium](https://medium.com/) son dos páginas con muy buenos tutoriales.\n",
        "\n",
        "* Por supuesto, Google, StackOverflow, chatGPT, Copilot, etc."
      ],
      "metadata": {
        "id": "JKsBtGNmWz0i"
      }
    }
  ]
}
