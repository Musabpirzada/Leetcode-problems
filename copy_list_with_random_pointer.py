if not head:
            return None

        # Step 1: Create a mapping between original and new nodes
        node_mapping = {}

        # Step 2: Create new nodes and populate the mapping
        current = head
        while current:
            node_mapping[current] = Node(current.val)
            current = current.next

        # Step 3: Update next and random pointers in the new list
        current = head
        while current:
            if current.next:
                node_mapping[current].next = node_mapping[current.next]
            if current.random:
                node_mapping[current].random = node_mapping[current.random]
            current = current.next

        # Step 4: Return the head of the new list
        return node_mapping[head]
