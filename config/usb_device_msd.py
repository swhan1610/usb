# USB Device MSD global 
msdInterfacesNumber = 1
msdDescriptorSize = 23
msdEndpointsNumber = 2
msdLunNumberMax = 3
usbDeviceMSDLunCount = 0
msdEndpointsPic32 = 1
msdEndpointsSAM = 2


indexFunction = None
configValue = None
startInterfaceNumber = None
numberOfInterfaces = None
queueSizeRead = None
queueSizeWrite = None
usbDeviceMsdEPNumberBulkOut = None
usbDeviceMsdEPNumberBulkIn = None


def onAttachmentConnected(source, target):

	global indexFunction
	global configValue
	global startInterfaceNumber
	global numberOfInterfaces
	global usbDeviceHidReportType
	global queueSizeRead
	global queueSizeWrite
	global usbDeviceHidBufPool
	global usbDeviceMsdEPNumberBulkOut
	global usbDeviceMsdEPNumberBulkIn
	global msdEndpointsPic32
	global msdEndpointsSAM
	
	dependencyID = source["id"]
	ownerComponent = source["component"]
	remoteComponent = target["component"]
	remoteID = remoteComponent.getID()
	connectID = source["id"]
	targetID = target["id"]
	
	if (dependencyID == "usb_device_dependency"):
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_FUNCTIONS_NUMBER")
		Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_FUNCTIONS_NUMBER")
		Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_FUNCTIONS_NUMBER", readValue + 1, 2)
		
		# Update Total configuration descriptor size 
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_CONFIG_DESCRPTR_SIZE")
		if readValue != None:
			Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_CONFIG_DESCRPTR_SIZE")
			Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_CONFIG_DESCRPTR_SIZE", readValue + msdDescriptorSize , 2)
	
		# Update Total Interfaces number 
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_INTERFACES_NUMBER")
		if readValue != None:
			Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_INTERFACES_NUMBER")
			Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_INTERFACES_NUMBER", readValue + 1 , 2)
			startInterfaceNumber.setValue(readValue, 1)
	
	# Update Total Endpoints used 
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER")
		if readValue != None:
			if any(x in Variables.get("__PROCESSOR") for x in ["PIC32MZ"]):
				Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER")
				Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER", readValue + msdEndpointsPic32 , 2)
				usbDeviceMsdEPNumberBulkIn.setValue(readValue + 1, 1)
				usbDeviceMsdEPNumberBulkOut.setValue(readValue + 1, 1)	
			else:
				Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER")
				Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER", readValue + msdEndpointsSAM , 2)
				usbDeviceMsdEPNumberBulkIn.setValue(readValue + 1, 1)
				usbDeviceMsdEPNumberBulkOut.setValue(readValue + 2, 1)
					
	if (dependencyID == "usb_device_msd_media_dependency"):
		global usbDeviceMSDLunCount
		usbDeviceMSDLunCount = usbDeviceMSDLunCount + 1 
		lunNoSymbol = ownerComponent.getSymbolByID("CONFIG_USB_DEVICE_FUNCTION_MSD_LUN")
		readValue = lunNoSymbol.getValue()
		readValue = readValue + 1
		lunNoSymbol.setValue(readValue, 2)
		
		# update media 
		symbolID = ownerComponent.getSymbolByID("CONFIG_USB_DEVICE_FUNCTION_MSD_LUN_0")
		symbolID.setVisible(True)
		symbolID = ownerComponent.getSymbolByID("USB_DEVICE_FUNCTION_MSD_LUN_MEDIA_TYPE_0")
		symbolID.setVisible(True)
		symbolID.setValue(remoteID.upper(), 1) 
		
		
