from flask import Flask, render_template, request, jsonify, redirect, url_for
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from bot.chatbot import Chatbot
from config import settings
from config.models import db, User

app = Flask(__name__)
app.config.from_object(settings)
db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
chatbot = Chatbot('data/intents.json')

@app.route('/')
@login_required
def home():
    return render_template('index.html',
                         bot_name=settings.BOT_NAME,
                         current_user=current_user)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if User.query.filter_by(username=username).first():
            return 'Username already exists!'
            
        if User.query.filter_by(email=email).first():
            return 'Email already registered!'
            
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        
        db.session.add(new_user)
        db.session.commit()
        
        login_user(new_user)
        return redirect(url_for('home'))
        
    return render_template('register.html', bot_name=settings.BOT_NAME)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('home'))
            
        return 'Invalid username or password'
        
    return render_template('login.html', bot_name=settings.BOT_NAME)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/chat', methods=['POST'])
def chat():
    message = request.json['message']
    response = chatbot.get_response(message)
    return jsonify({'response': response})

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    print(f"{settings.BOT_NAME} is now running...")
    app.run(host='127.0.0.1', port=5000, debug=True) 