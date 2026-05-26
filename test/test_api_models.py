from easy_pyechart.examples import get_example
from easy_pyechart.schemas import ChartRequest


def test_swagger_example_can_build_chart_request():
    example = get_example("bar")
    request = ChartRequest(**example)

    assert request.chart_type == "bar"
    assert request.title == example["title"]
    assert request.series[0].name == example["series"][0]["name"]


def test_other_chart_examples_are_valid_requests():
    chart_types = [
        "line",
        "pie",
        "radar",
        "sankey",
        "scatter",
        "treemap",
        "liquid",
        "gauge",
        "funnel",
        "graph",
        "parallel",
        "grid",
        "table",
    ]
    for chart_type in chart_types:
        request = ChartRequest(**get_example(chart_type))

        assert request.chart_type == chart_type


def test_openapi_contains_chart_request_example():
    from easy_pyechart.api import app

    schema = app.openapi()
    examples = schema["components"]["schemas"]["ChartRequest"]["examples"]
    style_enum = schema["components"]["schemas"]["ChartRequest"]["properties"]["style"]["enum"]

    assert examples[0]["chart_type"] == "bar"
    assert examples[0]["series"][0]["name"] == get_example("bar")["series"][0]["name"]
    assert "aurora" in style_enum
    assert "neon" in style_enum
    assert "luxe" in style_enum


def test_batch_render_examples_endpoint(tmp_path, monkeypatch):
    monkeypatch.setenv("EASY_PYECHART_OUTPUT_DIR", str(tmp_path))
    monkeypatch.setenv("EASY_PYECHART_CAPTURE_IMAGES", "false")

    from fastapi.testclient import TestClient
    from easy_pyechart.api import app

    with TestClient(app) as client:
        response = client.post("/api/v1/charts/render/examples")

    payload = response.json()
    assert response.status_code == 200
    assert payload["total"] == 14
    assert len(payload["rendered"]) == 14
    assert any(item["gif_path"] is None for item in payload["rendered"])
    assert (tmp_path / "logs" / "render-history.jsonl").exists()
    assert (tmp_path / "html" / "bar.html").exists()
    assert (tmp_path / "requests").exists()
