# File Decryption Guide (Base64 Chunked Format)

## Encrypted File Info

| Item | Value |
|------|-------|
| Original filename | 张曦月-转正答辩-0817.pptx |
| Hash algorithm | MD5 (of original filename, UTF-8 encoded) |
| MD5 hash | e51db051a1300bb7323239f172e8858b |
| Total size | 4,540,312 bytes (~4.33 MB) |
| Chunk count | 76 |
| Chunk size | 60,000 bytes (binary) |
| Encoding | Base64 |
| Location | assets/encrypted_ppt/ |

## How to Decrypt (Restore the PPT)

### Method 1: Python Script (Recommended)

Save the following as `decrypt.py` and run it in the repo root:

```python
import base64, os, hashlib

original_name = "张曦月-转正答辩-0817.pptx"
name_hash = hashlib.md5(original_name.encode("utf-8")).hexdigest()
chunk_count = 76

assert name_hash == "e51db051a1300bb7323239f172e8858b", "Hash mismatch!"

with open(original_name, "wb") as out:
    for i in range(chunk_count):
        chunk_file = "assets/encrypted_ppt/{}.part{:03d}".format(name_hash, i)
        with open(chunk_file, "rb") as f:
            out.write(base64.b64decode(f.read()))

expected_size = 4540312
actual_size = os.path.getsize(original_name)
assert actual_size == expected_size, "Size mismatch: {} != {}".format(actual_size, expected_size)
print("Restored: {} ({} bytes)".format(original_name, actual_size))
```

### Method 2: One-liner (Git Bash / Linux / macOS)

```bash
git clone https://github.com/Xiyuejiushikaixindeyisi/PPT-skill.git
cd PPT-skill
python3 -c "import base64,hashlib; h='e51db051a1300bb7323239f172e8858b'; open('张曦月-转正答辩-0817.pptx','wb').write(b''.join(base64.b64decode(open('assets/encrypted_ppt/{}.part{:03d}'.format(h,i),'rb').read()) for i in range(76))); print('Done')"
```

### Method 3: PowerShell (Windows)

```powershell
git clone https://github.com/Xiyuejiushikaixindeyisi/PPT-skill.git
cd PPT-skill
python -c "import base64,hashlib; h='e51db051a1300bb7323239f172e8858b'; open('张曦月-转正答辩-0817.pptx','wb').write(b''.join(base64.b64decode(open('assets/encrypted_ppt/{}.part{:03d}'.format(h,i),'rb').read()) for i in range(76))); print('Done')"
```

## File Structure

```
PPT-skill/
├── DECRYPT_GUIDE.md
└── assets/encrypted_ppt/
    ├── MANIFEST.txt
    ├── e51db051a1300bb7323239f172e8858b.part000
    ├── e51db051a1300bb7323239f172e8858b.part001
    ├── ... (76 parts total)
    └── e51db051a1300bb7323239f172e8858b.part075
```

## Verification

```bash
ls -la 张曦月-转正答辩-0817.pptx
# Expected: 4540312 bytes
```

## Notes

- Filename hash: MD5("张曦月-转正答辩-0817.pptx") = e51db051a1300bb7323239f172e8858b
- Each chunk is base64-encoded binary data
- This is file disguise, not cryptographic encryption
