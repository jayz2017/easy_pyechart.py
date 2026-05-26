# easy_pyechart

`easy_pyechart` 是基于 pyecharts 的图表封装项目。当前保留原有图表类和示例脚本，同时新增了一套对外访问的 FastAPI 服务结构。

## 新增结构

```text
easy_pyechart/
  api.py          # FastAPI 应用，Swagger 地址为 /docs
  examples.py     # Swagger 和示例接口使用的模拟数据
  factory.py      # 统一请求模型到 pyecharts 图表的构建工厂
  schemas.py      # Pydantic 请求/响应模型
  services.py     # 线程池渲染服务
  styles.py       # 统一样式、主题和配色
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 启动 API

```bash
python -m easy_pyechart
```

或：

```bash
uvicorn easy_pyechart.api:app --host 0.0.0.0 --port 8889
```

启动后访问：

- Swagger: <http://127.0.0.1:8889/docs>
- 健康检查: <http://127.0.0.1:8889/health>
- 示例列表: <http://127.0.0.1:8889/api/v1/examples>
- 柱状图示例: <http://127.0.0.1:8889/api/v1/examples/bar>

Swagger 的 `/api/v1/charts/render` 请求体已内置柱状图模拟数据，可直接点击 `Try it out` 调用。

## 渲染接口

`POST /api/v1/charts/render`

- `render_format=html`: 返回 HTML 字符串。
- `render_format=file`: 保存 HTML 到 `G:\echaet\html\` 目录，`output_path` 只能是相对路径。

`POST /api/v1/charts/render/html`

- 直接返回可展示的 HTML 页面。

`POST /api/v1/charts/render/examples`

- 一次性渲染所有内置示例图表。
- HTML 输出目录：`G:\echaet\html\`
- PNG 图片目录：`G:\echaet\images\`
- GIF 动图目录：`G:\echaet\gifs\`
- 请求入参目录：`G:\echaet\requests\`
- 渲染追踪日志：`G:\echaet\logs\render-history.jsonl`
- 最新输出清单：`G:\echaet\latest-manifest.json`

每条日志都会记录 `render_id`、图表类型、样式、配色、HTML/PNG/GIF 输出路径和完整请求入参，后续调整样式和配色时可以按文件追溯。
批量示例默认会为 `line`、`liquid`、`gauge`、`graph`、`sankey`、`parallel` 输出 GIF；单张图可在请求体里设置 `capture_gif=true`。

## 支持图表

当前统一 API 支持：

- `bar`
- `line`
- `pie`
- `radar`
- `sankey`
- `scatter`
- `treemap`
- `liquid`
- `gauge`
- `funnel`
- `graph`
- `parallel`
- `grid`
- `table`

## 并发说明

API 服务内部使用 `ThreadPoolExecutor` 渲染图表，避免同步 pyecharts 渲染阻塞事件循环。可通过环境变量调整：

```bash
set EASY_PYECHART_MAX_WORKERS=16
set EASY_PYECHART_OUTPUT_DIR=G:\echaet
```
