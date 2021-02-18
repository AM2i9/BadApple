So I got bored today, and decided to make Bad Apple in Windows File Manager.
You can see it working here: https://youtu.be/TnIHfMHRBnw

Disclaimer: I DO NOT OWN A PART OF THIS CODE

The section of code in img.py that converts the frames to ASCII is NOT mine, and can be found at https://gist.github.com/A2x2/b1b27b15b0590d36351b9b19ce25a04e

The video and song Bad Apple is also not mine, and can be found at https://www.youtube.com/watch?v=FtutLA63Cp8
<br><br>

### How I made it:
First, I used FFmpeg to resize the image to a more useable resolution for ASCII art, 70x54 (which I also stole from A2x2 as a size), then once again used FFmpeg to generate somewhere close to 6527 png files, for each frame of the video running at 20 fps.


I then stole some code, and wrote part of a script to take each of those frames, convert it to ASCII art, and then paste each frame as ASCII into a file called `raw`, with each frame being seperated by a comma. I then wrote another program to play it, which opened the `raw` file, split the frames into a list using the commas, and then renamed the files inside the folder based on those frames.
