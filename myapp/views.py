
from django.shortcuts import render, redirect
import os
from pytube import YouTube
from django.http import FileResponse
from io import BytesIO
from datetime import datetime


def home(request):

    return render(request, "index.html")

def done(request):

    return render(request, "done.html")
# Create your views here.


def download(request):
		try:
			global url
			url = request.GET.get('myurl')
			resolutions = []
			if request.method == 'GET' and url is not None:
				obj = YouTube(url)
				thumb = obj.thumbnail_url
				title = obj.title
				streamAll = obj.streams.all()
				for i in streamAll:
					resolutions.append(i.resolution)
				resolutions = list(dict.fromkeys(resolutions))
				resolutions.remove(None)
				# print(resolutions, thumb)
				return render(request, "download.html", {'res': resolutions, 'thum': thumb, 'title': title})
			return redirect('/')
		except Exception as e:
			raise e	


# def downloaded(request,resolution):
# 	global url 
# 	homedir=os.path.expanduser("~")
# 	dirs=homedir+'/Downloads'
# 	if request.method == 'POST':
		
	
# 		YouTube(url).streams.filter(res=resolution).first().download(dirs)
# 		# return FileResponse(open(YouTube(url).streams.first().download(skip_existing=True),'rb'))
# 		return render(request, "done.html")

def downloaded(request,resolution):
			try:	
				yt=YouTube(url)
				
				time = datetime.now().strftime("%H:%M")
				title=yt.title
				stream=yt.streams.filter(res=resolution).first()
				data=stream.download(skip_existing=False)

				path=os.path.normpath(data)
				
				with open(path,'rb') as f:
					byteData=f.read()
				os.remove(data)
				return FileResponse(BytesIO(byteData),filename=title+' '+resolution+' ' +time+' youDown.mp4',as_attachment=True,content_type='video/mp4')
			except Exception as e:
				raise e	

def downloaded_audio(request):
		try:
			yt=YouTube(url)
			
			time = datetime.now().strftime("%H:%M")
			title=yt.title
			stream=yt.streams.filter(only_audio=True).first()
			data=stream.download(skip_existing=False)
			path=os.path.normpath(data)
			with open(path,'rb') as f:
				byteData=f.read()
			os.remove(data)
			return FileResponse(BytesIO(byteData),filename=title +' '+time+' youDown.mp3',as_attachment=True,content_type='audio/mpeg')
		except Exception as e:
			raise e		
		# return redirect (request, "done.html")
