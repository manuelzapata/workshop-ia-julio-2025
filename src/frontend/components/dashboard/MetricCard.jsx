import { ArrowUp, ArrowDown } from 'lucide-react';

export function MetricCard({ title, value, icon: Icon }) {
  return (
    <div className="bg-white p-4 rounded-lg border">
      <div className="flex justify-between items-start">
        <p className="text-sm text-gray-500">{title}</p>
        {Icon && <Icon className="w-5 h-5 text-gray-400" />}
      </div>
      <p className="text-2xl font-bold mt-2">{value}</p>
    </div>
  );
} 