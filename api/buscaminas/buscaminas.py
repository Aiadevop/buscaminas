# Definir la clase y el método para generar el table
# La clase se llamará Buscaminas y el primer método initial_table.
# Este método recibirá como parámetro el número de rows, de cols y el caracter con el que deseamos rellenar el table.
# El método devolverá una lista con tantas listas como rows y de longitud igual a las cols donde el valor de cada uno de los elementos sea igual a un mismo caracter.
# Por ejemplo generar un table de 5 rows y 5 cols relleno de 0.
import random


class Buscaminas:
    def __init__(self):
        # Iniciar las variables 
        self.rows = 0
        self.cols = 0
        self.bombs = 0
        self.table = []

    def initial_table(self, rows=5, cols=5, caracter=0):
        self.rows = rows
        self.cols = cols
        self.caracter = caracter
        matrix = []
        for x in range(self.rows):
            matrix.append([])
            for y in range(self.cols):
                matrix[x].append(self.caracter)
        return matrix

    # Ahora crearemos el método put_booms, encargado de colocar las bombs aleatoriamente. Este método recibirá como parámetros el número de rows, el número de cols y el número de bombs.
    # El método debe:
    # Llamar al método initial_table para las rows y cols introducidas por parámetro y rellenarlo con ceros.
    # Comprobar que el número de bombs que deseas introducir es menor que el número de casillas del table y si no es así pedir al usuario mediante un input con el mensaje 'El número de bombs no puede ser mayor que el número de casillas, introduzca un número de bombs menor' hasta que se cumpla.
    # Colocar las bombs aleatoriamente en el table, sustituyendo el 0 en esa posición por una 'B'. Asegúrate que el número final de bombs colocadas en el table debe ser igual al número introducido como parámetro.
    # Ejemplo Colocar, en un table 5x5, 5 bombs.
    def put_booms(self, rows, cols, bombs):
        self.rows = rows
        self.cols = cols
        self.bombs = bombs
        matrix = Buscaminas().initial_table(self.rows, self.cols, 0)
        put_bombs = 0
        while self.bombs >= self.rows*self.cols:
            self.bombs = int(input(
                'El número de bombs no puede ser mayor que el número de casillas, introduzca un número de bombs menor'))
        while put_bombs < self.bombs:
            f, c = [random.randint(0, self.rows-1),
                    random.randint(0, self.cols-1)]
            if matrix[f][c] != 'B':
                matrix[f][c] = 'B'
                put_bombs += 1
        return matrix

    # Generar las pistas en el table
    # Ahora generaremos los números que indican cuantas bombas hay alrededor de dicha cell (diagonales incluidas).
    # Recibiendo como parámetro el número de rows, de cols y de bombs deberá:
    # Llamar al método put_booms y generar el table con las bombas.
    # Buscar las bombas en el table e incrementar en 1 las cells adyacentes. Debes tener en cuenta el comportamiento especial de las esquinas y las primeras y últimas rows y cols.
    # Devolver la lista de lista resultante:
    def numbers(self, rows, cols, bombs):
      self.rows = rows
      self.cols = cols
      self.bombs = bombs
      matrix_booms = Buscaminas().put_booms(self.rows, self.cols, self.bombs)
      for i in range(0, self.rows):
          for j in range(0, self.cols):
              if matrix_booms[i][j] == 'B':
                  if i != 0 and matrix_booms[i-1][j] != 'B':
                      matrix_booms[i-1][j] += 1  # arriba
                  if i != (self.rows-1) and matrix_booms[i+1][j] != 'B':
                      matrix_booms[i+1][j] += 1  # abajo
                  if j != 0 and matrix_booms[i][j-1] != 'B':
                      matrix_booms[i][j-1] += 1  # izq
                  if j != (self.cols-1) and matrix_booms[i][j+1] != 'B':
                      matrix_booms[i][j+1] += 1  # der
                  if i != 0 and j != 0 and matrix_booms[i-1][j-1] != 'B':
                      matrix_booms[i-1][j-1] += 1  # arriba a la izq
                  if i != (self.rows-1) and j != (self.cols-1) and matrix_booms[i+1][j+1] != 'B':
                      matrix_booms[i+1][j+1] += 1  # abajo a la derecha
                  if i != 0 and j != (self.cols-1) and matrix_booms[i-1][j+1] != 'B':
                      matrix_booms[i-1][j+1] += 1  # arriba a la derecha
                  if i != self.cols-1 and j != 0 and matrix_booms[i+1][j-1] != 'B':
                      matrix_booms[i+1][j-1] += 1  # abajo a la izq
      return matrix_booms
    
    def play(self, matrix_booms,tiradax,tiraday):
    #   print(f"Jugada: {matrix_booms} tiradax: {tiradax} tiraday: {tiraday} play: {matrix_booms[tiradax][tiraday]}")
      if matrix_booms[tiradax][tiraday]!='B':
        return 1
      else:
        return 0

    def table_html(self, matrix_booms):
        # numbers=Buscaminas().numbers(self.rows,self.cols,self.bombs)
        boomicon = "https://cdn-icons-png.flaticon.com/128/7675/7675020.png"
        # <a href="https://www.flaticon.es/iconos-gratis/bomba-atomica" title="bomba atómica iconos">Bomba atómica iconos creados por Freepik - Flaticon</a>
        num1icon = "https://cdn-icons-png.flaticon.com/128/3570/3570098.png"
        # <a href="https://www.flaticon.es/iconos-gratis/numero" title="número iconos">Número iconos creados por Freepik - Flaticon</a>
        # num2icon = "https://cdn-icons-png.flaticon.com/128/6287/6287699.png"
        num2icon = "https://cdn-icons-png.flaticon.com/128/2880/2880484.png"
        # <a href="https://www.flaticon.es/iconos-gratis/ninos" title="niños iconos">Niños iconos creados por Freepik - Flaticon</a>
        num3icon = "https://cdn-icons-png.flaticon.com/128/9957/9957062.png"
        # <a href="https://www.flaticon.es/iconos-gratis/omega-3" title="omega 3 iconos">Omega 3 iconos creados por Freepik - Flaticon</a>
        num4icon = "https://cdn-icons-png.flaticon.com/128/4020/4020013.png"
        # <a href="https://www.flaticon.es/iconos-gratis/4" title="4 iconos">4 iconos creados por Freepik - Flaticon</a>
        num5icon = "https://cdn-icons-png.flaticon.com/128/4020/4020014.png"
        # <a href="https://www.flaticon.es/iconos-gratis/5" title="5 iconos">5 iconos creados por Freepik - Flaticon</a>
        num6icon = "https://cdn-icons-png.flaticon.com/128/6287/6287083.png"
        # <a href="https://www.flaticon.es/iconos-gratis/seis" title="seis iconos">Seis iconos creados por Freepik - Flaticon</a>
        num7icon = "https://cdn-icons-png.flaticon.com/128/4020/4020016.png"
        # <a href="https://www.flaticon.es/iconos-gratis/7" title="7 iconos">7 iconos creados por Freepik - Flaticon</a>
        num8icon = "https://res.cloudinary.com/dguhnftxe/image/upload/v1741509723/8_nafzli.png"
        # <a href="https://www.flaticon.es/iconos-gratis/8" title="8 iconos">8 iconos creados por Freepik - Flaticon</a>
        plant = "https://cdn-icons-png.flaticon.com/128/1598/1598196.png"
        # <a href="https://www.flaticon.es/iconos-gratis/sustentabilidad" title="sustentabilidad iconos">Sustentabilidad iconos creados por Freepik - Flaticon</a>
    
        # Generar HTML para el table con las imágenes correspondientes
        table_html = ""
        for i, row in enumerate(matrix_booms):
            table_html += "<tr>"
            for j, cell in enumerate(row):
                # Mostrar imágenes según el valor de la cell
                if cell == 'B':  # Si es bomba
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img  src="{boomicon}" alt="Boom" width="30"></div></td>'
                elif cell == 1:  # Si es un número 1
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num1icon}" alt="1" width="30"></div></td>'
                elif cell == 2:  # Si es un número 2
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num2icon}" alt="2" width="30"></div></td>'
                elif cell == 3:  # Si es un número 3
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num3icon}" alt="3" width="30"></div></td>'
                elif cell == 4:  # Si es un número 4
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num4icon}" alt="4" width="30"></div></td>'
                elif cell == 5:  # Si es un número 5
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num5icon}" alt="5" width="30"></div></td>'
                elif cell == 6:  # Si es un número 6
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num6icon}" alt="6" width="30"></div></td>'
                elif cell == 7:  # Si es un número 7
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num7icon}" alt="7" width="30"></div></td>'
                elif cell == 8:  # Si es un número 8
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{num8icon}" alt="8" width="30"></div></td>'
                else:  # Si es un espacio vacío o sin revelar
                    table_html += f'<td class="cell" style="border: solid black 1px" data-row="{i}" data-col="{j}"><div class="icon" data-img="img_{i}{j}" style="display:none;"><img src="{plant}" alt="4" width="30"></div></td>'
            table_html += "</tr>"

        return table_html