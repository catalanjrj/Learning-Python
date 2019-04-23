from sys import argv

script, filename = argv

print(f"Let's read {filename}:")
txt = open(filename)

print(txt.read())


txt.close()
