
const runCommand = id => {
  console.log(id)
  // yes we hardcode local ip's here
  fetch('http://192.168.1.225:8000/run/' + id)
    .then(response => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${reponse.status}`)
      }

      return response.json()
    })
}

const createButton = (command) => {
  const btn = document.createElement("button")

  btn.innerText = command.name
  btn.id = command.id

  btn.addEventListener('click', () => {
    //console.log(btn.id)
    runCommand(btn.id)
  })

  document.getElementById('buttons').appendChild(btn)
}

window.addEventListener("load", () => {

  fetch('http://192.168.1.225:8000/list')
    .then(response => {
      if (!response.ok) {
        throw new Error(`Request failed with status ${reponse.status}`)
      }

      return response.json()
    })
    .then(data => {
      data.commands.forEach(command => {
        createButton(command)
      });
      console.log(data)
    })

})

