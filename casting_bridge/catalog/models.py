# -*- coding: utf-8 -*-
from decimal import Decimal
from wtforms import TextField, DecimalField, SelectField, FileField, DateField, BooleanField, SelectMultipleField, RadioField, TextAreaField
from wtforms.validators import InputRequired, NumberRange, ValidationError, Optional, Length
from wtforms.widgets import html_params, Select, HTMLString
from flask_wtf import Form
from flask_wtf.html5 import TelField
from casting_bridge import db

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), index=True)
    type = db.Column(db.String(255))
    name = db.Column(db.String(255))

    def __init__(self, created=None, person_id=None, type='', name=''):
        self.created = created
        self.person_id = person_id
        self.type = type
        self.name = name

    def __repr__(self):
        return '<Document %d>' % self.id

class Classifier(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(255), index=True)
    tag_lv = db.Column(db.String(255), index=True)
    tag_en = db.Column(db.String(255), index=True)
    tag_ru = db.Column(db.String(255), index=True)
    skills = db.relationship('Skill', backref='classifier', lazy='dynamic')

    def __init__(self, category='', tag_en='', tag_lv='', tag_ru=''):
        self.category = category
        self.tag_en = tag_en
        self.tag_lv = tag_lv
        self.tag_ru = tag_ru

    def __repr__(self):
        return '<Classifier %d>' % self.id

class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime)
    modified = db.Column(db.DateTime)
    name = db.Column(db.String(255), index=True)
    surname = db.Column(db.String(255), index=True)
    nickname = db.Column(db.String(255))
    pcode = db.Column(db.String(255))
    contract_nr = db.Column(db.String(255))
    #birthdate = db.Column(db.String(255))
    birthdate = db.Column(db.Date)
    my_phone_code = db.Column(db.String(255))
    my_phone = db.Column(db.String(255))
    email = db.Column(db.String(255))
    other_phone_code = db.Column(db.String(255))
    other_phone = db.Column(db.String(255))
    home_address = db.Column(db.String(255))
    height = db.Column(db.Integer)
    foot_size = db.Column(db.Integer)
    cloth_size = db.Column(db.String(255))
    voice = db.Column(db.String(255))
    contact_lenses = db.Column(db.Boolean)
    be_dressed = db.Column(db.Boolean)
    profile_image = db.Column(db.String(255))
    is_active = db.Column(db.Boolean) # inactive by default
    species = db.Column(db.String(255)) # 1-man, 2-woman, 3- animal
    mother_phone_code = db.Column(db.String(255))
    mother_phone = db.Column(db.String(255))
    mother_name = db.Column(db.String(255))
    father_phone_code = db.Column(db.String(255))
    father_phone = db.Column(db.String(255))
    father_name = db.Column(db.String(255))
    speciality = db.Column(db.String(255))
    experience = db.Column(db.String(1000))
    cv = db.Column(db.String(255))
    current_occupation = db.Column(db.String(255))
    workplace = db.Column(db.String(255))
    play_age_from = db.Column(db.Integer)
    play_age_to = db.Column(db.Integer)

    skills = db.relationship('Skill', backref='person', lazy='dynamic')
    documents = db.relationship('Document', backref='document', lazy='dynamic')

    def __init__(self, created=None, modified=None, name='', surname='', nickname='', pcode='', contract_nr='', birthdate='', my_phone_code='', my_phone='', email='', other_phone_code='', other_phone='', home_address='', height='', foot_size='', cloth_size='', voice='', contact_lenses=False, be_dressed=False, profile_image=None, is_active=False, species='',mother_phone_code = '',mother_phone = '',mother_name = '',father_phone_code = '',father_phone = '',father_name = '',speciality = '',experience = '',cv=None, current_occupation=None, workplace=None, play_age_from='', play_age_to=''):
        self.created = created
        self.modified = modified
        self.name = name
        self.surname = surname
        self.nickname = nickname
        self.pcode = pcode
        self.contract_nr = contract_nr
        self.birthdate = birthdate
        self.my_phone_code = my_phone_code
        self.my_phone = my_phone
        self.email = email
        self.other_phone_code = other_phone_code
        self.other_phone = other_phone
        self.home_address = home_address
        self.height = height
        self.foot_size = foot_size
        self.cloth_size = cloth_size
        self.voice = voice
        self.contact_lenses = contact_lenses
        self.be_dressed = be_dressed
        self.profile_image = profile_image
        self.is_active = is_active
        self.species = species
        self.mother_phone_code = mother_phone_code
        self.mother_phone = mother_phone
        self.mother_name = mother_name
        self.father_phone_code = father_phone_code
        self.father_phone = father_phone
        self.father_name = father_name
        self.speciality = speciality
        self.experience = experience
        self.cv = cv
        self.current_occupation = current_occupation
        self.workplace = workplace
        self.play_age_from = play_age_from
        self.play_age_to = play_age_to

    def __repr__(self):
        return '<Person %d>' % self.id

class Skill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), index=True)
    classifier_id = db.Column(db.Integer, db.ForeignKey('classifier.id'), index=True)

    def __repr__(self):
        return '<Skill %d>' % self.id

class SelectMultipleFieldNoValidate(SelectMultipleField):
    # Disable valiadation
    def pre_validate(self, form):
        pass

class SelectFieldNoValidate(SelectField):
    # Disable valiadation
    def pre_validate(self, form):
        pass

