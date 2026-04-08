import tkinter as tk
from tkinter import messagebox, ttk
from planner import find_route_with_penalty, load_data

# Load initial data
data = load_data()
STOPS = sorted(data['stops'])

def calculate():
    start = start_var.get()
    end = end_var.get()
    
    if start == end:
        messagebox.showwarning("Input Error", "Start and End locations must be different.")
        return

    # Call the logic from your previous planner.py
    cost, path = find_route_with_penalty(data, start, end)
    
    if path:
        result_label.config(text=f"Total Time: {cost} mins", fg="#2ecc71")
        path_label.config(text=f"Route: {' → '.join(path)}")
    else:
        result_label.config(text="No route found.", fg="#e74c3c")

# Initialize Window
root = tk.Tk()
root.title("Smart Transit Planner")
root.geometry("400x450")
root.configure(padx=20, pady=20)

# UI Elements
tk.Label(root, text="Transit Route Optimizer", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Select Start:").pack(anchor="w")
start_var = tk.StringVar(value=STOPS[0])
start_menu = ttk.Combobox(root, textvariable=start_var, values=STOPS, state="readonly")
start_menu.pack(fill="x", pady=5)

tk.Label(root, text="Select Destination:").pack(anchor="w")
end_var = tk.StringVar(value=STOPS[-1])
end_menu = ttk.Combobox(root, textvariable=end_var, values=STOPS, state="readonly")
end_menu.pack(fill="x", pady=5)

btn = tk.Button(root, text="Find Best Route", command=calculate, bg="#3498db", fg="white", font=("Arial", 10, "bold"))
btn.pack(pady=20, fill="x")

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

path_label = tk.Label(root, text="", wraplength=350, justify="center")
path_label.pack(pady=10)

root.mainloop()