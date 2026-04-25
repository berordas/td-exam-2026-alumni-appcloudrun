import os
import datetime
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def inspect_env():
    version = os.environ.get('VERSION', 'Sin versión')
    user_agent = request.headers.get('User-Agent', 'Desconocido')
    
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

    html = f"""
    <h1>Inspección de Nodo - Cloud Run</h1>
    <p><b>Estado:</b> Activo</p>
    <p><b>Versión del Software:</b> {version}</p>
    <p><b>Hora del Servidor:</b> {datetime.datetime.now()}</p>
    <hr>
    <p><b>IP del Cliente:</b> {client_ip}</p>
    <p><b>Navegador:</b> {user_agent}</p>
    """
    return html

@app.route('/api/status')
def status_json():
    return jsonify({
        "node_status": "online",
        "container_id": os.uname().nodename,
        "platform": "Google Cloud Run",
        "subject": "Tecnologías de la Digitalización"
    })

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 8080))
    )