import subprocess
from flask import Flask, request, jsonify

app = Flask(__name)
recording_process = None  # Define recording_process as a global variable

@app.route('/api/start-recording', methods=['POST'])
def start_recording():
    global recording_process  # Access the global recording_process variable
    if recording_process is not None and recording_process.poll() is None:
        return jsonify(message="Recording already in progress.")
    
    # Define the FFmpeg command to start recording
    command = [
        "ffmpeg",
        "-f", "x11grab",
        "-s", "1920x1080",  # Recording area (adjust as needed)
        "-i", ":0.0",
        "output.mp4"  # Output file name
    ]

    # Start the recording process
    recording_process = subprocess.Popen(command)
    return jsonify(message="Screen recording started.")

@app.route('/api/stop-recording', methods=['POST'])
def stop_recording():
    global recording_process  # Access the global recording_process variable
    if recording_process is None or recording_process.poll() is not None:
        return jsonify(message="No recording in progress.")
    
    # Terminate the recording process
    recording_process.terminate()
    recording_process.wait()
    return jsonify(message="Screen recording stopped.")

if __name__ == '__main__':
    app.run(debug=True)
