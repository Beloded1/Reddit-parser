import requests
from collections import Counter


def display_instruct()->None:
    print('Это простая программа выполняет парсинг с нужного раздела Reddit, \n выводит на экран заголовки постов,\
          \n выводит на экран топ пользователей по комментариям,\
          \n выводит на экран топ пользователей по постам.')


def input_subreddit()->str:
    subreddit_name = str(input('Введите название раздела Reddit > '))
    return subreddit_name


def get_top_users(data:list[dict], key:str, limit:int)->list[tuple[str, int]]:
    users = Counter([item['data']['author'] for item in data])
    top_users = users.most_common(limit)
    return top_users

def main():
    display_instruct()
    subreddit = input_subreddit()
    url = f'https://www.reddit.com/r/{subreddit}/new.json?limit=100'

    response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        print("Заголовки постов:")
        for post in posts:
            title = post['data']['title']
            print(title)

        top_comment_users = get_top_users(posts, 'num_comments', 10)
        print("\nТоп пользователей по комментариям:")
        for user, count in top_comment_users:
            print(f"{user}: {count} комментариев")

        top_post_users = get_top_users(posts, 'num_comments', 10)
        print("\nТоп пользователей по постам:")
        for user, count in top_post_users:
            print(f"{user}: {count} постов")
    else:
        print('Error:', response.status_code)

if __name__ == '__main__':
    main()

