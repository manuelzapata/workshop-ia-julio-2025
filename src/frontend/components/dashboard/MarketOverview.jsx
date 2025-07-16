const mockSectorRevenue = [
  { name: 'FinTech', value: '$7400B', color: 'bg-teal-500' },
  { name: 'Data Analytics', value: '$800B', color: 'bg-red-500' },
  { name: 'Design', value: '$1400B', color: 'bg-gray-800' },
  { name: 'Communication', value: '$130B', color: 'bg-yellow-500' },
  { name: 'Productivity', value: '$100B', color: 'bg-orange-500' },
];

export function MarketOverview() {
  return (
    <div className="bg-white p-4 rounded-lg border">
      <h2 className="text-lg font-semibold">Market Overview</h2>
      <div className="mt-4">
        <h3 className="font-semibold">Revenue by Sector</h3>
        <p className="text-sm text-gray-500 mb-4">
          Distribution of revenue across sectors (in billions)
        </p>
        <ul>
          {mockSectorRevenue.map((sector) => (
            <li key={sector.name} className="flex justify-between items-center py-2">
              <div className="flex items-center">
                <span className={`w-3 h-3 rounded-full mr-3 ${sector.color}`}></span>
                <span>{sector.name}</span>
              </div>
              <span className="font-semibold">{sector.value}</span>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
} 