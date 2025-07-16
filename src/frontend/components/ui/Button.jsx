import React from 'react';

export function Button({ children, className, ...props }) {
  return (
    <button
      className={`flex items-center gap-2 px-4 py-2 border rounded-md transition-colors hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed ${className}`}
      {...props}
    >
      {children}
    </button>
  );
} 