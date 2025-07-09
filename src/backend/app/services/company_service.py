def get_company_details(company_id: int) -> dict | None:
    # Aquí iría la lógica real para buscar la empresa en la base de datos
    # Por ahora, retorna datos dummy si el ID es 1
    if company_id == 1:
        return {
            'id': 1,
            'name': 'Acme SaaS',
            'revenue': 1000000,
            'employees': 50,
            'valuation': 5000000
        }
    return None 