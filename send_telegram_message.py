import requests
import sys


def send_telegram_message(*args):
    message = f"{args[3]} created commit:\n" \
              f"Commit message: {args[4]}\n" \
              f"Repository: {args[5]}\n" \
              f"See changes: {args[6]}\n" \
              f"\n👌 Deployment successfully completed!\n" \
              f"\nPR Information:" \
              f"\nTitle: {args[7]}" \
              f"\nPR Number: {args[8]}" \
              f"\nAuthor: {args[9]}" \
              f"\nBase Branch: {args[10]}" \
              f"\nHead Branch: {args[11]}" \
              f"\nURL: {args[12]}"

    url = f'https://api.telegram.org/bot{args[0]}/sendMessage'
    params = {
        'chat_id': args[1],
        'text': message,
        'parse_mode': 'HTML',
        'message_thread_id': args[2]
    }

    response = requests.post(url, params=params)

    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message. Status code: {response.status_code}")
        print(response.text)


if __name__ == '__main__':
    print(*sys.argv)
    send_telegram_message(*sys.argv)
