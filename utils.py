
def calculate_bmi(weight, height):
    return weight / ((height/100)**2)

def bmi_category(bmi):
    if bmi<18.5: return "Төмен","blue"
    elif bmi<25: return "Қалыпты","green"
    elif bmi<30: return "Артық","orange"
    else: return "Семіздік","red"

def water_intake(weight):
    return weight*30

def calories_needed(weight):
    return weight*30

def ideal_weight(height,age):
    return round((height-100)*0.9,1)
