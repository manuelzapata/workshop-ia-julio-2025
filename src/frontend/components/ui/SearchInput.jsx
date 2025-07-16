import { Search } from 'lucide-react';

export function SearchInput({ className, ...props }) {
  return (
    <div className="relative">
      <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
      <input
        type="text"
        className={`pl-10 pr-4 py-2 border rounded-md w-80 ${className}`}
        {...props}
      />
    </div>
  );
} 