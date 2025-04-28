import requests

def get_qids_from_class(class_qid="Q6256", limit=100):
    endpoint = "https://query.wikidata.org/sparql"
    query = f"""
    SELECT ?item WHERE {{
      ?item wdt:P31 wd:{class_qid}.
    }}
    LIMIT {limit}
    """
    headers = {
        "Accept": "application/sparql-results+json"
    }
    response = requests.get(endpoint, params={"query": query}, headers=headers)
    data = response.json()
    qids = [item["item"]["value"].split("/")[-1] for item in data["results"]["bindings"]]
    return qids

# 示例：获取前 100 个国家的 Q 编号
country_qids = get_qids_from_class("Q6256", limit=100)
print("国家实体 QID 列表：", country_qids)
