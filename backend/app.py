from flask import Flask, render_template
from flask_socketio import SocketIO, join_room, leave_room, send, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app)

# Store game state (you can implement a better data structure)
games = {}

# Serve a basic HTML file for testing (not necessary for your game)
@app.route('/')
def index():
    return "Multiplayer Chess Server Running"

# Event when a player joins a game
@socketio.on('join_game')
def on_join(data):
    game_id = data['game_id']
    username = data['username']
    join_room(game_id)
    
    if game_id not in games:
        games[game_id] = {"players": [], "board": None}
    
    games[game_id]["players"].append(username)
    
    emit('status', {'msg': f'{username} has joined the game!'}, room=game_id)

# Handle chess move
@socketio.on('move')
def handle_move(data):
    game_id = data['game_id']
    move = data['move']
    
    # Update game state here (process move, update board, etc.)
    # Example: simply broadcast the move to all players
    emit('move', {'move': move}, room=game_id)

# Event when a player leaves a game
@socketio.on('leave_game')
def on_leave(data):
    game_id = data['game_id']
    username = data['username']
    
    leave_room(game_id)
    if game_id in games:
        games[game_id]["players"].remove(username)
        emit('status', {'msg': f'{username} has left the game!'}, room=game_id)

if __name__ == '__main__':
    socketio.run(app, debug=True)
