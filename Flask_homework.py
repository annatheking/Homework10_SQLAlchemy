from flask import Flask, jsonify
import csv
import datetime as dt

measurement = "10_advanced_data_storage_and_retrieval_homework_Instructions_Resources_hawaii_measurements.csv"

with open(measurement, newline="", encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader,None)

    date = []
    attrs = {}
    temp = []
    temp2 = []
    for value in csvreader:
        attrs[value[1]] = value[2]
        temp.append([value[1], value[3]])
        date.append(value[1])

Max_Date = max(date)
Max_Date2 = str.split(Max_Date, '-')
oneyear = dt.date(int(Max_Date2[0]), int(Max_Date2[1]), int(Max_Date2[2])) - dt.timedelta(days = 365)

for i in temp:
    if i[0] >= str(oneyear): 
        temp2.append(i)

station = "10_advanced_data_storage_and_retrieval_homework_Instructions_Resources_hawaii_stations.csv"

with open(station, newline="", encoding="UTF-8") as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter=",")
    next(csvreader2,None)

    sttn = []
    for value in csvreader2:
        sttn.append(value[0])

app = Flask(__name__)

@app.route("/")
def home():
    return(f"Welcome to my API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end"
    )
    
@app.route("/api/v1.0/precipitation")
def precipitation():
    return jsonify(attrs)

@app.route("/api/v1.0/stations")
def stations():
    return jsonify(sttn)

@app.route("/api/v1.0/tobs")
def tobs():
    return jsonify(temp2)

@app.route("/api/v1.0/<start>")
def calc_temps_short(start):

    sDate = str.split(start, '-')
    sDate2 = dt.date(int(sDate[0]), int(sDate[1]), int(sDate[2]))
    Max_Date = max(date)
    Max_Date2 = str.split(Max_Date, '-')
    eDate2 = dt.date(int(Max_Date2[0]), int(Max_Date2[1]), int(Max_Date2[2]))

    temp2 = []
    for i in temp:
        if i[0] >= str(sDate2) and i[0] <= str(eDate2): 
            temp2.append(i)

    sub_temp = []
    for i in temp2:
        sub_temp.append(int(i[1]))

    min_temp = min(sub_temp)
    mean_temp = sum(sub_temp)/len(sub_temp) 
    max_temp = max(sub_temp)

    return (f"From {start}: <br/>" 
            f"Minium temperature is {min_temp},<br/>" 
            f"Average temperature is {mean_temp},<br/>" 
            f"Maximum temperature is {max_temp}<br/>" 
            f"<br/>"
            f"[{min_temp}, {mean_temp}, {max_temp}]"
            )   
        

@app.route("/api/v1.0/<start>/<end>")
def calc_temps(start, end):

    sDate = str.split(start, '-')
    sDate2 = dt.date(int(sDate[0]), int(sDate[1]), int(sDate[2]))
    eDate = str.split(end, '-')
    eDate2 = dt.date(int(eDate[0]), int(eDate[1]), int(eDate[2]))

    temp2 = []
    for i in temp:
        if i[0] >= str(sDate2) and i[0] <= str(eDate2): 
            temp2.append(i)

    sub_temp = []
    for i in temp2:
        sub_temp.append(int(i[1]))

    min_temp = min(sub_temp)
    mean_temp = sum(sub_temp)/len(sub_temp) 
    max_temp = max(sub_temp)

    return (f"From {start} to {end}:<br/>" 
            f"Minium temperature is {min_temp},<br/>" 
            f"Average temperature is {mean_temp},<br/>" 
            f"Maximum temperature is {max_temp}<br/>" 
            f"<br/>"
            f"[{min_temp}, {mean_temp}, {max_temp}]"
            )
        
if __name__ == "__main__":
    app.run(debug=True)