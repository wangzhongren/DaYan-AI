import os
from dotenv import load_dotenv
from flask import Flask, render_template, Response, request, stream_with_context
from openai import OpenAI
import json

load_dotenv()

app = Flask(__name__)

# 从环境变量读取配置
CONFIG = {
    "API_KEY": os.getenv("DEEPSEEK_API_KEY"),
    "BASE_URL": os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"),
    "MODEL": os.getenv("DEEPSEEK_MODEL", "deepseek-chat")
}

SYSTEM_PROMPT = """你是一个基于《易经》分类学逻辑的AI推演系统。
你的核心逻辑是：将用户描述的“环境上下文”映射为六十四卦中的某种“语义原型”。
请执行：
1. 提取特征：分析输入中的阴阳动静特征。
2. 确定卦象：识别当前所属卦象并给出符号。
3. 推演未来：基于Transformer的动态概率逻辑，推演此卦象在当前语境下的演化趋势。
请以深邃、宁静、具有启发性的语气输出。"""

# 初始化 OpenAI 兼容客户端
client = OpenAI(
    api_key=CONFIG["API_KEY"],
    base_url=CONFIG["BASE_URL"].rstrip()  # 确保无多余空格
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/deduce', methods=['POST'])
def deduce():
    user_input = request.json.get('content')

    def generate():
        stream = client.chat.completions.create(
            model=CONFIG["MODEL"],
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_input}
            ],
            stream=True
        )
        for chunk in stream:
            # chunk 是 ChatCompletionChunk 对象
            if chunk.choices and chunk.choices[0].delta and chunk.choices[0].delta.content:
                content = chunk.choices[0].delta.content
                # 按照 SSE 格式发送
                yield f"data: {json.dumps({'content': content})}\n\n"
        yield "data: [DONE]\n\n"

    return Response(stream_with_context(generate()), mimetype='text/event-stream')

if __name__ == '__main__':
    app.run(debug=True, port=5000)