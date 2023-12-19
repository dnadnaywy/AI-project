import json
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer

data = json.loads(open('data.json', 'r').read())
train_data = []

for row in data:
    train_data.append(row['question'])
    train_data.append(row['answer'])

chess_bot = ChatBot(
    'ChessBot',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'The question is too ambiguous and there are too many answers. Please be more specific!',
            'maximum_similarity_threshold': 0.90
        },
        'chatterbot.logic.MathematicalEvaluation',
    ],
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii'
    ]
)

custom_trainer = ListTrainer(chess_bot)
custom_trainer.train(train_data)

# trainer = ChatterBotCorpusTrainer(chess_bot)
# trainer.train('chatterbot.corpus.english')

exit_conditions = (":q", "quit", "exit")
while True:
    query = input('🌻 Your turn >>: ')
    if query in exit_conditions:
        break
    response = chess_bot.get_response(query)
    print(f"🪴 ChessBot: {response}")
