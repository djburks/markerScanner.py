#! /usr/bin/env python3
# Optional replacement for AMPHORA2's MarkerScanner Perl Script

import argparse
import os
from sys import exit

def parseArguments():
	parser = argparse.ArgumentParser()
	parser.add_argument("faa",help="Protein fasta file containing the bacterial proteome.",type=str)
	parser.add_argument("-E","--evalue",help="Optional e-value paramater for hmmsearch.",type=float,default=1e-7)
	parser.add_argument("-D","--domain",help="Domain for organism providing the proteome.",type=str,default="Bacteria")
	parser.add_argument("-M","--directory",help="Directory containing the AMPHORA2 marker files.",type=str,default="Marker/")
	
	parser.add_argument("--version",action="version",version='%markerScanner - Version 0.1a')
	
	args = parser.parse_args()
	
	return args
	

def faaScanner(faa):
	fasta = {}
	with open(faa) as infile:
		for lines in infile:
			if lines.startswith('>'):
				cur_index = (lines.split(' ')[0])[1:]
				fasta[cur_index] = lines
			else:
				fasta[cur_index] += lines
	return fasta
	
def markerList(dom):
	mlist = []
	with open(marker_directory + '/marker.list') as infile:
		for lines in infile:
			values = lines.split('\t')
			if values[1].lower() == dom:
				mlist.append(values[0])
			else:
				pass
	return mlist
			
	
	
def hmmProcess(markerlist,outhmm):
	hits = {}
	candidates = {}
	with open(outhmm) as infile:
		for lines in infile:
			if lines.startswith('#'):
				continue
			outdata = lines.split()
			query = outdata[0]
			hmm = outdata[3]
			
			if hmm not in markerlist:
				continue
			score = float(outdata[7])
			hperc = (float(outdata[16]) - float(outdata[15])) / float(outdata[5])
			tperc = (float(outdata[18]) - float(outdata[17])) / float(outdata[2])
			if query not in hits:
				hits[query] = {}
				hits[query] = [hmm,score,hperc,tperc]
			elif hits[query][1] < score:
				hits[query] = [hmm,score,hperc,tperc]
			if hits[query][0] == hmm:
				hits[query][2] += hperc
				hits[query][3] += tperc
	
	for q in hits:
		if (hits[q][2] > 0.7) and (hits[q][3] > 0.7):
			candidates[q] = hits[q][0]
			
	return candidates
			
				

args = parseArguments()
marker_directory = args.directory


if args.domain.lower() == 'bacteria':
	hmm = marker_directory + 'Bacteria.markers.hmm'
elif args.domain.lower() == 'archaea':
	hmm = marker_directory + 'Archaea.markers.hmm'
else:
	print('Invalid domain.')
	exit()
	
# HMM Search and Main

os.system("hmmsearch -Z 5000 -E " + str(args.evalue) + " --domE " + str(args.evalue) + " --domtblout py.hmmsearch -o /dev/null " + hmm + " " + args.faa)
candidates = hmmProcess(markerList(args.domain.lower()),'py.hmmsearch')
fasta = faaScanner(args.faa)
for cand in candidates:
	newfile = open(candidates[cand] + '.pep','a')
	newfile.write(fasta[cand])
	newfile.close()
	

