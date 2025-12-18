# 大衍 AI · 后台推演系统

本项目是一个基于《易经》分类学逻辑的AI推演系统，通过用户输入的环境上下文，映射为六十四卦中的语义原型，并结合大模型进行动态演化推演。

## 🌟 核心功能

- **卦象识别**：分析用户输入中的阴阳动静特征，识别对应卦象
- **动态推演**：基于Transformer模型的概率逻辑，推演卦象在当前语境下的演化趋势
- **流式响应**：支持SSE（Server-Sent Events）实时流式输出，提供沉浸式推演体验
- **Markdown渲染**：前端自动将AI输出的Markdown格式内容渲染为富文本

## 🛠 技术栈

- **后端**：Python + Flask
- **前端**：HTML5 + JavaScript + marked.js
- **AI引擎**：兼容OpenAI API的LLM（默认配置为DeepSeek）
- **环境管理**：python-dotenv

## ⚙️ 环境配置

1. 安装依赖：
```bash
pip install flask python-dotenv openai
```

2. 创建 `.env` 文件并配置API密钥：
```env
DEEPSEEK_API_KEY=your_api_key_here
DEEPSEEK_BASE_URL=https://api.deepseek.com
DEEPSEEK_MODEL=deepseek-chat
```

> 支持任意兼容OpenAI API的模型服务，只需修改对应的环境变量即可。

## 🚀 启动服务

```bash
python app.py
```

服务默认运行在 `http://localhost:5000`

## 📁 项目结构

```
├── app.py              # Flask主应用
├── .env                # 环境配置文件
├── readme.md           # 项目说明文档
└── templates/
    └── index.html      # 前端界面
```

## 💡 使用说明

1. 访问 `http://localhost:5000`
2. 在文本框中描述当前的环境、局势或困惑
3. 点击"开启推演"按钮
4. 系统将实时输出基于《易经》逻辑的推演结果

## 🎯 设计理念

> "观乎天文以察时变，观乎人文以化成天下"

本系统旨在将古老的《易经》智慧与现代AI技术相结合，为用户提供具有启发性的决策参考，而非确定性预测。

## 📄 许可证

本项目仅供学习和研究使用。