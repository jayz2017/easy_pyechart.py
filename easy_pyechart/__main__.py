from __future__ import annotations

import uvicorn


def main() -> None:
    uvicorn.run(
        "easy_pyechart.api:app",
        host="0.0.0.0",
        port=8889,
        reload=False,
        workers=1,
    )


if __name__ == "__main__":
    main()
