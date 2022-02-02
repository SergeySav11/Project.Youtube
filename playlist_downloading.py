from tqdm import tqdm,tqdm_gui,trange
from time import sleep

for i in trange(100,leave =True,mininterval =1,ncols = 100,unit_scale = 10):
    sleep(0.1)

