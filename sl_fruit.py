import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
import tkinter as tk
from tkinter import ttk, PhotoImage


# ---------- Load Excel Data ----------
df = pd.read_excel("fruit.xlsx")  # Make sure this file exists

# Map categorical data
color_map = {"Red": 1, "Yellow": 2, "Orange": 3, "Green": 4}
size_map = {"Small": 1, "Medium": 2, "Large": 3}

df['ColorCode'] = df['Color'].map(color_map)
df['SizeCode'] = df['Size'].map(size_map)

# Features and labels
X = df[['ColorCode', 'Sweetness', 'Acidity', 'SizeCode']]
y = df['Fruit']

# Train KNN
model = KNeighborsClassifier(n_neighbors=1)
model.fit(X, y)

# ---------- Tkinter GUI ----------
root = tk.Tk()
root.title("SL- Guess the Fruit!")

# ---------- Window Icon and bg ----------
icon = PhotoImage(file="fruit_basket.png")
root.iconphoto(False, icon)
root.configure(bg="#F59127")  



# ---------- Tkinter Variables ----------
color_var = tk.StringVar(value="Red")
sweetness_var = tk.StringVar(value="7")
acidity_var = tk.StringVar(value="4")
size_var = tk.StringVar(value="Medium")
result_var = tk.StringVar(value="")

# ---------- Prediction Function ----------
def predict_fruit():
    try:
        features = [[color_map[color_var.get()],
                     int(sweetness_var.get()),
                     int(acidity_var.get()),
                     size_map[size_var.get()]]]
        prediction = model.predict(features)
        result_var.set(f"Predicted fruit: {prediction[0]}")
    except Exception as e:
        result_var.set("Error: please check your inputs")

# ---------- Center Frame ----------
frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)

# ---------- Layout: Labels & Inputs ----------
ttk.Label(frame, text="Color", font=("Impact", 16)).grid(row=0, column=0, pady=5, sticky="e")
ttk.Combobox(frame, textvariable=color_var, values=list(color_map.keys()), state="readonly").grid(row=0, column=1, pady=5, sticky="w")

ttk.Label(frame, text="Sweetness (1-10)", font=("Impact", 16)).grid(row=1, column=0, pady=5, sticky="e")
ttk.Entry(frame, textvariable=sweetness_var).grid(row=1, column=1, pady=5, sticky="w")

ttk.Label(frame, text="Acidity (1-10)", font=("Impact", 16)).grid(row=2, column=0, pady=5, sticky="e")
ttk.Entry(frame, textvariable=acidity_var).grid(row=2, column=1, pady=5, sticky="w")

ttk.Label(frame, text="Size", font=("Impact", 16)).grid(row=3, column=0, pady=5, sticky="e")
ttk.Combobox(frame, textvariable=size_var, values=list(size_map.keys()), state="readonly").grid(row=3, column=1, pady=5, sticky="w")

# ---------- Predict Button ----------
style = ttk.Style()
style.configure("Impact.TButton", font=("Impact", 14))
ttk.Button(frame, text="Predict", command=predict_fruit, style="Impact.TButton").grid(row=4, column=0, columnspan=2, pady=10)

# ---------- Result Label ----------
ttk.Label(frame, textvariable=result_var, font=("Impact", 12, "bold")).grid(row=5, column=0, columnspan=2, pady=10)



root.mainloop()
