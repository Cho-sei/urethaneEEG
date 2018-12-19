import wx
import pandas as pd
import time
import winsound
import random

class MainFrame(wx.Frame):
	#--------------------------------------
	#フレーム初期化
	#--------------------------------------
	def __init__(self):
		super().__init__(None, wx.ID_ANY, 'urethaneEEG', style=wx.MAXIMIZE)

		self.SetBackgroundColour('white')

		#キーイベント設定
		self.Bind(wx.EVT_KEY_DOWN, self.Start)

		#中心座標取得
		img_w,img_h = wait.GetSize()
		frame_w,frame_h = self.GetSize()
		self.offset_w = int((frame_w - img_w)/2)
		self.offset_h = int((frame_h - img_h)/2)

		#"Wait..."表示
		self.default_display = wx.StaticBitmap(self, -1, wait, size=wait.GetSize())
		self.default_display.SetPosition((self.offset_w,self.offset_h))

	#--------------------------------------
	#"Start soon!!"表示して、刺激のループ開始
	#--------------------------------------
	def Start(self, event):

		#"Start soon!!"表示
		start_display = wx.StaticBitmap(frame, -1, startsoon, size=startsoon.GetSize())
		start_display.SetPosition((self.offset_w, self.offset_h))
		time.sleep(1)

		for i in range(len(stimorder)):
			blank_time = random.randint(8,12) * 0.1
			self.stimulus(stimorder[i], blank_time)

		self.exit()

	#--------------------------------------
	#１周期分の刺激呈示
	#--------------------------------------
	def stimulus(self, stimkind, blank_time):

		#fixation表示
		fixation_display = wx.StaticBitmap(frame, -1, fixation, size=fixation.GetSize())
		fixation_display.SetPosition((self.offset_w, self.offset_h))
		time.sleep(1.5)

		#blank
		blank_display = wx.StaticBitmap(frame, -1, blank, size=blank.GetSize())
		blank_display.SetPosition((self.offset_w, self.offset_h))
		time.sleep(blank_time)

		#刺激呈示
		if stimkind == 0:
			stimulus_display = wx.StaticBitmap(frame, -1, landolt_up, size=landolt_up.GetSize())
			stimulus_display.SetPosition((self.offset_w, self.offset_h))
			#winsound.Beep(audtarget,200)
			time.sleep(visduration)
		elif stimkind == 1:
			stimulus_display = wx.StaticBitmap(frame, -1, landolt_down, size=landolt_down.GetSize())
			stimulus_display.SetPosition((self.offset_w, self.offset_h))
			#winsound.Beep(audnomal,200)
			time.sleep(visduration)
		elif stimkind == 2:
			stimulus_display = wx.StaticBitmap(frame, -1, landolt_up, size=landolt_up.GetSize())
			stimulus_display.SetPosition((self.offset_w, self.offset_h))
			#winsound.Beep(audnomal,200)
			time.sleep(visduration)
		else:
			stimulus_display = wx.StaticBitmap(frame, -1, landolt_down, size=landolt_down.GetSize())
			stimulus_display.SetPosition((self.offset_w, self.offset_h))
			#winsound.Beep(audtarget,200)
			time.sleep(visduration)

	#--------------------------------------
	#終了処理
	#--------------------------------------
	def exit(self):

		finish_display = wx.StaticBitmap(frame, -1, finish, size=finish.GetSize())
		finish_display.SetPosition((self.offset_w, self.offset_h))
		time.sleep(1)
		self.Destroy()


if __name__ == '__main__':
	app = wx.App()

	#画像読み込み
	landolt_up = wx.Image('landolt_up.tif').ConvertToBitmap()
	landolt_down = wx.Image('landolt_down.tif').ConvertToBitmap()
	fixation = wx.Image('fixation.tif').ConvertToBitmap()
	wait = wx.Image('wait.jpg').ConvertToBitmap()
	startsoon = wx.Image('startsoon.jpg').ConvertToBitmap()
	blank = wx.Image('blank.jpg').ConvertToBitmap()
	finish = wx.Image('finish.jpg').ConvertToBitmap()

	stimorder = [0,1,2,3]

	#パラメータ
	visduration = 0.05
	audtarget = 1020
	audnomal = 1000

	#frame初期化
	frame = MainFrame()	

	frame.Show()
	app.MainLoop()