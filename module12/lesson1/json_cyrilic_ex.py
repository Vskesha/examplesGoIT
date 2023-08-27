import json


if __name__ == '__main__':
    data = {
        'dev':
            {
                'name': 'Вася',
                'position': 'програміст'
            }
    }

    with open('data_user.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    with open('data_user.json', 'r', encoding='utf-8') as f:
        restore_data = json.load(f)
        print(restore_data)
