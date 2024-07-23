# Test PiCamera2
## Sơ đồ khối:
<br>
<img src="https://github.com/user-attachments/assets/fa7d6360-516e-4966-bd7b-f9053fd0b0ed" width="501">
<br>

## Mô tả:
Raspberry Pi 4:

|  |  |
| :--: | :-- |
| testPiCamera.py | Sử dụng thư viện **picamera2**, chụp ảnh và lưu local thành test.jpg mỗi 250ms, sau đó gọi chương trình SendBack.sh. |
| SendBack.sh | Sử dụng **scp** gởi đến máy tính cá nhân chạy Ubuntu đã bật ssh-server và lưu tại **~/Downloads/**. |

Computer:

|  |  |
| :--: | :-- |
| ShowImg.sh | Sử dụng **eog** để mở ảnh lưu tại **~/Downloads/** mỗi 250ms. |

<br>
<div style="page-break-after: always;"></div>
<br>

# Install Anaconda on Raspberry Pi 4 B+
## References link list:
    https://github.com/conda-forge/miniforge 

Sử dụng wget để tải Miniforge3-Linux-aarch64.sh
<br>
<img src="https://github.com/user-attachments/assets/f964ed7c-b5b9-40d0-a98a-91269b832fdf" width="501">
<br>

Chạy file Miniforge3-Linux-aarch64.sh
<br>
<img src="https://github.com/user-attachments/assets/dffb8bb9-938b-4cae-a23a-8e6e3d9ebafc" width="501">
<br>
NOTE: ở bước đọc giấy phép, nhấn q để hoàn thành viện đọc giấy phép.


Chấp nhận điều khoảng, chọn nơi lưu mã nguồn (đường dẫn cài đặt) mặc định là /home/<username>/miniforge3 nếu dùng đường dẫn mặc định này thì nhấn enter. (Trong hình, username là msnp) 
<br>
<img src="https://github.com/user-attachments/assets/3e591e50-7b1d-4976-a0f8-ffc4dd7aadc1" width="501">
<br>
Hoàn tất cài đặt
<br>
<img src="https://github.com/user-attachments/assets/4d6fddee-3df9-4c5f-897f-ccc0611d3d2f" width="501">
<br>
Trong trường hợp vẫn chưa sử dụng được lệnh “conda” thì: truy cập vào đường dẫn cài đặt  /home/<username>/miniforge3/bin/, “bin” là thư mục chứ tệp tin thực thi “conda” sau đó chạy local “conda” với parameter init.
<br>
<img src="https://github.com/user-attachments/assets/733a291b-9744-4d99-ae0d-6f925629b077" width="501">
<br>

# Install lib picamera2 on Raspberry Pi 4 B+
Hướng dẫn chính thức, nếu làm theo hướng dẫn không được, thì thử cách bên dưới:

    https://github.com/raspberrypi/picamera2
    https://datasheets.raspberrypi.com/camera/picamera2-manual.pdf

Mình khuyến nghị thực thi các lệnh sau:

    sudo apt install -y python3-libcamera python3-kms++
    sudo apt install -y python3-pyqt5 python3-prctl libatlas-base-dev ffmpeg python3-pip
    pip3 install numpy --upgrade
    pip3 install picamera2[gui]

Phòng khi không cài được nhưng vẫn đủ thư viện cho các bước sau! Trường hợp lỗi và ta sẽ cài thủ công với các thao thác bên dưới. Kiểm tra phiên bản hiện tại của python3 (global):
<br>
<img src="https://github.com/user-attachments/assets/3a44abd8-81ed-4d14-81d7-4c56282b8e39" width="501">
<br>
Sau đó tạo một môi trường ão cùng phiên bản bằng conda (hình bên dưới đặt tên môi trường này là “python3.11”:
<br>
<img src="https://github.com/user-attachments/assets/aa170209-ee86-498d-8529-66ef807a867c" width="501">
<br>
Hoàn tất cài đặt:
<br>
<img src="https://github.com/user-attachments/assets/11eec511-73f5-481a-aa31-f017236e7c67" width="501">
<br>
Sau đó kích hoạt môi trường python3.11:
<br>
<img src="https://github.com/user-attachments/assets/f16fcaca-5673-420d-8ff5-d3467e4d876a" width="501">
<br>
Truy cập repo của picamera2 tại, clone về ~/Downloads, truy cập vào thư mục vừa clone, và cài đặt thư viện:

        https://github.com/raspberrypi/picamera2

<br>
<img src="https://github.com/user-attachments/assets/d9acdb17-7c8b-41c8-a519-1e61ee9ffb3f" width="501">
<br>
Lúc này ta tiến hành thử xem đã dùng được thư viện picamera2 hay chưa. Trường hợp thành công sẽ không báo lỗi gì:
<br>
<img src="https://github.com/user-attachments/assets/f233a571-bd42-43e9-a05b-bf90fdf03289" width="501">
<br>
Trường hợp không thành công sẽ báo thiếu thư viện, với trường hợp trong bài viết này gặp thì là báo thiếu thư viện kms và libcamera (hình bên dưới báo thiế pykms - nếu không mất trí bạn sẽ nhớ ở trang github picamera2 có một lệnh là “sudo apt install -y python3-libcamera python3-kms++”, lệnh này cài với quyền root hai thư viện là libcamera và kms, vì thế ta chỉ cần copy vào môi trường ảo - và đó cũng là lý do từ đầu yêu cầu môi trường ảo có cùng phiên bản với global!).  
<br>
<img src="https://github.com/user-attachments/assets/33b058f8-42ac-4990-a0c7-f4482fc3dfee" width="501">
<br>
Đối với thiếu module, đầu tiên bận cần làm là thử với pip install <tên module> trước khi làm các bước khác. Trong trường hợp bất khả kháng:Như vầy thì bạn phải tìm cách khác, bên dưới bài viết gợi ý cách bài viết đã làm thành công!
<br>
<img src="https://github.com/user-attachments/assets/bf7d5f98-1a90-4d81-800e-24b8294c410f" width="501">
<br>
Trước khi tiếp tục, cần kiểm tra với sudo, khi import picamera2 có lỗi không, nếu không có lỗi ta tiếp tục, nếu có thì mình bó tay!
<br>
<img src="https://github.com/user-attachments/assets/70c67ef4-85b5-4d22-b320-8abe39d746d3" width="501">
<br>
Nếu không lỗi, ta tiến hành cp -r các module thiếu vào trong môi trường ảo. Đường dẫn global của chúng chứa ở /usr/lib/ yêu cầu quyền root để thực thi, thứ hai là global k cho phép dùng pip để install lung tung. Việc tìm ra vị trí lưu của các thư viện đó ta có thể thông qua nhiều cách, đơn giản nhất là tra Google về vị trí lưu! Ngoài ra, tìm bằng phương thức print(module.__file__). Hoặc dùng lệnh find <vị trí tìm> -name <”tên file"> để tìm. Sau khi xác định vị trí lưu rồi thì copy module đó vào thư mục. Để nhanh chóng thì bài viết gợi ý hai đường dẫn bạn có thể thử:

Vị trí chứa thư viện khi chạy python3 quyền root
  
    /usr/lib/python3/dist-packages
Vị trí chứa thư viện bạn cần copy vào trong môi trường ảo trên conda.

    /home/msnp/miniforge3/envs/env_name/lib/python_version_name/site-packages
Với

    env_name =  python3.11
    python_version_name = python3.11

**Tóm lại trường hợp bài viết, ta copy hết cái gì trong dist-packages vào site-packages 🙂**
Cuối cùng: Thử import lại và chạy!
