import urllib.request
import urllib.error

fw = open("dump_results.txt", 'w')
# fw = open("dump_results.txt", 'a')

def inNout(urlin, filein):
	fr = open(filein, 'r')
	while True:
		front = fr.readline()
		# EOF
		if not front: break

		if 'txt' in front:
			data = urllib.request.urlopen(urlin+str(front))
			print(urlin+str(front))
			for line in data :		
				try:
					line = line.decode()
				except urllib.error.HTTPError:
					break
				except urllib.error.URLError:
					break
				except UnicodeDecodeError:
					break
				except UnicodeEncodeError:
					break
				if 'HTML' in line :
					break
				line = str(line).rstrip('\r').rstrip('\n')
				print(line)
				fw.write(line)
			data.close()
	fr.close()

if __name__=='__main__':
	#inNout("http://textfiles.com/stories/", "urls_to_read.txt")
	#inNout("http://textfiles.com/sf/", "urls_to_read2.txt")
	#inNout("http://textfiles.com/humor/", "urls_to_read3.txt")
	inNout("http://textfiles.com/hacking/", "urls_to_read4.txt")
	inNout("http://textfiles.com/fun/", "urls_to_read5.txt")
	fw.close()