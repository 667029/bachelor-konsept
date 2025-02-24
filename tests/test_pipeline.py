import os
import pytest
from components.copy_file import CopyFileModule
from components.move_file import MoveFileModule
from components.rename_file import RenameFileModule

TEST_INPUT_FILE = "???"
TEST_OUTPUT_DIR = "???"

#TODO
@pytest.fixture
def setup_test_files():
    os.makedirs(TEST_OUTPUT_DIR, exist_ok=True)
    with open(TEST_INPUT_FILE, "w") as f:
        f.write("Test file content")
    yield
    os.remove(TEST_INPUT_FILE)

#TODO
def test_copy_file(setup_test_files):
    module = CopyFileModule()
    output_file = module.process(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
    assert os.path.exists(output_file)

#TODO
def test_move_file(setup_test_files):
    module = MoveFileModule()
    output_file = module.process(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
    assert os.path.exists(output_file)

#TODO
def test_rename_file(setup_test_files):
    module = RenameFileModule("new_name.txt")
    output_file = module.process(TEST_INPUT_FILE, TEST_OUTPUT_DIR)
    assert os.path.exists(os.path.join(TEST_OUTPUT_DIR, "new_name.txt"))

#TODO
def test_ingestion(setup_test_files):
    #TODO
    return True

#TODO
def test_capture(setup_test_files):
    #TODO
    return True

#TODO
def test_classification(setup_test_files):
    #TODO
    return True

#TODO
def test_extraction(setup_test_files):
    #TODO
    return True

#TODO
def test_validation(setup_test_files):
    #TODO
    return True

#TODO
def test_extraction(setup_test_files):
    #TODO
    return True

#TODO
def test_validation(setup_test_files):
    #TODO
    return True

#TODO
def test_enrichment(setup_test_files):
    #TODO
    return True

#TODO
def test_insights(setup_test_files):
    #TODO
    return True

#TODO
def test_curation(setup_test_files):
    #TODO
    return True
