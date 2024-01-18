from flask import Flask, render_template, request, jsonify, g, session
from flask_session import Session
import sqlite3
from model_handler import setup_conversation_buff, do_query, load_llm

app = Flask(__name__)

app.secret_key = 'your_secret_key'
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)
DATABASE_PATH = '/home/ksaff/Desktop/sql/choosen_DB.sqlite'

def get_db():
    db = sqlite3.connect(DATABASE_PATH)
    return db

def reset_memory():
    session.clear()
    del session['context']
    return '', 200

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert-query', methods=['POST'])
def convert_query():
    data = request.get_json()
    user_query = data['user_query']

    if 'context' not in session or len(session['context']) >= 3:
        session['context'] = [user_query]
    else:
        session['context'].append(user_query)
        

    sql_query = do_query(question=user_query, conversation=conversation_buff)

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
    llm = load_llm()
    conversation_buff = setup_conversation_buff(llm)
    app.run(debug=True, use_reloader=False)