from flask import Flask,render_template,request,url_for,redirect,jsonify,session
from flask_pymongo import PyMongo
from datetime import datetime
#import geocoder
import sys

app=Flask(__name__)
app.config["MONGO_URI"]="mongodb+srv://himanshuparida191003:hi%40191003@projects.dvdnu49.mongodb.net/doctor_appointment"
mongo=PyMongo(app)
@app.route("/")
def index():
    return render_template('index.html')

@app.route("/desktop-2.html",methods=['GET','POST'])
def desktop_2():
    if request.method=='POST':
        name=request.form['name']
        Gender=request.form['gender']
        DOB=request.form['date-of-birth']
        Contact=request.form['contact-no']
        email=request.form['email-id']
        password=request.form['password']
        confirm=request.form['confirm-password']
        city=request.form['city']
        address=request.form['address1']
        state=request.form['state'] 
        if password==confirm:
            if mongo.db.signup_data.find_one({'name':name}):
                print("This name is already taken",file=sys.stderr)
                return render_template('desktop-2.html')
            elif mongo.db.signup_data.find_one({'contact':Contact}):
                return render_template('desktop-2.html')
            elif mongo.db.signup_data.find_one({'emailid':email}):
                return render_template('desktop-2.html')
            elif mongo.db.signup_data.find_one({'password':password}):
                return render_template('desktop-2.html')
            else:
                mongo.db.signup_data.insert_one({'name':name,'gender':Gender,'dateofbirth':DOB,'contact':Contact,'emailid':email,'password':password,'confirm password':confirm,'city name':city,'address':address,'state':state})
                return render_template('desktop-3.html')
        else:
            return render_template('desktop-2.html')
    return render_template('desktop-2.html')

@app.route("/index.html")
def index1():
    return render_template('index.html')


@app.route("/desktop-3.html")
def desktop_3():
    return render_template('desktop-3.html')

@app.route("/desktop-4.html",methods=['GET','POST'])
def desktop_4():
    if request.method=='POST':
        email=request.form["email"]
        password1=request.form["password1"]
        try:
            user=mongo.db.signup_data.find_one_or_404({'password': password1,'emailid':email})
            print("email-id or password is wrong")
            return render_template("desktop-3.html",user=user)
        except Exception as e:
            error_message=str(e)
            return render_template('desktop-4.html',error_message=error_message)
    return render_template('desktop-4.html')

@app.route("/desktop-5.html")
def desktop_5():
    return render_template('desktop-5.html')

@app.route("/desktop-7.html")
def desktop_7():
    return render_template('desktop-7.html')

@app.route("/desktop-9.html")
def desktop_9():
    return render_template('desktop-9.html')

@app.route("/desktop-10.html")
def desktop_10():
    return render_template('desktop-10.html')

@app.route("/desktop-11.html")
def desktop_11():
    return render_template('desktop-11.html')

@app.route("/desktop-12.html",methods=['GET','POST'])
def desktop_12():
    if request.method=='POST':
        Name=request.form['patient-name2']
        contact=request.form['contact-no1']
        age=request.form['patient-age']
        date=request.form['appointment_date1']
        time=request.form['appointment_time1']
        if mongo.db.appointment_date_and_time.find_one({'appointment_date':date}):
            render_template('desktop-12.html')
        elif mongo.db.appointment_date_and_time.find_one({'appointment_time':time}):
            render_template('desktop-12.html')
        else:
            mongo.db.appointment_date_and_time.insert_one({'patient_name':Name,'contact_number':contact,'patient_age':age,'appointment_date':date,'appointment_time':time})
            return render_template('desktop-13.html') 
    return render_template('desktop-12.html')

@app.route("/desktop-13.html")
def desktop_13():
    return render_template('desktop-13.html')

@app.route("/enter.html")
def enter():
    return render_template('enter.html')

@app.route("/desktop-14.html",methods=['GET','POST'])
def desktop_14():
    if request.method=='POST':
       name=request.form['name']
       contact_no=request.form['contactno']
       location=request.form['location']
       #g = geocoder.bing(location, key='AjPzpUQtctTuUUvOX4uPH8YcA7uAwTNu2kgngxmLR5TwRHHh5Z0YRH8C09RNWaBj')
       #latitude=g.json['lat']
       #longitude=g.json['lng']
       mongo.db.nearby_hospital.insert_one({'patient_name':name,'contact_number':contact_no,'Location':location})
       return render_template('enter.html')
    return render_template('desktop-14.html')
    
if __name__=="__main__":
    app.run(debug=True)