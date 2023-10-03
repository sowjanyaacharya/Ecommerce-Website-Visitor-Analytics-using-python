from flask import Blueprint,jsonify,request
from sqlalchemy.sql import text #convert the sql query into string then overcomes sql injection(hacking)
from db import db 
import datetime

landing_blueprint = Blueprint('landing_blueprint',__name__)

@landing_blueprint.route('/products') #displaying the ui of products
def products():

    tdate = datetime.datetime.today().strftime('%Y-%m-%d')

    #log no of visitors for date
    sqlChkVisitor = text('SELECT COUNT(id) AS today_count,count FROM visitors_log WHERE date = :tdate')
    todayData = db.engine.execute(sqlChkVisitor,tdate = tdate)
    resultTodayData = todayData.fetchall()
    todayVisitorCount = resultTodayData[0].today_count
    numberOfVisitors = resultTodayData[0].count

    if todayVisitorCount == 0:

        sqlInsVisitors = text('INSERT INTO visitors_log(date,count) VALUES (:tdate,1)')
        db.engine.execute(sqlInsVisitors,tdate = tdate)

    else:

        newVisitorCount = numberOfVisitors + 1
        sqlupdvisitors = text('UPDATE visitors_log SET count = :newVisitorCount WHERE date = :tdate')
        db.engine.execute(sqlupdvisitors,newVisitorCount = newVisitorCount,tdate = tdate)

    sqlProducts = text('SELECT * FROM products')
    resultSet = db.engine.execute(sqlProducts)
    resultData = resultSet.fetchall()

    jsondata = jsonify([dict(row) for row in resultData])
    return jsondata #dictionanry-collection in python has the format of json

@landing_blueprint.route('/save-contact-data',methods=['POST'])
def saveContactData():

    f_name = request.form['name']
    f_email = request.form['email']
    f_mobile = request.form['mobile']
    f_comments = request.form['comments']  #to run 1-virtual environment connect then activate =C:\Users\achar\Documents\ecommerce-server>venv\Scripts\Activate(connect to virtual screen) then python app.py localhost:5000/products
     
    tdate = datetime.datetime.today().strftime('%Y-%m-%d')
    sqlSave = text('INSERT INTO contacts (name,email,mobile,comments,date) VALUES (:name, :email, :mobile,:comments,:todaydate)')    #: is used for sql injection(security purpose)

    db.engine.execute(sqlSave,name = f_name,email = f_email,mobile = f_mobile,comments = f_comments,todaydate = tdate )

    return 'Data Saved Successfully'
@landing_blueprint.route('/ad-click')
def adClick():

    tdate = datetime.datetime.today().strftime('%Y-%m-%d')

    # Log ad click 
    sqlAdClick = text('SELECT COUNT(id) AS adrow_count,total_clicks FROM ad_clicks WHERE date = :tdate')
    adClickData = db.engine.execute(sqlAdClick,tdate = tdate)
    resAdclickData = adClickData.fetchall()
    adClickRowCount = resAdclickData[0].adrow_count
    totalAdClickForDay = resAdclickData[0].total_clicks

    if adClickRowCount == 0:

        sqlInsAd = text('INSERT INTO ad_clicks (date,total_clicks) VALUES (:tdate,1)')
        db.engine.execute(sqlInsAd,tdate = tdate)

    else:

        newAdCount = totalAdClickForDay + 1
        sqlUpdVisitors = text('UPDATE ad_clicks SET total_clicks = :newAdCount WHERE date = :tdate')
        db.engine.execute(sqlUpdVisitors,newAdCount = newAdCount,tdate = tdate)

    return('adclick log successfully')
