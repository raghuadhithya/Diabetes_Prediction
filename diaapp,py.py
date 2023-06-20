from tkinter import *
from PIL import Image,ImageTk
import pickle
from tkinter import messagebox
model=pickle.load(open("diabetes.pkl","rb"))

app=Tk()
app.title("my app")
app.geometry("1200x864")
app.configure(background="skyblue")
bg_image=Image.open("dia.png")
test_img=ImageTk.PhotoImage(bg_image)

Glucose=DoubleVar()
BloodPressure=DoubleVar()
SkinThickness=DoubleVar()
Insulin=DoubleVar()
BMI=DoubleVar()
DiabetesPedigreeFunction=DoubleVar()
Age=DoubleVar()


def submit():
    
    Glucoseval=Glucose.get()
    print(Glucoseval)
    BloodPressureval=BloodPressure.get()
    print(BloodPressureval)
    SkinThicknessval=SkinThickness.get()
    print(SkinThicknessval)
    Insulinval=Insulin.get()
    print(Insulinval)
    BMIval=BMI.get()
    print(BMIval)
    DiabetesPedigreeFunctionval=DiabetesPedigreeFunction.get()
    print(DiabetesPedigreeFunctionval)
    Ageval=Age.get()
    print(Ageval)

    
    
    result=model.predict([[Glucoseval,BloodPressureval,SkinThicknessval,Insulinval,BMIval,DiabetesPedigreeFunctionval,Ageval]])
    result_percentage=model.predict_proba([[Glucoseval,BloodPressureval,SkinThicknessval,Insulinval,BMIval,DiabetesPedigreeFunctionval,Ageval]])
#    ans.config(text=str(round(max(result_percentage[0])*100,2))+"% the patient may have diabetes")
#  print(round(max(result_percentage[0])*100,2),"% it is ", result[0])
    #diabetes="{} % it is {}".format(round(max(result_percentage[0])*100,2),result[0])
    #print(prob," % ",result[0])
    if result[0]==1:
        a='have diabetes'
        diabetes="{} % may {}".format(round(max(result_percentage[0])*100,2),a)
        print(diabetes)
    else:
        b='not have diabetes'
        diabetes="{} % may {}".format(round(max(result_percentage[0])*100,2),b)
        print(diabetes)

    ans.configure(text=diabetes)
    
    ent1.delete(first=0,last=END)
    ent2.delete(first=0,last=END)
    ent3.delete(first=0,last=END)
    ent4.delete(first=0,last=END)
    ent5.delete(first=0,last=END)
    ent6.delete(first=0,last=END)
    ent7.delete(first=0,last=END)
    
        
    #else:
        #print("Invalid values")
       
       # ans.configure(text="Invalid values")
        #messagebox.showerror('Invalid Error', 'Error: Enter a valid data!')
        


bg_lb=Label(app,image=test_img)
bg_lb.place(x=0,y=0,relwidth=1,relheight=1)

lb1=Label(app,text="Enter the Glucose_level",font=("Georgia",20),bg="skyblue",fg="#663300")
lb1.grid(row=0,column=0,padx=15,pady=15)
ent1=Entry(app,textvariable=Glucose,font=("Georgia",20))
ent1.grid(row=0,column=2,padx=15,pady=15)


lb2=Label(app,text="Enter the BloodPressure_level",font=("Georgia",20),bg="skyblue",fg="#663300")
lb2.grid(row=1,column=0,padx=15,pady=15)
ent2=Entry(app,textvariable=BloodPressure,font=("Georgia",20))
ent2.grid(row=1,column=2,padx=15,pady=15)



lb3=Label(app,text="Enter the SkinThickness_level",font=("Georgia",20),bg="skyblue",fg="#663300")
lb3.grid(row=2,column=0,padx=15,pady=15)
ent3=Entry(app,textvariable=SkinThickness,font=("Georgia",20))
ent3.grid(row=2,column=2,padx=15,pady=15)

lb4=Label(app,text="Enter the Insulin_level",font=("Georgia",20),bg="skyblue",fg="#663300")
lb4.grid(row=3,column=0,padx=15,pady=15)
ent4=Entry(app,textvariable=Insulin,font=("Georgia",20))
ent4.grid(row=3,column=2,padx=15,pady=15)

lb5=Label(app,text="Enter the BMI_level",font=("Georgia",20),bg="skyblue",fg="#663300")
lb5.grid(row=4,column=0,padx=15,pady=15)
ent5=Entry(app,textvariable=BMI,font=("Georgia",20))
ent5.grid(row=4,column=2,padx=15,pady=15)


lb6=Label(app,text="Enter the DiabetesPedigreeFunction",font=("Georgia",20),bg="skyblue",fg="#663300")
lb6.grid(row=5,column=0,padx=15,pady=15)
ent6=Entry(app,textvariable=DiabetesPedigreeFunction,font=("Georgia",20))
ent6.grid(row=5,column=2,padx=15,pady=15)



lb7=Label(app,text="Enter the Age",font=("Georgia",20),bg="skyblue",fg="#663300")
lb7.grid(row=6,column=0,padx=15,pady=15)
ent7=Entry(app,textvariable=Age,font=("Georgia",20))
ent7.grid(row=6,column=2,padx=15,pady=15)



lb8=Label(app,text="Predicted Diabetes ",font=("Georgia",20),bg="skyblue",fg="#663300")
lb8.grid(row=7,column=0,padx=15,pady=15)
ans=Label(app,font=("Georgia",26),width=25)
ans.grid(row=7,column=2,padx=15,pady=15)




btn1=Button(app,command=submit,text="submit",font=("Georgia",16),bg="green",fg="white",activebackground="red",activeforeground="yellow",width=10,bd=5)
btn1.grid(row=8,column=2,padx=15,pady=15)
app.mainloop()
