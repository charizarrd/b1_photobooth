from ctypes import *

_stdcall_libraries = {}
_stdcall_libraries['CDSDK.dll'] = WinDLL('CDSDK.dll')
STRING = c_char_p


cdUInt32 = c_ulong
cdError = cdUInt32
class cdVersionInfo(Structure):
    pass
CDStartSDK = _stdcall_libraries['CDSDK.dll'].CDStartSDK
CDStartSDK.restype = cdError
CDStartSDK.argtypes = [POINTER(cdVersionInfo), cdUInt32]
CDFinishSDK = _stdcall_libraries['CDSDK.dll'].CDFinishSDK
CDFinishSDK.restype = cdError
CDFinishSDK.argtypes = []
CDGetSDKVersion = _stdcall_libraries['CDSDK.dll'].CDGetSDKVersion
CDGetSDKVersion.restype = cdError
CDGetSDKVersion.argtypes = [POINTER(cdVersionInfo)]
class cdFunctions(Structure):
    pass
CDGetFunctions = _stdcall_libraries['CDSDK.dll'].CDGetFunctions
CDGetFunctions.restype = cdError
CDGetFunctions.argtypes = [POINTER(cdFunctions)]
cdHandle = cdUInt32
cdHEnum = cdHandle
CDEnumDeviceReset = _stdcall_libraries['CDSDK.dll'].CDEnumDeviceReset
CDEnumDeviceReset.restype = cdError
CDEnumDeviceReset.argtypes = [cdUInt32, POINTER(cdHEnum)]
class cdSourceInfo(Structure):
    pass
CDEnumDeviceNext = _stdcall_libraries['CDSDK.dll'].CDEnumDeviceNext
CDEnumDeviceNext.restype = cdError
CDEnumDeviceNext.argtypes = [cdHEnum, POINTER(cdSourceInfo)]
CDGetDeviceCount = _stdcall_libraries['CDSDK.dll'].CDGetDeviceCount
CDGetDeviceCount.restype = cdError
CDGetDeviceCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumDeviceRelease = _stdcall_libraries['CDSDK.dll'].CDEnumDeviceRelease
CDEnumDeviceRelease.restype = cdError
CDEnumDeviceRelease.argtypes = [cdHEnum]
cdHSource = cdHandle
CDOpenSource = _stdcall_libraries['CDSDK.dll'].CDOpenSource
CDOpenSource.restype = cdError
CDOpenSource.argtypes = [POINTER(cdSourceInfo), POINTER(cdHSource)]
CDCloseSource = _stdcall_libraries['CDSDK.dll'].CDCloseSource
CDCloseSource.restype = cdError
CDCloseSource.argtypes = [cdHSource]
cdEventCallbackFunction = WINFUNCTYPE(cdUInt32, c_ulong, c_void_p, c_ulong, c_ulong)
cdContext = cdUInt32
CDRegisterEventCallbackFunction = _stdcall_libraries['CDSDK.dll'].CDRegisterEventCallbackFunction
CDRegisterEventCallbackFunction.restype = cdError
#CDRegisterEventCallbackFunction.argtypes = [cdHSource, POINTER(cdEventCallbackFunction), cdContext, POINTER(cdHandle)]
CDRegisterEventCallbackFunction.argtypes = [cdHSource, cdEventCallbackFunction, cdContext, POINTER(cdHandle)]
CDUnregisterEventCallbackFunction = _stdcall_libraries['CDSDK.dll'].CDUnregisterEventCallbackFunction
CDUnregisterEventCallbackFunction.restype = cdError
CDUnregisterEventCallbackFunction.argtypes = [cdHSource, cdHandle]
CDEnumDevicePropertyReset = _stdcall_libraries['CDSDK.dll'].CDEnumDevicePropertyReset
CDEnumDevicePropertyReset.restype = cdError
CDEnumDevicePropertyReset.argtypes = [cdHSource, cdUInt32, POINTER(cdHEnum)]
class cdDevicePropertyStruct(Structure):
    pass
CDEnumDevicePropertyNext = _stdcall_libraries['CDSDK.dll'].CDEnumDevicePropertyNext
CDEnumDevicePropertyNext.restype = cdError
CDEnumDevicePropertyNext.argtypes = [cdHEnum, POINTER(cdDevicePropertyStruct)]
CDGetDevicePropertyCount = _stdcall_libraries['CDSDK.dll'].CDGetDevicePropertyCount
CDGetDevicePropertyCount.restype = cdError
CDGetDevicePropertyCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumDevicePropertyRelease = _stdcall_libraries['CDSDK.dll'].CDEnumDevicePropertyRelease
CDEnumDevicePropertyRelease.restype = cdError
CDEnumDevicePropertyRelease.argtypes = [cdHEnum]
cdDevicePropertyID = cdUInt32
cdVoid = None
CDGetDevicePropertyData = _stdcall_libraries['CDSDK.dll'].CDGetDevicePropertyData
CDGetDevicePropertyData.restype = cdError
CDGetDevicePropertyData.argtypes = [cdHSource, cdDevicePropertyID, POINTER(cdUInt32), POINTER(cdVoid), cdUInt32]
CDSetDevicePropertyData = _stdcall_libraries['CDSDK.dll'].CDSetDevicePropertyData
CDSetDevicePropertyData.restype = cdError
CDSetDevicePropertyData.argtypes = [cdHSource, cdDevicePropertyID, POINTER(cdUInt32), POINTER(cdVoid)]
CDEnumSupportedImageSizeReset = _stdcall_libraries['CDSDK.dll'].CDEnumSupportedImageSizeReset
CDEnumSupportedImageSizeReset.restype = cdError
CDEnumSupportedImageSizeReset.argtypes = [cdHSource, cdUInt32, POINTER(cdHEnum)]
class cdImageSizeSpec(Structure):
    pass
CDEnumSupportedImageSizeNext = _stdcall_libraries['CDSDK.dll'].CDEnumSupportedImageSizeNext
CDEnumSupportedImageSizeNext.restype = cdError
CDEnumSupportedImageSizeNext.argtypes = [cdHEnum, POINTER(cdImageSizeSpec)]
CDGetSupportedImageSizeCount = _stdcall_libraries['CDSDK.dll'].CDGetSupportedImageSizeCount
CDGetSupportedImageSizeCount.restype = cdError
CDGetSupportedImageSizeCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumSupportedImageSizeRelease = _stdcall_libraries['CDSDK.dll'].CDEnumSupportedImageSizeRelease
CDEnumSupportedImageSizeRelease.restype = cdError
CDEnumSupportedImageSizeRelease.argtypes = [cdHEnum]
CDLockUI = _stdcall_libraries['CDSDK.dll'].CDLockUI
CDLockUI.restype = cdError
CDLockUI.argtypes = [cdHSource]
CDUnlockUI = _stdcall_libraries['CDSDK.dll'].CDUnlockUI
CDUnlockUI.restype = cdError
CDUnlockUI.argtypes = [cdHSource]
CDSetUILockTimeOutTime = _stdcall_libraries['CDSDK.dll'].CDSetUILockTimeOutTime
CDSetUILockTimeOutTime.restype = cdError
CDSetUILockTimeOutTime.argtypes = [cdHSource, cdUInt32]
cdHItem = cdHandle
cdHVolume = cdHItem
CDFormat = _stdcall_libraries['CDSDK.dll'].CDFormat
CDFormat.restype = cdError
CDFormat.argtypes = [cdHVolume]
CDEnumVolumeReset = _stdcall_libraries['CDSDK.dll'].CDEnumVolumeReset
CDEnumVolumeReset.restype = cdError
CDEnumVolumeReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumVolumeNext = _stdcall_libraries['CDSDK.dll'].CDEnumVolumeNext
CDEnumVolumeNext.restype = cdError
CDEnumVolumeNext.argtypes = [cdHEnum, POINTER(cdHVolume)]
CDGetVolumeCount = _stdcall_libraries['CDSDK.dll'].CDGetVolumeCount
CDGetVolumeCount.restype = cdError
CDGetVolumeCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumVolumeRelease = _stdcall_libraries['CDSDK.dll'].CDEnumVolumeRelease
CDEnumVolumeRelease.restype = cdError
CDEnumVolumeRelease.argtypes = [cdHEnum]
cdChar = c_char
cdVolName = cdChar * 64
CDGetVolumeName = _stdcall_libraries['CDSDK.dll'].CDGetVolumeName
CDGetVolumeName.restype = cdError
CDGetVolumeName.argtypes = [cdHVolume, POINTER(cdVolName)]
class cdVolumeInfo(Structure):
    pass
CDGetVolumeInfo = _stdcall_libraries['CDSDK.dll'].CDGetVolumeInfo
CDGetVolumeInfo.restype = cdError
CDGetVolumeInfo.argtypes = [cdHVolume, POINTER(cdVolumeInfo)]
cdEnumItemOption = cdUInt32
CDEnumItemReset = _stdcall_libraries['CDSDK.dll'].CDEnumItemReset
CDEnumItemReset.restype = cdError
CDEnumItemReset.argtypes = [cdHItem, cdEnumItemOption, POINTER(cdHEnum)]
CDEnumItemNext = _stdcall_libraries['CDSDK.dll'].CDEnumItemNext
CDEnumItemNext.restype = cdError
CDEnumItemNext.argtypes = [cdHEnum, POINTER(cdHItem)]
CDGetItemCount = _stdcall_libraries['CDSDK.dll'].CDGetItemCount
CDGetItemCount.restype = cdError
CDGetItemCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumItemRelease = _stdcall_libraries['CDSDK.dll'].CDEnumItemRelease
CDEnumItemRelease.restype = cdError
CDEnumItemRelease.argtypes = [cdHEnum]
CDEnumImageItemReset = _stdcall_libraries['CDSDK.dll'].CDEnumImageItemReset
CDEnumImageItemReset.restype = cdError
CDEnumImageItemReset.argtypes = [cdHItem, cdUInt32, cdEnumItemOption, POINTER(cdHEnum)]
cdHImageItem = cdHItem
CDEnumImageItemNext = _stdcall_libraries['CDSDK.dll'].CDEnumImageItemNext
CDEnumImageItemNext.restype = cdError
CDEnumImageItemNext.argtypes = [cdHEnum, POINTER(cdHImageItem)]
CDGetImageItemCount = _stdcall_libraries['CDSDK.dll'].CDGetImageItemCount
CDGetImageItemCount.restype = cdError
CDGetImageItemCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumImageItemRelease = _stdcall_libraries['CDSDK.dll'].CDEnumImageItemRelease
CDEnumImageItemRelease.restype = cdError
CDEnumImageItemRelease.argtypes = [cdHEnum]
class cdItemInfo(Structure):
    pass
CDGetItemInfo = _stdcall_libraries['CDSDK.dll'].CDGetItemInfo
CDGetItemInfo.restype = cdError
CDGetItemInfo.argtypes = [cdHItem, POINTER(cdItemInfo)]
class cdStgMedium(Structure):
    pass
cdMemType = cdUInt32
class N11cdStgMedium3DOLLAR_5E(Union):
    pass
class cdStream(Structure):
    pass
N11cdStgMedium3DOLLAR_5E._pack_ = 1
N11cdStgMedium3DOLLAR_5E._fields_ = [
    ('lpszFileName', STRING),
    ('pStream', POINTER(cdStream)),
]
cdStgMedium._pack_ = 1
cdStgMedium._fields_ = [
    ('Type', cdMemType),
    ('u', N11cdStgMedium3DOLLAR_5E),
]
cdUInt16 = c_ushort
cdImageFormat = cdUInt16
CDMakeImageItem = _stdcall_libraries['CDSDK.dll'].CDMakeImageItem
CDMakeImageItem.restype = cdError
CDMakeImageItem.argtypes = [cdStgMedium, cdImageFormat, POINTER(cdHImageItem)]
CDFreeImageItem = _stdcall_libraries['CDSDK.dll'].CDFreeImageItem
CDFreeImageItem.restype = cdError
CDFreeImageItem.argtypes = [cdHImageItem]
CDOpenImage = _stdcall_libraries['CDSDK.dll'].CDOpenImage
CDOpenImage.restype = cdError
CDOpenImage.argtypes = [cdHImageItem]
CDCloseImage = _stdcall_libraries['CDSDK.dll'].CDCloseImage
CDCloseImage.restype = cdError
CDCloseImage.argtypes = [cdHImageItem]
cdHImageData = cdHandle
CDGetThumbnail = _stdcall_libraries['CDSDK.dll'].CDGetThumbnail
CDGetThumbnail.restype = cdError
CDGetThumbnail.argtypes = [cdHImageItem, POINTER(cdHImageData)]
CDGetPicture = _stdcall_libraries['CDSDK.dll'].CDGetPicture
CDGetPicture.restype = cdError
CDGetPicture.argtypes = [cdHImageItem, POINTER(cdHImageData)]
CDGetMovie = _stdcall_libraries['CDSDK.dll'].CDGetMovie
CDGetMovie.restype = cdError
CDGetMovie.argtypes = [cdHImageItem, POINTER(cdHImageData)]
CDGetSound = _stdcall_libraries['CDSDK.dll'].CDGetSound
CDGetSound.restype = cdError
CDGetSound.argtypes = [cdHImageItem, POINTER(cdHImageData)]
CDEnumImageDataInItemReset = _stdcall_libraries['CDSDK.dll'].CDEnumImageDataInItemReset
CDEnumImageDataInItemReset.restype = cdError
CDEnumImageDataInItemReset.argtypes = [cdHImageItem, POINTER(cdHEnum)]
CDEnumImageDataInItemNext = _stdcall_libraries['CDSDK.dll'].CDEnumImageDataInItemNext
CDEnumImageDataInItemNext.restype = cdError
CDEnumImageDataInItemNext.argtypes = [cdHEnum, POINTER(cdHImageData)]
CDGetImageDataInItemCount = _stdcall_libraries['CDSDK.dll'].CDGetImageDataInItemCount
CDGetImageDataInItemCount.restype = cdError
CDGetImageDataInItemCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumImageDataInItemRelease = _stdcall_libraries['CDSDK.dll'].CDEnumImageDataInItemRelease
CDEnumImageDataInItemRelease.restype = cdError
CDEnumImageDataInItemRelease.argtypes = [cdHEnum]
class cdImageDataInfo(Structure):
    pass
