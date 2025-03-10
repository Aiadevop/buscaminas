import os 
from flask import Flask, render_template, request, session, jsonify
from buscaminas.buscaminas import Buscaminas
import secrets
# app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_dir = os.path.join(BASE_DIR, "templates")
static_dir = os.path.join(BASE_DIR, "static")
buscaminas_dir = os.path.join(BASE_DIR, "buscaminas")
app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
app.secret_key = secrets.token_hex(16) 

@app.route('/', methods=['GET', 'POST'])
def home():
    # Crear una instancia de Buscaminas y generar el tablero
    session.clear() 
    rows = int(request.form['rows']) if 'rows' in request.form else 5
    cols = rows
    # cols = int(request.form['cols']) if 'cols' in request.form else 5
    bombs = int(request.form['bombs']) if 'bombs' in request.form else 5    
    buscaminas = Buscaminas()
    session['game_over'] = False
    total_cells = rows*cols
    empty_cells = total_cells - bombs
    session['empty_cells'] = empty_cells
    if 'matrix_booms' not in session:
        # Si no hay matrix, generar una nueva
        matrix_booms = buscaminas.numbers(rows, cols, bombs)
        session['matrix_booms'] = matrix_booms  # Guardar la matrix en la sesión
        session['game_over'] = False  # Inicializar state del juego
        print(session)        
        total_cells = rows*cols
        empty_cells = total_cells - bombs
        session['empty_cells'] = empty_cells
        table_web = buscaminas.table_html(matrix_booms)
        return render_template('index.html', table_html=table_web)
    else:
        # Si ya existe una matrix, obtenerla de la sesión
        matrix_booms = session['matrix_booms']
        
    table_web = buscaminas.table_html(matrix_booms)
    if 'game_over' not in session:
        session['game_over'] = False
        
    return render_template('index.html', table_html=table_web)

@app.route('/play', methods=['GET', 'POST'])

def play():
    # Crear una instancia de Buscaminas y generar el tablero
    buscaminas = Buscaminas()  
    matrix_booms = session['matrix_booms']
    table_web = buscaminas.table_html(matrix_booms)    
    if 'game_over' not in session:
        session['game_over'] = False
    if request.method == 'POST' and 'row' in request.form and 'col' in request.form:
        # Obtener las coordenadas de la jugada desde el formulario
        row = int(request.form['row'])
        col = int(request.form['col'])

        # Llamamos al método play para procesar la jugada
        state= buscaminas.play(matrix_booms, row , col)

        # Si el state es 1, el jugador puede seguir jugando, sino el juego acaba
        if state == 1:
            # Si el state es 1, el jugador puede seguir jugando
            if 'moves' not in session:
                session['moves'] = 0
            session['moves'] = 1 + session['moves']
            if session['empty_cells'] == session['moves']:
                session.clear()  
                return jsonify({"status": 2, "msg": "Has ganado!✨✨"})
            session['game_over'] = False
            session['matrix_booms'] = matrix_booms  # Guardamos el state actualizado
            return jsonify({"status": 0, "msg": "Sigue jugando!"})
        else:
            # Si el state es 0 (Game Over), cambiamos el state del juego
            session.clear()  
            session['game_over'] = True
            return jsonify({"status": 1, "msg": "Game Over!"})

    return render_template('index.html', table_html=table_web)

@app.route('/about')
def about():
    return 'About'