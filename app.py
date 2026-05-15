import pymssql

server = 'myserver.database.windows.net'
database = 'dnjghmmbvgkjhe'
user_name = 'dhjfgj,in'
password = 'Aghfyyrfuggiyfy5r5614'


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


    query2 = """select top 7 * from Daily_Packing_Data where Location ='Agarpara' and Weight_of_Bag>7.5 order by Weight_of_Bag ASC;"""
    cursor.execute(query2)
    result2 = cursor.fetchall()
    now_connect.close()
    return render_template("index.html",ans=result, ans2=result2)

if __name__=="__main__":
    app.run(debug=True)
