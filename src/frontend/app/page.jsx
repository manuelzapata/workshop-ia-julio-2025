'use client';

import { useEffect, useState } from 'react';

export default function Home() {
  const [apiStatus, setApiStatus] = useState('loading...');

  useEffect(() => {
    async function checkApiHealth() {
      try {
        const response = await fetch(`${process.env.NEXT_PUBLIC_API_URL}/health`);
        if (response.ok) {
          const data = await response.json();
          setApiStatus(`OK: ${JSON.stringify(data)}`);
        } else {
          setApiStatus(`Error: ${response.statusText}`);
        }
      } catch (error) {
        setApiStatus(`Failed to connect: ${error.message}`);
      }
    }

    checkApiHealth();
  }, []);

  return (
    <div>
      <h2>Frontend</h2>
      <p>API Status: {apiStatus}</p>
    </div>
  );
} 