/*
  The point of this program is to make a bot that will automaticall type in !disboard every two hours(120mins) 
  Question: How would I actually have the os think that I typed in a key?
  
  I have all the keyboard hexadecimal codes provided by microsoft and I have comments 
  to outline what needs to be done I just don't know what I would have to use to do it
*/

#include <iostream>
#include <windows.h>
#include <Winuser.h>
#include <cstdlib>
#include <algorithm>
#define WM_KEYDOWN 0x0100
#define WM_KEYUP 0x0101
#define WN_SYSKEYDOWN 0x0104
#define WM_SYSKEYUP 0x0105
#define VK_LBUTTON 0x01 //LEFT MOUSE BUTTON
#define VK_RBUTTON 0x02 //RIGHT MOUSE BUTTON
#define VK_LEFT 0x25
#define VK_UP 0x26
#define VK_RIGHT 0x27 
#define VK_DOWN 0x28
#define number1key 0x31
#define VK_LCONTROL 0xA2
#define VK_RCONTROL 0xA3
#define VK_LWIN 0x5B
#define VK_RWIN 0x5C
#define VK_SPACE 0x20
#define VK_RETURN 0x0D

#define a 0x61
#define b 0x62
#define c 0x63
#define d 0x64
#define e 0x65
#define f 0x66
#define g 0x67
#define h 0x68
#define i 0x69
#define j 0x6A
#define k 0x6B
#define l 0x6C
#define m 0x6D
#define n 0x6E
#define o 0x6F
#define p 0x70
#define q 0x71
#define r 0x72
#define s 0x73
#define t 0x74
#define u 0x75
#define v 0x76 
#define w 0x77
#define x 0x78
#define y 0x79
#define z 0x7A

#define VK_Exclamation 0x21



using namespace std;

int main()
{
  INPUT ipK;
  ipK.type = INPUT_KEYBOARD
	//IGNORE THIS COMMMENT
	//To do: Find the discord window and find the specific server and channel needed 
  /*HWND = FindWindowA(NULL, "WINDOW NAME")

  if(HWND == NULL)
  {
    cout << "Window not found.\n";
    Sleep(3000);
    exit(0);
  }
  */
  bool IsRunning = true;
	while (IsRunning == true) 
	{
		
		//type in !disboard bump
		//!
    UINT SendInput(UINT cInputs,LPINPUT pInputs,INT cbsize)
    {

    }
		//d

		//i

		//s

		//b

		//o

		//a

		//r

		//d

		//VK_SPACE

		//b

		//u

		//m

		//p

		//TIMER for how long to wait before you type in !disboard bump again 
		int MaxTime = 120;
		for (int min = 0; min < MaxTime; min++)//wait for the 120 mins of disboard
		{
			Sleep(60000); //Wait for a min
		}
	}
}