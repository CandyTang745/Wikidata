# 导入必要模块
# import openai
# sk-87ab1d6ce0f34fe493a8109009a2d700

import dashscope

# 设置你的通义API Key
dashscope.api_key = 'sk-87ab1d6ce0f34fe493a8109009a2d700'  # ⚠️把这里换成自己的key

# 小型知识库
wikidata_knowledge = [
    {
        'subject': 'http://www.wikidata.org/entity/Q148',  # China
        'predicate': 'http://www.wikidata.org/prop/direct/P2924',  # population
        'object': '1411778724'
    },
    {
        'subject': 'http://www.wikidata.org/entity/Q30',  # USA
        'predicate': 'http://www.wikidata.org/prop/direct/P2924',
        'object': '331893745'
    }
]

# 检索函数
def retrieve_facts(question):
    facts = []
    if "China" in question and "population" in question:
        facts.append("China (Q148) has a population of 1411778724.")
    elif "USA" in question and "population" in question:
        facts.append("USA (Q30) has a population of 331893745.")
    else:
        facts.append("No relevant data found.")
    return " ".join(facts)

# 调用通义千问生成回答
def generate_answer(question, context):
    prompt = f"""根据以下背景信息回答问题，要求详细且人性化。
背景信息：
{context}

问题：
{question}

答案："""

    response = dashscope.Generation.call(
        model='qwen-turbo',  # 使用轻量版模型，够用了
        prompt=prompt,
    )
    return response['output']['text'].strip()

# 主程序入口
if __name__ == "__main__":
    question = "What is the population of China?"

    # 1. 检索相关事实
    context = retrieve_facts(question)
    print("📚 检索到的背景知识：")
    print(context)
    print()

    # 2. 大模型生成回答
    answer = generate_answer(question, context)
    print("🤖 大模型生成的回答：")
    print(answer)
