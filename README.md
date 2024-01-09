# Introduction

This is a python script intended to fix the format of srt files so that they may be used to caption videos. The basic function of the script is to recieve a specified text file (.txt) in srt-format and produce a corrected srt file (.srt).

# Setup

- In order to use this script, clone this code to your workstaion and have python installed. I recommend using Visual Studio Code as your code editor/IDE as that is what I used and what I will base the instructions off of
- In the same folder as the python script (format.py), paste the text file (.txt) which you wish to format into a corrected srt file (.srt)

# Instructions 

- Open up the 'format.py' file in Visual Studio Code
- Scroll to line 55 to the function 'generate_srt()'
- Copy the local file path of the .txt file you wish to format (this can be done by right clicking the file name in the file tree to the left side of the code editor window and selecting 'Copy Relative Path'
- Paste the local file path into the 'generate_srt()' function with the appropriate quotation marks around the filename (e.g., generate_srt('file.txt')
- Scroll to line 51 of the code and locate the 'open()' function
- ONLY edit the file name, which is the first parameter of the function (seperated by commas)
- It should look like this: open('formatted file.srt', 'w', encoding='utf-8')
- Make sure to leave the '.srt' so the generated file is in the correct format
- When the correct file path and filename have been entered on lines 55 and 51, respectively, right click on a blank space within the code window and select 'Run Python File in Terminal'
- When this is done, a new .srt file will appear in the same folder as the 'format.py' file
- Please note that due to a transcoding error in some characters, French captions may be missing for several lines, however this will not effect the synchronization of the captions with the video
