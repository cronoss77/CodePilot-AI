import ast


def generate_documentation(code):
    tree = ast.parse(code)
    docs = []

    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            params = [arg.arg for arg in node.args.args]

            docs.append(
                f"""
## {node.name}()

Automatically generated documentation.

Parameters:
{', '.join(params)}
"""
            )

    if not docs:
        return "No functions found to document."

    return "\n".join(docs)
