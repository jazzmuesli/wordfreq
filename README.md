# wordfreq

wget -q -O- http://storage.googleapis.com/books/ngrams/books/datasetsv2.html | perl -lane "print \$1 if (m%href='(.*?googlebooks-ger-all-1gram-2012.*?)'%);" > 1grams.url
time for i in `cat 1grams.url`; do wget -q -O- $i | zgrep 2009 >> all.txt; done
time cat all.txt | sort --parallel=8 -rnk3 | awk '!/_/ {print $1, $3, NR}' > de-1grams.txt

python3 freqs.py text1.txt text2.txt
