from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.gridlayout import GridLayout 
from kivy.uix.textinput import TextInput 
from kivy.uix.button import Button
from kivy.uix.widget import Widget 
from kivy.properties import ObjectProperty
#

import os
from moviepy.video.io.VideoFileClip import VideoFileClip
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip

#
class MyGrid(GridLayout):
	filechooser=ObjectProperty(None)
	op=ObjectProperty(None)
	status=ObjectProperty(None)
	but1=ObjectProperty(None)
	def selected(self):
		self.op.text=self.filechooser.selection[0]
		self.status.text="Click On [b]Create Status. [i]FOR ONCE[/i][/b]"
	def disable_button(self):
		self.but1.disabled=True
	def enable_button(self):
		self.but1.disabled=False
	def status_maker(self):
		self.disable_button()
		file=self.op.text
		reading_directory=os.path.dirname(file)
		basename=os.path.basename(file)
		basename_root=os.path.splitext(basename)[0]
		ext=os.path.splitext(basename)[1]
		if ext==".mp4":
			os.chdir(reading_directory)#changing file directory
			writing_directory=os.path.join(reading_directory,basename_root+"_WA_Status")
			if not os.path.exists(writing_directory):
				os.mkdir(writing_directory)
			os.chdir(writing_directory)
			size=VideoFileClip(file).duration
			i=0
			ii=1
			while i<size:
				try:
					ffmpeg_extract_subclip(file,i,i+25,str(ii)+ext)
				except:
					self.status.text="Error: File Could not be manipulated."
				i+=25
				ii+=1
			self.status.text=f"Your o/p saved in {writing_directory}"
		else:
			self.status.text=f"Extension Error. Choose .mp4 extension."
		self.enable_button()
class WaApp(App):
	def build(self):
		return MyGrid()

if __name__ == '__main__':
	WaApp().run()