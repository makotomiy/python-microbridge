# Python (SL4A) MicroBridge demo

## What is this?

This is a [MicroBridge](http://code.google.com/p/microbridge/) demo written in Python to use with [Scripting Layer for Android](http://code.google.com/p/android-scripting/) (SL4A). It's based on the Android demo written by Niels Brouwers. You can see my demo running [here](http://www.youtube.com/watch?v=euBPivEOckY). Feel free to watch and fork.

## Why?

I was doing an Arduino project where I needed to control some stuffs over the network. Instead of buying a Wifi Shield, I bought an USB Host Shield to plug my Android cellphone and use its wireless link.

Since I was too lazy to install Eclipse, Android SDK and learn the basics of Android programming, I have installed SL4A and started to prototype with Python when I found out that I could use scripting languages with MicroBridge when I saw [this](http://www.youtube.com/watch?v=Y5C3xxyQMSw) guy using it with SL4A JRuby.

## Installation

* Copy `microbridge` folder into your Android SDCard path: `/sdcard/sl4a/scripts`;
* Build the circuit following the schematics and upload `arduino_demo.ino` to your Arduino;
* Run `demo.py` from SL4A.

# License

## MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS," WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.