# tests/test_routes.py
def test_home_200(client):
    res = client.get("/")
    assert res.status_code == 200

# This test checks that the /projects route returns a 200 status code and that the response contains the word "Test", which indicates that the projects are being listed correctly.
def test_projects_200_and_lists_projects(client):
    res = client.get("/projects")
    assert res.status_code == 200
    assert b"Test" in res.data
