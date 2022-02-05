class HashTable {
  constructor(size){
    this.data = new Array(size);
  }

  //Custom hash function
  _hash(key) {//O(1), since it is really fast.
    let hash = 0;
    for (let i =0; i < key.length; i++){
        hash = (hash + key.charCodeAt(i) * i) % this.data.length
    }
    return hash;
  }

//Sets value in hash table.
set(key, value){//O(1) since no looping
  let address = this._hash(key)
  if(!this.data[address]){
    this.data[address]=[]
  }
  this.data[address].push([key,value])
}

//Gets value from hash table.
get(key){//O(1) in most cases when enough memory so no for loop but can be O(n)
  let address = this._hash(key)
  let curBucket = this.data[address]
  if(curBucket){
    for(let i= 0; i<curBucket.length; i++){
      if(curBucket[i][0] === key){
        console.log(curBucket[i][1])
      }
    }
  }
  return(undefined)
}
}

//Lists all the keys in the hash table.
lister(){
  let listArray = []
  for(let i =0; i<this.data.length; i++){//Big draw back as we have to loop the entire hashtable since the keys can be anywhere: O(n)
    if(this.data[i]){
      console.log(this.data[i][0][0])
    }
  }
}
}


const myHashTable = new HashTable(50);
myHashTable.set('grapes', 10000)
myHashTable.get('grapes')
myHashTable.set('apples', 67)
myHashTable.get('apples')
myHashTable.set('chicken', 88)
myHashTable.set('banana', 45)
myHashTable.lister()
