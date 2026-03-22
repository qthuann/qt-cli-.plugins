import hashlib
import re
import os

qtp_path = r'o:\prj\p01\.wip\qt.cli\qt.build\dist\plugins\qasa.qtp'
toml_path = r'o:\prj\p01\.wip\qt.cli\qt.build\dist\plugins\qasa.toml'

h = hashlib.sha256(open(qtp_path, 'rb').read()).hexdigest()
c = open(toml_path, 'r').read()
c = re.sub(r'sha256 = ".*"', f'sha256 = "{h}"', c)
open(toml_path, 'w', encoding='utf-8').write(c)
print(f"Update SUCCESS. Hash: {h}")
