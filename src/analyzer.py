import ast


def analyze_code(code):
    issues = []

    try:
        tree = ast.parse(code)
    except SyntaxError:
        return "❌ Syntax error detected."

    functions = [
        node for node in ast.walk(tree)
        if isinstance(node, ast.FunctionDef)
    ]

    if not functions:
        issues.append(
            "No functions found. Consider organizing your code into functions."
        )

    for function in functions:
        if len(function.body) > 20:
            issues.append(
                f"Function '{function.name}' is too long."
            )

    if not issues:
        return "✅ No major issues found."

    return "\n".join("- " + issue for issue in issues)
