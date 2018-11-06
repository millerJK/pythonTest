try:
    print("---")
    10/0
    print("----------")
except ZeroDivisionError as  e:
    print("except: ",e)
finally:
    print("final....")