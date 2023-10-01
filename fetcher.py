import requests
import time

# Hacker NewsのAPIのベースURL
HN_API_BASE_URL = "https://hacker-news.firebaseio.com/v0"


def get_top_stories_ids():
    # トップニュースのIDを取得する関数。
    response = requests.get(f"{HN_API_BASE_URL}/topstories.json")
    return response.json()[:30]  # 最初の30つのニュースのIDを返す


def get_story_details(story_id):
    """
    特定のニュースの詳細情報を取得する関数。
    :param story_id: ニュースのID
    :return: ニュースの詳細情報を含む辞書
    """
    response = requests.get(f"{HN_API_BASE_URL}/item/{story_id}.json")
    return response.json()


def main():
    # メインの処理を行う関数。
    top_stories_ids = get_top_stories_ids()
    for story_id in top_stories_ids:
        story_details = get_story_details(story_id)
        title = story_details.get("title")
        link = story_details.get("url", "None")
        # リンクが存在するニュースのみを表示
        if link != "None":
            # 指定された形式で出力
            print(f"{{'title': '{title}', 'link': '{link}'}}")
        # 次のAPI呼び出しまで1秒待機
        time.sleep(1)


if __name__ == "__main__":
    main()
