import time


def loading_bar(ready,whole=100):
    finished = round(10 * ready / whole)
    in_progress = 10 - finished
    
    finished_text = "#" * finished
    in_progress_text = "_"*in_progress

    print(f"\r[{finished_text}{in_progress_text}]",end=" ")


for i in range(100):
    loading_bar(i, 100)
    time.sleep(0.1)
    pass
