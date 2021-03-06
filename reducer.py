#!/usr/bin/env python
# 
# Adapted from script by Diana MacLean 2011
#
# Adapted fro CS448G from Michael Noll's tutorial on : http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
#
#

from operator import itemgetter

import sys
import re

def get_stopwords():
	stop_words = set()
	with open("stop-words") as file:
		for line in file:
			for word in re.findall(r'\w+', line):
				stop_words.add(word)
        return stop_words
		
def get_word_counts():
	# maps words to their counts
	word2count = {}

	# get list of stopwords
	stop_words = get_stopwords()
	
	# input comes from STDIN
	for line in sys.stdin:
		# remove leading and trailing whitespace
		line = line.strip()

		# parse the input we got from mapper.py
		word, count = line.split('\t', 1)
		# convert count (currently a string) to int
		try:
			if word not in stop_words:
				count = int(count)
				word2count[word] = word2count.get(word, 0) + count
		except ValueError:
			# count was not a number, so silently
			# ignore/discard this line
			pass
        return word2count

def print_out_word_counts(counted_words):
	# write the results to STDOUT (standard output)
	for word, count in counted_words:
		print '%s\t%s'% (word, count)

word2count = get_word_counts()

counted_words = word2count.items()
counted_words.sort()

print_out_word_counts(counted_words)