CDGetImageDataInfo = _stdcall_libraries['CDSDK.dll'].CDGetImageDataInfo
CDGetImageDataInfo.restype = cdError
CDGetImageDataInfo.argtypes = [cdHImageData, POINTER(cdImageDataInfo)]
cdProgressCallbackFunction = WINFUNCTYPE(cdUInt32, c_ulong, c_ulong, c_ulong)
cdProgressOption = cdUInt32
CDGetImageData = _stdcall_libraries['CDSDK.dll'].CDGetImageData
CDGetImageData.restype = cdError
CDGetImageData.argtypes = [cdHImageData, POINTER(cdStgMedium), POINTER(cdProgressCallbackFunction), cdContext, cdProgressOption]
class cdImageFormatStruct(Structure):
    pass
cdHFolder = cdHItem
cdCompQuality = cdUInt16
cdAddPictureFlags = cdUInt32
class cdAddPictureProps(Structure):
    pass
class cdAddPictureInfo(Structure):
    pass
CDAddPicture = _stdcall_libraries['CDSDK.dll'].CDAddPicture
CDAddPicture.restype = cdError
CDAddPicture.argtypes = [POINTER(cdStgMedium), POINTER(cdImageFormatStruct), cdHVolume, cdHFolder, cdCompQuality, STRING, cdAddPictureFlags, POINTER(cdAddPictureProps), POINTER(cdProgressCallbackFunction), cdContext, cdProgressOption, POINTER(cdAddPictureInfo)]
CDDeleteImage = _stdcall_libraries['CDSDK.dll'].CDDeleteImage
CDDeleteImage.restype = cdError
CDDeleteImage.argtypes = [cdHItem, cdHImageItem]
cdBoolean = cdUInt16
CDIsPrintMarked = _stdcall_libraries['CDSDK.dll'].CDIsPrintMarked
CDIsPrintMarked.restype = cdError
CDIsPrintMarked.argtypes = [cdHImageItem, POINTER(cdBoolean)]
CDIsSlideMarked = _stdcall_libraries['CDSDK.dll'].CDIsSlideMarked
CDIsSlideMarked.restype = cdError
CDIsSlideMarked.argtypes = [cdHImageItem, POINTER(cdBoolean)]
CDIsTransferMarked = _stdcall_libraries['CDSDK.dll'].CDIsTransferMarked
CDIsTransferMarked.restype = cdError
CDIsTransferMarked.argtypes = [cdHImageItem, POINTER(cdBoolean)]
CDEnumBaseImageDataPropertyReset = _stdcall_libraries['CDSDK.dll'].CDEnumBaseImageDataPropertyReset
CDEnumBaseImageDataPropertyReset.restype = cdError
CDEnumBaseImageDataPropertyReset.argtypes = [cdHImageData, POINTER(cdHEnum)]
class cdBaseImagePropertyStruct(Structure):
    pass
CDEnumBaseImageDataPropertyNext = _stdcall_libraries['CDSDK.dll'].CDEnumBaseImageDataPropertyNext
CDEnumBaseImageDataPropertyNext.restype = cdError
CDEnumBaseImageDataPropertyNext.argtypes = [cdHEnum, POINTER(cdBaseImagePropertyStruct)]
CDGetBaseImageDataPropertyCount = _stdcall_libraries['CDSDK.dll'].CDGetBaseImageDataPropertyCount
CDGetBaseImageDataPropertyCount.restype = cdError
CDGetBaseImageDataPropertyCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumBaseImageDataPropertyRelease = _stdcall_libraries['CDSDK.dll'].CDEnumBaseImageDataPropertyRelease
CDEnumBaseImageDataPropertyRelease.restype = cdError
CDEnumBaseImageDataPropertyRelease.argtypes = [cdHEnum]
cdImagePropertyID = cdUInt32
cdBaseImagePropertyID = cdImagePropertyID
CDGetBaseImageDataProperty = _stdcall_libraries['CDSDK.dll'].CDGetBaseImageDataProperty
CDGetBaseImageDataProperty.restype = cdError
CDGetBaseImageDataProperty.argtypes = [cdHImageData, cdBaseImagePropertyID, POINTER(cdUInt32), POINTER(cdVoid)]
CDEnumImageItemPropertyReset = _stdcall_libraries['CDSDK.dll'].CDEnumImageItemPropertyReset
CDEnumImageItemPropertyReset.restype = cdError
CDEnumImageItemPropertyReset.argtypes = [cdHImageItem, POINTER(cdHEnum)]
class cdImagePropertyStruct(Structure):
    pass
CDEnumImageItemPropertyNext = _stdcall_libraries['CDSDK.dll'].CDEnumImageItemPropertyNext
CDEnumImageItemPropertyNext.restype = cdError
CDEnumImageItemPropertyNext.argtypes = [cdHEnum, POINTER(cdImagePropertyStruct)]
CDGetImageItemPropertyCount = _stdcall_libraries['CDSDK.dll'].CDGetImageItemPropertyCount
CDGetImageItemPropertyCount.restype = cdError
CDGetImageItemPropertyCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumImageItemPropertyRelease = _stdcall_libraries['CDSDK.dll'].CDEnumImageItemPropertyRelease
CDEnumImageItemPropertyRelease.restype = cdError
CDEnumImageItemPropertyRelease.argtypes = [cdHEnum]
CDGetImageItemProperty = _stdcall_libraries['CDSDK.dll'].CDGetImageItemProperty
CDGetImageItemProperty.restype = cdError
CDGetImageItemProperty.argtypes = [cdHImageItem, cdImagePropertyID, POINTER(cdUInt32), POINTER(cdVoid)]
CDSetImageItemProperty = _stdcall_libraries['CDSDK.dll'].CDSetImageItemProperty
CDSetImageItemProperty.restype = cdError
CDSetImageItemProperty.argtypes = [cdHImageItem, cdImagePropertyID, POINTER(cdUInt32), POINTER(cdVoid)]
CDFlashImageItemProperty = _stdcall_libraries['CDSDK.dll'].CDFlashImageItemProperty
CDFlashImageItemProperty.restype = cdError
CDFlashImageItemProperty.argtypes = [cdHImageItem]
class cdRect(Structure):
    pass
CDGetThumbnailValidArea = _stdcall_libraries['CDSDK.dll'].CDGetThumbnailValidArea
CDGetThumbnailValidArea.restype = cdError
CDGetThumbnailValidArea.argtypes = [cdHImageItem, POINTER(cdRect)]
cdReleaseEventCallbackFunction = WINFUNCTYPE(cdUInt32, c_ulong, c_void_p, c_ulong, c_ulong)
CDEnterReleaseControl = _stdcall_libraries['CDSDK.dll'].CDEnterReleaseControl
CDEnterReleaseControl.restype = cdError
#CDEnterReleaseControl.argtypes = [cdHSource, POINTER(cdReleaseEventCallbackFunction), cdContext]
CDEnterReleaseControl.argtypes = [cdHSource, cdReleaseEventCallbackFunction, cdContext]
CDExitReleaseControl = _stdcall_libraries['CDSDK.dll'].CDExitReleaseControl
CDExitReleaseControl.restype = cdError
CDExitReleaseControl.argtypes = [cdHSource]
cdRelDataKind = cdUInt16
CDSelectReleaseDataKind = _stdcall_libraries['CDSDK.dll'].CDSelectReleaseDataKind
CDSelectReleaseDataKind.restype = cdError
CDSelectReleaseDataKind.argtypes = [cdHSource, cdRelDataKind]
CDRelease = _stdcall_libraries['CDSDK.dll'].CDRelease
CDRelease.restype = cdError
CDRelease.argtypes = [cdHSource, cdBoolean, POINTER(cdProgressCallbackFunction), cdContext, cdProgressOption, POINTER(cdUInt32)]
class cdReleaseImageInfo(Structure):
    pass
CDGetReleasedData = _stdcall_libraries['CDSDK.dll'].CDGetReleasedData
CDGetReleasedData.restype = cdError
CDGetReleasedData.argtypes = [cdHSource, POINTER(cdProgressCallbackFunction), cdContext, cdProgressOption, POINTER(cdReleaseImageInfo), POINTER(cdStgMedium)]
cdViewFinderCallbackFunction = WINFUNCTYPE(cdUInt32, POINTER(cdVoid), c_ulong, c_ulong, c_ulong)
CDStartViewfinder = _stdcall_libraries['CDSDK.dll'].CDStartViewfinder
CDStartViewfinder.restype = cdError
#CDStartViewfinder.argtypes = [cdHSource, cdUInt32, POINTER(cdViewFinderCallbackFunction), cdContext]
CDStartViewfinder.argtypes = [cdHSource, cdUInt32, cdViewFinderCallbackFunction, cdContext]
CDTermViewfinder = _stdcall_libraries['CDSDK.dll'].CDTermViewfinder
CDTermViewfinder.restype = cdError
CDTermViewfinder.argtypes = [cdHSource]
cdRelViewfinderOutput = cdUInt32
CDSelectViewFinderCameraOutput = _stdcall_libraries['CDSDK.dll'].CDSelectViewFinderCameraOutput
CDSelectViewFinderCameraOutput.restype = cdError
CDSelectViewFinderCameraOutput.argtypes = [cdHSource, cdRelViewfinderOutput]
CDActViewfinderAutoFunctions = _stdcall_libraries['CDSDK.dll'].CDActViewfinderAutoFunctions
CDActViewfinderAutoFunctions.restype = cdError
CDActViewfinderAutoFunctions.argtypes = [cdHSource, cdUInt32]
CDGetMaximumZoomPos = _stdcall_libraries['CDSDK.dll'].CDGetMaximumZoomPos
CDGetMaximumZoomPos.restype = cdError
CDGetMaximumZoomPos.argtypes = [cdHSource, POINTER(cdUInt32), POINTER(cdUInt32)]
CDGetZoomPos = _stdcall_libraries['CDSDK.dll'].CDGetZoomPos
CDGetZoomPos.restype = cdError
CDGetZoomPos.argtypes = [cdHSource, POINTER(cdUInt32)]
class cdURational(Structure):
    pass
