'use client';

import { useState, useEffect } from 'react';
import { DollarSign, BarChart2, Briefcase, MapPin } from 'lucide-react';
import { MetricCard } from './MetricCard';

// Mock data for now, will be replaced with API call
const mockMetrics = {
    totalRevenue: {
        title: "Total Revenue",
        value: "$9.8B",
        icon: DollarSign,
    },
    avgValuation: {
        title: "Avg Valuation",
        value: "$37.2B",
        icon: BarChart2,
    },
    fundingRounds: {
        title: "Funding Rounds",
        value: "1.2K",
        icon: Briefcase,
    },
    topLocation: {
        title: "Top Location",
        value: "San Francisco",
        icon: MapPin,
    },
};

export function MetricsSection() {
//   const [metrics, setMetrics] = useState(null);
//   const [loading, setLoading] = useState(true);

//   useEffect(() => {
//     async function fetchMetrics() {
//       try {
//         // const data = await getMetrics(); // API call
//         setMetrics(mockMetrics);
//       } catch (error) {
//         console.error("Failed to fetch metrics:", error);
//       } finally {
//         setLoading(false);
//       }
//     }
//     fetchMetrics();
//   }, []);

//   if (loading) {
//     return <div>Loading metrics...</div>;
//   }

//   if (!metrics) {
//     return <div>Failed to load metrics.</div>;
//   }
  const metrics = mockMetrics;

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      <MetricCard {...metrics.totalRevenue} />
      <MetricCard {...metrics.avgValuation} />
      <MetricCard {...metrics.fundingRounds} />
      <MetricCard {...metrics.topLocation} />
    </div>
  );
} 