import sys, json

for t in json.load(sys.stdin):
	sys.stdout.write(t['text'].encode('UTF-8'))
	sys.stdout.write('\n\n')