CDGetDZoomMagnification = _stdcall_libraries['CDSDK.dll'].CDGetDZoomMagnification
CDGetDZoomMagnification.restype = cdError
CDGetDZoomMagnification.argtypes = [cdHSource, POINTER(cdURational)]
CDSetZoomPos = _stdcall_libraries['CDSDK.dll'].CDSetZoomPos
CDSetZoomPos.restype = cdError
CDSetZoomPos.argtypes = [cdHSource, cdUInt32]
CDAFLock = _stdcall_libraries['CDSDK.dll'].CDAFLock
CDAFLock.restype = cdError
CDAFLock.argtypes = [cdHSource, cdBoolean]
cdImageSize = cdUInt16
CDSetImageFormatAttribute = _stdcall_libraries['CDSDK.dll'].CDSetImageFormatAttribute
CDSetImageFormatAttribute.restype = cdError
CDSetImageFormatAttribute.argtypes = [cdHSource, cdCompQuality, cdImageSize]
CDGetImageFormatAttribute = _stdcall_libraries['CDSDK.dll'].CDGetImageFormatAttribute
CDGetImageFormatAttribute.restype = cdError
CDGetImageFormatAttribute.argtypes = [cdHSource, POINTER(cdCompQuality), POINTER(cdImageSize)]
CDEnumImageFormatAttributeReset = _stdcall_libraries['CDSDK.dll'].CDEnumImageFormatAttributeReset
CDEnumImageFormatAttributeReset.restype = cdError
CDEnumImageFormatAttributeReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumImageFormatAttributeNext = _stdcall_libraries['CDSDK.dll'].CDEnumImageFormatAttributeNext
CDEnumImageFormatAttributeNext.restype = cdError
CDEnumImageFormatAttributeNext.argtypes = [cdHEnum, POINTER(cdCompQuality), POINTER(cdImageSize)]
CDEnumImageFormatAttributeRelease = _stdcall_libraries['CDSDK.dll'].CDEnumImageFormatAttributeRelease
CDEnumImageFormatAttributeRelease.restype = cdError
CDEnumImageFormatAttributeRelease.argtypes = [cdHEnum]
CDGetImageFormatAttributeCount = _stdcall_libraries['CDSDK.dll'].CDGetImageFormatAttributeCount
CDGetImageFormatAttributeCount.restype = cdError
CDGetImageFormatAttributeCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
cdDriveMode = cdUInt16
CDSetDriveMode = _stdcall_libraries['CDSDK.dll'].CDSetDriveMode
CDSetDriveMode.restype = cdError
CDSetDriveMode.argtypes = [cdHSource, cdDriveMode]
CDGetDriveMode = _stdcall_libraries['CDSDK.dll'].CDGetDriveMode
CDGetDriveMode.restype = cdError
CDGetDriveMode.argtypes = [cdHSource, POINTER(cdDriveMode)]
CDEnumDriveModeReset = _stdcall_libraries['CDSDK.dll'].CDEnumDriveModeReset
CDEnumDriveModeReset.restype = cdError
CDEnumDriveModeReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumDriveModeNext = _stdcall_libraries['CDSDK.dll'].CDEnumDriveModeNext
CDEnumDriveModeNext.restype = cdError
CDEnumDriveModeNext.argtypes = [cdHEnum, POINTER(cdDriveMode)]
CDEnumDriveModeRelease = _stdcall_libraries['CDSDK.dll'].CDEnumDriveModeRelease
CDEnumDriveModeRelease.restype = cdError
CDEnumDriveModeRelease.argtypes = [cdHEnum]
CDGetDriveModeCount = _stdcall_libraries['CDSDK.dll'].CDGetDriveModeCount
CDGetDriveModeCount.restype = cdError
CDGetDriveModeCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
cdShootingMode = cdUInt16
CDSetShootingMode = _stdcall_libraries['CDSDK.dll'].CDSetShootingMode
CDSetShootingMode.restype = cdError
CDSetShootingMode.argtypes = [cdHSource, cdShootingMode]
CDGetShootingMode = _stdcall_libraries['CDSDK.dll'].CDGetShootingMode
CDGetShootingMode.restype = cdError
CDGetShootingMode.argtypes = [cdHSource, POINTER(cdShootingMode)]
CDEnumShootingModeReset = _stdcall_libraries['CDSDK.dll'].CDEnumShootingModeReset
CDEnumShootingModeReset.restype = cdError
CDEnumShootingModeReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumShootingModeNext = _stdcall_libraries['CDSDK.dll'].CDEnumShootingModeNext
CDEnumShootingModeNext.restype = cdError
CDEnumShootingModeNext.argtypes = [cdHEnum, POINTER(cdShootingMode)]
CDEnumShootingModeRelease = _stdcall_libraries['CDSDK.dll'].CDEnumShootingModeRelease
CDEnumShootingModeRelease.restype = cdError
CDEnumShootingModeRelease.argtypes = [cdHEnum]
CDGetShootingModeCount = _stdcall_libraries['CDSDK.dll'].CDGetShootingModeCount
CDGetShootingModeCount.restype = cdError
CDGetShootingModeCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
cdRemoteSetAv = cdUInt16
CDSetAvValue = _stdcall_libraries['CDSDK.dll'].CDSetAvValue
CDSetAvValue.restype = cdError
CDSetAvValue.argtypes = [cdHSource, cdRemoteSetAv]
CDGetAvValue = _stdcall_libraries['CDSDK.dll'].CDGetAvValue
CDGetAvValue.restype = cdError
CDGetAvValue.argtypes = [cdHSource, POINTER(cdRemoteSetAv)]
cdRemoteSetTv = cdUInt16
CDSetTvValue = _stdcall_libraries['CDSDK.dll'].CDSetTvValue
CDSetTvValue.restype = cdError
CDSetTvValue.argtypes = [cdHSource, cdRemoteSetTv]
CDGetTvValue = _stdcall_libraries['CDSDK.dll'].CDGetTvValue
CDGetTvValue.restype = cdError
CDGetTvValue.argtypes = [cdHSource, POINTER(cdRemoteSetTv)]
CDEnumAvValueReset = _stdcall_libraries['CDSDK.dll'].CDEnumAvValueReset
CDEnumAvValueReset.restype = cdError
CDEnumAvValueReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumAvValueNext = _stdcall_libraries['CDSDK.dll'].CDEnumAvValueNext
CDEnumAvValueNext.restype = cdError
CDEnumAvValueNext.argtypes = [cdHEnum, POINTER(cdRemoteSetAv)]
CDEnumAvValueRelease = _stdcall_libraries['CDSDK.dll'].CDEnumAvValueRelease
CDEnumAvValueRelease.restype = cdError
CDEnumAvValueRelease.argtypes = [cdHEnum]
CDGetAvValueCount = _stdcall_libraries['CDSDK.dll'].CDGetAvValueCount
CDGetAvValueCount.restype = cdError
CDGetAvValueCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumTvValueReset = _stdcall_libraries['CDSDK.dll'].CDEnumTvValueReset
CDEnumTvValueReset.restype = cdError
CDEnumTvValueReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumTvValueNext = _stdcall_libraries['CDSDK.dll'].CDEnumTvValueNext
CDEnumTvValueNext.restype = cdError
CDEnumTvValueNext.argtypes = [cdHEnum, POINTER(cdRemoteSetTv)]
CDEnumTvValueRelease = _stdcall_libraries['CDSDK.dll'].CDEnumTvValueRelease
CDEnumTvValueRelease.restype = cdError
CDEnumTvValueRelease.argtypes = [cdHEnum]
CDGetTvValueCount = _stdcall_libraries['CDSDK.dll'].CDGetTvValueCount
CDGetTvValueCount.restype = cdError
CDGetTvValueCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
cdCompensation = cdUInt16
CDSetExposureComp = _stdcall_libraries['CDSDK.dll'].CDSetExposureComp
CDSetExposureComp.restype = cdError
CDSetExposureComp.argtypes = [cdHSource, cdCompensation]
CDGetExposureComp = _stdcall_libraries['CDSDK.dll'].CDGetExposureComp
CDGetExposureComp.restype = cdError
CDGetExposureComp.argtypes = [cdHSource, POINTER(cdCompensation)]
CDEnumExposureCompReset = _stdcall_libraries['CDSDK.dll'].CDEnumExposureCompReset
CDEnumExposureCompReset.restype = cdError
CDEnumExposureCompReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumExposureCompNext = _stdcall_libraries['CDSDK.dll'].CDEnumExposureCompNext
CDEnumExposureCompNext.restype = cdError
CDEnumExposureCompNext.argtypes = [cdHEnum, POINTER(cdCompensation)]
CDEnumExposureCompRelease = _stdcall_libraries['CDSDK.dll'].CDEnumExposureCompRelease
CDEnumExposureCompRelease.restype = cdError
CDEnumExposureCompRelease.argtypes = [cdHEnum]
CDGetExposureCompCount = _stdcall_libraries['CDSDK.dll'].CDGetExposureCompCount
CDGetExposureCompCount.restype = cdError
CDGetExposureCompCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
cdWBLightSrc = cdUInt16
CDSetWBSetting = _stdcall_libraries['CDSDK.dll'].CDSetWBSetting
CDSetWBSetting.restype = cdError
CDSetWBSetting.argtypes = [cdHSource, cdWBLightSrc]
CDGetWBSetting = _stdcall_libraries['CDSDK.dll'].CDGetWBSetting
CDGetWBSetting.restype = cdError
CDGetWBSetting.argtypes = [cdHSource, POINTER(cdWBLightSrc)]
CDEnumWBSettingReset = _stdcall_libraries['CDSDK.dll'].CDEnumWBSettingReset
CDEnumWBSettingReset.restype = cdError
CDEnumWBSettingReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumWBSettingNext = _stdcall_libraries['CDSDK.dll'].CDEnumWBSettingNext
CDEnumWBSettingNext.restype = cdError
CDEnumWBSettingNext.argtypes = [cdHEnum, POINTER(cdWBLightSrc)]
CDEnumWBSettingRelease = _stdcall_libraries['CDSDK.dll'].CDEnumWBSettingRelease
CDEnumWBSettingRelease.restype = cdError
CDEnumWBSettingRelease.argtypes = [cdHEnum]
CDGetWBSettingCount = _stdcall_libraries['CDSDK.dll'].CDGetWBSettingCount
CDGetWBSettingCount.restype = cdError
CDGetWBSettingCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
cdAFDistance = cdUInt16
CDSetAFDistanceSetting = _stdcall_libraries['CDSDK.dll'].CDSetAFDistanceSetting
CDSetAFDistanceSetting.restype = cdError
CDSetAFDistanceSetting.argtypes = [cdHSource, cdAFDistance]
CDGetAFDistanceSetting = _stdcall_libraries['CDSDK.dll'].CDGetAFDistanceSetting
CDGetAFDistanceSetting.restype = cdError
CDGetAFDistanceSetting.argtypes = [cdHSource, POINTER(cdAFDistance)]
CDEnumAFDistanceSettingReset = _stdcall_libraries['CDSDK.dll'].CDEnumAFDistanceSettingReset
CDEnumAFDistanceSettingReset.restype = cdError
CDEnumAFDistanceSettingReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumAFDistanceSettingNext = _stdcall_libraries['CDSDK.dll'].CDEnumAFDistanceSettingNext
CDEnumAFDistanceSettingNext.restype = cdError
CDEnumAFDistanceSettingNext.argtypes = [cdHEnum, POINTER(cdAFDistance)]
CDEnumAFDistanceSettingRelease = _stdcall_libraries['CDSDK.dll'].CDEnumAFDistanceSettingRelease
CDEnumAFDistanceSettingRelease.restype = cdError
CDEnumAFDistanceSettingRelease.argtypes = [cdHEnum]
CDGetAFDistanceSettingCount = _stdcall_libraries['CDSDK.dll'].CDGetAFDistanceSettingCount
CDGetAFDistanceSettingCount.restype = cdError
CDGetAFDistanceSettingCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
cdFlashMode = cdUInt16
CDSetFlashSetting = _stdcall_libraries['CDSDK.dll'].CDSetFlashSetting
CDSetFlashSetting.restype = cdError
CDSetFlashSetting.argtypes = [cdHSource, cdFlashMode, cdCompensation]
CDGetFlashSetting = _stdcall_libraries['CDSDK.dll'].CDGetFlashSetting
CDGetFlashSetting.restype = cdError
CDGetFlashSetting.argtypes = [cdHSource, POINTER(cdFlashMode), POINTER(cdCompensation)]
CDEnumFlashSettingReset = _stdcall_libraries['CDSDK.dll'].CDEnumFlashSettingReset
CDEnumFlashSettingReset.restype = cdError
CDEnumFlashSettingReset.argtypes = [cdHSource, POINTER(cdHEnum)]
CDEnumFlashSettingNext = _stdcall_libraries['CDSDK.dll'].CDEnumFlashSettingNext
CDEnumFlashSettingNext.restype = cdError
CDEnumFlashSettingNext.argtypes = [cdHEnum, POINTER(cdFlashMode)]
CDEnumFlashSettingRelease = _stdcall_libraries['CDSDK.dll'].CDEnumFlashSettingRelease
CDEnumFlashSettingRelease.restype = cdError
CDEnumFlashSettingRelease.argtypes = [cdHEnum]
CDGetFlashSettingCount = _stdcall_libraries['CDSDK.dll'].CDGetFlashSettingCount
CDGetFlashSettingCount.restype = cdError
CDGetFlashSettingCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDGetNumAvailableShot = _stdcall_libraries['CDSDK.dll'].CDGetNumAvailableShot
CDGetNumAvailableShot.restype = cdError
CDGetNumAvailableShot.argtypes = [cdHSource, POINTER(cdUInt32)]
CDEnumRelCamSettingReset = _stdcall_libraries['CDSDK.dll'].CDEnumRelCamSettingReset
CDEnumRelCamSettingReset.restype = cdError
CDEnumRelCamSettingReset.argtypes = [cdHSource, POINTER(cdHEnum)]
class cdRelCamSettingStruct(Structure):
    pass
