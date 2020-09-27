from concurrent.futures import ThreadPoolExecutor
import random
import statistics
import matplotlib.pyplot as plt
import settings


def step(amount):
    coin = random.choice(['h', 't'])
    if coin == 'h':
        return amount * 1.5
    else:
        return amount * 0.6

def game(number_steps, initial_amount):
    current_amount = initial_amount
    step_results = []
    for i in range(0, number_steps):
        current_amount = step(current_amount)
        step_results.append(current_amount)
    return step_results


def simulation(number_players, initial_amount, number_steps):
    results = []
    with ThreadPoolExecutor(max_workers = 100) as executor:
        for p in range(0, number_players):
            future = executor.submit(game, number_steps, initial_amount)
            results.append(future.result())

    list_averages = []
    for i in range(0, number_steps):
        list_averages.append(statistics.mean([pr[i] for pr in results]))
    fig = plt.figure("Average")
    plt.plot(list_averages)
    fig.savefig(f'output/average_{number_players}.png')
    

simulation(
    settings.NUMBER_OF_PLAYERS,
    settings.INITIAL_AMOUNT,
    settings.NUMBER_OF_STEPS
)
