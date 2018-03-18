# BotAutomation contains functions that assist with mouse clicks, sending keys, etc.

# directx scan codes http://www.gamespp.com/directx/directInputKeyboardScanCodes.html
Return = 0x1C

import ctypes
import time

SendInput = ctypes.windll.user32.SendInput

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)
class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))






# Headers from BotAutomation.h
"""
    static void ColorClick(int x, int y, int color, int timeout);
	static void DragAndDrop(int x1, int y1, int x2, int y2);
    static void MessageInTrade(String^ TradeMessage);
	static void MouseClick(int x, int y);
    static void MouseDoubleClick(int x, int y);
	static void MouseMove(int x, int y);
	static void MouseWheel(int WheelClicks);
	static void NotColorClick(int x, int y, int color, int timeout);
	static void PixelColorBlock(int x, int y, int width, int height, array<int, 2>^  PixelBlock);
	static int PixelSum(int x, int y, int width, int height);
	static int PixelColor(int x, int y);
	static void RightClick(int x, int y);
	static int ScanCommonImagePoints(void);
	static int ScanSpecialImagePoints(void);
	static void ScanItemNumber(int x, int y, array<int, 2>^  PixelBlock);
	static void ScanItemName(int x, int y, array<int, 2>^  PixelBlock);
	static void ScanItemFoil(int x, int y, array<int, 2>^  PixelBlock);
	static void ScanItemSet(int x, int y, array<int, 2>^  PixelBlock);
	static void ScanTotalNumber(int x, int y, array<int, 2>^  PixelBlock);
	static void ScreenShot(System::String ^FolderAddress);
	static void ScreenShot2(System::String ^FolderAddress);
	static void SendKeys(System::String ^StringInput);
	static void Wait(int Wait_ms);
	static void WiggleClick(int x, int y);
	static void WriteBMP(HBITMAP bitmap, HDC hDC, LPTSTR filename);
"""

def main():
    time.sleep(3.0)
    SendInput("W")

    return

if __name__ == "__main__":
    main()