def onAttachmentDisconnected(source, target):
	global indexFunction
	global configValue
	global startInterfaceNumber
	global numberOfInterfaces
	global usbDeviceHidReportType
	global queueSizeRead
	global queueSizeWrite
	global usbDeviceHidBufPool
	global usbDeviceMsdEPNumberBulkOut
	global usbDeviceMsdEPNumberBulkIn
	global msdEndpointsPic32
	global msdEndpointsSAM
	
	dependencyID = source["id"]
	ownerComponent = source["component"]
	
	if  dependencyID == "usb_device_dependency":
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_FUNCTIONS_NUMBER")
		if readValue!= None:
			Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_FUNCTIONS_NUMBER")
			Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_FUNCTIONS_NUMBER", readValue - 1, 2)
		
		# Update Total configuration descriptor size 
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_CONFIG_DESCRPTR_SIZE")
		if readValue != None:
			Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_CONFIG_DESCRPTR_SIZE")
			Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_CONFIG_DESCRPTR_SIZE", readValue - msdDescriptorSize , 2)
	
		# Update Total Interfaces number 
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_INTERFACES_NUMBER")
		if readValue != None:
			Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_INTERFACES_NUMBER")
			Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_INTERFACES_NUMBER", readValue - 1 , 2)
			startInterfaceNumber.setValue(readValue, 1)
			
		readValue = Database.getSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER")
		if readValue != None:
			if any(x in Variables.get("__PROCESSOR") for x in ["PIC32MZ"]):
				Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER")
				Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER", readValue - msdEndpointsPic32 , 2)
			else:
				Database.clearSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER")
				Database.setSymbolValue("usb_device", "CONFIG_USB_DEVICE_ENDPOINTS_NUMBER", readValue - msdEndpointsSAM , 2)		
			
	if  dependencyID == "usb_device_msd_media_dependency":
		lunNoSymbol = ownerComponent.getSymbolByID("CONFIG_USB_DEVICE_FUNCTION_MSD_LUN")
		readValue = lunNoSymbol.getValue()
		readValue = readValue - 1
		lunNoSymbol.setValue(readValue, 2)
		
	if (dependencyID == "usb_device_msd_media_dependency"):
		global usbDeviceMSDLunCount
		usbDeviceMSDLunCount = usbDeviceMSDLunCount - 1 
		lunNoSymbol = ownerComponent.getSymbolByID("CONFIG_USB_DEVICE_FUNCTION_MSD_LUN")
		readValue = lunNoSymbol.getValue()
		readValue = readValue - 1
		lunNoSymbol.setValue(readValue, 2)
		
		# update media 
		symbolID = ownerComponent.getSymbolByID("CONFIG_USB_DEVICE_FUNCTION_MSD_LUN_0")
		symbolID.setVisible(False)
		symbolID = ownerComponent.getSymbolByID("USB_DEVICE_FUNCTION_MSD_LUN_MEDIA_TYPE_0")
		symbolID.setVisible(False)

	
def destroyComponent(component):
	print ("MSD Function Driver: Destroyed")

def setVisible(symbol, event):
    if (event["value"] == True):
        symbol.setVisible(True)
    else:
        symbol.setVisible(False)
		
