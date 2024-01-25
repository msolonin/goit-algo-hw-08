# -*- coding: utf-8 -*-
"""
Уявіть, що вам на технічному інтерв'ю дають наступну задачу, яку треба розв'язати за допомогою купи.
Є декілька мережевих кабелів різної довжини, їх потрібно об'єднати по два за раз в один кабель,
використовуючи з'єднувачі, у порядку, який призведе до найменших витрат. Витрати на з'єднання двох кабелів дорівнюють
їхній сумі довжин, а загальні витрати дорівнюють сумі з'єднання всіх кабелів.
Завдання полягає в тому, щоб знайти порядок об'єднання, який мінімізує загальні витрати.
"""

import heapq


def minimize_costs(cables):
    cables = cables[:]
    heapq.heapify(cables)
    while len(cables) > 1:
        cable_1 = heapq.heappop(cables)
        cable_2 = heapq.heappop(cables)
        combined_cable = cable_1 + cable_2
        heapq.heappush(cables, combined_cable)
    try:
        total_costs = cables[0]
    except IndexError:
        total_costs = None
    return total_costs


if __name__ == "__main__":
    cable_lengths = [1, 3, 3, 4, 5, 5, 9, 9, 10, 11, 11, 12, 13, 13, 14, 15, 16, 16, 16, 17, 18, 19, 20]
    result = minimize_costs(cable_lengths)
    print("Sum of costs:", result)
