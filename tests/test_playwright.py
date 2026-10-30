from playwright.sync_api import sync_playwright


def test_get_employees():
    with sync_playwright() as playwright:
        request = playwright.request.new_context(
            base_url="http://127.0.0.1:5000"
        )

        response = request.get("/employees")

        assert response.status == 200

        data = response.json()
        assert isinstance(data, list)

        request.dispose()

def test_add_employee():
    with sync_playwright() as playwright:
        request = playwright.request.new_context(
            base_url="http://127.0.0.1:5000"
        )

        employee = {
            "name": "Test Employee",
            "start_date": "2026-09-15",
            "location": "London",
            "role": "Developer"
        }

        response = request.post(
            "/employees",
            data=employee
        )

        assert response.status == 201

        request.dispose()
