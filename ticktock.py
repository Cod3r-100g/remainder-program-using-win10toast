import win10toast
import time
toaster = win10toast.ToastNotifier()
def msg():
    toaster.show_toast("TickTock! - Let it happen Again","Stand up + Drink Water +Smile",icon_path="C:\\Users\\sog\\Documents\\Atom Project\\Remainder\icon.ico")

while True:
    msg()
    time.sleep(60*60)
