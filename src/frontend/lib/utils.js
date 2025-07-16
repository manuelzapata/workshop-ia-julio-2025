export function formatCurrency(amount) {
  if (typeof amount !== 'number') {
    return amount;
  }
  
  const formatter = new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0,
    maximumFractionDigits: 1,
    notation: 'compact',
    compactDisplay: 'short'
  });

  return formatter.format(amount);
}

export function formatNumber(number) {
    if (typeof number !== 'number') {
        return number;
    }
    
    const formatter = new Intl.NumberFormat('en-US', {
        notation: 'compact',
        compactDisplay: 'short'
    });
    
    return formatter.format(number);
} 