import pytest
from pathlib import Path
import shutil


@pytest.fixture(scope="session")
def test_data_path():
    test_data_path = Path(__file__).parent / "test_data"
    test_data_path.mkdir(exist_ok=True)
    yield test_data_path
    shutil.rmtree(test_data_path)
