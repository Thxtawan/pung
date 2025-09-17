#งานAdmin
# รับค่า Username และ Password
username = input("Username: ")
password = input("Password: ")

# ตรวจสอบ Username และ Password
if username == "admin" and password == "Ad13n@23t":
    print("Welcome, admin")
else:
    print("You are not admin")
    
    
    
#งานBMI    
# รับค่าน้ำหนักและส่วนสูง
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

# คำนวณค่า BMI
bmi = weight / (height ** 2)

# แสดงค่าผลลัพธ์ BMI
print(f"BMI = {bmi:.1f}")

# แสดงเกณฑ์วิเคราะห์สุขภาพ
if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <= 24.9:
    print("Normal weight")
elif 25 <= bmi <= 29.9:
    print("Overweight")
else:
    print("Obesity")    
    
    
    


#งานขนาดอก
# รับค่าขนาดหน้าอก (จำนวนเต็ม)
chest_size = int(input("กรุณาใส่ขนาดหน้าอก: "))

# ตรวจสอบขนาดเสื้อ
if chest_size <= 34:
    size = "XS"
elif chest_size <= 36:
    size = "S"
elif chest_size <= 38:
    size = "M"
elif chest_size <= 40:
    size = "L"
else:
    size = "XL"

# แสดงผล
print(f"ขนาดเสื้อโปโลที่เหมาะสมคือ: {size}")



#งานบัตรเครดิต
# รับค่ารายได้
income = float(input("กรุณาใส่รายได้ของคุณ (บาท): "))

# ตรวจสอบประเภทบัตรเครดิต
if income < 15000:
    print("รายได้ต่ำกว่าเกณฑ์ ไม่สามารถทำบัตรเครดิตได้")
elif income < 30000:
    print("รายได้ไม่เพียงพอ วงเงินคุณไม่สามารถทำบัตรได้")
elif 30000 <= income < 40000:
    print("สามารถทำบัตรเงินได้")
elif 40000 <= income < 70000:
    print("สามารถทำบัตรเงินได้")
elif 70000 <= income < 100000:
    print("สามารถทำบัตรทองได้")
else:  # income >= 100000
    print("สามารถทำบัตร Platinum ได้")
    
    
    
 #งานเกรด   
    # รับค่าคะแนนเต็มจำนวนเต็ม
score = int(input("กรุณาใส่คะแนนเต็ม: "))

# กำหนดเกรดตามช่วงคะแนน
if score >= 80:
    grade = "A"
elif 70 <= score <= 79:
    grade = "B"
elif 60 <= score <= 69:
    grade = "C"
elif 50 <= score <= 59:
    grade = "D"
else:
    grade = "F"

# แสดงผลเกรด
print(f"เกรดที่ได้คือ: {grade}")