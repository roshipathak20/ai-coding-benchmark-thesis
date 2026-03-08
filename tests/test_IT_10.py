import sys
import os
from pathlib import Path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from solutions.IT_10 import save_line_plot

def test_save_line_plot(tmp_path):
    output_file = tmp_path / "plot.png"
    save_line_plot([1, 3, 2, 5], str(output_file))
    assert output_file.exists()
    assert output_file.stat().st_size > 0
