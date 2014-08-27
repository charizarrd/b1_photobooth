#!/bin/env python

# __________________________________________________________________________
# 
# Project: pycanon
# Module: n/a
#
# Developed by pstegmann
#
# $Id: pycanon.py,v 1.1.1.1 2008/10/31 01:13:08 kpoman Exp $
#
#  DESCRIPTION     : Canon camera remote control via python module
#
#  MODIFICATIONS   :
#               mm/dd/yyyy modif_author_name modif description ...
#
#  Copyright (c) PATRICIO STEGMANN
# __________________________________________________________________________



# ____________________________BEGIN_IMPORT__________________________________
# sdk api and prototypes issued from cdAPI.h through ctypeslib codegenerator
from cdAPI import *
# return codes from cdError.h via ctypeslib codegenerator
from cdERR import *
# constants from cdType.h via ctypeslib codegenerator
from cdCST import *
# import the rest of ctypes
from ctypes import *
import logging, time
# _____________________________IMPORT_END___________________________________



# ____________________________BEGIN_GLOBAL__________________________________
# _____________________________GLOBAL_END___________________________________


# ____________________________BEGIN_FUNCTION________________________________

# __________________________________________________________________________
class CanonCam:
	""" This class implements a Canon digital camera controller"""
	def __init__(self, name=None, name_in_os=None, port_type=None, source_type=None, sdk_major=7, sdk_minor=3):

		# set some variables for when we connect to a specific camera
		self.name = name
		self.name_in_os = name_in_os
		self.port_type = port_type
		self.source_type = source_type
		self.sdk_major = sdk_major
		self.sdk_minor = sdk_minor
		self.sdk_loaded = False
		self.cam_selected = None
		self.devices = []
		self.callbacks = {}
		self.messages = []
		self.logs = None
		self.dumped_image_count = 0
		self.device_handle = None
		self.vf_target = None
		self.zoom_pos = None
		self.max_zoom_pos = None
		self.use_digital_zoom = True
		self.release_datakind = None
		self.viewfinder_running = False
		self.save_path = 'C:\\TEMP\\'
		self.taken_pictures = []
		self.picsession_prefix = ''

		# Class Initialization starts here
		# create python callable callback functions
		self.createCallbacks()
		# initialize a logger
		self.initLogger()
		# load and initialize the sdk dll
		self.startSdk()
	

	def createCallbacks(self):
		self.callbacks['eventCallbackFunction'] = cdEventCallbackFunction(self.eventCallbackFunction)
		self.callbacks['viewFinderCallbackFunction'] = cdViewFinderCallbackFunction(self.viewFinderCallbackFunction)
		self.callbacks['releaseEventCallbackFunction'] = cdReleaseEventCallbackFunction(self.releaseEventCallbackFunction)
		self.callbacks['progressCallbackFunction'] = cdProgressCallbackFunction(self.progressCallbackFunction)

	def initLogger(self):
		self.logs = logging.getLogger('canoncam_logger')
		self.logs.setLevel(logging.DEBUG)
		ch = logging.FileHandler('./pycanon_debug.log')
		ch.setLevel(logging.DEBUG)
		formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
		ch.setFormatter(formatter)
		self.logs.addHandler(ch)

	def startSdk(self):
		self.logs.info('initializing sdk')
		# create version info structure
		v = cdVersionInfo()
		self.logs.info(v)

		# set sdk version
		v.MajorVersion = self.sdk_major
		v.MinorVersion = self.sdk_minor
		
		# start the correspondent sdk
		o = CDStartSDK(v,0)
		self.logs.info(o)
		self.logs.info(cdsdk_retcodes['cdOK'])
		#self.logs.info(cdsdk_retcodes)

		if o == cdsdk_retcodes['cdOK']:
			self.sdk_loaded = True
			self.logs.info('...done')
		else:
			self.logs.info('...failed')

	def endSdk(self):
		o = CDFinishSDK()
		self.logs.info('CDFinishSdk returned '+str(hex(o)))


	def listCams(self):
		self.logs.info('listing available cameras')
		# reset device enumerator and get a handle
		h = cdUInt32()
		x = cdUInt32(1)
		o = CDEnumDeviceReset(x, pointer(h))
		if o == cdsdk_retcodes['cdOK']:
			# count number of devices and 
			dev_count = cdUInt32()
			o = CDGetDeviceCount(h, pointer(dev_count))
			if o == cdsdk_retcodes['cdOK']:
				self.logs.info('found '+str(dev_count.value)+' devices')
				sources = []
				for i in range(0,dev_count.value):
					source = cdSourceInfo()
					o = CDEnumDeviceNext(h,source)
					if o == cdsdk_retcodes['cdOK']:
						sources.append(source)
					else:
						pass
				self.devices = sources
				return sources
			else:
				self.logs.info('error getting devices count')
		else:
			self.logs.info('error resetting device enumerator')


	def getDefaultWebcam(self):
		if len(self.devices) > 0:
			if self.name_in_os:
				for c in self.devices:
					if c.NameInOS == self.name_in_os: 
						return c
			if self.name:
				for c in self.devices:
					if c.Name == self.name:
						return c
			if self.port_type:
				for c in self.devices:
					if c.PortType == self.port_type:
						return c
			if self.source_type:
				for c in self.devices:
					if c.SurceType == self.source_type:
						return c
			return self.devices[0]
		# no suitable camera found
		return None

	def selectCam(self, cam_index=-1, cam_name=None, cam_name_in_os=None, cam_port_type=None, cam_source_type=None):
		if cam_index >= 0:
			# camera is specified by its index
			self.cam_selected = self.devices[cam_index]
		else:
			# use some kind of priority for automatic selection
			if cam_name != None:
				self.name == cam_name
			elif cam_name_in_os != None:
				self.name_in_os = cam_name_in_os
			elif cam_port_type != None:
				self.port_type = cam_port_type
			elif cam_source_type != None:
				self.source_type = cam_source_type
			self.cam_selected = self.getDefaultWebcam()
	
	def openCam(self):
		if self.cam_selected:
			devhandle = cdHSource()
			evthandle = cdHandle()
			evtcontext = cdContext()
			o = CDOpenSource(self.cam_selected, devhandle)
			if o == cdsdk_retcodes['cdOK']:
				o = CDLockUI( devhandle )
				if o == cdsdk_retcodes['cdOK']:
					CDRegisterEventCallbackFunction(devhandle,self.callbacks['eventCallbackFunction'],evtcontext,evthandle)
					self.device_handle = devhandle
			
	def startViewFinder(self):
		if self.device_handle and not self.viewfinder_running:
			o = CDEnterReleaseControl(self.device_handle, self.callbacks['releaseEventCallbackFunction'], cdContext())
			if o == cdsdk_retcodes['cdOK']:
				# initialize some internal variables
				self.getMaxZoom()
				self.getZoom()
				# start the viewfinder mode	
				format = cdUInt32(1)	# 0: JPEG, 1: BMP
				o = CDStartViewfinder(self.device_handle, format, self.callbacks['viewFinderCallbackFunction'], cdContext())
				self.viewfinder_running = True

	def setViewFinderTarget(self, obj=None):
		self.vf_target = obj
		

	def stopViewFinder(self):
		self.logs.info('stopping viewfinder mode')
		if self.device_handle:
			self.viewfinder_running = False
			o = CDTermViewfinder(self.device_handle)
			self.logs.info('stop viewfinder returned '+str(o))
			o = CDExitReleaseControl(self.device_handle)
			self.logs.info('exit release control returned '+str(o))

	# Image Shooting Definitions
	# __________________________________________________________________________
	def takePicture(self):
		if not self.release_datakind:
			datakind = cdRelDataKind(cdsdk_constants['cdREL_KIND_PICT_TO_PC'])
			o = CDSelectReleaseDataKind(self.device_handle, datakind)
			if o == cdsdk_retcodes['cdOK']:
				pic_number = cdUInt32()
				o = CDRelease(self.device_handle, True, self.callbacks['progressCallbackFunction'], cdContext(), cdProgressOption(), pic_number)
				self.logs.info('CDRelease returned '+str(o))
				self.logs.info('took picture number '+str(pic_number))
				return self.getTakenPicture(pic_number)

	def getTakenPicture(self, pic_number):
		image_info = cdReleaseImageInfo()
		stg_medium = cdStgMedium()
		#o = CDGetReleasedData(self.device_handle, self.callbacks['progressCallbackFunction'], cdContext(), cdProgressOption(), pointer(image_info), pointer(stg_medium))
		o = CDGetReleasedData(self.device_handle, None, 0, 0, image_info, None)
		self.logs.info('CDGetReleasedData returned '+str(hex(o)))
		self.logs.info('SequenceID: '+str(image_info.SequenceID))
		self.logs.info('DataType: '+str(image_info.DataType))
		self.logs.info('Format: '+str(image_info.Format))
		self.logs.info('DataSize: '+str(image_info.DataSize))
		self.logs.info('FileName: '+str(image_info.FileName))

		if image_info.DataType == cdsdk_constants['cdDATA_TYPE_THUMBNAIL']:
			sz_prefix = 'TH'
			sz_ext = 'JPG'
		elif image_info.DataType == cdsdk_constants['cdDATA_TYPE_PICTURE']:
			sz_prefix = 'FV'
			if image_info.Format == 1:
				sz_ext = 'JPG'
			else:
				sz_ext = 'CRW'
		elif image_info.DataType == cdsdk_constants['cdDATA_TYPE_PLUS_JPEG']:
				sz_prefix = 'FP'
				sz_ext = 'JPG'
		
		output_filename = self.save_path + sz_prefix + self.picsession_prefix + str(len(self.taken_pictures)) + '.' + sz_ext

		#filestream = open(output_filename, 'wb')
		stg_medium.Type = cdsdk_constants['cdMEMTYPE_FILE']
		stg_medium.u.lpszFileName = output_filename #pointer(cdStream())
		o = CDGetReleasedData(self.device_handle, None, cdContext(), cdsdk_constants['cdPROG_REPORT_PERIODICALLY'], image_info, stg_medium)
		self.logs.info('getreleaseddata returned '+str(hex(o)))
		if o == cdsdk_retcodes['cdOK']:
			self.taken_pictures.append(output_filename)
			return len(self.taken_pictures)-1
		else:
			return -1

	def getPicturePath(self, takenpic_index):
		return self.taken_pictures[takenpic_index]




	# Zoom Related Definitions
	# __________________________________________________________________________
	def getMaxZoom(self):
		max_zoom_pos = cdUInt32()
		max_optical_zoom_pos = cdUInt32()
		o = CDGetMaximumZoomPos(self.device_handle, max_zoom_pos, max_optical_zoom_pos)
		if self.use_digital_zoom:
			self.max_zoom_pos = int(max_zoom_pos.value)
		else:
			self.max_zoom_pos = int(max_optical_zoom_pos.value)
		return self.max_zoom_pos		

	def getZoom(self):
		zoom_pos = cdUInt32()
		o = CDGetZoomPos(self.device_handle, zoom_pos)
		self.zoom_pos = int(zoom_pos.value)
		return self.zoom_pos

	def setZoom(self, pos):
		if self.zoom_pos != pos:
			# do the zoom operation
			o = CDSetZoomPos(self.device_handle, c_ulong(pos))
			if o == cdsdk_retcodes['cdOK']:
				self.zoom_pos = pos

	def zoomIn(self):
		self.logs.info('zooming in camera ...')
		if self.zoom_pos < self.max_zoom_pos:
			self.setZoom(self.zoom_pos+1)
		else:
			self.logs.info('not zooming ...')

	def zoomOut(self):
		self.logs.info('zooming out camera ...')
		if self.zoom_pos > 0:
			self.setZoom(self.zoom_pos-1)
		else:
			self.logs.info('not zooming out...')


	def enableFlash(self):
		self.logs.info('setting flash to enabled ...')
		o = CDSetFlashSetting(self.device_handle, cdFlashMode(cdsdk_constants['cdFLASH_MODE_ON']), cdCompensation(cdsdk_constants['cdCOMP_NA']))
		#cdFLASH_MODE_ON

	def disableFlash(self):
		self.logs.info('setting flash to disabled ...')
		o = CDSetFlashSetting(self.device_handle, cdFlashMode(cdsdk_constants['cdFLASH_MODE_OFF']), cdCompensation(cdsdk_constants['cdCOMP_NA']))


	# Callback Definitions
	# __________________________________________________________________________
	# general events
	def eventCallbackFunction(self, event_id, p_event_data, data_size, context):
		# do nothing
		self.logs.info('called generic callback')
		return 0
	# viewfinder data event
	def viewFinderCallbackFunction(self, p_data_buffer, data_size, data_format, context):
		# save data buffer to file
		if self.vf_target:
			#print 'calling a vf_target'
			self.vf_target(string_at(p_data_buffer,data_size))
		else:
			f = open('c:\\temp\\canoncam_'+str(self.dumped_image_count)+'.bmp','wb')
			f.write(string_at(p_data_buffer,data_size))
			f.close()
			self.dumped_image_count = self.dumped_image_count + 1
		return 0
	# release control event
	def releaseEventCallbackFunction(self, event_id, p_event_data, data_size, context):
		# do nothing
		self.logs.info('release event callback')
		return 0
	
	# release shot callback
	def progressCallbackFunction(self, progress, status, context):
		self.logs.info('progress:'+str(progress)+', status:'+str(status)+', context:'+str(context))
		return 0

# _____________________________FUNCTION_END_________________________________

if __name__ == '__main__':
	c = CanonCam()
	cams = c.listCams()
	c.selectCam(cam_index=0)
	c.openCam()
	c.startViewFinder()
	time.sleep(10)
	c.stopViewFinder()
	print 'ok'