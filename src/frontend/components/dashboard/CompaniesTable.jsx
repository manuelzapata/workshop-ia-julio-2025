'use client';

import { useState, useEffect } from 'react';
import { Badge } from '@/components/ui/Badge';
import { SearchInput } from '@/components/ui/SearchInput';
import { Select } from '@/components/ui/Select';
import { ExternalLink, ArrowUpDown } from 'lucide-react';
import { Button } from '../ui/Button';

const mockCompanies = [
  { id: 1, name: 'Notion', founded: 2016, revenue: '$100.0M', valuation: '$10.0B', sector: 'Productivity', location: 'San Francisco' },
  { id: 2, name: 'Discord', founded: 2012, revenue: '$130.0M', valuation: '$15.0B', sector: 'Communication', location: 'San Francisco' },
  { id: 3, name: 'Figma', founded: 2012, revenue: '$400.0M', valuation: '$20.0B', sector: 'Design', location: 'San Francisco' },
  { id: 4, name: 'Canva', founded: 2012, revenue: '$1.0B', valuation: '$40.0B', sector: 'Design', location: 'Sydney' },
  { id: 5, name: 'Databricks', founded: 2013, revenue: '$800.0M', valuation: '$43.0B', sector: 'Data Analytics', location: 'San Francisco' },
  { id: 6, name: 'Stripe', founded: 2010, revenue: '$7.4B', valuation: '$95.0B', sector: 'FinTech', location: 'San Francisco' },
];

export function CompaniesTable() {
//   const [companies, setCompanies] = useState([]);
//   const [loading, setLoading] = useState(true);
  
//   useEffect(() => {
//     async function fetchCompanies() {
//       try {
//         // const data = await getCompanies(); // API call
//         setCompanies(mockCompanies);
//       } catch (error) {
//         console.error("Failed to fetch companies:", error);
//       } finally {
//         setLoading(false);
//       }
//     }
//     fetchCompanies();
//   }, []);

//   if (loading) return <p>Loading companies...</p>;
//   if (companies.length === 0) return <p>No companies found.</p>;

  const companies = mockCompanies;

  return (
    <div className="bg-white p-4 rounded-lg border">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-lg font-semibold">Companies ({companies.length} total)</h2>
        <div className="flex items-center gap-2">
          <SearchInput placeholder="Search companies..." className="w-72" />
          <Select>
            <option>Valuation</option>
            <option>High to Low</option>
            <option>Low to High</option>
          </Select>
        </div>
      </div>
      <table className="w-full text-sm text-left">
        <thead className="text-xs text-gray-500 uppercase bg-gray-50">
          <tr>
            <th scope="col" className="px-6 py-3">#</th>
            <th scope="col" className="px-6 py-3">Company</th>
            <th scope="col" className="px-6 py-3">Revenue</th>
            <th scope="col" className="px-6 py-3">Valuation <ArrowUpDown className="inline w-4 h-4 ml-1" /></th>
            <th scope="col" className="px-6 py-3">Sector</th>
            <th scope="col" className="px-6 py-3">Location</th>
            <th scope="col" className="px-6 py-3">Actions</th>
          </tr>
        </thead>
        <tbody>
          {companies.map((company, index) => (
            <tr key={company.id} className="bg-white border-b">
              <td className="px-6 py-4">{index + 1}</td>
              <td className="px-6 py-4">
                <div className="font-semibold">{company.name}</div>
                <div className="text-xs text-gray-500">Founded {company.founded}</div>
              </td>
              <td className="px-6 py-4">{company.revenue}</td>
              <td className="px-6 py-4">{company.valuation}</td>
              <td className="px-6 py-4">
                <Badge>{company.sector}</Badge>
              </td>
              <td className="px-6 py-4">{company.location}</td>
              <td className="px-6 py-4">
                <Button className="p-2">
                  <ExternalLink className="w-4 h-4" />
                </Button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
} 