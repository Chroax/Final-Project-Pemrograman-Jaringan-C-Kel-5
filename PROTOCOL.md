### Autentikasi
```auth [username] [password]``` 
- Tujuan : autentikasi pengguna terdaftar
- Parameter :
  - username: username yang digunakan pengguna 
  -  password: password yang digunakan pengguna

### Register
```register [username] [password] [name] [country]``` 
- Tujuan : mendaftarkan data pengguna 
- Parameter :
  - username : username yang digunakan pengguna 
  - password : password yang digunakan pengguna 
  - name : nama pengguna 
  - country : negara pengguna

### Log Out
```logout``` 
- Tujuan : untuk keluar dari akun atau aplikasi 
- Parameter : tidak ada

### Send Private
```sendprivate [receiver] [message] ```
- Tujuan : mengirimkan pesan secara privat
- Parameter : 
  - receiver: nama penerima 
  - message: pesan yang dikirimkan

### Send Private File
```sendprivatefile [receiver] [filepath]``` 
- Tujuan : mengirimkan file secara privat
- Parameter : 
  - receiver: nama penerima 
  - filepath: lokasi file yang ingin dikirim

### Send Group
```sendgroup [group_receiver] [message]```
- Tujuan : mengirimkan pesan ke banyak orang
- Parameter : 
  - group_receiver: group penerima pesan 
  - message: pesan yang dikirimkan

### Send Group File
```sendgroupfile [group_receiver] [message]``` 
- Tujuan : mengirimkan file ke banyak orang
- Parameter :
  - group_receiver: group penerima pesan 
  - message: pesan yang akan dikirimkan

### Inbox
 ```inbox``` 
- Tujuan: pesan yang didapatkan 
- Parameter: tidak ada

### Add Realm
```addrealm [realm_id] [realm_address_to] [realm_port_to]```
- Tujuan : untuk menambahkan realm baru 
- Parameter :
  - realm_id: id dari realm 
  - realm_address_to: ip address dari realm yang ingin disambungkan 
  - realm_port_to: port dari realm yang ingin disambungkan

### Send Private Realm
```sendprivaterealm [realm_id] [receiver] [message]```
- Tujuan : mengirimkan pesan ke realm lain yang telah tersambung atau ditambahkan 
- Parameter :
  - realm_id: id dari realm 
  - receiver: penerima pesan yang dikirim 
  - message: pesan yang akan dikirimkan

### Send Private File Realm
```sendprivatefilerealm [realm_id] [receiver] [filepath]```
- Tujuan : mengirimkan file ke realm yang telah tersambung atau ditambahkan 
- Parameter :  
  - realm_id: id dari realm 
  - receiver: penerima file yang dikirim 
  - filepath: lokasi file yang mau dikirimkan

### Send Group Realm
```sendgrouprealm [realm_id] [group_receiver] [message]``` 
- Tujuan: mengirimkan pesan ke beberapa user dalam satu realm 
- Parameter :
  - realm_id: id dari realm 
  - group_receiver: penerima pesan yang dikirim

### Send Group File Realm
```sendgroupfilerealm [realm_id] [group_receiver] [filepath]```
- Tujuan : mengirimkan file ke beberapa user dalam satu realm 
- Parameter :
  - realm_id: id dari realm 
  - group_receiver: penerima file yang dikirim 
  -  filepath: lokasi file yang ingin dikirimkan

### Inbox Realm
```inboxrealm [realm_id]```
- Tujuan : pesan yang didapatkan
- Parameter : 
  - realm_id: id dari realm

### Login Info
```login_info``` 
- Tujuan : melihat info dari user yang aktif 
- Parameter : tidak ada
