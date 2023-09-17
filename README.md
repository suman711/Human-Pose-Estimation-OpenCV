# Human Pose Estimation

### Overview:
Human pose estimation from video plays a critical role in various applications such as quantifying physical exercises, sign language recognition, and full-body gesture control. For example, it can form the basis for AR systems, yoga, dance, and fitness applications. It can also enable the overlay of digital content and information on top of the physical world in augmented reality.

In this project I'm implementing Pose Estimation using OpenCV and MediaPipe on Input Videos and also Livestream video (Webcam). This involves tracking of Human body parts and then identifying the important landmarks on each body part such as Head position, Arm & Elbow position, Lower body, legs, etc. Then will make use of all those body landmarks to detect and draw or connect the landmarks to form the actual human body pose on the video. Finally, I extracted the actual body pose that was detected and drawn or highlighted from the video and displayed it on a separate blank screen.

<b>Output: </b>https://drive.google.com/file/d/1psjlHy76MJHPUj2mNs6tL2H20NebsFWA/view?usp=sharing

### Libraries Used:
<ol>
  <li>NumPy</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
  </ol>

### MediaPipe:
MediaPipe is a Deep Learning library developed by Google. MediaPipe Pose is a ML solution for high-fidelity body pose tracking, inferring 33 3D landmarks and background segmentation mask on the whole body from RGB video frames utilizing the BlazePose research that also powers the ML Kit Pose Detection API. Current state-of-the-art approaches rely primarily on powerful desktop environments for inference, whereas this method achieves real-time performance on most modern mobile phones, desktops/laptops, in python and even on the web. It is one of the simplest ways for researchers and developers to build world-class ML solutions & applications and also it works very well on CPU and light weight devices.

If you want to know more about MediaPipe, checkout the given link:  https://google.github.io/mediapipe/

### Find Videos for Input:
We need to find some videos to serve as our test cases.
We want to download videos that contain humans. The video files should be in mp4 format and preferrably with max dimensions of 1920 x 1080.

Here are a couple of good sources where you can download videos from :
<ol>
 <li>Pixabay.com</li> 
 <li>Dreamstime.com</li>
</ol> 

Take your videos and put them inside a directory on your computer