CDEnumRelCamSettingNext = _stdcall_libraries['CDSDK.dll'].CDEnumRelCamSettingNext
CDEnumRelCamSettingNext.restype = cdError
CDEnumRelCamSettingNext.argtypes = [cdHEnum, POINTER(cdRelCamSettingStruct)]
CDGetRelCamSettingCount = _stdcall_libraries['CDSDK.dll'].CDGetRelCamSettingCount
CDGetRelCamSettingCount.restype = cdError
CDGetRelCamSettingCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDEnumRelCamSettingRelease = _stdcall_libraries['CDSDK.dll'].CDEnumRelCamSettingRelease
CDEnumRelCamSettingRelease.restype = cdError
CDEnumRelCamSettingRelease.argtypes = [cdHEnum]
cdRelCamSettingID = cdUInt32
CDGetRelCamSettingData = _stdcall_libraries['CDSDK.dll'].CDGetRelCamSettingData
CDGetRelCamSettingData.restype = cdError
CDGetRelCamSettingData.argtypes = [cdHSource, cdRelCamSettingID, POINTER(cdUInt32), POINTER(cdVoid)]
CDSetRelCamSettingData = _stdcall_libraries['CDSDK.dll'].CDSetRelCamSettingData
CDSetRelCamSettingData.restype = cdError
CDSetRelCamSettingData.argtypes = [cdHSource, cdRelCamSettingID, cdUInt32, POINTER(cdVoid)]
CDEnumRelCamSettingDataReset = _stdcall_libraries['CDSDK.dll'].CDEnumRelCamSettingDataReset
CDEnumRelCamSettingDataReset.restype = cdError
CDEnumRelCamSettingDataReset.argtypes = [cdHSource, cdRelCamSettingID, POINTER(cdHEnum), POINTER(cdUInt32)]
CDEnumRelCamSettingDataNext = _stdcall_libraries['CDSDK.dll'].CDEnumRelCamSettingDataNext
CDEnumRelCamSettingDataNext.restype = cdError
CDEnumRelCamSettingDataNext.argtypes = [cdHEnum, cdUInt32, POINTER(cdVoid)]
CDEnumRelCamSettingDataRelease = _stdcall_libraries['CDSDK.dll'].CDEnumRelCamSettingDataRelease
CDEnumRelCamSettingDataRelease.restype = cdError
CDEnumRelCamSettingDataRelease.argtypes = [cdHEnum]
CDGetRelCamSettingDataCount = _stdcall_libraries['CDSDK.dll'].CDGetRelCamSettingDataCount
CDGetRelCamSettingDataCount.restype = cdError
CDGetRelCamSettingDataCount.argtypes = [cdHEnum, POINTER(cdUInt32)]
CDCreateMemStream = _stdcall_libraries['CDSDK.dll'].CDCreateMemStream
CDCreateMemStream.restype = cdError
CDCreateMemStream.argtypes = [cdUInt32, cdUInt32, POINTER(cdStream)]
CDDestroyMemStream = _stdcall_libraries['CDSDK.dll'].CDDestroyMemStream
CDDestroyMemStream.restype = cdError
CDDestroyMemStream.argtypes = [POINTER(cdStream)]
CDGetStreamInfo = _stdcall_libraries['CDSDK.dll'].CDGetStreamInfo
CDGetStreamInfo.restype = cdError
CDGetStreamInfo.argtypes = [POINTER(cdStream), POINTER(cdUInt32), POINTER(POINTER(cdVoid))]
CDGetImagePropertyPart = _stdcall_libraries['CDSDK.dll'].CDGetImagePropertyPart
CDGetImagePropertyPart.restype = cdError
CDGetImagePropertyPart.argtypes = [cdHImageItem, POINTER(cdStgMedium)]
cdStartSDK = WINFUNCTYPE(cdError, POINTER(cdVersionInfo), c_ulong)
cdFinishSDK = WINFUNCTYPE(cdError)
cdGetSDKVersion = WINFUNCTYPE(cdError, POINTER(cdVersionInfo))
cdCreateMemStream = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdStream))
cdDestroyMemStream = WINFUNCTYPE(cdError, POINTER(cdStream))
cdGetStreamInfo = WINFUNCTYPE(cdError, POINTER(cdStream), POINTER(cdUInt32), POINTER(POINTER(cdVoid)))
cdGetImagePropertyPart = WINFUNCTYPE(cdError, c_ulong, POINTER(cdStgMedium))
cdEnumDeviceReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumDeviceNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdSourceInfo))
cdGetDeviceCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumDeviceRelease = WINFUNCTYPE(cdError, c_ulong)
cdOpenSource = WINFUNCTYPE(cdError, POINTER(cdSourceInfo), POINTER(cdHSource))
cdCloseSource = WINFUNCTYPE(cdError, c_ulong)
cdRegisterEventCallbackFunction = WINFUNCTYPE(cdError, c_ulong, POINTER(cdEventCallbackFunction), c_ulong, POINTER(cdHandle))
cdUnregisterEventCallbackFunction = WINFUNCTYPE(cdError, c_ulong, c_ulong)
cdEnumDevicePropertyReset = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdHEnum))
cdEnumDevicePropertyNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdDevicePropertyStruct))
cdGetDevicePropertyCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumDevicePropertyRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetDevicePropertyData = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdUInt32), POINTER(cdVoid), c_ulong)
cdSetDevicePropertyData = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdUInt32), POINTER(cdVoid))
cdEnumSupportedImageSizeReset = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdHEnum))
cdEnumSupportedImageSizeNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdImageSizeSpec))
cdGetSupportedImageSizeCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumSupportedImageSizeRelease = WINFUNCTYPE(cdError, c_ulong)
cdLockUI = WINFUNCTYPE(cdError, c_ulong)
cdUnlockUI = WINFUNCTYPE(cdError, c_ulong)
cdSetUILockTimeOutTime = WINFUNCTYPE(cdError, c_ulong, c_ulong)
cdFormat = WINFUNCTYPE(cdError, c_ulong)
cdEnumVolumeReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumVolumeNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHVolume))
cdGetVolumeCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumVolumeRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetVolumeName = WINFUNCTYPE(cdError, c_ulong, POINTER(cdVolName))
cdGetVolumeInfo = WINFUNCTYPE(cdError, c_ulong, POINTER(cdVolumeInfo))
cdEnumItemReset = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdHEnum))
cdEnumItemNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHItem))
cdGetItemCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumItemRelease = WINFUNCTYPE(cdError, c_ulong)
cdEnumImageItemReset = WINFUNCTYPE(cdError, c_ulong, c_ulong, c_ulong, POINTER(cdHEnum))
cdEnumImageItemNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHImageItem))
cdGetImageItemCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumImageItemRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetItemInfo = WINFUNCTYPE(cdError, c_ulong, POINTER(cdItemInfo))
cdMakeImageItem = WINFUNCTYPE(cdError, cdStgMedium, c_ushort, POINTER(cdHImageItem))
cdFreeImageItem = WINFUNCTYPE(cdError, c_ulong)
cdOpenImage = WINFUNCTYPE(cdError, c_ulong)
cdCloseImage = WINFUNCTYPE(cdError, c_ulong)
cdGetThumbnail = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHImageData))
cdGetPicture = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHImageData))
cdGetMovie = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHImageData))
cdGetSound = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHImageData))
cdEnumImageDataInItemReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumImageDataInItemNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHImageData))
cdGetImageDataInItemCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumImageDataInItemRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetImageDataInfo = WINFUNCTYPE(cdError, c_ulong, POINTER(cdImageDataInfo))
cdGetImageData = WINFUNCTYPE(cdError, c_ulong, POINTER(cdStgMedium), POINTER(cdProgressCallbackFunction), c_ulong, c_ulong)
cdAddPicture = WINFUNCTYPE(cdError, POINTER(cdStgMedium), POINTER(cdImageFormatStruct), c_ulong, c_ulong, c_ushort, STRING, c_ulong, POINTER(cdAddPictureProps), POINTER(cdProgressCallbackFunction), c_ulong, c_ulong, POINTER(cdAddPictureInfo))
cdDeleteImage = WINFUNCTYPE(cdError, c_ulong, c_ulong)
cdIsPrintMarked = WINFUNCTYPE(cdError, c_ulong, POINTER(cdBoolean))
cdIsSlideMarked = WINFUNCTYPE(cdError, c_ulong, POINTER(cdBoolean))
cdIsTransferMarked = WINFUNCTYPE(cdError, c_ulong, POINTER(cdBoolean))
cdEnumBaseImageDataPropertyReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumBaseImageDataPropertyNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdBaseImagePropertyStruct))
cdGetBaseImageDataPropertyCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumBaseImageDataPropertyRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetBaseImageDataProperty = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdUInt32), POINTER(cdVoid))
cdEnumImageItemPropertyReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumImageItemPropertyNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdImagePropertyStruct))
cdGetImageItemPropertyCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumImageItemPropertyRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetImageItemProperty = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdUInt32), POINTER(cdVoid))
cdSetImageItemProperty = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdUInt32), POINTER(cdVoid))
cdFlashImageItemProperty = WINFUNCTYPE(cdError, c_ulong)
cdGetThumbnailValidArea = WINFUNCTYPE(cdError, c_ulong, POINTER(cdRect))
cdEnterReleaseControl = WINFUNCTYPE(cdError, c_ulong, POINTER(cdReleaseEventCallbackFunction), c_ulong)
cdExitReleaseControl = WINFUNCTYPE(cdError, c_ulong)
cdReleaseControlCap = cdUInt32
cdReleaseControlFaculty = cdReleaseControlCap
cdGetReleaseControlFaculty = WINFUNCTYPE(cdError, c_ulong, POINTER(cdReleaseControlFaculty))
cdSelectReleaseDataKind = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdRelease = WINFUNCTYPE(cdError, c_ulong, c_ushort, POINTER(cdProgressCallbackFunction), c_ulong, c_ulong, POINTER(cdUInt32))
cdGetReleasedData = WINFUNCTYPE(cdError, c_ulong, POINTER(cdProgressCallbackFunction), c_ulong, c_ulong, POINTER(cdReleaseImageInfo), POINTER(cdStgMedium))
cdStartViewfinder = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdViewFinderCallbackFunction), c_ulong)
cdTermViewfinder = WINFUNCTYPE(cdError, c_ulong)
cdSelectViewFinderCameraOutput = WINFUNCTYPE(cdError, c_ulong, c_ulong)
cdActViewfinderAutoFunctions = WINFUNCTYPE(cdError, c_ulong, c_ulong)
cdGetMaximumZoomPos = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32), POINTER(cdUInt32))
cdGetZoomPos = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdGetDZoomMagnification = WINFUNCTYPE(cdError, c_ulong, POINTER(cdURational))
cdSetZoomPos = WINFUNCTYPE(cdError, c_ulong, c_ulong)
cdAFLock = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdSetImageFormatAttribute = WINFUNCTYPE(cdError, c_ulong, c_ushort, c_ushort)
cdGetImageFormatAttribute = WINFUNCTYPE(cdError, c_ulong, POINTER(cdCompQuality), POINTER(cdImageSize))
cdEnumImageFormatAttributeReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumImageFormatAttributeNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdCompQuality), POINTER(cdImageSize))
cdEnumImageFormatAttributeRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetImageFormatAttributeCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdSetDriveMode = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdGetDriveMode = WINFUNCTYPE(cdError, c_ulong, POINTER(cdDriveMode))
cdEnumDriveModeReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumDriveModeNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdDriveMode))
cdEnumDriveModeRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetDriveModeCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdSetShootingMode = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdGetShootingMode = WINFUNCTYPE(cdError, c_ulong, POINTER(cdShootingMode))
cdEnumShootingModeReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumShootingModeNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdShootingMode))
cdEnumShootingModeRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetShootingModeCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdSetAvValue = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdGetAvValue = WINFUNCTYPE(cdError, c_ulong, POINTER(cdRemoteSetAv))
cdSetTvValue = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdGetTvValue = WINFUNCTYPE(cdError, c_ulong, POINTER(cdRemoteSetTv))
cdEnumAvValueReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumAvValueNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdRemoteSetAv))
cdEnumAvValueRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetAvValueCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumTvValueReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumTvValueNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdRemoteSetTv))
cdEnumTvValueRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetTvValueCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdSetExposureComp = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdGetExposureComp = WINFUNCTYPE(cdError, c_ulong, POINTER(cdCompensation))
cdEnumExposureCompReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumExposureCompNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdCompensation))
cdEnumExposureCompRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetExposureCompCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdSetWBSetting = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdGetWBSetting = WINFUNCTYPE(cdError, c_ulong, POINTER(cdWBLightSrc))
cdEnumWBSettingReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumWBSettingNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdWBLightSrc))
cdEnumWBSettingRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetWBSettingCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdSetAFDistanceSetting = WINFUNCTYPE(cdError, c_ulong, c_ushort)
cdGetAFDistanceSetting = WINFUNCTYPE(cdError, c_ulong, POINTER(cdAFDistance))
cdEnumAFDistanceSettingReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumAFDistanceSettingNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdAFDistance))
cdEnumAFDistanceSettingRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetAFDistanceSettingCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdSetFlashSetting = WINFUNCTYPE(cdError, c_ulong, c_ushort, c_ushort)
cdGetFlashSetting = WINFUNCTYPE(cdError, c_ulong, POINTER(cdFlashMode), POINTER(cdCompensation))
cdEnumFlashSettingReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumFlashSettingNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdFlashMode))
cdEnumFlashSettingRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetFlashSettingCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdGetNumAvailableShot = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumRelCamSettingReset = WINFUNCTYPE(cdError, c_ulong, POINTER(cdHEnum))
cdEnumRelCamSettingNext = WINFUNCTYPE(cdError, c_ulong, POINTER(cdRelCamSettingStruct))
cdGetRelCamSettingCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdEnumRelCamSettingRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetRelCamSettingData = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdUInt32), POINTER(cdVoid))
cdSetRelCamSettingData = WINFUNCTYPE(cdError, c_ulong, c_ulong, c_ulong, POINTER(cdVoid))
cdEnumRelCamSettingDataReset = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdHEnum), POINTER(cdUInt32))
cdEnumRelCamSettingDataNext = WINFUNCTYPE(cdError, c_ulong, c_ulong, POINTER(cdVoid))
cdEnumRelCamSettingDataRelease = WINFUNCTYPE(cdError, c_ulong)
cdGetRelCamSettingDataCount = WINFUNCTYPE(cdError, c_ulong, POINTER(cdUInt32))
cdFunctions._fields_ = [
    ('Version', cdUInt32),
    ('pStartSDK', POINTER(cdStartSDK)),
    ('pFinishSDK', POINTER(cdFinishSDK)),
    ('pGetSDKVersion', POINTER(cdGetSDKVersion)),
    ('pCreateMemStream', POINTER(cdCreateMemStream)),
    ('pDestroyMemStream', POINTER(cdDestroyMemStream)),
    ('pGetStreamInfo', POINTER(cdGetStreamInfo)),
    ('pEnumDeviceReset', POINTER(cdEnumDeviceReset)),
    ('pEnumDeviceNext', POINTER(cdEnumDeviceNext)),
    ('pGetDeviceCount', POINTER(cdGetDeviceCount)),
    ('pEnumDeviceRelease', POINTER(cdEnumDeviceRelease)),
    ('pOpenSource', POINTER(cdOpenSource)),
    ('pCloseSource', POINTER(cdCloseSource)),
    ('pRegisterEventCallbackFunction', POINTER(cdRegisterEventCallbackFunction)),
    ('pUnregisterEventCallbackFunction', POINTER(cdUnregisterEventCallbackFunction)),
    ('pEnumDevicePropertyReset', POINTER(cdEnumDevicePropertyReset)),
    ('pEnumDevicePropertyNext', POINTER(cdEnumDevicePropertyNext)),
    ('pGetDevicePropertyCount', POINTER(cdGetDevicePropertyCount)),
    ('pEnumDevicePropertyRelease', POINTER(cdEnumDevicePropertyRelease)),
    ('pGetDevicePropertyData', POINTER(cdGetDevicePropertyData)),
    ('pSetDevicePropertyData', POINTER(cdSetDevicePropertyData)),
    ('pEnumSupportedImageSizeReset', POINTER(cdEnumSupportedImageSizeReset)),
    ('pEnumSupportedImageSizeNext', POINTER(cdEnumSupportedImageSizeNext)),
    ('pGetSupportedImageSizeCount', POINTER(cdGetSupportedImageSizeCount)),
    ('pEnumSupportedImageSizeRelease', POINTER(cdEnumSupportedImageSizeRelease)),
    ('pLockUI', POINTER(cdLockUI)),
    ('pUnlockUI', POINTER(cdUnlockUI)),
    ('pSetUILockTimeOutTime', POINTER(cdSetUILockTimeOutTime)),
    ('pFormat', POINTER(cdFormat)),
    ('pEnumVolumeReset', POINTER(cdEnumVolumeReset)),
    ('pEnumVolumeNext', POINTER(cdEnumVolumeNext)),
    ('pGetVolumeCount', POINTER(cdGetVolumeCount)),
    ('pEnumVolumeRelease', POINTER(cdEnumVolumeRelease)),
    ('pGetVolumeInfo', POINTER(cdGetVolumeInfo)),
    ('pEnumItemReset', POINTER(cdEnumItemReset)),
    ('pEnumItemNext', POINTER(cdEnumItemNext)),
    ('pGetItemCount', POINTER(cdGetItemCount)),
    ('pEnumItemRelease', POINTER(cdEnumItemRelease)),
    ('pEnumImageItemReset', POINTER(cdEnumImageItemReset)),
    ('pEnumImageItemNext', POINTER(cdEnumImageItemNext)),
    ('pGetImageItemCount', POINTER(cdGetImageItemCount)),
    ('pEnumImageItemRelease', POINTER(cdEnumImageItemRelease)),
    ('pGetItemInfo', POINTER(cdGetItemInfo)),
    ('pMakeImageItem', POINTER(cdMakeImageItem)),
    ('pOpenImage', POINTER(cdOpenImage)),
    ('pCloseImage', POINTER(cdCloseImage)),
    ('pGetThumbnail', POINTER(cdGetThumbnail)),
    ('pGetPicture', POINTER(cdGetPicture)),
    ('pGetMovie', POINTER(cdGetMovie)),
    ('pGetSound', POINTER(cdGetSound)),
    ('pEnumImageDataInItemReset', POINTER(cdEnumImageDataInItemReset)),
    ('pEnumImageDataInItemNext', POINTER(cdEnumImageDataInItemNext)),
    ('pGetImageDataInItemCount', POINTER(cdGetImageDataInItemCount)),
    ('pEnumImageDataInItemRelease', POINTER(cdEnumImageDataInItemRelease)),
    ('pGetImageDataInfo', POINTER(cdGetImageDataInfo)),
    ('pGetImageData', POINTER(cdGetImageData)),
    ('pAddPicture', POINTER(cdAddPicture)),
    ('pDeleteImage', POINTER(cdDeleteImage)),
    ('pIsPrintMarked', POINTER(cdIsPrintMarked)),
    ('pIsSlideMarked', POINTER(cdIsSlideMarked)),
    ('pIsTransferMarked', POINTER(cdIsTransferMarked)),
    ('pEnumBaseImageDataPropertyReset', POINTER(cdEnumBaseImageDataPropertyReset)),
    ('pEnumBaseImageDataPropertyNext', POINTER(cdEnumBaseImageDataPropertyNext)),
    ('pGetBaseImageDataPropertyCount', POINTER(cdGetBaseImageDataPropertyCount)),
    ('pEnumBaseImageDataPropertyRelease', POINTER(cdEnumBaseImageDataPropertyRelease)),
    ('pGetBaseImageDataProperty', POINTER(cdGetBaseImageDataProperty)),
    ('pEnumImageItemPropertyReset', POINTER(cdEnumImageItemPropertyReset)),
    ('pEnumImageItemPropertyNext', POINTER(cdEnumImageItemPropertyNext)),
    ('pGetImageItemPropertyCount', POINTER(cdGetImageItemPropertyCount)),
    ('pEnumImageItemPropertyRelease', POINTER(cdEnumImageItemPropertyRelease)),
    ('pGetImageItemProperty', POINTER(cdGetImageItemProperty)),
    ('pSetImageItemProperty', POINTER(cdSetImageItemProperty)),
    ('pFlashImageItemProperty', POINTER(cdFlashImageItemProperty)),
    ('pGetThumbnailValidArea', POINTER(cdGetThumbnailValidArea)),
    ('pEnterReleaseControl', POINTER(cdEnterReleaseControl)),
    ('pExitReleaseControl', POINTER(cdExitReleaseControl)),
    ('pSelectReleaseDataKind', POINTER(cdSelectReleaseDataKind)),
    ('pRelease', POINTER(cdRelease)),
    ('pGetReleasedData', POINTER(cdGetReleasedData)),
    ('pStartViewfinder', POINTER(cdStartViewfinder)),
    ('pTermViewfinder', POINTER(cdTermViewfinder)),
    ('pSelectViewFinderCameraOutput', POINTER(cdSelectViewFinderCameraOutput)),
    ('pActViewfinderAutoFunctions', POINTER(cdActViewfinderAutoFunctions)),
    ('pGetMaximumZoomPos', POINTER(cdGetMaximumZoomPos)),
    ('pGetZoomPos', POINTER(cdGetZoomPos)),
    ('pGetDZoomMagnification', POINTER(cdGetDZoomMagnification)),
    ('pSetZoomPos', POINTER(cdSetZoomPos)),
    ('pSetImageFormatAttribute', POINTER(cdSetImageFormatAttribute)),
    ('pGetImageFormatAttribute', POINTER(cdGetImageFormatAttribute)),
    ('pSetDriveMode', POINTER(cdSetDriveMode)),
    ('pGetDriveMode', POINTER(cdGetDriveMode)),
    ('pSetShootingMode', POINTER(cdSetShootingMode)),
    ('pGetShootingMode', POINTER(cdGetShootingMode)),
    ('pSetAvValue', POINTER(cdSetAvValue)),
    ('pGetAvValue', POINTER(cdGetAvValue)),
    ('pSetTvValue', POINTER(cdSetTvValue)),
    ('pGetTvValue', POINTER(cdGetTvValue)),
    ('pSetExposureComp', POINTER(cdSetExposureComp)),
    ('pGetExposureComp', POINTER(cdGetExposureComp)),
    ('pSetWBSetting', POINTER(cdSetWBSetting)),
    ('pGetWBSetting', POINTER(cdGetWBSetting)),
    ('pSetAFDistanceSetting', POINTER(cdSetAFDistanceSetting)),
    ('pGetAFDistanceSetting', POINTER(cdGetAFDistanceSetting)),
    ('pSetFlashSetting', POINTER(cdSetFlashSetting)),
    ('pGetFlashSetting', POINTER(cdGetFlashSetting)),
    ('pGetNumAvailableShot', POINTER(cdGetNumAvailableShot)),
    ('pEnumRelCamSettingReset', POINTER(cdEnumRelCamSettingReset)),
    ('pEnumRelCamSettingNext', POINTER(cdEnumRelCamSettingNext)),
    ('pGetRelCamSettingCount', POINTER(cdGetRelCamSettingCount)),
    ('pEnumRelCamSettingRelease', POINTER(cdEnumRelCamSettingRelease)),
    ('pGetRelCamSettingData', POINTER(cdGetRelCamSettingData)),
    ('pSetRelCamSettingData', POINTER(cdSetRelCamSettingData)),
    ('pEnumImageFormatAttributeReset', POINTER(cdEnumImageFormatAttributeReset)),
    ('pEnumImageFormatAttributeNext', POINTER(cdEnumImageFormatAttributeNext)),
    ('pEnumImageFormatAttributeRelease', POINTER(cdEnumImageFormatAttributeRelease)),
    ('pGetImageFormatAttributeCount', POINTER(cdGetImageFormatAttributeCount)),
    ('pEnumDriveModeReset', POINTER(cdEnumDriveModeReset)),
    ('pEnumDriveModeNext', POINTER(cdEnumDriveModeNext)),
    ('pEnumDriveModeRelease', POINTER(cdEnumDriveModeRelease)),
    ('pGetDriveModeCount', POINTER(cdGetDriveModeCount)),
    ('pEnumShootingModeReset', POINTER(cdEnumShootingModeReset)),
    ('pEnumShootingModeNext', POINTER(cdEnumShootingModeNext)),
    ('pEnumShootingModeRelease', POINTER(cdEnumShootingModeRelease)),
    ('pGetShootingModeCount', POINTER(cdGetShootingModeCount)),
    ('pEnumAvValueReset', POINTER(cdEnumAvValueReset)),
    ('pEnumAvValueNext', POINTER(cdEnumAvValueNext)),
    ('pEnumAvValueRelease', POINTER(cdEnumAvValueRelease)),
    ('pGetAvValueCount', POINTER(cdGetAvValueCount)),
    ('pEnumTvValueReset', POINTER(cdEnumTvValueReset)),
    ('pEnumTvValueNext', POINTER(cdEnumTvValueNext)),
    ('pEnumTvValueRelease', POINTER(cdEnumTvValueRelease)),
    ('pGetTvValueCount', POINTER(cdGetTvValueCount)),
    ('pEnumExposureCompReset', POINTER(cdEnumExposureCompReset)),
    ('pEnumExposureCompNext', POINTER(cdEnumExposureCompNext)),
    ('pEnumExposureCompRelease', POINTER(cdEnumExposureCompRelease)),
    ('pGetExposureCompCount', POINTER(cdGetExposureCompCount)),
    ('pEnumWBSettingReset', POINTER(cdEnumWBSettingReset)),
    ('pEnumWBSettingNext', POINTER(cdEnumWBSettingNext)),
    ('pEnumWBSettingRelease', POINTER(cdEnumWBSettingRelease)),
    ('pGetWBSettingCount', POINTER(cdGetWBSettingCount)),
    ('pEnumAFDistanceSettingReset', POINTER(cdEnumAFDistanceSettingReset)),
    ('pEnumAFDistanceSettingNext', POINTER(cdEnumAFDistanceSettingNext)),
    ('pEnumAFDistanceSettingRelease', POINTER(cdEnumAFDistanceSettingRelease)),
    ('pGetAFDistanceSettingCount', POINTER(cdGetAFDistanceSettingCount)),
    ('pEnumFlashSettingReset', POINTER(cdEnumFlashSettingReset)),
    ('pEnumFlashSettingNext', POINTER(cdEnumFlashSettingNext)),
    ('pEnumFlashSettingRelease', POINTER(cdEnumFlashSettingRelease)),
    ('pGetFlashSettingCount', POINTER(cdGetFlashSettingCount)),
    ('pEnumRelCamSettingDataReset', POINTER(cdEnumRelCamSettingDataReset)),
    ('pEnumRelCamSettingDataNext', POINTER(cdEnumRelCamSettingDataNext)),
    ('pEnumRelCamSettingDataRelease', POINTER(cdEnumRelCamSettingDataRelease)),
    ('pGetRelCamSettingDataCount', POINTER(cdGetRelCamSettingDataCount)),
    ('pAFLock', POINTER(cdAFLock)),
    ('pGetVolumeName', POINTER(cdGetVolumeName)),
    ('pGetReleaseControlFaculty', POINTER(cdGetReleaseControlFaculty)),
    ('pFreeImageItem', POINTER(cdFreeImageItem)),
    ('pGetImagePropertyPart', POINTER(cdGetImagePropertyPart)),
]
cdGetFunctions = WINFUNCTYPE(cdError, POINTER(cdFunctions))
cdUInt8 = c_ubyte
cdInt8 = c_char
cdWChar = c_ushort
cdInt16 = c_short
cdInt32 = c_long
cdFloat32 = c_float
cdUInt64 = c_ulonglong
cdTime = cdUInt32
cdEventID = cdUInt32
cdReleaseEventID = cdUInt32
cdHLocalHost = cdHSource
cdHRAWData = cdHandle
cdStr31 = cdChar * 32
cdStr63 = cdChar * 64
cdStr255 = cdChar * 256
cdURational._pack_ = 1
cdURational._fields_ = [
    ('Numerator', cdUInt32),
    ('Denominator', cdUInt32),
]
class cdRational(Structure):
    pass
