'use client';

import { DollarSign, BarChart2, Briefcase, MapPin } from 'lucide-react';
import { MetricCard } from './MetricCard';

export function MetricsSection({ metrics }) {
  if (!metrics) {
    return (
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
        {[...Array(4)].map((_, i) => (
          <div key={i} className="bg-white p-4 rounded-lg border animate-pulse">
            <div className="h-4 bg-gray-200 rounded w-3/4"></div>
            <div className="h-8 bg-gray-200 rounded w-1/2 mt-2"></div>
          </div>
        ))}
      </div>
    );
  }

  const metricConfig = {
    total_companies: { title: 'Total Companies', icon: Briefcase, isCurrency: false },
    total_revenue: { title: 'Total Revenue', icon: DollarSign, isCurrency: true },
    average_valuation: { title: 'Avg Valuation', icon: BarChart2, isCurrency: true },
    funding_rounds: { title: 'Funding Rounds', icon: Briefcase, isCurrency: false },
    top_location: { title: 'Top Location', icon: MapPin, isCurrency: false },
  };

  const formatCurrency = (value) => {
    if (value >= 1e9) {
      return `$${(value / 1e9).toFixed(1)}B`;
    }
    if (value >= 1e6) {
      return `$${(value / 1e6).toFixed(1)}M`;
    }
    if (value >= 1e3) {
      return `$${(value / 1e3).toFixed(1)}K`;
    }
    return `$${value}`;
  }

  return (
    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4 mb-8">
      {Object.entries(metrics).map(([key, value]) => {
        const config = metricConfig[key];
        if (!config) return null;

        let displayValue = value;
        if (config.isCurrency) {
          displayValue = formatCurrency(value);
        } else if (key === 'top_location' && typeof value === 'object' && value !== null) {
          displayValue = value.name ? `${value.name} (${value.companies} companies)` : 'N/A';
        }

        return <MetricCard key={key} title={config.title} value={displayValue} icon={config.icon} />;
      })}
    </div>
  );
} 