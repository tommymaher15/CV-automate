import React, { useState } from 'react';
import './App.css';

function App() {
  const [recording, setRecording] = useState(false);

  // Function to start screen recording
  const startRecording = () => {
    fetch('/api/start-recording', { method: 'POST' })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message); // Display the response message
        setRecording(true); // Update state to indicate recording is in progress
      })
      .catch((error) => {
        console.error('Error starting recording:', error);
      });
  };

  // Function to stop screen recording
  const stopRecording = () => {
    fetch('/api/stop-recording', { method: 'POST' })
      .then((response) => response.json())
      .then((data) => {
        console.log(data.message); // Display the response message
        setRecording(false); // Update state to indicate recording is stopped
      })
      .catch((error) => {
        console.error('Error stopping recording:', error);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
   
        <p>
          {recording ? 'Recording in progress' : 'Ready to record'}
        </p>
        <button onClick={recording ? stopRecording : startRecording}>
          {recording ? 'Stop Recording' : 'Start Recording'}
        </button>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>
    </div>
  );
}

export default App;