cdRational._pack_ = 1
cdRational._fields_ = [
    ('Numerator', cdInt32),
    ('Denominator', cdInt32),
]
cdSourceType = cdUInt32
cdPortType = cdUInt32
cdDevDataType = cdUInt32
cdPortSelector = cdUInt16
cdModelID = cdUInt32
cdVolHWType = cdUInt16
cdAttribute = cdUInt32
cdItemType = cdUInt32
cdDataType = cdUInt32
cdProgressStatus = cdUInt32
cdSlideShowCap = cdUInt32
cdParseFaculty = cdUInt32
cdFocusMode = cdUInt16
cdCompressionType = cdUInt8
cdPhotoEffect = cdUInt16
cdColorMatrix = cdUInt16
cdRawDevelopFaculty = cdUInt32
cdRAWDevType = cdUInt32
cdDevContrast = cdInt16
cdDevColorDepth = cdInt16
cdDevEnhance = cdInt16
cdDevPhotoEffect = cdPhotoEffect
cdDevHue = cdInt16
cdDevEdgeLevel = cdInt16
cdDevEdgeFreq = cdInt16
cdDevGammaSrc = cdInt16
cdDevColorMatrix = cdColorMatrix
cdDevColorSpace = cdUInt16
cdVersionInfo._pack_ = 1
cdVersionInfo._fields_ = [
    ('Size', cdUInt16),
    ('MajorVersion', cdUInt16),
    ('MinorVersion', cdUInt16),
    ('ReleaseVersion', cdUInt16),
    ('chVersion', cdChar * 32),
]
cdWhence = cdUInt16
cdPermission = cdUInt16
cdSOpen = WINFUNCTYPE(None, c_ulong, c_ushort, POINTER(cdError))
cdSClose = WINFUNCTYPE(None, c_ulong, POINTER(cdError))
cdSRead = WINFUNCTYPE(None, c_ulong, c_void_p, POINTER(cdUInt32), POINTER(cdError))
cdSWrite = WINFUNCTYPE(None, c_ulong, c_void_p, POINTER(cdUInt32), POINTER(cdError))
cdSSeek = WINFUNCTYPE(None, c_ulong, c_ushort, c_long, POINTER(cdError))
cdSTell = WINFUNCTYPE(cdInt32, c_ulong, POINTER(cdError))
cdSProgress = WINFUNCTYPE(None, c_ulong, c_ushort, POINTER(cdError))
cdStream._pack_ = 1
cdStream._fields_ = [
    ('contextH', cdContext),
    ('open', POINTER(cdSOpen)),
    ('close', POINTER(cdSClose)),
    ('read', POINTER(cdSRead)),
    ('write', POINTER(cdSWrite)),
    ('seek', POINTER(cdSSeek)),
    ('tell', POINTER(cdSTell)),
]
class cdSize(Structure):
    pass
