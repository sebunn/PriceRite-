# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jun  5 2014)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class wxFBclass
###########################################################################

class wxFBclass ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"The Price is Right", pos = wx.DefaultPosition, size = wx.Size( 500,350 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"One of the three doors has the prize...but WHICH one?", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 14, 70, 90, 90, False, wx.EmptyString ) )
		
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		gSizer1 = wx.GridSizer( 0, 3, 0, 0 )
		
		self.DoorOne = wx.Button( self, wx.ID_ANY, u"Choose Me!", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		gSizer1.Add( self.DoorOne, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.DoorTwo = wx.Button( self, wx.ID_ANY, u"Choose Me!", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		gSizer1.Add( self.DoorTwo, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		self.DoorThree = wx.Button( self, wx.ID_ANY, u"Choose Me!", wx.DefaultPosition, wx.Size( 100,100 ), 0 )
		gSizer1.Add( self.DoorThree, 0, wx.ALIGN_CENTER|wx.ALL, 5 )
		
		
		bSizer1.Add( gSizer1, 10, wx.EXPAND, 5 )
		
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNHIGHLIGHT ) )
		
		gSizer2 = wx.GridSizer( 0, 4, 0, 0 )
		
		self.WonLabel = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Won:   0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.WonLabel.Wrap( -1 )
		gSizer2.Add( self.WonLabel, 0, wx.ALL, 5 )
		
		self.TriesLabel = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Tries :  0", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.TriesLabel.Wrap( -1 )
		gSizer2.Add( self.TriesLabel, 0, wx.ALL, 5 )
		
		self.Percent = wx.StaticText( self.m_panel1, wx.ID_ANY, u"0%", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.Percent.Wrap( -1 )
		self.Percent.SetFont( wx.Font( 15, 70, 90, 90, False, wx.EmptyString ) )
		
		gSizer2.Add( self.Percent, 0, wx.ALL, 5 )
		
		self.TryAgainButton = wx.Button( self.m_panel1, wx.ID_ANY, u"Try Again", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer2.Add( self.TryAgainButton, 0, wx.ALL, 5 )
		
		
		self.m_panel1.SetSizer( gSizer2 )
		self.m_panel1.Layout()
		gSizer2.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )
		
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.DoorOne.Bind( wx.EVT_LEFT_UP, self.doorOneClick )
		self.DoorTwo.Bind( wx.EVT_LEFT_UP, self.doorTwoClick )
		self.DoorThree.Bind( wx.EVT_LEFT_UP, self.doorThreeClick )
		self.TryAgainButton.Bind( wx.EVT_LEFT_UP, self.tryAgainClick )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def doorOneClick( self, event ):
		event.Skip()
	
	def doorTwoClick( self, event ):
		event.Skip()
	
	def doorThreeClick( self, event ):
		event.Skip()
	
	def tryAgainClick( self, event ):
		event.Skip()
	

