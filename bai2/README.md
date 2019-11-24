##Bài tập 2 môn Truyền thông đa phương tiện
#####Thành viên phụ trách: Phạm Văn Trọng - MSV 16021198

**Đề bài:** 
Hãy sinh ra các file wave (âm thanh) tương ứng với các nốt nhạc trong một quãng tám (octave)
- Nốt chuẩn là nốt La tương ứng với tần số 440Hz.
- Hai nốt cách nhau 1 quãng tám có tần số gấp đôi nhau. Ví dụ nốt Lá có tần số 2*440Hz = 880Hz
- Trong một quãng tám có 12 nốt: Đồ - Đồ# - Rê - Mi - Fa - Fa# - Son - Son# - La - Si - Si# - Đô
Hai nốt liên tục có tỉ số tần số là 1.059463 (căn bậc 12 của 2). Ví dụ nốt Si có tần số 1.059463 * 440Hz = 466.16 Hz

Yêu cầu: Cần viết 02 chương trình: Generator và Player. Chạy chương trình Generator sinh ra 12 file âm thanh (wav file) tương ứng với 12 nốt nhạc. Chạy chương trình Player với tham số là tên file wav sẽ chơi file wav đó kéo dài, lặp đi lặp lại.

**Hướng dẫn chạy chương trình:**
1. Chương trình sử dụng 3 thư viện là _**numpy**_, **_scipy_** và **_playsound_**. Để cài đặt, chạy:
    
    ```pip3 install -r requirements.txt```
    
   
2. Để tạo 13 file cho 1 quãng tám, chạy:
    
     ```python3 generator.py```

3. Xem hướng dẫn play:

    ```python3 player.py -h```

4. Play 1 file:
    
    ```python3 player.py -i <tên file>```
    
    Ví dụ: python3 player.py -i 0.wav (các file đánh số từ 0 -> 12)
    
5. Play tất cả 13 file:

    ```python3 player.py -a```
