import os, json

wpaths = []
wfiles = []
outfile = "indexedfiles-out.txt"

if os.path.exists(outfile):
	os.remove(outfile)

for root, dirs, files in os.walk("."):
	path = root[1:].split("https://cdn.jsdelivr.net/gh/Haha64142/seraph@main/")
	wpaths.append(["https://cdn.jsdelivr.net/gh/Haha64142/seraph@main/".join(path[:-1]), path[-1]])
	if root[1:]:
		for f in files:
			wfiles.append(root[1:] + "https://cdn.jsdelivr.net/gh/Haha64142/seraph@main/" + f)

wpaths = wpaths[1:]

open(outfile, "w").write(json.dumps(wpaths)+",,,\n"+("\n".join(wfiles)))