"""Tests for hello endpoints"""
from fastapi.testclient import TestClient


def test_hello(client: TestClient):
    """Test hello endpoint"""
    response = client.get("/api/v1/hello")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, World!"


def test_hello_with_name(client: TestClient):
    """Test hello endpoint with name parameter"""
    response = client.get("/api/v1/hello/ToBox")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Hello, ToBox!"


def test_root(client: TestClient):
    """Test root endpoint"""
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert "version" in data


def test_health_check(client: TestClient):
    """Test health check endpoint"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
