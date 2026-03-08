import sys
import os
import pandas as pd
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.RW_1 import total_sales_per_product

def test_total_sales_per_product():
    df = pd.DataFrame({"product": ["A", "B", "A"], "amount": [10, 20, 5]})
    result = total_sales_per_product(df)
    result_dict = dict(zip(result["product"], result["amount"]))
    assert result_dict == {"A": 15, "B": 20}
