# File Decryption Guide (Chunked Format)

## Encrypted File Info

| Item | Value |
|------|-------|
| Original filename | `张曦月-转正答辩-0817.pptx` |
| Hash algorithm | MD5 (of original filename, UTF-8 encoded) |
| MD5 hash | `e51db051a1300bb7323239f172e8858b` |
| Total size | 4,540,312 bytes (~4.5 MB) |
| Chunk count | 12 |
| Chunk size | 409,600 bytes (400 KB) |
| Last chunk size | 34,712 bytes |
| Location | `assets/encrypted_ppt/` |

## File List

```
assets/encrypted_ppt/
├── MANIFEST.txt                              # Metadata
├── e51db051a1300bb7323239f172e8858b.part000  # Chunk 0
├── e51db051a1300bb7323239f172e8858b.part001  # Chunk 1
├── e51db051a1300bb7323239f172e8858b.part002  # Chunk 2
├── e51db051a1300bb7323239f172e8858b.part003  # Chunk 3
├── e51db051a1300bb7323239f172e8858b.part004  # Chunk 4
├── e51db051a1300bb7323239f172e8858b.part005  # Chunk 5
├── e51db051a1300bb7323239f172e8858b.part006  # Chunk 6
├── e51db051a1300bb7323239f172e8858b.part007  # Chunk 7
├── e51db051a1300bb7323239f172e8858b.part008  # Chunk 8
├── e51db051a1300bb7323239f172e8858b.part009  # Chunk 9
├── e51db051a1300bb7323239f172e8858b.part010  # Chunk 10
└── e51db051a1300bb7323239f172e8858b.part011  # Chunk 11 (last, smaller)
```

## How to Decrypt (Restore the PPT)

### Method 1: Python Script (Recommended)

```python
import hashlib
import os

# Configuration
original_name = '张曦月-转正答辩-0817.pptx'
name_hash = hashlib.md5(original_name.encode('utf-8')).hexdigest()
chunk_count = 12

# Verify hash
assert name_hash == 'e51db051a1300bb7323239f172e8858b', 'Hash mismatch!'

# Reassemble chunks
output_file = original_name
with open(output_file, 'wb') as out:
    for i in range(chunk_count):
        chunk_file = f'assets/encrypted_ppt/{name_hash}.part{i:03d}'
        with open(chunk_file, 'rb') as chunk:
            out.write(chunk.read())

# Verify size
expected_size = 4540312
actual_size = os.path.getsize(output_file)
assert actual_size == expected_size, f'Size mismatch: {actual_size} != {expected_size}'

print(f'Successfully restored: {output_file} ({actual_size} bytes)')
```

### Method 2: Shell Script (Git Bash / Linux / macOS)

```bash
# After cloning the repo
cd PPT-skill
cat assets/encrypted_ppt/e51db051a1300bb7323239f172e8858b.part* > 张曦月-转正答辩-0817.pptx
echo "Restored: 张曦月-转正答辩-0817.pptx"
ls -la 张曦月-转正答辩-0817.pptx
```

### Method 3: PowerShell (Windows)

```powershell
cd PPT-skill
$hash = "e51db051a1300bb7323239f172e8858b"
$output = "张曦月-转正答辩-0817.pptx"
$stream = [System.IO.File]::Create($output)
for ($i = 0; $i -lt 12; $i++) {
    $chunkFile = "assets/encrypted_ppt/$hash.part$($i.ToString('000'))"
    $bytes = [System.IO.File]::ReadAllBytes($chunkFile)
    $stream.Write($bytes, 0, $bytes.Length)
}
$stream.Close()
Write-Host "Restored: $output"
```

### Method 4: Command Prompt (Windows)

```cmd
cd PPT-skill
copy /b assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part000 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part001 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part002 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part003 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part004 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part005 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part006 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part007 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part008 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part009 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part010 + ^
       assets\encrypted_ppt\e51db051a1300bb7323239f172e8858b.part011 ^
       张曦月-转正答辩-0817.pptx
```

## Verification

After reassembly, verify the file integrity:

```bash
# Check file size (should be 4540312 bytes)
ls -la 张曦月-转正答辩-0817.pptx

# Compute MD5 of the restored file content
md5sum 张曦月-转正答辩-0817.pptx
```

## Notes

- This is a simple file disguise (filename hash + extension change), not cryptographic encryption.
- The file content is unchanged; only the filename is hashed and the file is split into chunks.
- The filename hash serves as a lookup key: `MD5("张曦月-转正答辩-0817.pptx") = e51db051a1300bb7323239f172e8858b`
- Anyone with access to this repo and this guide can restore the original PPT.
