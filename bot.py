from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

chess_bot = ChatBot('ChessBot')

trainer = ChatterBotCorpusTrainer(chess_bot)
trainer.train('chatterbot.corpus.english')

custom_trainer = ListTrainer(chess_bot)

custom_trainer.train([
    'How does a pawn move?',
    'A pawn moves forward one square, but captures diagonally.',
    'What is chess?',
    'Chess is a two-player abstract strategy board game.',
    'What is the goal in chess?',
    'The object of the game is to checkmate the opponent\'s king;',
])


exit_conditions = (":q", "quit", "exit")
while True:
    query = input('🌻 Your turn >>: ')
    if query in exit_conditions:
        break
    response = chess_bot.get_response(query)
    print(f"🪴 ChessBot: {response}")
