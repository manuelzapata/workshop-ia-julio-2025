import { getCompanies, getMetrics } from '@/lib/api';
import { MetricsSection } from '@/components/dashboard/MetricsSection';
import { CompaniesTable } from '@/components/dashboard/CompaniesTable';
import { MarketOverview } from '@/components/dashboard/MarketOverview';

export default async function Home() {
  const metrics = await getMetrics();
  const companies = await getCompanies();

  return (
    <div className="p-8 bg-gray-50 min-h-screen">
      <MetricsSection metrics={metrics} />
      <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <div className="lg:col-span-2">
          <CompaniesTable companies={companies} />
        </div>
        <div>
          <MarketOverview companies={companies} />
        </div>
      </div>
    </div>
  );
} 