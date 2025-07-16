import { ArrowUp, ArrowDown } from 'lucide-react';

export function MetricCard({ title, value, change, changeType, icon: Icon }) {
  const isPositive = changeType === 'positive';
  const ChangeIcon = isPositive ? ArrowUp : ArrowDown;
  const changeColor = isPositive ? 'text-green-500' : 'text-red-500';

  return (
    <div className="bg-white p-4 rounded-lg border">
      <div className="flex justify-between items-start">
        <p className="text-sm text-gray-500">{title}</p>
        {Icon && <Icon className="w-5 h-5 text-gray-400" />}
      </div>
      <p className="text-2xl font-bold mt-2">{value}</p>
      {change && (
        <div className="flex items-center text-sm mt-1">
          <ChangeIcon className={`w-4 h-4 mr-1 ${changeColor}`} />
          <span className={changeColor}>{change}</span>
        </div>
      )}
    </div>
  );
} 