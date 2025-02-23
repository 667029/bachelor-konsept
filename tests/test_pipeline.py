import os
import pytest
from modules.ingestion.copy_file import CopyFileModule
from modules.preparation.move_file import MoveFileModule
from modules.enrichment.rename_file import RenameFileModule

TEST_INPUT_FILE = "input/test_sample.txt"
TEST_OUTPUT_DIR = "tests/output"

@pytest.fixture
def setup_test_files():
    os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)
    with open(TEST_INPUT_FILE, "w") as f:
        f.write("Test file content")
    yield
    os.remove(TEST_INPUT_FILE)

def test_copy_file(setup_test_files):
    module = CopyFileModule()
    output_file = module.process(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
    assert os.path.exists(output_file)

def test_move_file(setup_test_files):
    module = MoveFileModule()
    output_file = module.process(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
    assert os.path.exists(output_file)

def test_rename_file(setup_test_files):
    module = RenameFileModule("new_name.txt")
    output_file = module.process(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
    assert os.path.exists(os.path.join(TEST_OUTPUT_DIR, "new_name.txt"))