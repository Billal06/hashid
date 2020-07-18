# HashID
HashID adalah sebuah alat untuk meretas atau membobol hash dengan metode Rainbow Table. HashID dibuat menggunakan bahasa program python.
## Cara install
- Linux
  - apt-get install git
  - git clone https://github.com/Billal06/hashid,git
  - cd hashid
  - python3 hashid.py
- Termux
  - pkg install git python
  - git clone https://github.com/Billal06/hashid.git
  - cd hashid
  - python hashid.py

Setelah install maka akan keluar

```
    _  _          HashID [0.5]
  _| || |_  Simple tool to crack hash
 |_  __  _|
  _| || |_   Author : Billal Fauzan
 |_  __  _|  Version: 0.5
   |_||_|  

Welcome to HashID ~Simple hash cracker~ 

{1.4} HashID is a tool that works to crack hashes, such as: md5, sha1, sha512, etc.
This tool support python 3.x

Commands                   Description
----------                -------------
  -t, --target [hash]      Set target hash
  -w, --wordlist [path]    Set wordlist from files
  -r, --random             Random wordlists
  -g, --gui                Use GUI version
        
Copyright (c) Billal Fauzan. All right reversed

```

## Fitur pada HashID
- Support 16 tipe hash
- Bisa mendeteksi tipe hash
- Support GUI (Masih dikembangkan)
- Cepat
- Bisa menggunakan random wordlist atau wordlist manual
- Mudah digunakan

## Kenapa pakai HashID?
HashID saya buat Open Source supaya bisa dipelajari dan dikembangkan.
## Macam-macam tipe hash
  1. MD4
  2. MD5
  3. Ripemd160
  4. SHA1
  5. SHA3-224
  6. SHA224
  7. Blake2s256
  8. SHA256
  9. Blake2s
  10. MD5-SHA1
  11. SHA384
  12. SHA3-512
  13. Blake2b512
  14. SHA512
  15. Blake2b
  16. Whirlpool

## Tangkapan layar
### Gambar 1
![Gambar 1](https://github.com/Billal06/hashid/blob/master/images/image%201.png?raw=true)
### Gambar 2
![Gambar 2](https://github.com/Billal06/hashid/blob/master/images/image%202.png?raw=true)
### Gambar 3
![Gambar 3](https://github.com/Billal06/hashid/blob/master/images/image%203.png?raw=true)

## License
[MIT](https://choosealicense.com/licenses/mit/)
