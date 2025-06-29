def evaluate_metrics(compile_result):
    return {
        "compilation": {
            "success_rate": 1.0 if compile_result["success"] else 0.0,
            "errors_count": compile_result["stderr"].count("error"),
            "warnings_count": compile_result["stderr"].count("warning")
        },
        "overall_score": 40.0 if compile_result["success"] else 0.0
    }
