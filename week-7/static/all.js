// gets data from API and sets the content of #result div
async function getData() {
  const fetchDataBtn = document.getElementById('fetchData')
  const result = document.getElementById('searchResult')
  result.innerText = "Loading....";
  let query = document.getElementById("username").value;
  let url = 'http://127.0.0.1:3000/api/member?username=' + query;
  console.log (url);
  const jsonResult = await fetch(url)
                      .then(res => res.json())
                      .then(data => {
                        const dataForm = data;
                        const nameJSON = data['data']['name'];
                        const usernameJSON = data['data']['username'];
                        console.log(nameJSON);
                        if (usernameJSON == null){
                          result.innerHTML = "無此帳號";
                        }
                        else{
                          result.innerHTML = nameJSON + '(' + usernameJSON + ')';
                        }
                      })
                      .catch(fail => {
                        result.innerText = "錯誤";
                      });
}


// post some data to the app
function editName(){
  const newName = document.getElementById('newName').value
  const result = document.getElementById('editResult')
  result.innerText = "Loading...."
  let url = 'http://127.0.0.1:3000/api/members'
  console.log (url);
  // data to be sent to the POST request
  let data = {
   'name': newName
  }
  fetch(url, {
  method: "POST",
  body: JSON.stringify(data),
  headers: {"Content-type": "application/json; charset=UTF-8"}
})
.then(res => res.json()) 
.then(success => result.innerHTML = "更新成功")
.catch(fail => console.log(fail));
  
}

