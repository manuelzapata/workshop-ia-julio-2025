import os
# Set environment variables before importing
os.environ['supabase_url'] = 'http://test-url'
os.environ['supabase_key'] = 'test-key'
os.environ['environment'] = 'test'

from app.persistence.repositories.dataset_repository import clean_money


def test_clean_money_trillions():
    assert clean_money("$3T") == 3_000_000_000_000
    assert clean_money("$1.5T") == 1_500_000_000_000
    assert clean_money("$0.5T") == 500_000_000_000


def test_clean_money_billions():
    assert clean_money("$270B") == 270_000_000_000
    assert clean_money("$1B") == 1_000_000_000
    assert clean_money("$0.5B") == 500_000_000


def test_clean_money_millions():
    assert abs(clean_money("$65.4M") - 65_400_000) < 0.01
    assert clean_money("$100M") == 100_000_000
    assert clean_money("$0.5M") == 500_000


def test_clean_money_thousands():
    assert clean_money("$2K") == 2_000
    assert clean_money("$100K") == 100_000
    assert clean_money("$0.5K") == 500


def test_clean_money_edge_cases():
    assert clean_money(None) is None
    assert clean_money("") is None
    assert clean_money("N/A") is None
    assert clean_money("$") is None
    assert clean_money("invalid") is None


def test_clean_money_with_commas():
    assert clean_money("$1,000,000") == 1_000_000
    assert clean_money("$1,000") == 1_000