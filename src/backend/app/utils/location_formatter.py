def format_location(location: dict) -> str:
    """
    Formats a location dictionary into a human-readable string.
    
    Args:
        location: Dictionary containing city, state_province, and country fields
        
    Returns:
        Formatted location string, e.g., "San Francisco, CA" or "London, UK"
    """
    if not location:
        return 'Unknown'
    
    city = location.get('city', '')
    state = location.get('state_province', '')
    country = location.get('country', '')
    
    # Format as "City, State" for US locations or "City, Country" for others
    if country == 'USA' and state:
        return f"{city}, {state}" if city else state
    elif city and country:
        return f"{city}, {country}"
    elif city:
        return city
    else:
        return 'Unknown'