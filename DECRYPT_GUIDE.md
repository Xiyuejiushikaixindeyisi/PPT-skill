# File Decryption Guide

## Encrypted File Info

| Item | Value |
|------|-------|
| Original filename | `张曦月-转正答辩-0817.pptx` |
| Hash algorithm | MD5 (of original filename, UTF-8 encoded) |
| MD5 hash | `e51db051a1300bb7323239f172e8858b` |
| Disguised filename | `e51db051a1300bb7323239f172e8858b.bin` |
| Disguised extension | `.bin` |
| Original extension | `.pptx` |
| File location | `assets/e51db051a1300bb7323239f172e8858b.bin` |

## How to Decrypt (Restore the PPT)

### Method 1: Manual Rename

1. Download `assets/e51db051a1300bb7323239f172e8858b.bin` from this repository.
2. Rename the file:
   - From: `e51db051a1300bb7323239f172e8858b.bin`
   - To: `张曦月-转正答辩-0817.pptx`
3. Open with PowerPoint.

### Method 2: Use Git Bash / Shell

```bash
# After cloning or downloading the repo
cd PPT-skill/assets
mv e51db051a1300bb7323239f172e8858b.bin 张曦月-转正答辩-0817.pptx
```

### Method 3: Use Python Script

```python
import hashlib

original_name = '张曦月-转正答辩-0817.pptx'
name_hash = hashlib.md5(original_name.encode('utf-8')).hexdigest()

# Verify hash matches the downloaded filename
assert name_hash == 'e51db051a1300bb7323239f172e8858b', 'Hash mismatch!'

# Rename the downloaded file
import shutil
shutil.move(f'{name_hash}.bin', original_name)
print(f'Restored: {original_name}')
```

### Method 4: Use PowerShell (Windows)

```powershell
Rename-Item -Path "e51db051a1300bb7323239f172e8858b.bin" -NewName "张曦月-转正答辩-0817.pptx"
```

## Verification

To verify the file integrity after download, you can compute the MD5 of the file content and compare it with the original:

```bash
md5sum e51db051a1300bb7323239f172e8858b.bin
```

## Notes

- This is a simple file disguise (extension + filename hash), not cryptographic encryption.
- The file content is unchanged; only the filename and extension are altered.
- Anyone with access to this repo and this guide can restore the original PPT.
