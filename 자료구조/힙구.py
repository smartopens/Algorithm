class MaxHeap(object):
    def __init__(self, items):
        self.queue = [None] + items  # 0 번 인덱스 사용하지 않은 경우

        # 절반의 노드만 heapify하면 됨
        for i in range(len(self.queue) // 2, 0, -1):
            self.max_heapify(i)

    def parent(self, index):
        return index // 2

    def left_child(self, index):
        return index * 2

    def right_child(self, index):
        return index * 2 + 1

    def swap(self, i, parent_index):
        self.queue[i], self.queue[parent_index] = self.queue[parent_index], self.queue[i]

    def insert(self, n):
        self.queue.append(n)
        for i in range(len(self.queue) // 2, 0, -1):
            self.max_heapify(i)

    def delete(self):
        last_index = len(self.queue) - 1
        if last_index == 0:
            return - 1  # empty

        self.swap(1, last_index)
        max_value = self.queue.pop()
        self.max_heapify(1)  # root에서부터 재정렬
        return max_value

    # 임시 root 부터 자식 노드와 값을 비교하며 재정렬하는 함수
    def max_heapify(self, i):
        last_index = len(self.queue) - 1
        left_index = self.left_child(i)
        right_index = self.right_child(i)
        temp_max_index = i  # 일단 자기 자신을 max로 둠 (임시 root노드)
        print(left_index,right_index)
        # 리프 노드에 한해, 임시 루트 노드보다 값이 더 크면, 해당 노드의 인덱스를 루트 인덱스로 변경
        if left_index <= last_index and self.queue[temp_max_index] < self.queue[left_index]:
            temp_max_index = left_index
        if right_index <= last_index and self.queue[temp_max_index] < self.queue[right_index]:
            temp_max_index = right_index

        # 만약 자신이 가장 큰게 아니면 heapify
        if temp_max_index != i:
            self.swap(i, temp_max_index)# temp_max_index가 루트 노드로 변경
            print(self.queue,temp_max_index)
            self.max_heapify(temp_max_index)  # 재정렬 재귀

    def print_heap(self):
        print(self.queue)


max_heap = MaxHeap([1,2,3,4,5,6])
max_heap.print_heap()