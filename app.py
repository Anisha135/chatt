from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)

bot = ChatBot(name='chatterbot',
                      logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch',
                                      'chatterbot.logic.SpecificResponseAdapter'])
trainer = ChatterBotCorpusTrainer(bot)
trainer.train("chatterbot.corpus.english")


@app.route('/')
def home():
    return render_template('index.html')
@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(bot.get_response(userText))

if __name__ == "__main__":
    app.config['ENV'] = 'development'
    app.config['DEBUG'] = True
    app.config['TESTING'] = True
