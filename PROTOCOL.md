```auth [username] [password]``` 
- tujuan: autentikasi pengguna terdaftar  
- username: username yang digunakan pengguna - password: password yang digunakan pengguna

```register [username] [password] [name] [country]``` 
- register: mendaftarkan data pengguna 
- username: username yang digunakan pengguna 
- password: password yang digunakan pengguna - name: nama pengguna - country: negara pengguna
- logout - logout: untuk keluar dari akun atau aplikasi - parameter : tidak ada

```sendprivate [receiver] [message] ```
- sendprivate: mengirimkan pesan secara privat 
- receiver: nama penerima 
- message: pesan yang dikirimkan

```sendprivatefile [receiver] [filepath]``` 
- sendprivatefile: mengirimkan file secara privat 
- receiver: nama penerima - filepath: lokasi file yang ingin dikirim

```sendgroup [group_receiver] [message]```
- sendgroup: mengirimkan pesan ke banyak orang 
- group_receiver: group penerima pesan 
- message: pesan yang dikirimkan

```sendgroupfile [group_receiver] [message]``` 
- sendroupfile: mengirimkan file ke banyak orang 
- group_receiver: group penerima pesan 
- message: pesan yang akan dikirimkan

 ```inbox``` 
- inbox: pesan yang didapatkan 
- parameter: tidak ada

```addrealm [realm_id] [realm_address_to] [realm_port_to]```
- addrealm: untuk menambahkan realm baru 
- realm_id: id dari realm 
- realm_address_to: ip address dari realm yang ingin disambungkan 
- realm_port_to: port dari realm yang ingin disambungkan

```sendprivaterealm [realm_id] [receiver] [message]```
- sendprivaterealm: mengirimkan pesan ke realm lain yang telah tersambung atau ditambahkan 
- realm_id: id dari realm 
- receiver: penerima pesan yang dikirim 
- message: pesan yang akan dikirimkan

```sendprivatefilerealm [realm_id] [receiver] [filepath]```
- sendprivatefilerealm: mengirimkan file ke realm yang telah tersambung atau ditambahkan 
- realm_id: id dari realm 
- receiver: penerima file yang dikirim 
- filepath: lokasi file yang mau dikirimkan

```sendgrouprealm [realm_id] [group_receiver] [message]``` 
- sendgrouprealm: mengirimkan pesan ke beberapa user dalam satu realm 
- realm_id: id dari realm 
- group_receiver: penerima pesan yang dikirim

```sendgroupfilerealm [realm_id] [group_receiver] [filepath]```
- sendgroupfilerealm: mengirimkan file ke beberapa user dalam satu realm 
- realm_id: id dari realm 
- group_receiver: penerima file yang dikirim 
- - filepath: lokasi file yang ingin dikirimkan

```inboxrealm [realm_id]```
- inboxrealm: pesan yang didapatkan 
- realm_id: id dari realm

```login_info``` 
- login_info: melihat info dari user yang aktif 
- parameter : tidak ada
