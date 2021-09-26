# from re import M, T
from admin.routes import *
from app import app
from app.models import *
from flask import render_template,request,redirect


@app.route('/')
def index():
   lefts=Skilleft.query.all()
   skills=Skill.query.all()
   teams=Team.query.all()
   contacts=ContactHeading.query.all()
   icons=Contact.query.all()
   return render_template('main/index.html',lefts=lefts,skills=skills,icons=icons,contacts=contacts,teams=teams)


@app.route('/admin/contactform', methods=['GET','POST']) 
def contactform():
   contactforms =ContactMe.query.all()
   if request.method=='POST':
      contactform=ContactMe(
   user_name=request.form['user_name'],
   user_email=request.form['user_email'],
   user_message=request.form['user_message']

      )     
      db.session.add(contactform)
      db.session.commit()
      return redirect('/')
   return loginCheck (render_template('admin/contactform.html',contactforms=contactforms ))
   
@app.route("/admin/contactformdelete/<id>")
def contactformdelete(id):
   contactform =ContactMe.query.get(id)
   db.session.delete(contactform)
   db.session.commit()
   return redirect('/admin/contactform')



 