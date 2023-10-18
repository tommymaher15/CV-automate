import subprocess

# Define recording parameters
recording_area = "1920x1080"  # Recording area (e.g., full HD resolution)
output_quality = 25  # Output video quality (adjust as needed, lower values mean higher quality)
output_format = "mp4"  # Output format (e.g., mp4)
output_filename = "output_video.mp4"  # Output video file name

def start_screen_recording(output_filename, recording_area, output_quality, output_format):
    # Define the FFmpeg command to start recording
    command = [
        "ffmpeg",
        "-f", "x11grab",  # Specify the screen capture format
        "-s", recording_area,  # Set the screen resolution
        "-i", ":0.0",  # Screen capture from display 0.0
        "-q:v", str(output_quality),  # Set the video quality
        output_filename  # Specify the output file
    ]

    # Start the screen recording using subprocess.Popen
    recording_process = subprocess.Popen(command)

    return recording_process

def stop_screen_recording(recording_process):
    # Terminate the recording process
    recording_process.terminate()
    recording_process.wait()

if __name__ == "__main__":
    # Start screen recording
    recording_process = start_screen_recording(output_filename, recording_area, output_quality, output_format)
    
    input("Press Enter to stop recording...")  # Wait for user input to stop recording
    
    # Stop screen recording
    stop_screen_recording(recording_process)
