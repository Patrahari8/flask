from flask import Flask,render_template,request
from flask_wtf import Form
from wtforms import StringField,IntegerField,SubmitField
from wtforms.validators import DataRequired

FAI=Flask(__name__)



@FAI.route('/htmlform',methods=['GET','POST'])
def htmlform():
    if request.method=='POST':
        return request.form['n']
    return render_template('htmlform.html')




class WebForm(Form):
    name=StringField(validators=[DataRequired()])
    age=IntegerField()
    submit=SubmitField()






@FAI.route('/webform',methods=['GET','POST'])
def webform():
    wfo=WebForm()
    if request.method=='POST':
        wfdo=WebForm(request.form)
        if wfdo.validate():
            return wfdo.data
        # if wfdo:
        #     return wfdo.name.data
        #     return wfdo.data
        
    return render_template('webform.html',wfo=wfo)










if __name__=='__main__':
    FAI.run(debug=True)