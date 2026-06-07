import random

# page_loading = {'loaded', 'loading', 'error'}

# page_condition = random.choice(list(page_loading))
internet_status = input("Is internet working? (y/n): ").strip().lower()

def page_status():
    if internet_status == 'y':
        page_loading = {'loaded', 'loading', 'error'}
        page_condition = random.choice(list(page_loading))
        print(page_condition)
    else:
        page_loading = {'loading', 'error'}
        page_condition = random.choice(list(page_loading))
        print(page_condition)


page_status()