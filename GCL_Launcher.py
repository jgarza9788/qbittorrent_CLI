import os,time


dir = os.path.dirname(__file__)

print(os.path.join(dir,'getCurrentList.cmd'))
os.startfile(os.path.join(dir,'getCurrentList.cmd'))
time.sleep(10)
exit()