const resultTEST = document.getElementById('resultTEST')


// gets data from API and sets the content of #result div
async function getData() {
  const fetchDataBtn = document.getElementById('fetchdata')
  const result = document.getElementById('result')
  result.innerText = "Loading....";
  let query = document.getElementById("username").value;
  let url = 'http://127.0.0.1:3000/api/members?username=' + query;
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
                        result.innerText = "無此帳號";
                      });
  
}

