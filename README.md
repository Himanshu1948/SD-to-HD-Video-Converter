# SD to HD Video Converter

This project presents a prototype tool designed to upscale SD resolution (640x480px) videos to HD resolution (1280x720px) using the Real-ESRGAN model. The process involves extracting frames from the video, applying the Real-ESRGAN model for upscaling, padding the frames to meet the target resolution, and reassembling the frames into a high-definition video.

## Requirements

- Python 3.7+
- OpenCV
- Pillow
- MoviePy
- Real-ESRGAN executable and models

## Installation

1. **Clone the repository:**
    ```bash
    git clone https://github.com/Himanshu1948/SD-to-HD-Video-Converter.git
    cd SD-to-HD-Video-Converter
    ```

2. **Install the required Python packages:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Download Real-ESRGAN executable and models:**
   The windows version is already present under the `realesrgan-ncnn-vulkan-20220424-windows` directory.
   If using any other OS, make changes accordingly.
   Make sure to place the `realesrgan-ncnn-vulkan.exe` and the `models` folder in the `realesrgan-ncnn-vulkan-20220424-windows` directory.

## Usage

1. **Prepare the input video:**

   Place the SD resolution video that you want to upscale in the `content` directory.
   For example, an `input_video.mp4` file is already present in the `content` directory.

3. **Run the converter script:**

   Ensure you are in the project directory and run the `converter.py` script:
    ```bash
    python converter.py
    ```

   This will perform the following steps:
   - Extract frames from the input video.
   - Upscale each frame using the Real-ESRGAN model.
   - Pad the frames to 1280x720 resolution.
   - Reassemble the upscaled and padded frames into an HD video.

4. **View the output:**

   The resulting HD video will be saved in the `content` directory as `output_video.mp4`.

## Notes

- Ensure that the Real-ESRGAN executable and models are correctly placed in the specified directory.
- The script assumes that the input video is named `input_video.mp4`. Adjust the script or rename your video file accordingly.
- Depending on the length and resolution of the input video, the conversion process may take some time.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.

