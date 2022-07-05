

function search(){
  const raw_tags = document.getElementById("answers").value;
}


  function post(){
    const post_content = document.getElementById("post").value;
    fetch('https://ciw53fwcnk.execute-api.us-east-1.amazonaws.com/Dev/post', {
      method: 'POST', // or 'PUT'
      mode: 'cors', // no-cors, *cors, same-origin
      cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
      credentials: 'same-origin', // include, *same-origin, omit
      origin: '*',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({"content": post_content}),
    }).then((response) => response.json())
    //Then with the data from the response in JSON...
    .then((data) => {
      document.getElementById('output1').innerHTML = JSON.stringify(data);
    })
    //Then with the error genereted...
    .catch((error) => {
      console.error('Error:', error);
    });

  }