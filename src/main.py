from tools import (
    network_diagnostic,
    password_guidance,
    printer_diagnostic,
    software_diagnostic,
    create_ticket,
)


def run_diagnostic(issue_type):
    diagnostics = {
        "network": network_diagnostic,
        "password": password_guidance,
        "printer": printer_diagnostic,
        "software": software_diagnostic,
    }

    diagnostic = diagnostics.get(issue_type.lower())

    if diagnostic is None:
        return create_ticket(f"Unknown issue type: {issue_type}")

    return diagnostic()


if __name__ == "__main__":
    print(run_diagnostic("network"))
