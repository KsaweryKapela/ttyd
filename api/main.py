from flask import Flask, render_template, request, jsonify, g, session
from flask_session import Session
import sqlite3


app = Flask(__name__)

app.secret_key = 'your_secret_key'  # Set this to a random string
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
DATABASE_PATH = '/home/ksaff/Desktop/sql/choosen_DB.sqlite'

def get_db():
    db = sqlite3.connect(DATABASE_PATH)
    return db

def reset_memory():
    session.clear()  # This will clear the session
    return '', 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert-query', methods=['POST'])
def convert_query():
    data = request.get_json()
    user_query = data['user_query']

    # Initialize or update session context
    if 'context' not in session or len(session['context']) >= 3:
        session['context'] = [user_query]
    else:
        session['context'].append(user_query)

    # Use session['context'] to generate SQL query
    # This is where you would use the sequence of inputs to generate the query
    sql_query = "SELECT EmployeeName FROM Salaries WHERE OvertimePay > 10000"

    return jsonify({'sql_query': sql_query})

@app.route('/execute-query', methods=['POST'])
def execute_query():
    data = request.get_json()
    sql_query = data['sql_query']
    
    try:
        db = get_db()
        cursor = db.execute(sql_query)

        rows = cursor.fetchall()

        columns = [column[0] for column in cursor.description]
        results = [dict(zip(columns, row)) for row in rows]
        print(results)
        return jsonify(results)
    except sqlite3.Error as e:
        return jsonify({'error': str(e)}), 500
    finally:
        if db:
            db.close()
        

if __name__ == '__main__':
    app.run(debug=True)