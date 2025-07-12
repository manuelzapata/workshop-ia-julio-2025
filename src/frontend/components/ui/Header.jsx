import { BarChart, Search, Filter, Download } from 'lucide-react';

function Header() {
  return (
    <header className="flex items-center justify-between p-4 border-b">
      <div className="flex items-center gap-2">
        <BarChart className="w-6 h-6 text-blue-600" />
        <h1 className="text-xl font-semibold">SaaS Investor Dashboard</h1>
      </div>
      <div className="flex items-center gap-4">
        <div className="relative">
          <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
          <input
            type="text"
            placeholder="Search companies, sectors..."
            className="pl-10 pr-4 py-2 border rounded-md w-80"
          />
        </div>
        <button className="flex items-center gap-2 px-4 py-2 border rounded-md">
          <Filter className="w-5 h-5" />
          <span>Filters</span>
        </button>
        <button className="flex items-center gap-2 px-4 py-2 border rounded-md">
          <Download className="w-5 h-5" />
          <span>Export</span>
        </button>
      </div>
    </header>
  );
}

export default Header; 