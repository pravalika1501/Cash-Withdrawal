import threading,time
def bankbalnc (withdrawamt):
  K.acquire()
  global totalbalnc
  K.release()

#main program
K=threading.Lock()
totalbalnc=15000
while(True):
    withdrawamt = (int(input("enter the amount u want u withdraw:")))
    name = input("enter the name of the person:")
    totalbalnc = totalbalnc - withdrawamt
    print("Hi:'{}', {} your amount is withdrawn".format(threading.current_thread().name, withdrawamt))
    time.sleep(1)
    if(totalbalnc<500):
        print("your check is bounced")
        break
    else:
        print("Now Available balance={}".format(totalbalnc))
        print("Thanks for using")

t1=threading.Thread(target=bankbalnc, args=(withdrawamt,))
t1.name=threading.Thread(target=bankbalnc,args=(name,))

#t2=threading.Thread(target=bankbalnc, args=(withdrawamt,))
#t2.name=threading.Thread(target=bankbalnc,args=(name,))

#t3=threading.Thread(target=bankbalnc, args=(withdrawamt,))
#t3.name=threading.Thread(target=bankbalnc,args=(name,))


t1.start()
#t2.start()
#t3.start()
