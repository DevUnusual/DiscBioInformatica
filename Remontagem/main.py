import re
file = open("kmer50.txt", "r")
kmer = re.findall('[ATCG]{50}', file.read())
file.close()

kmer = [x.strip() for x in kmer]

print(kmer)