import time
from plyer import notification

if __name__=='__main__':
    while True:
        notification.notify(
            title='YO BOY , HAVE SOME WATER NOW !',
            message='An adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids a day for men',
            timeout=10,
            app_icon="icon.ICO"

        ) 
        time.sleep(60*60)