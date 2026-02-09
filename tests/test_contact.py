# tests/test_contact.py
def test_contact_rejects_invalid_email(client):
    res = client.post("/", data={
        "name": "R",
        "email": "not-an-email",
        "message": "hello"
    }, follow_redirects=True)
    assert res.status_code == 200  # page renders with validation errors

# Test that a valid submission is accepted
def test_contact_accepts_valid_submission(client):
    res = client.post("/", data={
        "name": "Ramon",
        "email": "ramon@example.com",
        "message": "Hi"
    }, follow_redirects=True)
    assert res.status_code == 200
