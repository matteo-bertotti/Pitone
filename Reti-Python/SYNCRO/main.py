import mythread
import time

# Alloco un po' di oggetti e li avvio
t1 = mythread.MyThread(1)
t2 = mythread.MyThread(2)
t3 = mythread.MyThread(3)
t4 = mythread.MyThread(4)
t5 = mythread.MyThread(5)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()

# Per attendere la morte dei thread uso il JOIN
t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
