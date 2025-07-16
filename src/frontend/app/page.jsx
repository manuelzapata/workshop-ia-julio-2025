'use client';

import { useEffect, useState } from 'react';
import { MetricsSection } from '@/components/dashboard/MetricsSection';
import { CompaniesTable } from '@/components/dashboard/CompaniesTable';
import { MarketOverview } from '@/components/dashboard/MarketOverview';

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
    <div className="p-8 bg-gray-50 min-h-screen">
      <MetricsSection />
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <CompaniesTable />
        </div>
        <div>
          <MarketOverview />
        </div>
      </div>
    </div>
  );
} 