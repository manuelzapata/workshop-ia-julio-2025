'use client';

import { useState } from 'react';
import { Badge } from '@/components/ui/Badge';
import { SearchInput } from '@/components/ui/SearchInput';
import { Select } from '@/components/ui/Select';
import { ExternalLink, ArrowUpDown } from 'lucide-react';
import { Button } from '../ui/Button';
import { formatCurrency, formatNumber } from '@/lib/utils';

export function CompaniesTable({ companies: initialCompanies }) {
  const [companies, setCompanies] = useState(initialCompanies);

  if (!companies) {
    return <div className="text-center p-8">Could not load companies.</div>;
  }

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
                <div className="text-xs text-gray-500">Founded {company.year_founded}</div>
              </td>
              <td className="px-6 py-4">{formatCurrency(company.annual_revenue)}</td>
              <td className="px-6 py-4">{formatCurrency(company.valuation)}</td>
              <td className="px-6 py-4">
                <Badge>{company.industry}</Badge>
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