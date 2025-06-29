import subprocess

def compile_driver(file_path):
    try:
        result = subprocess.run(
            ["gcc", "-Wall", "-Wextra", "-Werror", file_path],
            capture_output=True, text=True
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr
        }
    except Exception as e:
        return {"success": False, "error": str(e)}