cdSize._pack_ = 1
cdSize._fields_ = [
    ('Width', cdUInt32),
    ('Height', cdUInt32),
]
class cdPosition(Structure):
    pass
cdPosition._pack_ = 1
cdPosition._fields_ = [
    ('X', cdInt32),
    ('Y', cdInt32),
]
cdRect._pack_ = 1
cdRect._fields_ = [
    ('Left', cdUInt32),
    ('Right', cdUInt32),
    ('Top', cdUInt32),
    ('Bottom', cdUInt32),
]
cdImageFormatStruct._pack_ = 1
cdImageFormatStruct._fields_ = [
    ('Format', cdImageFormat),
    ('ImageSize', cdSize),
]
cdImageSizeSpec._pack_ = 1
cdImageSizeSpec._fields_ = [
    ('ImageSize', cdImageSize),
    ('Size', cdSize),
    ('SizeName', cdChar * 64),
]
class cdPortDescripSTI(Structure):
    pass
cdPortDescripSTI._pack_ = 1
cdPortDescripSTI._fields_ = [
    ('DataType', cdDevDataType),
    ('DeviceInternalName', cdWChar * 128),
]
class cdPortDescripWIA(Structure):
    pass
cdPortDescripWIA._pack_ = 1
cdPortDescripWIA._fields_ = [
    ('DataType', cdDevDataType),
    ('pDIPDevID', POINTER(cdWChar)),
]
class cdPortDescripRsrvd(Structure):
    pass
cdPortDescripRsrvd._pack_ = 1
cdPortDescripRsrvd._fields_ = [
    ('ModelID', cdUInt32),
    ('szLaunchedDeviceName', cdChar * 76),
]
class cdPortDescripUnion(Union):
    pass
cdPortDescripUnion._fields_ = [
    ('STI', cdPortDescripSTI),
    ('WIA', cdPortDescripWIA),
    ('rsrvd', cdPortDescripRsrvd),
]
cdSourceInfo._pack_ = 1
cdSourceInfo._fields_ = [
    ('SurceType', cdSourceType),
    ('rsrvd', cdUInt32),
    ('Name', cdStr63),
    ('NameInOS', cdStr63),
    ('PortType', cdPortType),
    ('u', cdPortDescripUnion),
]
cdVolumeInfo._pack_ = 1
cdVolumeInfo._fields_ = [
    ('HWtype', cdVolHWType),
    ('isRemoveable', cdBoolean),
    ('TotalSpace', cdUInt64),
    ('FreeSpace', cdUInt64),
    ('Name', cdChar * 64),
]
cdItemInfo._pack_ = 1
cdItemInfo._fields_ = [
    ('Type', cdItemType),
    ('Attributes', cdAttribute),
    ('TimeStamp', cdTime),
    ('Name', cdChar * 512),
    ('Size', cdUInt32),
    ('numThumbnail', cdUInt32),
    ('numPicture', cdUInt32),
    ('numMovie', cdUInt32),
    ('numSound', cdUInt32),
]
cdImageDataInfo._pack_ = 1
cdImageDataInfo._fields_ = [
    ('DataType', cdDataType),
    ('Attributes', cdAttribute),
    ('DataSize', cdUInt32),
    ('TimeStamp', cdTime),
    ('FileName', cdChar * 512),
]
pcdReleaseImageInfo = POINTER(cdReleaseImageInfo)
cdReleaseImageInfo._pack_ = 1
cdReleaseImageInfo._fields_ = [
    ('SequenceID', cdUInt32),
    ('DataType', cdDataType),
    ('Format', cdUInt8),
    ('DataSize', cdUInt32),
    ('FileName', cdChar * 2),
]
cdDevicePropertyStruct._pack_ = 1
cdDevicePropertyStruct._fields_ = [
    ('DevPropID', cdDevicePropertyID),
    ('Access', cdAttribute),
    ('DataSize', cdUInt32),
    ('rsrvd', cdUInt32),
]
cdRelCamSettingStruct._pack_ = 1
cdRelCamSettingStruct._fields_ = [
    ('SettingID', cdRelCamSettingID),
    ('Access', cdAttribute),
    ('rsrvd', cdUInt32),
]
cdImagePropertyStruct._pack_ = 1
cdImagePropertyStruct._fields_ = [
    ('PicPropID', cdImagePropertyID),
    ('Access', cdAttribute),
    ('DataSize', cdUInt32),
    ('rsrvd', cdUInt32),
]
cdBaseImagePropertyStruct._pack_ = 1
cdBaseImagePropertyStruct._fields_ = [
    ('BaseImgPropID', cdBaseImagePropertyID),
    ('DataSize', cdUInt32),
    ('rsrvd', cdUInt32),
]
class cdIIMInfoStruct(Structure):
    pass
cdIIMInfoStruct._pack_ = 1
cdIIMInfoStruct._fields_ = [
    ('RecordNo', cdUInt8),
    ('DataSetNo', cdUInt8),
    ('Access', cdAttribute),
    ('DataSize', cdUInt32),
]
pcdAddPictureProps = POINTER(cdAddPictureProps)
cdAddPictureProps._pack_ = 1
cdAddPictureProps._fields_ = [
    ('Size', cdUInt32),
    ('FilePrefix', cdChar * 4),
    ('RotationAngle', cdInt16),
    ('pOwnerName', STRING),
]
cdAddPictureInfo._pack_ = 1
cdAddPictureInfo._fields_ = [
    ('Path', cdChar * 256),
    ('FileName', cdChar * 256),
    ('FileNumber', cdUInt32),
]
pcdAddPictureInfo = POINTER(cdAddPictureInfo)
class cdPersonalFunction(Structure):
    pass
cdPersonalFunction._pack_ = 1
cdPersonalFunction._fields_ = [
    ('Length', cdUInt16),
    ('PFn_0', cdUInt16),
    ('PFn_1', cdUInt16),
    ('PFn_2', cdUInt16),
    ('PFn_3', cdUInt16),
    ('PFn_4', cdUInt16),
    ('PFn_5', cdUInt16),
    ('PFn_6', cdUInt16),
    ('PFn_7', cdUInt16),
    ('PFn_8', cdUInt16),
    ('PFn_9', cdUInt16),
    ('PFn_10', cdUInt16),
    ('PFn_11', cdUInt16),
    ('PFn_12', cdUInt16),
    ('PFn_13', cdUInt16),
    ('PFn_14', cdUInt16),
    ('PFn_15', cdUInt16),
    ('PFn_16', cdUInt16),
    ('PFn_17', cdUInt16),
    ('PFn_18', cdUInt16),
    ('PFn_19', cdUInt16),
    ('PFn_20', cdUInt16),
    ('PFn_21', cdUInt16),
    ('PFn_22', cdUInt16),
    ('PFn_23', cdUInt16),
    ('PFn_24', cdUInt16),
    ('PFn_25', cdUInt16),
    ('PFn_26', cdUInt16),
    ('PFn_27', cdUInt16),
    ('PFn_28', cdUInt16),
    ('PFn_29', cdUInt16),
    ('PFn_30', cdUInt16),
]
class cdPersonalFunctionValue(Structure):
    pass
