import sys
import re

if len(sys.argv) >= 3:
    mode = sys.argv[1]
    file = sys.argv[2]
else:
    print(
        "Not enough arguments: figs.py [tikzfig|standalone|macros|section] file.tex (output.txt=figs.txt)")
    quit()

if len(sys.argv) >= 4:
    outp = sys.argv[3]
else:
    outp = "figs.txt"


def inputexp(dir):
    return 'input\{' + dir + '/(.*?)\}'


braces = '\{(.*?)\}'
macro = inputexp('macro')
section = inputexp('section')
standalone = 'includestandalone(?:\[.*?\])?' + braces
tikzfig = 'tikzfig' + braces
refs = 'bibliography\{refs/(.*?)\}'

section = 'input\{sections/(.*?)\}'
macro = 'input\{macros/(.*?)\}'

if mode == "tikzfig":
    regex = tikzfig
elif mode == "standalone":
    regex = standalone
elif mode == "section":
    regex = section
elif mode == "macros":
    regex = macro
elif mode == "refs":
    regex = refs
else:
    print("Bad mode " + mode)
    quit()

with open(file) as f:
    text = f.read()
    matches = re.findall(regex, text)

if len(matches) > 0:

    matches = sorted(set(matches))

    with open(outp, "w") as f:
        for m in matches[:-1]:
            f.write(m + "\n")
        f.write(matches[-1])