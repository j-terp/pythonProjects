import csv
SETTINGS = (
    ("s","stop","0"),   #DEFAULT
    ("w","write","1"),
    ("r","read","2"),
    ("e","exit","3")
)
user_setting = input("Write, Read or Exit? [W/R/E]\n").lower()
for setting_lst in SETTINGS:
    for variation in setting_lst:
        if variation == user_setting:
            user_setting = SETTINGS.index(setting_lst)
if user_setting == 1:
    #write
    print("Writing")
elif user_setting == 2:
    #read
    print("Reading")
elif user_setting == 3:
    #exit
    print("Exiting")
else:
    #stop
    print("Stopping")
