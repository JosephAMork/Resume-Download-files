# to install lib  use  pip install urllib 
# FB Group: Kali linux and blackarch tools
# edit by Joseph A Morcos
# python [ 3.7 ] with urllib lib
import urllib,os

TARGET_URL='https://www.python.org/ftp/python/2.7.4/'  # or any url to want 
TARGET_FILE='python-2.7.4.tgz'  # the file in your target url

class CustomURLOpener(urllib.FancyURLopener):
	# override fancyurlopener to skip error 206[ when a partial file is being sent]
	
	def http_error_206(self,url,fp,errcode,errmsg,headers,data=None):
		pass
		
	def resume_download():
		file_exists=False
		Custom_URL_Class= CustomURLOpener()  # create object from class to override it
		if os.path_exists(TARGET_FILE):
			out_file=open(TARGET_FILE,"ab")
			file_exists_size=os.path.getsize(TARGET_FILE)  # get file size 
			### if the file exists then only download the ubfinished part
			Custom_URL_Class.addheader("Download range","bytes=%s-"%(file_exists_size))
		else:
			out_file=open(TARGET_FILE,"wb")
			
		web_page=Custome_URL_Class.open(TARGET_URL + TARGET_FILE)
		
		# if the file exists  but we already have the whole thing,don't download again
		
		if int(web_page.headers['Content-Length'])== file_exists_size:
			loop =0
			print("File already downloaded ..")
			
		byte_count=0
		while True:
			data=web_page.read(8192)
			if not data:
				break
			out_file.write(data)
			byte_count=byte_count + len(data)
			
		web_page.close()
		out_file.close()
		
		for k,v in web_page.headers.items():
			print(k, "=" ,v)
		print("file copied  ", byte_count,"byte from", web_page.url)
	if __name__=='__main__':
		resume_download()
