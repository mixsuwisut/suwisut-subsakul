import math

def calculate_current(voltage=None, resistance=None, power=None):
    try:
        if voltage is not None and resistance is not None:
            current = voltage / resistance
        elif power is not None and voltage is not None:
            current = power / voltage
        elif power is not None and resistance is not None:
            current = math.sqrt(power / resistance)
        else:
            print("ข้อผิดพลาด: กรุณาป้อนค่าที่เพียงพอสำหรับการคำนวณ")
            return
        
        print(f"กระแสไฟฟ้า (I) = {current:.2f} แอมแปร์")
    except ValueError:
        print("ข้อผิดพลาด: กรุณาป้อนค่าตัวเลขที่ถูกต้อง")

# รับค่าจากผู้ใช้
print("=== โปรแกรมคำนวณกระแสไฟฟ้า (I) ===")
try:
    voltage = input("ป้อนแรงดันไฟฟ้า (V) หรือเว้นว่างไว้: ")
    resistance = input("ป้อนความต้านทาน (R) หรือเว้นว่างไว้: ")
    power = input("ป้อนกำลังไฟฟ้า (P) หรือเว้นว่างไว้: ")

    voltage = float(voltage) if voltage else None
    resistance = float(resistance) if resistance else None
    power = float(power) if power else None

    calculate_current(voltage, resistance, power)

except ValueError:
    print("ข้อผิดพลาด: กรุณาป้อนค่าตัวเลขที่ถูกต้อง")