cdPersonalFunctionValue._pack_ = 1
cdPersonalFunctionValue._fields_ = [
    ('Length', cdUInt16),
    ('PFn_1_Value', cdUInt16),
    ('PFn_2_Value', cdUInt16),
    ('PFn_3_Value', cdUInt16),
    ('PFn_4_Value_High', cdUInt16),
    ('PFn_4_Value_Low', cdUInt16),
    ('PFn_5_Value_High', cdUInt16),
    ('PFn_5_Value_Low', cdUInt16),
    ('PFn_8_Value', cdUInt16),
    ('PFn_19_Value_High', cdUInt16),
    ('PFn_19_Value_Low', cdUInt16),
    ('PFn_20_Value', cdUInt16),
    ('PFn_23_Value_Timer6', cdUInt16),
    ('PFn_23_Value_Timer16', cdUInt16),
    ('PFn_23_Value_Release', cdUInt16),
    ('PFn_25_Value_AEmode', cdUInt16),
    ('PFn_25_Value_Metering', cdUInt16),
    ('PFn_25_Value_Shutter', cdUInt16),
    ('PFn_25_Value_AFmode', cdUInt16),
    ('PFn_25_Value_AFframe', cdUInt16),
    ('PFn_25_Value_Quality', cdUInt16),
    ('PFn_25_Value_WBmode', cdUInt16),
    ('PFn_25_Value_Develop', cdUInt16),
    ('PFn_25_Value_Matrix', cdUInt16),
    ('PFn_27_Value', cdUInt16),
]
class cdCustomFunction(Structure):
    pass
cdCustomFunction._pack_ = 1
cdCustomFunction._fields_ = [
    ('length', cdUInt16),
    ('CFn_1', cdUInt16),
    ('CFn_2', cdUInt16),
    ('CFn_3', cdUInt16),
    ('CFn_4', cdUInt16),
    ('CFn_5', cdUInt16),
    ('CFn_6', cdUInt16),
    ('CFn_7', cdUInt16),
    ('CFn_8', cdUInt16),
    ('CFn_9', cdUInt16),
    ('CFn_10', cdUInt16),
    ('CFn_11', cdUInt16),
    ('CFn_12', cdUInt16),
    ('CFn_13', cdUInt16),
    ('CFn_14', cdUInt16),
    ('CFn_15', cdUInt16),
]
class cdCustomFunction2(Structure):
    pass
cdCustomFunction2._pack_ = 1
cdCustomFunction2._fields_ = [
    ('length', cdUInt16),
    ('CFn_0', cdUInt16),
    ('CFn_1', cdUInt16),
    ('CFn_2', cdUInt16),
    ('CFn_3', cdUInt16),
    ('CFn_4', cdUInt16),
    ('CFn_5', cdUInt16),
    ('CFn_6', cdUInt16),
    ('CFn_7', cdUInt16),
    ('CFn_8', cdUInt16),
    ('CFn_9', cdUInt16),
    ('CFn_10', cdUInt16),
    ('CFn_11', cdUInt16),
    ('CFn_12', cdUInt16),
    ('CFn_13', cdUInt16),
    ('CFn_14', cdUInt16),
    ('CFn_15', cdUInt16),
    ('CFn_16', cdUInt16),
    ('CFn_17', cdUInt16),
    ('CFn_18', cdUInt16),
    ('CFn_19', cdUInt16),
    ('CFn_20', cdUInt16),
    ('CFn_21', cdUInt16),
]
class cdStitchDesc(Structure):
    pass
cdStitchDesc._pack_ = 1
cdStitchDesc._fields_ = [
    ('NumImages', cdUInt16),
    ('Position', cdInt16),
    ('Order', cdUInt16),
    ('OverlapH', cdUInt16),
    ('OverLapV', cdUInt16),
    ('Configuration', cdUInt16),
]
class cdDevPoint(Structure):
    pass
cdDevPoint._pack_ = 1
cdDevPoint._fields_ = [
    ('x', cdUInt16),
    ('y', cdUInt16),
]
class cdDevLUTPoint(Structure):
    pass
cdDevLUTPoint._fields_ = [
    ('p0', cdDevPoint),
    ('p1', cdDevPoint),
    ('p2', cdDevPoint),
    ('p3', cdDevPoint),
]
class cdDevGammaLUT(Structure):
    pass
cdDevGammaLUT._fields_ = [
    ('r', cdDevLUTPoint),
    ('g', cdDevLUTPoint),
    ('b', cdDevLUTPoint),
]
class cdDevGammaLUTTable(Structure):
    pass
cdDevGammaLUTTable._pack_ = 1
cdDevGammaLUTTable._fields_ = [
    ('Num', cdUInt16),
    ('GammaLUT', cdDevGammaLUT * 1),
]
class cdDevGammaLUTMatching(Structure):
    pass
cdDevGammaLUTMatching._fields_ = [
    ('Right', cdDevGammaLUT),
    ('Left', cdDevGammaLUT),
]
class cdEdgeLevel(Structure):
    pass
cdEdgeLevel._pack_ = 1
cdEdgeLevel._fields_ = [
    ('xyz_hi', cdUInt16),
    ('xyz_lo', cdUInt16),
    ('level', cdUInt16),
]
class cdDevEdgeLevelTable(Structure):
    pass
cdDevEdgeLevelTable._fields_ = [
    ('param', cdEdgeLevel * 5),
]
class cdEdgeFreq(Structure):
    pass
cdEdgeFreq._pack_ = 1
cdEdgeFreq._fields_ = [
    ('filter1_hi', cdUInt16),
    ('filter1_lo', cdUInt16),
    ('filter2_hi', cdUInt16),
    ('filter2_lo', cdUInt16),
    ('x', cdUInt16),
    ('y', cdUInt16),
]
class cdDevEdgeFreqTable(Structure):
    pass
cdDevEdgeFreqTable._fields_ = [
    ('param', cdEdgeFreq * 5),
]
class cdWhiteBalance(Structure):
    pass
cdWhiteBalance._pack_ = 1
cdWhiteBalance._fields_ = [
    ('r', cdUInt16),
    ('g', cdUInt16),
    ('b', cdUInt16),
]
class cdColorCollect(Structure):
    pass
cdColorCollect._pack_ = 1
cdColorCollect._fields_ = [
    ('mat00', cdUInt16),
    ('mat01', cdUInt16),
    ('mat02', cdUInt16),
    ('mat10', cdUInt16),
    ('mat11', cdUInt16),
    ('mat12', cdUInt16),
    ('mat20', cdUInt16),
    ('mat21', cdUInt16),
    ('mat22', cdUInt16),
]
class cdWBParam(Structure):
    pass
cdWBParam._fields_ = [
    ('wb1', cdWhiteBalance),
    ('cc1', cdColorCollect),
    ('wb2', cdWhiteBalance),
    ('cc2', cdColorCollect),
]
class cdDevWBParamTable(Structure):
    pass
cdDevWBParamTable._fields_ = [
    ('Auto', cdWBParam),
    ('Daylight', cdWBParam),
    ('Cloudy', cdWBParam),
    ('Tungsten', cdWBParam),
    ('Fluorescent', cdWBParam),
    ('Flash', cdWBParam),
    ('Manual', cdWBParam),
    ('Monochrome', cdWBParam),
    ('Shade', cdWBParam),
    ('Kelvin', cdWBParam),
    ('PCset1', cdWBParam),
    ('PCset2', cdWBParam),
    ('PCset3', cdWBParam),
    ('T2000K', cdWBParam),
    ('T3000K', cdWBParam),
    ('T4000K', cdWBParam),
    ('T5000K', cdWBParam),
    ('T6000K', cdWBParam),
    ('T7000K', cdWBParam),
    ('T8000K', cdWBParam),
    ('T9000K', cdWBParam),
    ('T10000K', cdWBParam),
    ('T11000K', cdWBParam),
    ('T12000K', cdWBParam),
]
class cdDevWBParamMatching(Structure):
    pass
cdDevWBParamMatching._pack_ = 1
cdDevWBParamMatching._fields_ = [
    ('Modified', cdWBParam),
    ('OffsetR', cdInt16),
    ('OffsetG', cdInt16),
    ('OffsetB', cdInt16),
    ('OffsetCenter', cdUInt16),
]
class cdDevWhiteBalance(Structure):
    pass
cdDevWhiteBalance._pack_ = 1
cdDevWhiteBalance._fields_ = [
    ('r', cdUInt16),
    ('g', cdUInt16),
    ('b', cdUInt16),
]
class cdDevColorCollect(Structure):
    pass
cdDevColorCollect._pack_ = 1
cdDevColorCollect._fields_ = [
    ('mat00', cdUInt16),
    ('mat01', cdUInt16),
    ('mat02', cdUInt16),
    ('mat10', cdUInt16),
    ('mat11', cdUInt16),
    ('mat12', cdUInt16),
    ('mat20', cdUInt16),
    ('mat21', cdUInt16),
    ('mat22', cdUInt16),
]
class cdDevWBParam(Structure):
    pass
cdDevWBParam._fields_ = [
    ('wb1', cdDevWhiteBalance),
    ('cc1', cdDevColorCollect),
    ('wb2', cdDevWhiteBalance),
    ('cc2', cdDevColorCollect),
]
class cdDevParamWBCoefficient(Structure):
    pass
pcdDevParamWBCoefficient = POINTER(cdDevParamWBCoefficient)
cdDevParamWBCoefficient._pack_ = 1
cdDevParamWBCoefficient._fields_ = [
    ('Type', cdUInt32),
    ('Size', cdUInt32),
    ('Data', cdUInt8 * 1),
]
class cdUserColorMatrix(Structure):
    pass
cdUserColorMatrix._pack_ = 1
cdUserColorMatrix._fields_ = [
    ('Index', cdUInt32),
    ('ColorSpace', cdUInt32),
    ('ColorDepth', cdInt32),
    ('ColorTone', cdInt32),
]
class cdJpegQuality(Structure):
    pass
cdJpegQuality._pack_ = 1
cdJpegQuality._fields_ = [
    ('LargeJpegQuality', cdUInt16),
    ('Medium1JpegQuality', cdUInt16),
    ('Medium2JpegQuality', cdUInt16),
    ('SmallJpegQuality', cdUInt16),
]
class cdWhiteBalanceShift(Structure):
    pass
