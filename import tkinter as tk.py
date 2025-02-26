import tkinter as tk
from tkinter import messagebox
import math

def calculate_current():
    try:
        voltage = entry_voltage.get()
        resistance = entry_resistance.get()
        power = entry_power.get()
        
        voltage = float(voltage) if voltage else None
        resistance = float(resistance) if resistance else None
        power = float(power) if power else None
        
        if voltage is not None and resistance is not None:
            current = voltage / resistance
        elif power is not None and voltage is not None:
            current = power / voltage
        elif power is not None and resistance is not None:
            current = math.sqrt(power / resistance)
        else:
            messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนค่าที่เพียงพอสำหรับการคำนวณ")
            return
        
        label_result.config(text=f"กระแสไฟฟ้า (I) = {current:.2f} แอมแปร์")
    except ValueError:
        messagebox.showerror("ข้อผิดพลาด", "กรุณาป้อนค่าตัวเลขที่ถูกต้อง")

# สร้าง GUI
root = tk.Tk()
root.title("คำนวณกระแสไฟฟ้า")

frame = tk.Frame(root)
frame.pack(pady=20)

# อินพุต
label_voltage = tk.Label(frame, text="แรงดันไฟฟ้า (V):")
label_voltage.grid(row=0, column=0)
entry_voltage = tk.Entry(frame)
entry_voltage.grid(row=0, column=1)

label_resistance = tk.Label(frame, text="ความต้านทาน (R):")
label_resistance.grid(row=1, column=0)
entry_resistance = tk.Entry(frame)
entry_resistance.grid(row=1, column=1)

label_power = tk.Label(frame, text="กำลังไฟฟ้า (P):")
label_power.grid(row=2, column=0)
entry_power = tk.Entry(frame)
entry_power.grid(row=2, column=1)

# ปุ่มคำนวณ
button_calculate = tk.Button(frame, text="คำนวณ", command=calculate_current)
button_calculate.grid(row=3, columnspan=2, pady=10)

# แสดงผลลัพธ์
label_result = tk.Label(root, text="")
label_result.pack()

root.mainloop()
