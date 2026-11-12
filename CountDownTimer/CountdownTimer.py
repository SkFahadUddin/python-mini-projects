#CountDown Timer
import time;


print(f"This is a countdown timer");
print(f"1. Count Backwards  2. Count Forwards");
choice = int(input(f"Enter your choice : "));
if(choice!=1 and choice!=2):
    print(f"Invalid choice");
else:
    if(choice==1):
        num = int(input(f"Enter the time in seconds to count backwards : "));
        if(num<0):
            print(f"Invalid time");
        else:
            for i in range(num, 0, -1):
                seconds=i%60;
                minutes=int((i/60)%60);
                hours=int((i/3600));
                print(f"{hours:02d}:{minutes:02d}:{seconds:02d}");
                time.sleep(1);
        print(f"Time's up!");  
    
    elif(choice==2):
        num = int(input(f"Enter the time in seconds to count forwards : "));
        if(num<0):
            print(f"Invalid time");
        else:
            for i in range(0, num):
                seconds=i%60;
                minutes=int((i/60)%60);
                hours=int((i/3600));
                print(f"{hours:02d}:{minutes:02d}:{seconds:02d}");
                time.sleep(1);
        print(f"Time's up!");  