import socketIO_client
import boardPoints as bp
import minimax as mn
import movement as mm
import math

tournament_id = 1
ip = "192.168.0.101"
port = 3000

print('init socket')
s = socketIO_client.SocketIO(ip, port)
print('init connect')
s.connect()
print('connection finished')
s.emit('signin',
       {'user_name': "Hugo",
        'tournament_id': tournament_id,
        'user_role': 'player'})
print('emited signin')
points = bp.initial()
print('point system ready')

def connected():
    print('Login ok')


def sendMovent(y):
    print('preparing movement')
    turn = y['player_turn_id']
    board = y['board']
    print('playing: ', turn)
    mm.analize(board, turn, False, True)
    a, o = mn.minimax2(board, turn, points, 3, True, math.inf, -math.inf )
    print('############## sending: ', o)
    s.emit('play',
           {'tournament_id': tournament_id,
            'player_turn_id': y['player_turn_id'],
            'game_id': y['game_id'],
            'movement': o
            })
    print('movement sent \n waiting...')


def end(y):
    print('Game ended')
    s.emit('player_ready', {
        'tournament_id': tournament_id,
        'game_id': y['game_id'],
        'player_turn_id': y['player_turn_id']
    })
    print('waiting for next game...')


s.on('ok_signin', connected)
s.on('ready', sendMovent)
s.on('finish', end)

s.wait()
