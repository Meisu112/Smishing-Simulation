import subprocess
import webbrowser
import tkinter as tk
from smishing_sender import send_smishing_sms  # smishing_sender.py မှာ function ရှိလို့ import လုပ်ထားတာ

def run_app_py():
    print("Starting app.py server...")
    # app.py ကို background မှာ run (Windows မှာ shell=True recommended)
    subprocess.Popen(["python", "app.py"], shell=True)

def on_send():
    number = phone_entry.get()
    link = link_entry.get()
    send_smishing_sms(number, link)   # Simulate sending SMS (print console)
    run_app_py()                      # Flask app.py ကို run
    webbrowser.open("http://127.0.0.1:5000")  # Browser မှာ localhost ဖွင့်
    result_label.config(text="Simulated SMS sent! Server started and browser opened.")

app = tk.Tk()
app.title("Smishing Simulation")
app.geometry("300x200")

tk.Label(app, text="Phone Number:").pack(pady=(10, 0))
phone_entry = tk.Entry(app)
phone_entry.pack()

tk.Label(app, text="Fake Link:").pack(pady=(10, 0))
link_entry = tk.Entry(app)
link_entry.insert(0, "http://127.0.0.1:5000/sms")
link_entry.pack()

tk.Button(app, text="Send SMS", command=on_send).pack(pady=15)

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
