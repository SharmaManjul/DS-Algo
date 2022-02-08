class Node{
  constructor(value){
      this.value = value,
      this.next = null
  }
}

class LinkedList{
  constructor(value){
    this.head = new Node(value);
    this.tail = this.head
    this.length = 1
  }

  append(value){
    const newNode = new Node(value);
    this.tail.next = newNode
    this.tail = newNode
    this.length ++
  }

  prepend(value){
    const newNode= new Node(value)
    newNode.next = this.head
    this.head = newNode
    this.length ++

  }

  insert(index, value){
    let newNode = new Node(value)

    if (index === 0) {
     this.prepend(value);
     return
    }

    if(index > this.length){
      this.append(value)
      return
    }

    let prev = this.traverseToIndex(index-1)
    newNode.next = prev.next
    prev.next = newNode

  }

  remove(index){
    if(index === 0){
      this.head = this.head.next
      this.length --
      return
    }

    if ((index>this.length)||(index<0)){
      console.log("Undefined index")
      return
    }

    let prev = this.traverseToIndex(index-1)
    let cur = prev.next
    prev.next = cur.next
    this.length --
  }

  traverseToIndex(index){
    let counter = 0
    let curNode = this.head
    while (counter !== index){
      curNode = curNode.next
      counter++
    }
    return curNode
  }

  printList(){
    const array = []
    let curNode = this.head
    while(curNode !== null){
      array.push(curNode.value)
      curNode = curNode.next
    }
    console.log(array)
  }
}

let myLinkedList = new LinkedList(10);
myLinkedList.append(5);
myLinkedList.append(16);
myLinkedList.prepend(100);
myLinkedList.insert(2, 66)
myLinkedList.printList()
myLinkedList.remove(2)
myLinkedList.printList()