# This function is called during component activation */ 	
def instantiateComponent(usbDeviceMsdComponent, index):
	
	global msdInterfacesNumber
	global indexFunction
	global configValue
	global startInterfaceNumber
	global numberOfInterfaces
	global usbDeviceHidReportType
	global queueSizeRead
	global queueSizeWrite
	global usbDeviceHidBufPool
	global usbDeviceMsdEPNumberBulkIn
	global usbDeviceMsdEPNumberBulkOut
	
	# Auto load USB Device Layer 
	res = Database.activateComponents(["usb_device"])

	#Index of this function 
	indexFunction = usbDeviceMsdComponent.createIntegerSymbol("CONFIG_USB_DEVICE_FUNCTION_INDEX", None)
	indexFunction.setVisible(False)
	indexFunction.setMin(0)
	indexFunction.setMax(16)
	indexFunction.setDefaultValue(index)
	
	# Config name: Configuration number
	configValue = usbDeviceMsdComponent.createIntegerSymbol("CONFIG_USB_DEVICE_FUNCTION_CONFIG_VALUE", None)
	configValue.setLabel("Configuration Value")
	configValue.setVisible(False)
	configValue.setMin(1)
	configValue.setMax(16)
	configValue.setDefaultValue(1)
	
	# Adding Start Interface number 
	startInterfaceNumber = usbDeviceMsdComponent.createIntegerSymbol("CONFIG_USB_DEVICE_FUNCTION_INTERFACE_NUMBER", None)
	startInterfaceNumber.setLabel("Start Interface Number")
	startInterfaceNumber.setVisible(False)
	startInterfaceNumber.setMin(0)
	startInterfaceNumber.setDefaultValue(0)
	
	# Adding Number of Interfaces
	numberOfInterfaces = usbDeviceMsdComponent.createIntegerSymbol("CONFIG_USB_DEVICE_FUNCTION_NUMBER_OF_INTERFACES", None)
	numberOfInterfaces.setLabel("Number of Interfaces")
	numberOfInterfaces.setVisible(False)
	numberOfInterfaces.setMin(1)
	numberOfInterfaces.setMax(16)
	numberOfInterfaces.setDefaultValue(msdInterfacesNumber)
	
	# MSD Function driver Number of Logical units  
	usbDeviceMsdNumberOfLogicalUnits = usbDeviceMsdComponent.createIntegerSymbol("CONFIG_USB_DEVICE_FUNCTION_MSD_LUN", None)
	usbDeviceMsdNumberOfLogicalUnits.setLabel("Number of Logical Units")
	usbDeviceMsdNumberOfLogicalUnits.setVisible(True)
	usbDeviceMsdNumberOfLogicalUnits.setMin(0)
	usbDeviceMsdNumberOfLogicalUnits.setUseSingleDynamicValue(True)
	usbDeviceMsdNumberOfLogicalUnits.setDefaultValue(0)
	
	usbDeviceMSDLun_0= usbDeviceMsdComponent.createMenuSymbol("CONFIG_USB_DEVICE_FUNCTION_MSD_LUN_0", usbDeviceMsdNumberOfLogicalUnits)
	usbDeviceMSDLun_0.setVisible(False)
	usbDeviceMSDLun_0.setLabel("LUN_1")
		
	usbDeviceMSDLunMedia_0 = usbDeviceMsdComponent.createStringSymbol("USB_DEVICE_FUNCTION_MSD_LUN_MEDIA_TYPE_0", usbDeviceMSDLun_0)
	usbDeviceMSDLunMedia_0.setLabel("Media Driver")
	usbDeviceMSDLunMedia_0.setReadOnly(True)
	usbDeviceMSDLunMedia_0.setVisible(False)

	# MSD Function driver Bulk IN Endpoint Number 
	usbDeviceMsdEPNumberBulkIn = usbDeviceMsdComponent.createIntegerSymbol("CONFIG_USB_DEVICE_FUNCTION_BULK_IN_ENDPOINT_NUMBER", None)		
	usbDeviceMsdEPNumberBulkIn.setLabel("Bulk IN Endpoint Number")
	usbDeviceMsdEPNumberBulkIn.setVisible(True)
	usbDeviceMsdEPNumberBulkIn.setMin(1)
	usbDeviceMsdEPNumberBulkIn.setDefaultValue(2)
	
	# MSD Function driver Bulk Out Endpoint Number 
	usbDeviceMsdEPNumberBulkOut = usbDeviceMsdComponent.createIntegerSymbol("CONFIG_USB_DEVICE_FUNCTION_BULK_OUT_ENDPOINT_NUMBER", None)		
	usbDeviceMsdEPNumberBulkOut.setLabel("Bulk OUT Endpoint Number")
	usbDeviceMsdEPNumberBulkOut.setVisible(True)
	usbDeviceMsdEPNumberBulkOut.setMin(1)
	usbDeviceMsdEPNumberBulkOut.setDefaultValue(1)
		
		
	############################################################################
	#### Dependency ####
	############################################################################
	# USB DEVICE MSD Common Dependency
	
	numInstances  = Database.getSymbolValue("usb_device_msd", "CONFIG_USB_DEVICE_MSD_INSTANCES")
	if (numInstances == None):
		numInstances = 0
	
	#if numInstances < (index+1):
	Database.clearSymbolValue("usb_device_msd", "CONFIG_USB_DEVICE_MSD_INSTANCES")
	Database.setSymbolValue("usb_device_msd", "CONFIG_USB_DEVICE_MSD_INSTANCES", (index+1), 2)
			
	##############################################################
	# system_definitions.h file for USB Device MSD Function driver   
	##############################################################
	usbDeviceMsdSystemDefFile = usbDeviceMsdComponent.createFileSymbol(None, None)
	usbDeviceMsdSystemDefFile.setType("STRING")
	usbDeviceMsdSystemDefFile.setOutputName("core.LIST_SYSTEM_DEFINITIONS_H_INCLUDES")
	usbDeviceMsdSystemDefFile.setSourcePath("templates/device/msd/system_definitions.h.device_msd_includes.ftl")
	usbDeviceMsdSystemDefFile.setMarkup(True)
	
	
	#############################################################
	# Function Init Entry for MSD 
	#############################################################
	usbDeviceMsdFunInitFile = usbDeviceMsdComponent.createFileSymbol(None, None)
	usbDeviceMsdFunInitFile.setType("STRING")
	usbDeviceMsdFunInitFile.setOutputName("usb_device.LIST_USB_DEVICE_FUNCTION_INIT_ENTRY")
	usbDeviceMsdFunInitFile.setSourcePath("templates/device/msd/system_init_c_device_data_msd_function_init.ftl")
	usbDeviceMsdFunInitFile.setMarkup(True)
	
	
	#############################################################
	# Function Registration table for MSD 
	#############################################################
	usbDeviceMsdFunRegTableFile = usbDeviceMsdComponent.createFileSymbol(None, None)
	usbDeviceMsdFunRegTableFile.setType("STRING")
	usbDeviceMsdFunRegTableFile.setOutputName("usb_device.LIST_USB_DEVICE_FUNCTION_ENTRY")
	usbDeviceMsdFunRegTableFile.setSourcePath("templates/device/msd/system_init_c_device_data_msd_function.ftl")
	usbDeviceMsdFunRegTableFile.setMarkup(True)
	
	#############################################################
	# HS Descriptors for MSD Function 
	#############################################################
	usbDeviceMsdDescriptorHsFile = usbDeviceMsdComponent.createFileSymbol(None, None)
	usbDeviceMsdDescriptorHsFile.setType("STRING")
	usbDeviceMsdDescriptorHsFile.setOutputName("usb_device.LIST_USB_DEVICE_FUNCTION_DESCRIPTOR_HS_ENTRY")
	usbDeviceMsdDescriptorHsFile.setSourcePath("templates/device/msd/system_init_c_device_data_msd_function_descrptr_hs.ftl")
	usbDeviceMsdDescriptorHsFile.setMarkup(True)
	
	#############################################################
	# FS Descriptors for MSD Function 
	#############################################################
	usbDeviceMsdDescriptorFsFile = usbDeviceMsdComponent.createFileSymbol(None, None)
	usbDeviceMsdDescriptorFsFile.setType("STRING")
	usbDeviceMsdDescriptorFsFile.setOutputName("usb_device.LIST_USB_DEVICE_FUNCTION_DESCRIPTOR_FS_ENTRY")
	usbDeviceMsdDescriptorFsFile.setSourcePath("templates/device/msd/system_init_c_device_data_msd_function_descrptr_fs.ftl")
	usbDeviceMsdDescriptorFsFile.setMarkup(True)
	
	
	#############################################################
	# Class code Entry for MSD Function 
	#############################################################
	usbDeviceMsdDescriptorClassCodeFile = usbDeviceMsdComponent.createFileSymbol(None, None)
	usbDeviceMsdDescriptorClassCodeFile.setType("STRING")
	usbDeviceMsdDescriptorClassCodeFile.setOutputName("usb_device.LIST_USB_DEVICE_DESCRIPTOR_CLASS_CODE_ENTRY")
	usbDeviceMsdDescriptorClassCodeFile.setSourcePath("templates/device/msd/system_init_c_device_data_msd_function_class_codes.ftl")
	usbDeviceMsdDescriptorClassCodeFile.setMarkup(True)
	
	################################################
	# USB MSD Function driver Files 
	################################################
	usbDeviceMsdHeaderFile = usbDeviceMsdComponent.createFileSymbol("USB_DEVICE_MSD_HEADER_FILE", None)
	addFileName('usb_device_msd.h', usbDeviceMsdHeaderFile, "middleware/", "/usb/", True, None)
	
	usbMsdHeaderFile = usbDeviceMsdComponent.createFileSymbol("USB_MSD_HEADER_FILE", None)
	addFileName('usb_msd.h', usbMsdHeaderFile, "middleware/", "/usb/", True, None)
	
	usbMsdScsiHeaderFile = usbDeviceMsdComponent.createFileSymbol("USB_MSD_SCSCI_HEADER_FILE", None)
	addFileName('scsi.h', usbMsdScsiHeaderFile, "middleware/", "/usb/", True, None)
	
	usbDeviceMsdSourceFile = usbDeviceMsdComponent.createFileSymbol("USB_DEVICE_MSD_SOURCE_FILE", None)
	addFileName('usb_device_msd.c', usbDeviceMsdSourceFile, "middleware/src/", "/usb/src", True, None)
	
	usbDeviceMsdLocalHeaderFile = usbDeviceMsdComponent.createFileSymbol("USB_DEVICE_MSD_LOCAL_HEADER_FILE", None)
	addFileName('usb_device_msd_local.h', usbDeviceMsdLocalHeaderFile, "middleware/src/", "/usb/src", True, None)
	
	
	# all files go into src/
def addFileName(fileName, symbol, srcPath, destPath, enabled, callback):
	configName1 = Variables.get("__CONFIGURATION_NAME")
	symbol.setProjectPath("config/" + configName1 + destPath)
	symbol.setSourcePath(srcPath + fileName)
	symbol.setOutputName(fileName)
	symbol.setDestPath(destPath)
	if fileName[-2:] == '.h':
		symbol.setType("HEADER")
	else:
		symbol.setType("SOURCE")
	symbol.setEnabled(enabled)
	if callback != None:
		symbol.setDependencies(callback, ["USB_DEVICE_FUNCTION_1_DEVICE_CLASS"])