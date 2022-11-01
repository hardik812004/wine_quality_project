import tkinter as ttk
import pandas as pd

model = pd.read_pickle("Wine_Quality_Prediction.pickle")
cols= model.feature_names_in_

app=ttk.Tk()
app.geometry("350x350")
app.title("Wine Quality Predictor")

#Alcohol
alcohol = ttk.Variable(app)
ttk.Label(app,text="Alcohol",padx=15,pady=15).grid(row=0,column=0)
ttk.Entry(app, textvariable=alcohol, width=10).grid(row=0, column=1)

#Volatile Acidity
volatile= ttk.Variable(app)
ttk.Label(app, text='Volatile Acidity',padx=15,pady=15).grid(row=1,column=0)
ttk.Entry(app, textvariable=volatile, width=10).grid(row=1, column=1)

#Sulphates
sulphates = ttk.Variable(app)
ttk.Label(app, text='Sulphates',padx=15,pady=15).grid(row=2,column=0)
ttk.Entry(app, textvariable=sulphates, width=10).grid(row=2, column=1)

#Citric Acid
citric = ttk.Variable(app)
ttk.Label(app, text='Citric Acid',padx=15,pady=15).grid(row=3,column=0)
ttk.Entry(app, textvariable=citric, width=10).grid(row=3, column=1)



#Prediction Button 
def find_quality():
    global model
    values = [[alcohol.get()],[volatile.get()],[sulphates.get()],[citric.get()]]
    cols = model.feature_names_in_
    query_df = pd.DataFrame(dict(zip(cols,values)))
    quality = model.predict(query_df)
    if quality[0] == 1:
        result.set("GOOD QUALITY!")
    else:
        result.set('BAD QUALITY')

ttk.Button(app, text='Predict', command=find_quality,font=('Arial',20)).grid(row=4,column=0,columnspan=2)

#Result
result = ttk.Variable(app)
result.set('0')
ttk.Label(app, textvariable=result, pady=15, font=('Arial',20)).grid(row=5,column=0,columnspan=2)

app.mainloop()