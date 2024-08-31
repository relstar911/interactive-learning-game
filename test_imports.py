import sys

def test_import(module_name):
    try:
        __import__(module_name)
        print(f"✅ {module_name} wurde erfolgreich importiert.")
    except ImportError as e:
        print(f"❌ Fehler beim Importieren von {module_name}: {e}")

if __name__ == "__main__":
    modules_to_test = [
        "pygame",
        "openai",
        "sqlite3",
        "json",
        "logging"
    ]

    print("Überprüfe Modulimporte:")
    for module in modules_to_test:
        test_import(module)

    print("\nÜberprüfe Projektmodule:")
    project_modules = [
        "player",
        "quiz",
        "npc",
        "mini_game",
        "sprites",
        "inventory",
        "game_objects",
        "progress",
        "config",
        "asset_manager",
        "logger",
        "llm_integration"
    ]

    for module in project_modules:
        test_import(module)

    print("\nPython-Version:")
    print(sys.version)

    print("\nWenn alle Module erfolgreich importiert wurden, ist Ihre Umgebung korrekt eingerichtet.")