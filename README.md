# 🔐 Python Password Cracker

A command-line dictionary attack password cracker built in Python.  
This project was built for educational purposes to understand how hashing works and why weak passwords are vulnerable.

---

## How It Works

When websites store passwords, they don't store the plain text — they store a **hash** of it. A hash is a one-way fingerprint of a string:

```
"password" → MD5 → 5f4dcc3b5aa765d61d8327deb882cf99
```

Since hashing is one-way (irreversible), the only way to crack a hash is to **guess**. This tool uses a **dictionary attack** — it takes a wordlist of common passwords, hashes each one, and compares it to the target hash. If they match, the original password is found.

### Supported Algorithms
| Algorithm | Hash Length | Notes |
|-----------|-------------|-------|
| MD5       | 32 chars    | Fast, widely used, considered weak |
| SHA-1     | 40 chars    | Stronger than MD5, still vulnerable |
| SHA-256   | 64 chars    | Modern, significantly more secure |

### Project Structure
```
password-cracker/
├── password_cracker.py   # Main script
├── wordlist.txt          # Sample wordlist for testing
├── .gitignore
├── LICENSE               # MIT
└── README.md
```

---

## Example Output

### Password Found ✅
```
=============================================
        Python Password Cracker
        For Educational Use Only
=============================================

Enter the target hash to crack : 5f4dcc3b5aa765d61d8327deb882cf99
Enter the algorithm (md5, sha1, sha256) : md5
Enter wordlist filename (default: wordlist.txt) :

[*] Target Hash  : 5f4dcc3b5aa765d61d8327deb882cf99
[*] Algorithm    : MD5
[*] Wordlist     : wordlist.txt
[*] Starting attack...

[+] Password Found  : password
[+] Attempts Made   : 6
[+] Time Taken      : 0.00 seconds
```

### Password Not Found ❌
```
[-] Password not found in wordlist.
[-] Attempts Made   : 10
[-] Time Taken      : 0.00 seconds
```

---

## ⚠️ Disclaimer & Ethical Use

This tool was built **strictly for educational purposes** to demonstrate:
- How password hashing works
- Why weak or common passwords are vulnerable
- How dictionary attacks are performed in controlled environments

**Only use this tool on hashes you own or have explicit permission to test.**  
Unauthorised use against real systems or accounts is illegal and unethical.  
The author takes no responsibility for misuse of this tool.

---

## What I Learned Building This

- How hashing algorithms work (MD5, SHA-1, SHA-256)
- Why passwords should never be stored in plain text
- How dictionary attacks exploit weak password choices
- Why salting and strong hashing algorithms (bcrypt, Argon2) exist as defences
- Python concepts: functions, file I/O, string manipulation, control flow, timing

---

*Built as part of a personal cybersecurity learning portfolio.*
