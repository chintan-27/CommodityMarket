var weight = 0;
function selected(id,price){
  var i;
  var x = document.getElementById(id.toString())
  weight = id;
  WeightChanged(weight,price);
  x.classList.remove('unselect');
  x.classList.add('select')
  siblings = getSiblings(x)
  for( i in siblings){
    siblings[i].classList.add('unselect');
    siblings[i].classList.remove('select');
  }
  var y = document.getElementById('in');
  y.classList.remove('show');
  var z = document.getElementById(9);
  z.classList.add('unselect');
}


function other(id){

  var x = document.getElementById(id)
  x.classList.remove('select');
  x.classList.add('unselect');
  siblings = getSiblings(x)
  for( i in siblings){
    siblings[i].classList.add('unselect');
    siblings[i].classList.remove('select');
  }
  var y = document.getElementById('in');
  y.classList.add('show');
  var z = document.getElementById(9);
  z.classList.add('select');
}

function weightNew(selectObject,price){
  weight = selectObject.value;
  WeightChanged(weight,price);
}

let getSiblings = function (e) {
  // for collecting siblings
  let siblings = [];
  // if no parent, return no sibling
  if(!e.parentNode) {
      return siblings;
  }
  // first child of the parent node
  let sibling  = e.parentNode.firstChild;

  // collecting siblings
  while (sibling) {
      if (sibling.nodeType === 1 && sibling !== e) {
          siblings.push(sibling);
      }
      sibling = sibling.nextSibling;
  }
  return siblings;
};

function New(){
  if(weight<=0.0){
    location.href=this.href+'/'+weight+ '/';
    return false;
  }
  else{
    alert('Please Select Weight')
  }
}

function WeightChanged(weight,price){
  var price1 = price
  if(weight>10.0 && weight<50.0){
    price1 = price1 - price1*0.01*weight
  }
  var bill = weight*price1;
  document.getElementById("bill").innerHTML = bill.toString();
}
