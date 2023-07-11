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
    let new_node = new Node(val);
    if (!this.head) {
      this.head = new_node;
      return this;
    }
    new_node.next = this.head;
    this.head = new_node;
    return this;
  }
  removeFront() {
    if (this.head) {
      let temp = this.head.next;
      this.head = temp;
      return this;
    }
    return this;
  }
  front() {
    return this.head.data;
  }
  contains(value) {
    let node = this.head;
    while (node !== null) {
      if (node.data == value) {
        return true;
      }
      node = node.next;
    }
    return false;
  }
  length() {
    let counter = 0;
    let node = this.head;
    while (node !== null) {
      counter++;
      node = node.next;
    }
    return counter;
  }
}

SLL1 = new SLL();
SLL1.addFront(76);
SLL1.addFront(9);
SLL1.addFront(67);
SLL1.addFront(45);
console.log(SLL1);
console.log(SLL1.front());
SLL1.removeFront();
console.log(SLL1.front());
SLL1.removeFront();
console.log(SLL1.front());
console.log(SLL1.contains(76));
console.log(SLL1.contains(5));
console.log(SLL1.length());
SLL1.addFront(13);
console.log(SLL1.length());
