<#--
/*******************************************************************************
  USB Device Freemarker Template File

  Company:
    Microchip Technology Inc.

  File Name:
    system_config.h.device_audio.ftl

  Summary:
    USB Device Freemarker Template File

  Description:
    This file contains configurations necessary to run the system.  It
    implements the "SYS_Initialize" function, configuration bits, and allocates
    any necessary global system resources, such as the systemObjects structure
    that contains the object handles to all the MPLAB Harmony module objects in
    the system.
*******************************************************************************/

/*******************************************************************************
* Copyright (C) 2019 Microchip Technology Inc. and its subsidiaries.
*
* Subject to your compliance with these terms, you may use Microchip software
* and any derivatives exclusively with Microchip products. It is your
* responsibility to comply with third party license terms applicable to your
* use of third party software (including open source software) that may
* accompany Microchip software.
*
* THIS SOFTWARE IS SUPPLIED BY MICROCHIP "AS IS". NO WARRANTIES, WHETHER
* EXPRESS, IMPLIED OR STATUTORY, APPLY TO THIS SOFTWARE, INCLUDING ANY IMPLIED
* WARRANTIES OF NON-INFRINGEMENT, MERCHANTABILITY, AND FITNESS FOR A
* PARTICULAR PURPOSE.
*
* IN NO EVENT WILL MICROCHIP BE LIABLE FOR ANY INDIRECT, SPECIAL, PUNITIVE,
* INCIDENTAL OR CONSEQUENTIAL LOSS, DAMAGE, COST OR EXPENSE OF ANY KIND
* WHATSOEVER RELATED TO THE SOFTWARE, HOWEVER CAUSED, EVEN IF MICROCHIP HAS
* BEEN ADVISED OF THE POSSIBILITY OR THE DAMAGES ARE FORESEEABLE. TO THE
* FULLEST EXTENT ALLOWED BY LAW, MICROCHIP'S TOTAL LIABILITY ON ALL CLAIMS IN
* ANY WAY RELATED TO THIS SOFTWARE WILL NOT EXCEED THE AMOUNT OF FEES, IF ANY,
* THAT YOU HAVE PAID DIRECTLY TO MICROCHIP FOR THIS SOFTWARE.
 *******************************************************************************/
-->
<#if CONFIG_USB_DEVICE_FUNCTION_AUDIO_DEVICE_TYPE == "Audio v1.0 USB Headset">
/* USB Device Audio Headset Descriptor macros for Audio Function driver instance ${CONFIG_USB_DEVICE_FUNCTION_INDEX} */ 
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_CONTROL_INTERFACE_ID           0x00
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_INPUT_TERMINAL_ID              0x01
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_FEATURE_UNIT_ID                0x02
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_OUTPUT_TERMINAL_ID                0x03
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_INPUT_TERMINAL_MICROPHONE_ID      0x04    
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_FEATURE_UNIT_MICROPHONE_ID        0x05
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_OUTPUT_TERMINAL_MICROPHONE_ID     0x06    
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_FEATURE_UNIT_SIDE_TONING_ID       0x07    
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_MIXER_UNIT_ID                     0x08    
#define USB_DEVICE_AUDIO_IDX${CONFIG_USB_DEVICE_FUNCTION_INDEX}_DESCRIPTOR_STREAMING_INTERFACE_ID_1       0x01
</#if>
<#--
/*******************************************************************************
 End of File
*/
-->

