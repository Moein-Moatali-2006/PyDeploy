import time
import random

def marriage(name):
    r = random.randint(0, 10)
    time.sleep(r)
    print("End",r)
    
def main():
    for child in ["Mohamad", "Ali", "Qoli", "Alex"]:
        marriage(child)

if __name__ == "__main__":
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()

    total_time = end_time - start_time
    print(total_time)