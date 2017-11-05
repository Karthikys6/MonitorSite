import requests
import argparse
import time

def read_urls(path):
    url_list = []
    with open(path) as f:
        lines = f.readlines()
        for l in lines:
            url_list.append(l.rstrip())
    return url_list

def get_status(url):
	count=1
	while count <=3:
		count += 1
		try:
			r = requests.get(url)
			retcode=r.status_code;
			break;
		except requests.exceptions.RequestException as e:
			 retcode=-1
	if count == 3:
		retcode=-1
	return retcode
    
def parse_options():
    parser = argparse.ArgumentParser(description='Options')
    parser.add_argument('-o', '--output', help='Output file name', default='', dest='logger')
    requiredNamed = parser.add_argument_group('required named arguments')
    requiredNamed.add_argument('-i', '--input', help='Input url file', required=True, dest='input_urls')
    args = parser.parse_args()
    return args
    
def get_log(target):
    log = sys.stdout
    if target:
        log = target and open(target, 'w') or sys.stdout
    return log
    
def main():
	input_args = parse_options()
	input_urls = input_args.input_urls
	url_list = read_urls(input_urls)
	log = get_log(input_args.logger)
	
	for url in url_list:
		try:
			start_time=time.time()
			code = get_status(url)
			end_time=time.time()
			response_time = int(end_time - start_time)
			if code==-1:
				log.write("\n" + "RED, Network Error after multiple attempts!!")
			elif code == 200:
			    log.write("\n" + str(int(time.time())) + " | "+ "GREEN |" +str(url) + " | "+str(response_time*1000) + "\n")
			else:
				log.write("\n" + 'WARNING! {0} returned {1}'.format(url,code))
		except:
			log.write("\n" + 'Invalid URL!' + "\n")
            
if __name__ == '__main__':
    main()