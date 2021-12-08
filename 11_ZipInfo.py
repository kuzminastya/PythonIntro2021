import zipfile
import sys
import io

z = zipfile.ZipFile(io.BytesIO(bytes.fromhex(sys.stdin.read())))
count = sum(1 for file in z.namelist() if not file.endswith('/'))
vol = sum([zinfo.file_size for zinfo in z.infolist()])
sys.stdout.write(f'{count} {vol}')
