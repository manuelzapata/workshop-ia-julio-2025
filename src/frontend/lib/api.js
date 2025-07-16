const API_URL = process.env.NEXT_PUBLIC_API_URL;

const mockMetrics = {
    totalRevenue: {
        title: "Total Revenue",
        value: "$9.8B",
    },
    avgValuation: {
        title: "Avg Valuation",
        value: "$37.2B",
    },
    fundingRounds: {
        title: "Funding Rounds",
        value: "1.2K",
    },
    topLocation: {
        title: "Top Location",
        value: "San Francisco",
    },
};

const mockCompanies = [
  { id: 1, name: 'Notion', founded: 2016, revenue: '$100.0M', valuation: '$10.0B', growth: '+120%', growthType: 'positive', sector: 'Productivity', location: 'San Francisco' },
  { id: 2, name: 'Discord', founded: 2012, revenue: '$130.0M', valuation: '$15.0B', growth: '+85%', growthType: 'positive', sector: 'Communication', location: 'San Francisco' },
  { id: 3, name: 'Figma', founded: 2012, revenue: '$400.0M', valuation: '$20.0B', growth: '+100%', growthType: 'positive', sector: 'Design', location: 'San Francisco' },
  { id: 4, name: 'Canva', founded: 2012, revenue: '$1.0B', valuation: '$40.0B', growth: '+60%', growthType: 'positive', sector: 'Design', location: 'Sydney' },
  { id: 5, name: 'Databricks', founded: 2013, revenue: '$800.0M', valuation: '$43.0B', growth: '+75%', growthType: 'positive', sector: 'Data Analytics', location: 'San Francisco' },
  { id: 6, name: 'Stripe', founded: 2010, revenue: '$7.4B', valuation: '$95.0B', growth: '+38%', growthType: 'positive', sector: 'FinTech', location: 'San Francisco' },
];


export async function getMetrics() {
  // try {
  //   const response = await fetch(`${API_URL}/metrics`);
  //   if (!response.ok) {
  //     throw new Error('Failed to fetch metrics');
  //   }
  //   return response.json();
  // } catch (error) {
  //   console.error(error);
  //   return mockMetrics; // fallback to mock data
  // }
  return Promise.resolve(mockMetrics);
}

export async function getCompanies() {
  // try {
  //   const response = await fetch(`${API_URL}/companies`);
  //   if (!response.ok) {
  //     throw new Error('Failed to fetch companies');
  //   }
  //   return response.json();
  // } catch (error) {
  //   console.error(error);
  //   return mockCompanies; // fallback to mock data
  // }
  return Promise.resolve(mockCompanies);
} 