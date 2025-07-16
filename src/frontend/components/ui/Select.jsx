export function Select({ children, className, ...props }) {
  return (
    <select
      className={`px-4 py-2 border rounded-md bg-white ${className}`}
      {...props}
    >
      {children}
    </select>
  );
} 