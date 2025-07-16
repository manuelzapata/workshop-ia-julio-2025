import React from 'react';

export function Badge({ children, className, variant = 'neutral' }) {
  const baseClasses = 'px-2.5 py-0.5 rounded-full text-xs font-semibold inline-flex items-center';
  
  const variants = {
    positive: 'bg-green-100 text-green-800',
    neutral: 'bg-gray-200 text-gray-800',
    // Add other variants if needed from design
  };

  const variantClasses = variants[variant] || variants.neutral;

  return (
    <span className={`${baseClasses} ${variantClasses} ${className}`}>
      {children}
    </span>
  );
} 