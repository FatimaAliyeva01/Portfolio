
from app import app
from app.models import *
from app import db
from flask import render_template,request,redirect
from flask import url_for
import os
# from flask_bcrypt import Bcrypt
def loginCheck(param):
    adminLoginStat = request.cookies.get('adminLoginStatus')
    if adminLoginStat=='beli':
        return param
    else:
               return redirect(url_for('login'))

@app.route('/admin')
def admin_index():
   lefts=Skilleft.query.all()
   skills=Skill.query.all()
   teams=Team.query.all()
   contacts=ContactHeading.query.all()
   icons=Contact.query.all()
   return loginCheck(render_template('admin/index.html',lefts=lefts,skills=skills,icons=icons,contacts=contacts,teams=teams))
  
# Skill left
@app.route('/admin/create', methods=['GET','POST']) 
def create():
   lefts=Skilleft.query.all()
   if request.method=='POST':
      left=Skilleft(
      skill_heading=request.form['skill_heading'],
      skill_desc=request.form['skill_desc']
      )     
      db.session.add(left)
      db.session.commit()
      return redirect('/admin/create')
   return loginCheck(render_template('admin/create.html',lefts=lefts))
   
@app.route("/admin/createdelete/<id>")
def createdelete(id):
   left=Skilleft.query.get(id)
   db.session.delete(left)
   db.session.commit()
   return redirect('/admin/create')


@app.route("/admin/createupdate/<id>" , methods=['GET','POST'])  
def createupdate(id):
   left=Skilleft.query.get(id)
   if request.method=='POST':
      left.skill_heading=request.form['skill_heading']
      left.skill_desc=request.form['skill_desc']
   
      db.session.commit()
      return redirect('/admin/create')
   return loginCheck(render_template('admin/createupdate.html',left=left))


@app.route('/admin/skill', methods=['GET','POST']) 
def skill():
   skills=Skill.query.all()
   if request.method=='POST':
      skill=Skill(
      ski_name=request.form['ski_name'],
      ski_persantage=request.form['ski_persantage']
      )     
      db.session.add(skill)
      db.session.commit()
      return redirect('/admin/skill')
   return loginCheck(render_template('admin/skill.html',skills=skills))
   
@app.route("/admin/skilldelete/<id>")
def skilldelete(id):
   skill=Skill.query.get(id)
   db.session.delete(skill)
   db.session.commit()
   return redirect('/admin/skill')


@app.route("/admin/skillupdate/<id>" , methods=['GET','POST'])  
def skillupdate(id):
   skill=Skill.query.get(id)
   if request.method=='POST':
      skill.ski_name=request.form['ski_name']
      skill.ski_persantage=request.form['ski_persantage']
   
      db.session.commit()
      return redirect('/admin/skill')
   return loginCheck(render_template('admin/skillupdate.html',skill=skill))


# 


@app.route('/admin/team', methods=['GET','POST']) 
def team():
   teams=Team.query.all()
   if request.method=='POST':
      file=request.files['commenter_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      team=Team(
         commenter_name=request.form['commenter_name'],
         commenter_desc =request.form['commenter_desc'],
         commenter_img=filename

      )     
      db.session.add(team)
      db.session.commit()
      return redirect('/admin/team')
   return loginCheck(render_template('admin/team.html',teams=teams))

# delete
@app.route("/admin/teamdelete/<id>")
def Teamdelete(id):
   team=Team.query.get(id)
   db.session.delete(team)
   db.session.commit()
   return redirect('/admin/team')


# update
@app.route("/admin/teamupdate/<id>" , methods=['GET','POST']) 
def Teamupdate(id):
   team=Team.query.get(id)
   if request.method=='POST':
      file=request.files['commenter_img']
      filename=file.filename
      file.save(os.path.join (app.config['UPLOAD_FOLDER'],filename))
      team.commenter_name==request.form['commenter_name']
      team.commenter_desc==request.form['commenter_desc']
      team.commenter_img=filename
      db.session.commit()
      return redirect('/admin/team')
   return loginCheck(render_template('admin/teamupdate.html',team=team))





@app.route('/admin/contactheading', methods=['GET','POST']) 
def contactheading():
   contacts=ContactHeading.query.all()
   if request.method=='POST':
      contact=ContactHeading(
      contact_subheading_name =request.form['contact_subheading_name'],
      contact_heading_name=request.form['contact_heading_name']
      )     
      db.session.add(contact)
      db.session.commit()
      return redirect('/admin/contactheading')
   return loginCheck(render_template('admin/contactheading.html',contacts=contacts))
   
   # update
@app.route("/admin/contactheadingupdate/<id>" , methods=['GET','POST'])  
def contactupdate(id):
   contact=ContactHeading.query.get(id)
   if request.method=='POST':
      contact.contact_subheading_name=request.form['contact_subheading_name']
      contact.contact_heading_name=request.form['contact_heading_name']
      db.session.commit()
      return redirect('/admin/contactheading')
   return loginCheck(render_template('admin/contactheadingupdate.html',contact=contact))

@app.route("/admin/contactheadingdelete/<id>")
def contactdelete(id):
   contact=ContactHeading.query.get(id)
   db.session.delete(contact)
   db.session.commit()
   return redirect('/admin/contactheading')

# icon

@app.route('/admin/icon', methods=['GET','POST']) 
def icon():
   icons=Contact.query.all()
   if request.method=='POST':
      icon=Contact(
      contact_icon=request.form['contact_icon'],
      contact_icon_txt=request.form['contact_icon_txt'],
      contact_desc=request.form['contact_desc']
      )     
      db.session.add(icon)
      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck(render_template('admin/icon.html',icons=icons))
   
   # update
@app.route("/admin/iconupdate/<id>" , methods=['GET','POST'])  
def iconupdate(id):
   icon=Contact.query.get(id)
   if request.method=='POST':
      icon.contact_icon=request.form['contact_icon']
      icon.contact_icon_txt=request.form['contact_icon_txt']
      icon.contact_desc=request.form['contact_desc']

      db.session.commit()
      return redirect('/admin/icon')
   return loginCheck(render_template('admin/iconupdate.html',icon=icon))

@app.route("/admin/icondelete/<id>")
def icondelete(id):
   icon=Contact.query.get(id)
   db.session.delete(icon)
   db.session.commit()
   return redirect('/admin/icon')