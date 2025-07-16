import { BarChart, Filter, Download } from 'lucide-react';
import { SearchInput } from './SearchInput';
import { Button } from './Button';

function Header() {
  return (
    <header className="flex items-center justify-between p-4 border-b bg-white">
      <div className="flex items-center gap-2">
        <BarChart className="w-6 h-6 text-blue-600" />
        <h1 className="text-xl font-semibold">SaaS Investor Dashboard</h1>
      </div>
      <div className="flex items-center gap-4">
        <SearchInput placeholder="Search companies, sectors..." />
        <Button>
          <Filter className="w-5 h-5" />
          <span>Filters</span>
        </Button>
        <Button>
          <Download className="w-5 h-5" />
          <span>Export</span>
        </Button>
      </div>
    </header>
  );
}

export default Header; 