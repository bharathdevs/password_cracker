import hashlib
import time
import os


# ──────────────────────────────────────────────
# Core Functions
# ──────────────────────────────────────────────

def hash_word(word, hash_type):
    """Hashes a word using the specified algorithm and returns the hex digest."""
    return hashlib.new(hash_type, word.encode()).hexdigest()


def crack_hash(target_hash, hash_type, filename="wordlist.txt"):
    """
    Attempts to crack a hash using a dictionary (wordlist) attack.
    Hashes each word in the wordlist and compares it to the target hash.
    """
    # Check if wordlist file exists before attempting to open it
    if not os.path.exists(filename):
        print(f"[!] Wordlist file '{filename}' not found.")
        return

    print(f"\n[*] Target Hash  : {target_hash}")
    print(f"[*] Algorithm    : {hash_type.upper()}")
    print(f"[*] Wordlist     : {filename}")
    print(f"[*] Starting attack...\n")

    found = False
    attempt_count = 0
    start_time = time.time()  # Start timer

    with open(filename, "r", encoding="utf-8", errors="ignore") as file:
        contents = file.readlines()

    for word in contents:
        word = word.strip()

        # Skip empty lines
        if not word:
            continue

        attempt_count += 1
        hashed = hash_word(word, hash_type)

        if hashed == target_hash:
            found = True
            elapsed = time.time() - start_time
            print(f"[+] Password Found  : {word}")
            print(f"[+] Attempts Made   : {attempt_count}")
            print(f"[+] Time Taken      : {elapsed:.2f} seconds")
            break

    if not found:
        elapsed = time.time() - start_time
        print(f"[-] Password not found in wordlist.")
        print(f"[-] Attempts Made   : {attempt_count}")
        print(f"[-] Time Taken      : {elapsed:.2f} seconds")


# ──────────────────────────────────────────────
# Main Entry Point
# ──────────────────────────────────────────────

def main():
    # Banner
    print("=" * 45)
    print("        Python Password Cracker")
    print("        For Educational Use Only")
    print("=" * 45)

    target_hash = input("\nEnter the target hash to crack : ").strip()
    algorithm   = input("Enter the algorithm (md5, sha1, sha256) : ").strip().lower()
    filename    = input("Enter wordlist filename (default: wordlist.txt) : ").strip()

    # Use default wordlist if user pressed enter without typing
    if not filename:
        filename = "wordlist.txt"

    supported = ["md5", "sha1", "sha256"]

    if algorithm not in supported:
        print(f"\n[!] Unsupported algorithm '{algorithm}'. Please use: md5, sha1, or sha256.")
        return

    crack_hash(target_hash, algorithm, filename)


if __name__ == "__main__":
    main()
