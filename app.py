from flask import redirect,render_template, request, session, url_for,flash
from Wtf_yasser import SignupForm,LoginForm
from database import app,bd,User,Team,Cup

#user dabase

admin = ''
@app.route('/')
def front():
    return render_template('front.html')

@app.route('/home')
def home():
    if 'user' in session:
        if  'yasser' == session["user"]:
            return render_template('users.html',users=User.query.all())
        else:
            return render_template('sports.html')
    return redirect(url_for('login'))


@app.route('/login',methods=['POST','GET'])
def login():
    form = LoginForm()  
    if form.validate_on_submit():
        name = form.name.data
        x = User.query.filter_by(username=name).first()
        if x==None:
            flash('you need to signup')
        elif x.password == form.password.data:
            session['user'] = x.username 
            print( session['user'])
            return redirect(url_for('home'))
        else:
            flash("password invalid")
            return redirect(url_for('login'))
    return render_template('login.html',form=form)

@app.route('/signup',methods=['POST','GET'])
def signup():
    sform = SignupForm()
    if sform.validate_on_submit():
        name = sform.name.data
        x = User.query.filter_by(username=name).first()
        if  x == None:
            if sform.password.data == sform.confirm.data: 
                user = User(username=name,password=sform.password.data,email=sform.email.data)
                bd.session.add(user)
                bd.session.commit()
                return redirect(url_for('login'))
            else:
                flash('password in not the same')
                return redirect(url_for('signup'))
        else:
            flash('you have alredy an account please login')
        return redirect(url_for('home'))
    return render_template('signup.html',Sform=sform)
     
@app.route('/history')
def history():
    if "user" in session:
        return render_template('history.html')
    return redirect(url_for('home'))



@app.route('/rules')
def rules():
    if "user" in session:
        return render_template('rules.html')
    return redirect(url_for('home'))


@app.route('/championship')
def championship():
    teams = Team.query.all()
    if "user" in session:
        return render_template('championship.html',teams=teams)
    return redirect(url_for('home'))


@app.route('/more/<name>')
def learn(name):
    if "user" in session:
        if Team.query.filter_by(name=name).first()!=None:
            return render_template('learnmore.html',team = Team.query.filter_by(name=name).first())
        return f"fk you team name wrong"
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    if 'user' in session:
        session.pop('user')
    return redirect(url_for('home'))

if __name__=="__main__":
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
