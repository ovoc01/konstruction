from resetdb import reset_db,generate_sequence
from flask import Flask, request, jsonify
from flask_cors import CORS

import psycopg2


app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})


conn = psycopg2.connect(
   database="konstruction", user="postgres", password="pixel", host="localhost", port="5432"
)


@app.route('/reset_database', methods=['POST'])
def reset_database():
    """
    Resets the database using the reset_db function.

    Returns:
        JSON response indicating success or failure.
    """
    try:
        reset_db(conn)
        generate_sequence(conn)
        conn.commit()
        return jsonify(
            {
                'message': 'Database reset successfully',
                'status':200
            }
            )
    except Exception as e:
        conn.rollback()
        return jsonify(
            {
                'error': str(e),
                'status':500
            }
            
            ), 500

@app.route('/generate_sequence', methods=['POST'])
def generate_sequence_route():
    """
    Generates a sequence using the generate_sequence function.

    Returns:
        JSON response containing the generated sequence or an error message.
    """
    try:
        generate_sequence(conn)
        conn.commit()
        return jsonify(
            {
                'message': 'Sequence generated successfully',
                'status':200
            }
            )
    except Exception as e:
        return jsonify(
            {
                'error': str(e),
                'status':500
            }
            ), 500

if __name__ == '__main__':
    app.run(debug=True)

