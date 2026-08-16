from analyzer import analyze_code
from documentation import generate_documentation


def main():
    print("🚀 CodePilot AI")
    print("----------------")

    file_path = input("Enter Python file path: ")

    with open(file_path, "r", encoding="utf-8") as file:
        code = file.read()

    print("\nCode Analysis:")
    print(analyze_code(code))

    print("\nGenerated Documentation:")
    print(generate_documentation(code))


if __name__ == "__main__":
    main()
