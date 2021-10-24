# Pose-Estimation-OpenCV

### Overview:
Human pose estimation from video plays a critical role in various applications such as quantifying physical exercises, sign language recognition, and full-body gesture control. For example, it can form the basis for AR systems, yoga, dance, and fitness applications. It can also enable the overlay of digital content and information on top of the physical world in augmented reality.
 
In this project we are doing Pose Estimation on Input Videos and also Livestream video (WebCam), which involves tracking of Human body parts and then identifying the important landmarks on each body part such as Head position, Arm & Elbow position, Lower, legs, etc. Then will make use of all those body landmarks to detect and draw the actual body pose. Finally we extract the actual body pose that was detected and drawn or highlighted from the video and display it in a separate blank screen.

### Libraries Used:
<ol>
  <li>NumPy</li>
  <li>OpenCV</li>
  <li>MediaPipe</li>
  </ol>

### MediaPipe:
MediaPipe is a Deep Learning library developed by Google. MediaPipe Pose is a ML solution for high-fidelity body pose tracking, inferring 33 3D landmarks and background segmentation mask on the whole body from RGB video frames utilizing our BlazePose research that also powers the ML Kit Pose Detection API. lCurrent state-of-the-art approaches rely primarily on powerful desktop environments for inference, whereas our method achieves real-time performance on most modern mobile phones, desktops/laptops, in python and even on the web.It is one of the simplest ways for researchers and developers to build world-class ML solutions & applications and also it works very well on CPU and light weight devices.

If you want to know more about MediaPipe, visit the given link:  https://google.github.io/mediapipe/
