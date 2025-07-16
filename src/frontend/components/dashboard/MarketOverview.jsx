export function MarketOverview({ companies }) {
  const calculateSectorRevenue = (companies) => {
    if (!companies || companies.length === 0) {
      return [];
    }

    const sectorRevenue = companies.reduce((acc, company) => {
      const { industry, annual_revenue } = company;
      if (acc[industry]) {
        acc[industry] += annual_revenue;
      } else {
        acc[industry] = annual_revenue;
      }
      return acc;
    }, {});

    const sortedSectors = Object.entries(sectorRevenue)
      .sort(([, a], [, b]) => b - a)
      .map(([name, value]) => ({ name, value }));

    return sortedSectors;
  };

  const sectorData = calculateSectorRevenue(companies);

  // Simple color mapping, can be expanded
  const colorMap = {
    'FinTech': 'bg-teal-500',
    'Data Analytics': 'bg-red-500',
    'Design': 'bg-gray-800',
    'Communication': 'bg-yellow-500',
    'Productivity': 'bg-orange-500',
  };

  return (
    <div className="bg-white p-4 rounded-lg border">
      <h2 className="text-lg font-semibold">Market Overview</h2>
      <div className="mt-4">
        <h3 className="font-semibold">Revenue by Sector</h3>
        <p className="text-sm text-gray-500 mb-4">
          Distribution of revenue across sectors
        </p>
        {!companies || companies.length === 0 ? (
          <p className="text-gray-500">No company data available.</p>
        ) : (
          <ul>
            {sectorData.map((sector) => (
              <li key={sector.name} className="flex justify-between items-center py-2">
                <div className="flex items-center">
                  <span className={`w-3 h-3 rounded-full mr-3 ${colorMap[sector.name] || 'bg-gray-400'}`}></span>
                  <span>{sector.name}</span>
                </div>
                <span className="font-semibold">${(sector.value / 1e9).toFixed(1)}B</span>
              </li>
            ))}
          </ul>
        )}
      </div>
    </div>
  );
} 