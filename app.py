import pymssql

server = 'sdplserver.database.windows.net'
database = 'dme'
user_name = 'dmeadmin'
password = 'Agri@774Safe#14'


#######################################################################################

from flask import Flask, render_template, request

app = Flask("__name__")

@app.route("/", methods=["GET", "POST"])

def home():

    now_connect = pymssql.connect(server= server, user= user_name, password= password, database= database)
    cursor = now_connect.cursor()
    query = """select top 7 * from Daily_Packing_Data where Location ='Agarpara' and Weight_of_Bag<7 order by Weight_of_Bag DESC;"""
    cursor.execute(query)
    result = cursor.fetchall()
    now_connect.close()
    return render_template("index.html",ans=result)

if __name__=="__main__":
    app.run(debug=True)
