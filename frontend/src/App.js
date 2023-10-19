import React, { useEffect, useState } from 'react';
import { fetchData } from './api';

function App() {
  const [data, setData] = useState(null);

  useEffect(() => {
    fetchData().then((response) => setData(response));
  }, []);

  return (
    <div className="App">
      <h1>React and Flask Example</h1>
      {data && <p>{data.message}</p>}
    </div>
  );
}

export default App;