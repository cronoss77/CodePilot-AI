from src.analyzer import analyze_code


def test_code_without_functions():
    code = """
print("Hello World")
"""

    result = analyze_code(code)

    assert "No functions found" in result


def test_good_code():
    code = """
def hello():
    return "Hello"
"""

    result = analyze_code(code)

    assert "No major issues found" in result


def test_syntax_error():
    code = """
def broken_function(
    return True
"""

    result = analyze_code(code)

    assert "Syntax error detected" in result
