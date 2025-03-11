# print("******************* MAINTENANCE SYSTEM*****************************")


# device_id = int(input("Enter the device id:    "))
# power_level = int(input("Enter the power level:    "))

# if power_level <= 89:
#     print(f"This device {device_id} is not ready")
# else:
#     print(f"This device {device_id} is ready to go🚚✅")
    


# for i in range(10):
#     print(i)


# power_level = 0

# while power_level <= 100:
#     print(f"Power level {power_level}")
#     power_level +=10
    


power_level = 0

while power_level <= 150:
    print(f"Power level {power_level}")
    if power_level == 20:
        continue
    if power_level == 30:
        pass
    if power_level == 40:
        break
    if power_level <=99:
        print(f"This device is ready to go")
    elif power_level == 100:
        print("Battery is full")
    
    power_level +=1
