import subprocess,os, shutil
from os.path import join
from Bio.Align.Applications import ClustalwCommandline


def GetListFile(mypath, extension):
    from os import listdir
    from os.path import isfile, join
    return [f for f in listdir(mypath) if isfile(join(mypath, f)) and os.path.splitext(f)[1] == extension]

def Parsefile(Path,start):
    fileIn = open(Path, "r")
    lines = fileIn.readlines()
    fileIn.close()
    return lines[start:]

def FilterfastaAlign(File): # some fasta Alignment from NCBI contain redundant sequences with the same id repeated, a filtering step is necessary to remove this redundancy, otherwise clustal will bug!
	lines = Parsefile(File,0)
	Listfasta=[]
        positions=[]
	for index,line in enumerate(lines):
		if line.isalnum()==False and line[0]=='>': #checks whether the string consists of alphanumeric characters.
			Listfasta.append((index,line))
	for(x,y) in  Listfasta:
		for (xx,yy) in Listfasta:
			if x!=xx and y==yy:
				positions.append(xx)
				positions.append(xx+1)
	#print positions
	removelinefromFile(File, positions)
def removelinefromFile(File,positions):
	f = open(File,"r+")
	d = f.readlines()
	f.seek(0)
	print positions
        
	for i,line in enumerate(d):
		#print i 
    		if i not in positions:
        		f.write(line)	
	f.truncate()
	f.close()

if __name__ == "__main__":
	Path="Fasta_MSA"
	Extensionfasta='.txt'

        # 1st step: Fasta file aLignment using Clustalw: clustalw -infile=infile.fasta -seqnos=ON -gapopen=2 -gapext=0.5
	for infile in GetListFile(Path, Extensionfasta):
		print "processing " + infile
		FilterfastaAlign(join(Path,infile))
		cline = ClustalwCommandline("clustalw", infile=join(Path,infile), seqnos="ON", gapopen=2, gapext=0.5)
		child = subprocess.call(str(cline), shell=True)
