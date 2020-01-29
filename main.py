import eel, sys, os, random

eel.init('front-end')

args=sys.argv
#print(args)

@eel.expose
def pick_file(folder):
    if folder=='':
	if len(args)==1:
		return "No command line input found!"
	else:
		folder=str(args[1])
    if os.path.isdir(folder):
        return os.listdir(folder)
    else:
        return 'Invalid Path'


eel.start('index.html', size=(1000, 600))
