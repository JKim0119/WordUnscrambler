#!/usr/bin/env python

from collections import defaultdict, Counter
from functools import reduce

class WordUnscrambler(object):

	def __init__(self):
		self.wordList = []
		with open("data.csv","r") as f:
			for line in f.readlines():
				self.wordList.append(list(map(self.toInt,line.strip().split(","))))

	def toInt(self,i):
		try:
			return int(i)
		except:
			return i

	def unscramble(self, letters):
		if(letters.isalpha()):
			count = Counter(letters.lower())
			freq=[0]*26
			for key,value in count.items():
				freq[ord(key)-97]=value

			for wordData in self.wordList:
				wordDataList = wordData
				isEligible = (freq == wordDataList[1:-1])
				if(isEligible):
					return wordDataList[0]
			return "fail"
		else:
			return letters
	
	def main(self):
		input = open("input.txt", "r")
		read = input.read()
		input.close()
		paragraphs = read.split("\n")
		f = open("output.txt", "w")
		for paragraph in paragraphs:
			words = paragraph.split()
			string = ""
			for word in words:
				string += " " + self.unscramble(word)
			f.write(string)
			f.write("\n")
		f.close()


if __name__=="__main__":
	wu=WordUnscrambler()
	wu.main()
