print('''
.______   .___  ___.  __       ______     ___       __        ______  __    __   __          ___   .___________. ______   .______      
|   _  \  |   \/   | |  |     /      |   /   \     |  |      /      ||  |  |  | |  |        /   \  |           |/  __  \  |   _  \     
|  |_)  | |  \  /  | |  |    |  ,----'  /  ^  \    |  |     |  ,----'|  |  |  | |  |       /  ^  \ `---|  |----|  |  |  | |  |_)  |    
|   _  <  |  |\/|  | |  |    |  |      /  /_\  \   |  |     |  |     |  |  |  | |  |      /  /_\  \    |  |    |  |  |  | |      /     
|  |_)  | |  |  |  | |  |    |  `----./  _____  \  |  `----.|  `----.|  `--'  | |  `----./  _____  \   |  |    |  `--'  | |  |\  \----.
|______/  |__|  |__| |__|     \______/__/     \__\ |_______| \______| \______/  |_______/__/     \__\  |__|     \______/  | _| `._____|
                                                                                                                            
''')

print('Welcome to BMI Calculator!!')

#inputs for height and weight
height = float(input('Enter your height in m: '))
weight = float(input('Enter your weight in kg: '))

#calculating height and weight
BMI = weight / (height * height)

#if statement

if BMI < 18.5:
    print("Your are under weighted !")
elif BMI > 18.5 and BMI < 25:
    print("Your are normal weighted!")
elif BMI > 25 and BMI < 30:
    print("Your are over weighted!")
elif BMI > 30 and BMI < 35:
    print("Your are obese!")
else:
    print("Your are clinically obese!")



