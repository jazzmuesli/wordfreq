import sys
import numpy as np
from nltk import word_tokenize

def prepare_freq_dict():
  # word total_occurences rating
  lines = open('de-1grams.txt').readlines()
  d = dict()
  for x in lines:
    d[x.split()[0]] = x.split()[1:3]
  return d

# pos=0 - occurences, pos=1 rating
def get_freqs(filename, d, pos=0):
  raw = open(filename).read()
  tokens = word_tokenize(raw)
  freqs = [d.get(x, [0,0])[pos] for x in tokens]
  a = np.array([int(x) for x in freqs if int(x) > 0])
  # words found, mean, 0/10/25/50/90/100 percentiles of frequencies
  return [len(a)] + [np.mean(a)] + np.percentile(a, [0,10,25,50,75,90,100]).tolist()

# print for every provided file
d = prepare_freq_dict()
print("\n".join(["\t".join([str(s) for s in get_freqs(f,d,1)]) for f in sys.argv[1:]]))
