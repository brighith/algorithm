class Node {
  constructor(data) {
    this.data = data;
    this.next = null;
  }
}

class SLL {
  constructor() {
    this.head = null;
  }
  addFront(val) {
    // Creating a new node object with the value provided
    let new_node = new Node(val);
    // If the list is empty, place the new node as the head
    if (!this.head) {
      this.head = new_node;
      return this;
    }
    // If the list is not empty, assign the head to be the next node to the new node
    new_node.next = this.head;
    this.head = new_node;
    return this;
  }
  removeFront() {
    // If the list is not empty
    if (this.head) {
      let temp = this.head.next;
      this.head = temp;
      return this;
    }
    // If the list is empty, return list
    return this;
  }
  front() {
    return this.head.data;
  }
}

SLL1 = new SLL();
SLL1.addFront(66);
SLL1.addFront(8);
SLL1.addFront(2);
console.log(SLL1);
console.log(SLL1.front());
SLL1.removeFront();
console.log(SLL1.front());
SLL1.removeFront();
console.log(SLL1.front());
SLL1.removeFront();
console.log(SLL1);
