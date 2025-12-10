import heapq 

def min_cost_to_connect_cables(cables): 

    """
   Обчислює мінімальну вартість з'єднання всіх кабелів у один.
   Використовує мінімальну купу для ефективного вибору найкоротших кабелів.
    """
    if not cables:
        return 0

    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        first = heapq.heappop(cables)
        second = heapq.heappop(cables)
        cost = first + second
        total_cost += cost
        heapq.heappush(cables, cost)

    return total_cost
# Приклад використання
if __name__ == "__main__":
    cables = [4, 3, 2, 6]
    print("Мінімальна вартість з'єднання кабелів:", min_cost_to_connect_cables(cables))