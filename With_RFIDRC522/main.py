from MFRC522 import MFRC522
from OLED_32x128_lib import OLED_32x128
import time

my_reader = MFRC522() 
my_oled   = OLED_32x128(based_canvas='black')



if __name__ == "__main__":
    my_oled.start()
    my_oled.add_text(text="WAITING...", pos=(0, 0), size=15)

    while True:
        my_reader.Init()
#        my_oled.clear()
#        my_oled.add_text(text="Waiting...", pos=(0, 0), size=15)

        (status, TagType) = my_reader.Request(my_reader.PICC_REQIDL)
        if status == my_reader.MI_OK:
            my_oled.clear()
            print("Connection Success!")
            my_oled.add_text(text="CONNECTED!", pos=(0, 0), size=15)
            my_oled.display()
        else:
            continue

        #read UID from Tag/Card
        my_oled.add_text(text="READING UID...", pos=(0, 0), size=15)
        UID = ''
        (status, uid) = my_reader.Anticoll()
        if status == my_reader.MI_OK:
            for ch in uid:
                UID += str(hex(ch))[2:]
            print(UID)
            my_oled.clear()
            my_oled.add_text(text="UID:\n", pos=(0, 0), size=13, save_curr=True)
            my_oled.add_text(text=UID, pos=(0, 13), size=15,load_prev=True)
            time.sleep(1)

        # select Tag/Card
        my_reader.SelectTag(uid)

        # auth Tag/Card
        trailer_block = 11
        # this is the default key for MIFARE Cards
        default_key = [0xFF, 0xFF, 0xFF , 0xFF, 0xFF, 0xFF]
        status = my_reader.Authenticate(my_reader.PICC_AUTHENT1A, trailer_block , default_key, uid)
        if status  == my_reader.MI_OK:
            status = "MI_OK"
        elif status == my_reader.MI_NOTAGERR:
            status = "MI_NOTAGERR"
        else:
            status = "MI_ERR"
        my_oled.add_text(text=f"AUTHENTICATED:", pos=(0, 0), size=14, save_curr=True)
        my_oled.add_text(text=f"{status}", pos=(0, 14), size=15, load_prev=True)
        time.sleep(1)
        if status != "MI_OK":
            continue

        # read data from card
        my_oled.add_text(text="READING CARD...", pos=(0, 0), size=15)
        content = '' 
        block_nums = [8, 9, 10]
        data = []
        for block_num in block_nums:
            block_data = my_reader.ReadTag(block_num)
            if block_data:
                data += block_data
        if data:
            for ch in data:
                content += chr(ch)
            print(f"Content: {content}")
            my_oled.clear()
            my_oled.add_text(text="CONTENT:", pos=(0,0), size=15)
            time.sleep(0.5)
            my_oled.add_text(text=content, pos=(0, 0), size=13, save_curr=True)
            my_oled.add_text(text="READ DONE!", pos=(0, 15), size=13, load_prev=True)
            time.sleep(2)
        else:
            my_oled.add_text(text="READING ERR!", pos=(0,0), size=15)
            time.sleep(0.5)
            my_reader.StopAuth()
            continue

        write_flag = False
        if write_flag == True:
            # write card
            my_oled.add_text(text="WRITING CARD...", pos=(0, 0), size=15)
            new_content = "Hello ngxxfus!"
            my_oled.add_text(text=f"\'{new_content}\'", pos=(0, 16), size=15, save_cur=True)
            data = bytearray()
            data.extend(bytearray(new_content.ljust(  len(block_nums)  *  16).encode('ascii')))
            i = 0
            for block_num in block_nums:
                my_reader.WriteTag(block_num, data[(i*16):(i+1)*16]) 
                i +=  1
            my_oled.add_text(text="WRITTEN CARD...", pos=(0, 0), size=15)
        #free Tag/Card
        my_reader.StopAuth()
    # close SPI and Card
    my_reader.Close()













