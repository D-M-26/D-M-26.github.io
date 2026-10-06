#!/bin/sh
# يضبط روابط المعاينة على العنوان النهائي. يمكن تشغيله أكثر من مرة.
# الاستخدام:  ./set-domain.sh https://d-m-26.github.io
[ -z "$1" ] && { echo "usage: ./set-domain.sh https://user.github.io/repo"; exit 1; }
BASE="$1" python3 - <<'PY'
import os, re, io
base = os.environ['BASE'].rstrip('/')
p = 'index.html'
s = io.open(p, encoding='utf-8').read()
s = re.sub(r'(<link rel="canonical" href=")[^"]*(")', r'\1' + base + r'/\2', s)
s = re.sub(r'((?:property|name)="og:url" content=")[^"]*(")', r'\1' + base + r'/\2', s)
s = re.sub(r'((?:property|name)="(?:og:image|og:image:secure_url|twitter:image)" content=")[^"]*(")',
           r'\1' + base + r'/share-v3.png\2', s)
io.open(p, 'w', encoding='utf-8').write(s)
print('تم الضبط على:', base)
for m in sorted(set(re.findall(r'content="(https://[^"]*)"', s))):
    print('  ', m)
PY