class CustomRadioInput(Select):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('id', field.id)
        html = []
        for val, label, selected in field.iter_choices():
            print("choices [%s] [%s] [%s]" % (val,label, selected))
            html.append(
                '<label class="btn btn-default %s"> <input type="radio" %s> %s </label>' % ( 'active' if selected else '',
                    html_params(
                        name=field.name, value=val, checked=selected, **kwargs
                    ), label
                )
            )
        return HTMLString(' '.join(html))

class RadioButtonField(SelectField):
    widget = CustomRadioInput()

class BaseForm(Form):
    # Personal data
    species = RadioButtonField('Species', validators=[InputRequired()], choices=[('man',u'Vīrietis'),('woman',u'Sieviete')], default='')
    name = TextField('Name', validators=[InputRequired(),Length(max=255)])
    surname = TextField('Surname', validators=[InputRequired(),Length(max=255)])
    nickname = TextField('Nickname', validators=[Length(max=255)])
    pcode = TextField('ID code', validators=[Length(max=255)])
    contract_nr = TextField('Passport nr.', validators=[Length(max=255)])
    birthdate = DateField('Birthdate')
    play_age_from = TextField('Play age from', validators=[Length(max=2)])
    play_age_to = TextField('Play age to', validators=[Length(max=2)])

    # Family
    mother_phone_code = TextField('Mother phone code', validators=[Length(max=255)])
    mother_phone = TextField('Mother phone', validators=[Length(max=255)])
    mother_name = TextField('Mother name', validators=[Length(max=255)])
    father_phone_code = TextField('Father phone code', validators=[Length(max=255)])
    father_phone = TextField('Father phone', validators=[Length(max=255)])
    father_name = TextField('Father name', validators=[Length(max=255)])

    #Contact information
    my_phone_code  = TelField('Phone code', validators=[Length(max=255)])
    my_phone = TelField('Phone', validators=[InputRequired(),Length(max=255)])
    email = TextField('E-mail', validators=[InputRequired(),Length(max=255)])
    other_phone_code = TextField('Other phone code', validators=[Length(max=255)])
    other_phone = TextField('Other phone', validators=[Length(max=255)])
    home_address = TextField('Home address', validators=[InputRequired(),Length(max=255)])
    city = SelectField('Nearest city', choices=[])

    #Personal carecteristics
    height = TextField('Height', validators=[Length(max=3)])
    foot_size = SelectFieldNoValidate('Foot size', choices=[])
    cloth_size = SelectFieldNoValidate('Cloth size', choices=[])
    voice = SelectFieldNoValidate('Voice', choices=[])
    haircolor = SelectField('Hair color', choices=[])
    eyecolor = SelectField('Eye color', choices=[])

    #Who you are?
    speciality = RadioButtonField('Speciality', validators=[InputRequired()], choices=[('actor',u'Aktieris'),('professional',u'Profesionālis'),('talent',u'Talants')])
    subspeciality = SelectMultipleFieldNoValidate('Subspeciality', choices=[])
    experience = TextAreaField('Experience', validators=[Length(max=1000)])
    cv = FileField('CV')
    #actor = TextField('Actor')
    #professional = TextField('Professional')
    #talent = TextField('Talent')

    #Skills
    #danceskill = TextField('Dance skill')
    danceskill = SelectMultipleFieldNoValidate('Dance skill', choices=[])
    singskill = SelectMultipleFieldNoValidate('Sing skill', choices=[])
    musicskill = SelectMultipleFieldNoValidate('Music skill', choices=[])
    sportskill = SelectMultipleFieldNoValidate('Sport skill', choices=[])
    swimskill = SelectMultipleFieldNoValidate('Swim skill', choices=[])
    driveskill = SelectMultipleFieldNoValidate('Drive skill', choices=[])
    languageskill = SelectMultipleFieldNoValidate('Language skill', choices=[])
    otherskill = SelectMultipleFieldNoValidate('Other skill', choices=[])

    #Work and Education
    educational_institution = SelectMultipleFieldNoValidate('Educational institution', choices=[])
    learned_profession = SelectMultipleFieldNoValidate('Learned profession', choices=[])
    degree = SelectMultipleFieldNoValidate('Level of education', choices=[])
    current_occupation = SelectFieldNoValidate('Current occupation', choices=[])
    workplace = TextField('Workplace', validators=[Length(max=255)])


    #My whishes
    want_participate = SelectMultipleFieldNoValidate('Want to participate', choices=[])
    dont_want_participate = SelectMultipleFieldNoValidate('Don`t want to participate', choices=[])
    interested_in = SelectMultipleFieldNoValidate('Interested in', choices=[])

    #Notes for consideration
    #contact_lenses = TextField('Contact Lenses')
    contact_lenses = BooleanField('Contact Lenses')
    be_dressed = BooleanField('Don`t want to be undressed')
    tattoo = SelectMultipleFieldNoValidate('Tattoos', choices=[])
    piercing = SelectMultipleFieldNoValidate('Piercings', choices=[])
    afraidof = SelectMultipleFieldNoValidate('I`am afraid of', choices=[])
    religion = SelectMultipleFieldNoValidate('Religion beliefs', choices=[])

    image1 = FileField('Image No.1')
    image2 = FileField('Image No.2')
    profile_image = FileField('Profile image')

    cb_tags = SelectMultipleFieldNoValidate('Casting bridge tags', choices=[])
    family_notes = SelectMultipleFieldNoValidate('Family notes', choices=[])

    video = FileField('Video')
    audio = FileField('Audio')

class UserForm(BaseForm):
    pass

class UpdateForm(BaseForm):
    image3 = FileField('Image No.3')
    image4 = FileField('Image No.4')
    image5 = FileField('Image No.5')


