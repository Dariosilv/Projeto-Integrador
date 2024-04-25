from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask import Flask, render_template

app = Flask(__name__, template_folder="../tam")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bank.db'
db = SQLAlchemy(app)
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Account {self.name}>'
@app.route('/create', methods=['POST'])
def create_account():
    name = request.form['name']
    email = request.form['email']
    balance = request.form['balance']
    new_account = Account(name=name, email=email, balance=balance)
    db.session.add(new_account)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/balance/<string:email>')
def check_balance(email):
    account = Account.query.filter_by(email=email).first()
    if account:
        return str(account.balance)
    else:
        return 'Conta não encontrada'

@app.route('/deposit', methods=['POST'])
def make_deposit():
    email = request.form['email']
    amount = request.form['amount']
    account = Account.query.filter_by(email=email).first()
    if account:
        account.balance += float(amount)
        db.session.commit()
        return str(account.balance)
    else:
        return 'Conta não encontrada'

@app.route('/withdraw', methods=['POST'])
def make_withdrawal():
    email = request.form['email']
    amount = request.form['amount']
    account = Account.query.filter_by(email=email).first()
    if account:
        if account.balance >= float(amount):
            account.balance -= float(amount)
            db.session.commit()
            return str(account.balance)
        else:
            return 'Saldo insuficiente'
    else:
        return 'Conta não encontrada'


Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/create')
def create():
    return render_template('create.html')

@app.route('/balance')
def balance():
    return render_template('balance.html')

@app.route('/deposit')
def deposit():
    return render_template('deposit.html')

@app.route('/withdraw')
def withdraw():
    return render_template('withdraw.html')

if __name__ == '__main__':
    app.run(debug=True)