import dashscope
from dashscope import Generation

dashscope.base_http_api_url = 'https://dashscope-intl.aliyuncs.com/api/v1'
dashscope.api_key = 'sk-8df1be7f178d46bca355735b2ff11757'

response = Generation.call(
    model='qwen-max',
    prompt='What is the capital of France?'
)

print("🤖 Response:")
print(response.output.text)
