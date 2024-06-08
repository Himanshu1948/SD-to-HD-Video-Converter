import cv2
import os
import subprocess
from PIL import Image
import numpy as np
from moviepy.editor import ImageSequenceClip

def extract_frames(video_path, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    vidcap = cv2.VideoCapture(video_path)
    success, image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(os.path.join(output_dir, f"frame_{count:04d}.png"), image)
        success, image = vidcap.read()
        count += 1
    vidcap.release()

def upscale_frame(input_frame, output_frame, model_name='realesrgan-x4plus'):
    cmd = [
        './realesrgan-ncnn-vulkan-20220424-windows/realesrgan-ncnn-vulkan.exe',
        '-i', input_frame,
        '-o', output_frame,
        '-n', model_name
    ]
    subprocess.run(cmd, check=True)

def pad_frame(input_frame_path, output_frame_path):
    # Load the upscaled frame
    img = Image.open(input_frame_path).convert('RGB')
    img = np.array(img)
    
    # Target resolution
    new_width = 1280
    new_height = 720
    
    # Calculate padding values
    top = max((new_height - img.shape[0]) // 2, 0)
    bottom = max(new_height - img.shape[0] - top, 0)
    left = max((new_width - img.shape[1]) // 2, 0)
    right = max(new_width - img.shape[1] - left, 0)
    
    # Pad the frame to 1280x720 by adding blank areas on the sides
    if img.shape[0] > new_height or img.shape[1] > new_width:
        # Resize if the image is larger than the target resolution
        img = cv2.resize(img, (new_width, new_height))
    else:
        # Pad the image to the target resolution
        img = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)
    
    # Save the padded frame
    padded_img = Image.fromarray(img)
    padded_img.save(output_frame_path)

def create_video_from_frames(frames_dir, output_video_path, fps=30):
    frame_files = sorted([os.path.join(frames_dir, f) for f in os.listdir(frames_dir)])
    clip = ImageSequenceClip(frame_files, fps=fps)
    clip.write_videofile(output_video_path, codec='libx264')

# Example usage:
input_video_path = 'realesrgan-ncnn-vulkan-20220424-windows/onepiece_demo.mp4'
frames_dir = 'content/frames'
upscaled_frames_dir = 'content/upscaled_frames'
final_frames_dir = 'content/final_frames'
output_video_path = 'content/output_video.mp4'

# Step 1: Extract frames from input video
extract_frames(input_video_path, frames_dir)

# Step 2: Upscale each frame
os.makedirs(upscaled_frames_dir, exist_ok=True)
frame_files = sorted(os.listdir(frames_dir))
for frame_file in frame_files:
    input_frame_path = os.path.join(frames_dir, frame_file)
    output_frame_path = os.path.join(upscaled_frames_dir, frame_file)
    upscale_frame(input_frame_path, output_frame_path)

# Step 3: Pad frames to 1280x720 resolution
os.makedirs(final_frames_dir, exist_ok=True)
upscaled_frame_files = sorted(os.listdir(upscaled_frames_dir))
for frame_file in upscaled_frame_files:
    input_frame_path = os.path.join(upscaled_frames_dir, frame_file)
    output_frame_path = os.path.join(final_frames_dir, frame_file)
    pad_frame(input_frame_path, output_frame_path)

# Step 4: Reassemble upscaled and padded frames into an HD video
create_video_from_frames(upscaled_frames_dir, output_video_path)
