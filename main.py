from superhero import SuperHero

def start_task(func):
    def wrapper():
        print(f"СТАРТ ЗАДАЧИ {func.__name__}")
        func()
        print(f"КОНЕЦ ЗАДАЧИ {func.__name__}")

    return wrapper


@start_task
def task_1():
    API = "2619421814940190"
    hulk = SuperHero("Hulk", API)
    captain_america = SuperHero("Captain America", API)
    thanos = SuperHero("Thanos", API)
    heroes = [hulk, captain_america, thanos]
    for hero in heroes:
        hero.load_id()
    heroes_iq = {hero.intelligence: hero for hero in heroes}
    key = max(heroes_iq.keys())
    print(f"Умнейший из героев {heroes_iq[key].name}, с интеллектом {heroes_iq[key].intelligence}")

if __name__ == "__main__":
    task_1()
