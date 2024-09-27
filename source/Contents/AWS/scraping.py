import argparse
import io
import os
from collections import defaultdict
from string import Template

import requests
from bs4 import BeautifulSoup

FEATURE_BASE_URL = "https://aws.amazon.com/jp/"
API_BASE_URL = "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/"
BAT_FILE = "../../../make.bat html"
TEMPLATE_BASE_PATH = "../../_templates/"


def scrape_aws_api_reference(url: str):
    """
    descriptionのstrとapiのlistを返す。
    """

    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # descriptionを取得
    description_div = soup.find("div", class_="section", id="description")
    p_tag = description_div.find("p").text

    # apiのliを取得
    api_div = soup.find("div", class_="section", id="available-commands")
    ul_elements = api_div.find_all("ul")

    li_items = []
    for ul in ul_elements:
        li_elements = ul.find_all("li")
        li_items = [li.get_text(strip=True) for li in li_elements]

    return p_tag, li_items


def categorize_api(api_list):
    """
    各APIをCRUDごとにまとめる。
    """

    result = defaultdict(list)
    uncategorized = []

    for api in api_list:
        # ハイフンが含まれない場合はスキップ
        if "-" not in api:
            uncategorized.append(api)
            continue

        parts = api.split("-")

        # 最初の部分を除去
        category_parts = parts[1:]

        # カテゴリを決定
        if len(category_parts) > 1:
            # 最後の部分が他のアクションと共通でない場合、それを含めてカテゴリ化
            potential_category = "-".join(category_parts)
            if sum(1 for a in api_list if a.endswith(potential_category)) > 1:
                category = potential_category
            else:
                # 最後の部分を除いてカテゴリ化
                category = "-".join(category_parts[:-1])
        else:
            category = category_parts[0]

        result[category].append(api)

    return dict(result), uncategorized


if __name__ == "__main__":
    # Create URL PATH
    parser = argparse.ArgumentParser()
    parser.add_argument("aws_service_name", help="Input aws service name.")
    args = parser.parse_args()
    service = args.aws_service_name

    feature_url = FEATURE_BASE_URL + service
    api_url = API_BASE_URL + service + "/index.html"

    # Run web scraping.
    api_list = []
    description, api_list = scrape_aws_api_reference(api_url)

    # 分類を実行
    categorized, uncategorized = categorize_api(api_list)

    # featureページを生成
    with open(
        TEMPLATE_BASE_PATH + "feature_template.txt", mode="r", encoding="utf-8"
    ) as f:
        feature_template = Template(f.read())
    feature_write_content = feature_template.substitute(page_url=feature_url)

    feature_path = "./" + service + "/001_Guide/"
    os.makedirs(feature_path, exist_ok=True)
    with open(feature_path + "index.rst", mode="w", encoding="utf-8") as f:
        f.write(feature_write_content)

    # APIページを生成
    output = io.StringIO()

    for category, link_list in categorized.items():
        output.write(f"{category}:\n")
        for link in link_list:
            output.write(f"  * `{link} <{API_BASE_URL}{service}/{link}.html>`_\n")
        output.write("\n")

    for link in uncategorized:
        output.write(f"  * `{link} <{API_BASE_URL}{service}/{link}.html>`_\n")

    api_sorted_text = output.getvalue()

    with open(TEMPLATE_BASE_PATH + "api_template.txt", mode="r", encoding="utf-8") as f:
        api_template = Template(f.read())
    api_write_content = api_template.substitute(
        description=description, api=api_sorted_text, page_url=api_url
    )

    api_path = "./" + service + "/002_API/"
    os.makedirs(api_path, exist_ok=True)
    with open(api_path + "index.rst", mode="w", encoding="utf-8") as f:
        f.write(api_write_content)

    # aws master index作成
    with open("./index.rst", mode="r", encoding="utf-8") as f:
        aws_master_index = f.read()
    if service not in aws_master_index:
        with open("./index.rst", mode="a", encoding="utf-8") as f:
            f.write("   " + service + "/index\n")

    # aws service index作成
    with open(
        TEMPLATE_BASE_PATH + "service_index.txt", mode="r", encoding="utf-8"
    ) as f:
        service_template = Template(f.read())
    service_index = service_template.substitute(service=service)
    with open("./" + service + "/index.rst", mode="w", encoding="utf-8") as f:
        f.write(service_index)
