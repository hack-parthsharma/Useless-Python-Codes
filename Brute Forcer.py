import urllib2
import threading
import Queue
import urllib

threads       = 50
target_url    = "http://testphp.vulnweb.com"
wordlist_file = "/tmp/all.txt" # from SVNDigger
resume        = NONE
user_agent    = "Mozilla/5.0 and Blah Blah......"

def build_wordlist(wordlist_file):

	#read in the wordlist
	fd = open(wordlist_file,"rb")
	raw_words = fd.readlines()
	fd.close()

	found_resume = False
	words        = Queue.Queue()

	for word in raw_words:

		word = word.rstrip()

		if resume is not NONE:

			if found_resume:
				words.put(word)
			else:
				if word == resume:
				found_resume = target_urlprint "Resuming wordlist from: %s" % resume

		else:
			words.put(word)

	return words
									 