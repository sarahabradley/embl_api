from app import app
from config import db, ma
from models import Gene, genes_schema
from flask import jsonify, request

@app.route('/genes/<geneSymbol>')
def listGenesForSymbol(geneSymbol):
    try:
        genes = Gene.query.all()
        return genes_schema.dump(genes)
    except Exception as e:
        print(e)

@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url
    }
    response = jsonify(message)
    response.status_code(404)
    return response

if __name__ == "__main__":
    app.run()