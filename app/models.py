from enum import unique
from app import db


class Skilleft(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skill_heading=db.Column(db.String(50))
    skill_desc=db.Column(db.String(50))

class Skill(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    ski_name=db.Column(db.String(50))
    ski_persantage=db.Column(db.String(50))




class Team(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    commenter_img=db.Column(db.String(50))
    commenter_name=db.Column(db.String(50))
    commenter_desc=db.Column(db.String(50))
    
class ContactHeading(db.Model):
     id=db.Column(db.Integer,primary_key=True)
     contact_subheading_name=db.Column(db.String(50))
     contact_heading_name=db.Column(db.String(50))




class Contact(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    contact_icon=db.Column(db.String(50))
    contact_icon_txt=db.Column(db.String(50))
    contact_desc=db.Column(db.String(50))
   



# var
class ContactMe(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    user_name=db.Column(db.String(50))
    user_email=db.Column(db.String(50))
    user_message=db.Column(db.Text)



