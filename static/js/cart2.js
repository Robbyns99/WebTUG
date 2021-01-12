var updateBtns = document.getElementsByClassName('update-cart')

for (var i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click', function(){
      var produkId = this.dataset.produk
      var action = this.dataset.action
      console.log('produkId:', produkId, 'Action:', action)

      console.log('USER:', user)
      if (user == 'AnonymousUser'){
        addCookieItem(produkId, action)
      }else{
        updateUserOrder(produkId, action)
      }
    })
}

function addCookieItem(produkId, action){
  console.log('User is not authenticated')

  if (action == 'add'){
    if (cart[produkId] == undefined){
      cart[produkId] = {'jumlah':1}
    }else{
      cart[produkId]['jumlah'] += 1
    }
  }
  if (action == 'remove'){
    cart[produkId]['jumlah'] -= 1

    if (cart[produkId]['jumlah'] <= 0){
      console.log('Item telah dihapus')
      delete cart[produkId];
    }
  }
  console.log('Cart:', cart)
  document.cookie = 'cart=' + JSON.stringify(cart)+";domain=;path=/"
  console.log('document.cookie :', document.cookie)
  location.reload()
}

function updateUserOrder(produkId, action){
  console.log('User is authenticated, mengirim data...')
  
    var url = '/update_item/'

    fetch(url, {
      method:'POST',
      headers:{
        'Content-Type':'application/json',
        'X-CSRFToken':csrftoken,
      }, 
      body:JSON.stringify({'produkId':produkId, 'action':action})
    })
    .then((response) => {
      return response.json();
    })
    .then((data) => {
      console.log('data:', data)
      location.reload()
    });
}