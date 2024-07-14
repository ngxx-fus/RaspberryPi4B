from MFRC522 import MFRC522
from OLED_32x128_lib import OLED_32x128

my_reader = MFRC522() 
my_oled   = OLED_32x128(based_canvas='black')

if __name__ == "__main__":
    my_oled.start()
    my_oled.add_text(text="Card connecting!", pos=(0, 0), size=15)
    
    while True:
        my_reader.Init()
        (status, TagType) = my_reader.Request(my_reader.PICC_REQIDL)
        print(status)
        if status == my_reader.MI_OK:
            print("Connection Success!")
            my_oled.add_text(text="Card connected!", pos=(0, 0), size=15)
            my_oled.display()
        my_oled.clear()
        my_oled.add_text(text="Card connecting!", pos=(0, 0), size=15)


































# from mfrc522 import SimpleMFRC522
# import RPi.GPIO as GPIO
# GPIO.setwarnings(False)
# reader = SimpleMFRC522()

# while True:
#     print("reading...")
#     id, text = reader.read()
#     print(f"ID: {id}")
#     print(f"Text: {text}")
#     if text == "write_new?":
#         print("writing...")
#         text = "hello_world"
#         id, text_written = reader.write(text)
#         print(f"ID: {id}")
#         print(f"Text Written: {text_written}")