cdWhiteBalanceShift._pack_ = 1
cdWhiteBalanceShift._fields_ = [
    ('ABLevel', cdUInt32),
    ('MGLevel', cdUInt32),
]
__all__ = ['CDGetExposureCompCount', 'cdFloat32',
           'cdSelectReleaseDataKind', 'cdProgressCallbackFunction',
           'cdGetAFDistanceSettingCount', 'cdSSeek', 'cdRemoteSetTv',
           'cdSProgress', 'cdEnumImageFormatAttributeRelease',
           'cdDevEdgeFreqTable', 'cdDevColorMatrix',
           'cdSetExposureComp', 'CDGetItemCount', 'cdGetPicture',
           'cdEnumImageItemReset', 'cdInt32',
           'CDEnumDevicePropertyRelease', 'CDEnumWBSettingNext',
           'CDEnumImageDataInItemRelease', 'cdHandle',
           'CDEnumRelCamSettingNext', 'cdEnumItemNext',
           'CDEnumDriveModeNext', 'CDEnumShootingModeNext',
           'cdDataType', 'CDEnumRelCamSettingDataRelease',
           'cdSourceType', 'CDGetTvValueCount', 'cdDevLUTPoint',
           'cdSWrite', 'cdDevicePropertyStruct', 'CDLockUI',
           'CDGetImageItemPropertyCount', 'cdUInt8',
           'CDGetVolumeInfo', 'CDGetShootingMode',
           'cdSetAFDistanceSetting', 'cdTermViewfinder',
           'CDEnumExposureCompRelease', 'cdGetImageItemProperty',
           'cdSourceInfo', 'CDGetAFDistanceSetting',
           'CDFreeImageItem', 'cdHRAWData', 'CDSetTvValue',
           'cdIsTransferMarked', 'cdUnlockUI',
           'cdSetImageFormatAttribute', 'cdDestroyMemStream',
           'cdGetImageFormatAttribute', 'CDCreateMemStream',
           'cdGetDriveModeCount', 'cdEnumImageFormatAttributeNext',
           'cdBoolean', 'CDExitReleaseControl', 'cdPermission',
           'CDEnumImageItemPropertyReset',
           'CDGetImageDataInItemCount', 'cdDevWBParamTable',
           'cdRelCamSettingStruct', 'cdVersionInfo',
           'CDGetMaximumZoomPos', 'cdPortDescripUnion',
           'CDSetImageFormatAttribute', 'cdAFDistance',
           'cdEnumBaseImageDataPropertyNext', 'cdPosition',
           'cdSetShootingMode', 'CDEnumImageItemPropertyRelease',
           'CDEnumAFDistanceSettingRelease', 'cdSTell',
           'CDEnumImageDataInItemNext', 'cdDevPoint',
           'cdEnumDevicePropertyRelease', 'cdEnumWBSettingNext',
           'cdEnumTvValueNext', 'CDGetImageItemCount',
           'cdEnumWBSettingRelease', 'CDSetZoomPos',
           'cdSetDevicePropertyData', 'CDEnumRelCamSettingDataNext',
           'cdDevGammaLUT', 'cdDevPhotoEffect', 'cdEnumItemOption',
           'cdInt8', 'cdRational', 'CDOpenImage', 'cdSize',
           'CDGetWBSetting', 'cdIsSlideMarked', 'cdReleaseEventID',
           'cdFocusMode', 'cdEnumDeviceRelease', 'cdGetVolumeName',
           'cdDevColorCollect', 'CDActViewfinderAutoFunctions',
           'cdGetSDKVersion', 'CDSetDevicePropertyData',
           'CDSetExposureComp', 'cdUnregisterEventCallbackFunction',
           'CDGetAvValueCount', 'cdGetExposureComp',
           'pcdAddPictureInfo', 'CDEnumWBSettingReset',
           'cdGetThumbnailValidArea', 'cdGetReleaseControlFaculty',
           'cdFinishSDK', 'cdAddPictureFlags',
           'CDEnumFlashSettingReset', 'cdSRead',
           'cdEnumShootingModeRelease', 'cdDevDataType',
           'cdGetImageDataInfo', 'cdGetTvValue',
           'CDUnregisterEventCallbackFunction',
           'cdEnumTvValueRelease', 'cdDevWBParamMatching',
           'cdGetSound', 'CDTermViewfinder', 'CDEnumExposureCompNext',
           'CDGetSupportedImageSizeCount', 'CDEnumTvValueRelease',
           'cdEnumFlashSettingNext', 'cdGetRelCamSettingData',
           'cdHFolder', 'cdEnumSupportedImageSizeNext',
           'cdDevParamWBCoefficient', 'cdEnumImageDataInItemRelease',
           'cdSlideShowCap', 'cdEnumRelCamSettingNext',
           'cdEnumDriveModeNext', 'CDAddPicture',
           'cdEnumRelCamSettingRelease',
           'CDGetBaseImageDataPropertyCount',
           'cdEventCallbackFunction', 'CDCloseImage',
           'cdGetTvValueCount', 'CDFlashImageItemProperty',
           'cdReleaseImageInfo', 'cdDevEnhance', 'cdLockUI',
           'cdCustomFunction2', 'N11cdStgMedium3DOLLAR_5E',
           'cdStgMedium', 'cdGetBaseImageDataProperty',
           'cdGetVolumeInfo', 'CDGetVolumeCount',
           'CDEnumSupportedImageSizeRelease', 'CDGetStreamInfo',
           'CDIsPrintMarked', 'CDSetUILockTimeOutTime',
           'CDEnumRelCamSettingRelease', 'CDGetImageFormatAttribute',
           'cdGetDriveMode', 'CDGetFunctions', 'cdSetDriveMode',
           'CDEnumImageFormatAttributeRelease',
           'cdGetImagePropertyPart', 'cdURational',
           'cdGetWBSettingCount', 'cdGetImageDataInItemCount',
           'cdFlashMode', 'CDSetDriveMode', 'CDEnumVolumeNext',
           'cdSetAvValue', 'cdEnumAFDistanceSettingRelease',
           'cdParseFaculty', 'CDSetAFDistanceSetting',
           'cdProgressOption', 'pcdReleaseImageInfo', 'cdUInt16',
           'CDUnlockUI', 'cdFlashImageItemProperty',
           'CDEnumAvValueReset', 'cdImagePropertyStruct',
           'CDGetDriveModeCount', 'CDEnumImageItemReset',
           'cdGetNumAvailableShot', 'cdSClose', 'CDGetDriveMode',
           'cdUserColorMatrix', 'cdGetVolumeCount', 'cdWChar',
           'cdGetStreamInfo', 'CDGetImageData', 'cdJpegQuality',
           'cdEnumShootingModeNext', 'cdCustomFunction',
           'cdDevWhiteBalance', 'cdContext', 'CDEnumFlashSettingNext',
           'cdEdgeLevel', 'cdVolumeInfo', 'cdGetDZoomMagnification',
           'CDSelectViewFinderCameraOutput',
           'CDEnumSupportedImageSizeNext',
           'cdEnumSupportedImageSizeReset', 'cdDevicePropertyID',
           'cdItemInfo', 'cdPortDescripWIA', 'cdEnumItemRelease',
           'CDSelectReleaseDataKind', 'CDEnumDriveModeReset',
           'cdEnumExposureCompRelease', 'cdStartSDK',
           'cdGetAFDistanceSetting', 'cdFreeImageItem',
           'cdGetFunctions', 'CDAFLock', 'cdEnumVolumeReset',
           'cdEnumItemReset', 'cdEnumFlashSettingReset',
           'cdDevGammaSrc', 'cdGetDeviceCount', 'cdReleaseControlCap',
           'cdPortSelector', 'cdStr63', 'cdGetDevicePropertyData',
           'cdSOpen', 'cdGetSupportedImageSizeCount',
           'CDEnumDeviceRelease', 'CDEnumAvValueNext',
           'CDEnumRelCamSettingDataReset', 'CDGetImagePropertyPart',
           'cdRemoteSetAv', 'CDGetDeviceCount',
           'cdEnumImageItemPropertyRelease',
           'cdReleaseControlFaculty', 'cdMakeImageItem',
           'CDGetDevicePropertyCount', 'cdCloseSource',
           'CDGetImageItemProperty', 'cdWhiteBalance',
           'cdProgressStatus', 'cdInt16', 'cdBaseImagePropertyID',
           'cdEnumImageFormatAttributeReset',
           'CDEnumImageDataInItemReset', 'CDSetAvValue',
           'cdGetItemCount', 'cdOpenSource', 'cdShootingMode',
           'cdOpenImage', 'cdRegisterEventCallbackFunction',
           'cdIsPrintMarked', 'cdGetWBSetting', 'cdWhiteBalanceShift',
           'cdGetAvValue', 'cdAddPictureInfo',
           'cdEnumSupportedImageSizeRelease',
           'CDEnumBaseImageDataPropertyNext', 'CDDeleteImage',
           'CDGetRelCamSettingData', 'cdRelease',
           'cdEnumDriveModeReset', 'cdEnumDevicePropertyNext',
           'cdEnumAFDistanceSettingNext', 'cdStitchDesc',
           'cdHImageItem', 'CDEnumTvValueNext', 'cdEdgeFreq',
           'CDGetAFDistanceSettingCount', 'CDSetFlashSetting',
           'cdMemType', 'cdDevGammaLUTTable', 'cdEnumAvValueNext',
           'cdEnumRelCamSettingDataReset', 'cdItemType',
           'cdRawDevelopFaculty', 'CDGetShootingModeCount',
           'cdHVolume', 'cdFormat', 'cdHSource', 'CDGetItemInfo',
           'cdAttribute', 'cdEnumImageItemPropertyReset',
           'cdGetRelCamSettingCount', 'cdEnumExposureCompNext',
           'cdPortDescripSTI', 'cdEnumExposureCompReset',
           'cdEnumImageDataInItemReset', 'cdSetRelCamSettingData',
           'cdEnumDriveModeRelease', 'cdEnumImageDataInItemNext',
           'cdGetRelCamSettingDataCount', 'cdGetExposureCompCount',
           'cdEnumImageItemPropertyNext', 'cdEnumDeviceReset',
           'cdGetImageItemCount', 'cdStream',
           'cdGetBaseImageDataPropertyCount', 'CDFinishSDK',
           'CDIsTransferMarked', 'cdVolHWType',
           'CDEnumImageFormatAttributeReset', 'CDDestroyMemStream',
           'cdEnumRelCamSettingDataNext', 'CDStartViewfinder',
           'cdColorCollect', 'CDSetRelCamSettingData',
           'CDGetImageDataInfo', 'cdEnumAFDistanceSettingReset',
           'CDGetTvValue', 'CDEnumImageFormatAttributeNext',
           'cdGetAvValueCount', 'cdDevHue', 'cdCompressionType',
           'cdIIMInfoStruct', 'cdHItem', 'cdAFLock',
           'CDGetImageFormatAttributeCount', 'cdGetFlashSetting',
           'CDSetShootingMode', 'cdGetShootingModeCount', 'cdStr255',
           'CDEnumImageItemRelease', 'CDOpenSource',
           'cdAddPictureProps', 'CDEnumVolumeRelease', 'cdWhence',
           'cdEnumDeviceNext', 'cdSetWBSetting',
           'cdEnumWBSettingReset', 'CDGetAvValue', 'cdSetTvValue',
           'CDEnumDevicePropertyNext', 'cdEnumDevicePropertyReset',
           'cdImageDataInfo', 'CDEnumAvValueRelease',
           'cdExitReleaseControl', 'CDEnumItemRelease', 'CDStartSDK',
           'cdEnumRelCamSettingReset', 'cdGetMaximumZoomPos',
           'CDGetVolumeName', 'cdVolName', 'CDEnumItemReset',
           'cdEnumImageItemNext', 'cdFunctions', 'cdDevEdgeFreq',
           'cdError', 'cdGetFlashSettingCount', 'cdRelDataKind',
           'CDEnumRelCamSettingReset', 'cdAddPicture',
           'CDEnumDeviceReset', 'cdSetZoomPos', 'cdEnumTvValueReset',
           'cdDeleteImage', 'CDEnumImageItemNext', 'cdGetThumbnail',
           'cdEnumImageItemRelease', 'cdImagePropertyID',
           'cdEnumVolumeRelease', 'cdPhotoEffect', 'CDGetSound',
           'CDEnumImageItemPropertyNext', 'CDGetSDKVersion',
           'CDEnumAFDistanceSettingReset', 'cdEventID',
           'cdEnumFlashSettingRelease', 'cdImageSizeSpec',
           'cdActViewfinderAutoFunctions',
           'cdEnumBaseImageDataPropertyReset',
           'cdSetImageItemProperty', 'cdDevWBParam',
           'CDEnumShootingModeRelease', 'CDGetNumAvailableShot',
           'CDGetZoomPos', 'cdHLocalHost', 'CDCloseSource',
           'cdImageFormatStruct', 'CDEnumFlashSettingRelease',
           'cdDevColorSpace', 'cdUInt32', 'cdRelViewfinderOutput',
           'cdColorMatrix', 'cdCreateMemStream',
           'CDGetBaseImageDataProperty', 'CDGetPicture',
           'CDEnumDeviceNext', 'CDSetWBSetting',
           'CDEnumBaseImageDataPropertyReset', 'cdEnumAvValueReset',
           'CDEnumDevicePropertyReset', 'CDFormat',
           'CDGetExposureComp', 'CDGetWBSettingCount',
           'CDEnumAFDistanceSettingNext', 'CDGetDZoomMagnification',
           'cdImageSize', 'cdRect', 'cdCloseImage',
           'cdGetImageFormatAttributeCount', 'cdGetMovie',
           'CDEnumExposureCompReset', 'cdDevGammaLUTMatching',
           'cdChar', 'CDEnumDriveModeRelease',
           'CDEnumShootingModeReset', 'cdSetUILockTimeOutTime',
           'cdEnumRelCamSettingDataRelease', 'cdSetFlashSetting',
           'cdCompensation', 'cdPortType', 'CDGetReleasedData',
           'cdGetItemInfo', 'cdEnumBaseImageDataPropertyRelease',
           'CDGetThumbnail', 'cdStr31', 'cdVoid',
           'cdGetImageItemPropertyCount', 'cdModelID',
           'CDRegisterEventCallbackFunction',
           'cdBaseImagePropertyStruct', 'CDIsSlideMarked',
           'cdGetShootingMode', 'CDEnumTvValueReset',
           'CDEnumWBSettingRelease', 'cdTime', 'cdDevEdgeLevelTable',
           'cdReleaseEventCallbackFunction', 'CDGetFlashSetting',
           'cdEnterReleaseControl', 'cdWBParam', 'cdDriveMode',
           'CDSetImageItemProperty', 'cdEnumVolumeNext',
           'CDEnumBaseImageDataPropertyRelease', 'CDRelease',
           'cdPersonalFunction', 'CDEnumSupportedImageSizeReset',
           'cdDevColorDepth', 'cdImageFormat', 'CDEnumItemNext',
           'cdDevContrast', 'CDEnterReleaseControl',
           'cdRelCamSettingID', 'CDEnumVolumeReset',
           'cdEnumAvValueRelease', 'cdCompQuality', 'cdRAWDevType',
           'cdUInt64', 'CDMakeImageItem', 'cdGetDevicePropertyCount',
           'pcdDevParamWBCoefficient', 'CDGetMovie', 'cdDevEdgeLevel',
           'cdGetImageData', 'CDGetDevicePropertyData',
           'cdEnumShootingModeReset', 'CDGetThumbnailValidArea',
           'CDGetRelCamSettingCount', 'CDGetFlashSettingCount',
           'cdViewFinderCallbackFunction', 'cdWBLightSrc',
           'cdGetReleasedData', 'pcdAddPictureProps', 'cdHEnum',
           'cdSelectViewFinderCameraOutput',
           'cdPersonalFunctionValue', 'cdPortDescripRsrvd',
           'cdStartViewfinder', 'cdGetZoomPos', 'cdHImageData',
           'CDGetRelCamSettingDataCount']
