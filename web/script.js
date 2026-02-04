const API = "http://localhost:5000/items";

document.getElementById("form").addEventListener("submit", criarItem);

// ⭐ FETCH GET
async function carregar() {

const res = await fetch(API);
const dados = await res.json();

const lista = document.getElementById("lista");
lista.innerHTML = "";

dados.forEach(item => {

lista.innerHTML += `
<tr>
<td>${item.id}</td>
<td>${item.titulo}</td>
<td>${item.tipo}</td>
<td>${item.status}</td>
<td>
<button onclick="deletar(${item.id})">Excluir</button>
</td>
</tr>
`;

});

}

// ⭐ FETCH POST
async function criarItem(e) {

e.preventDefault();

const item = {
titulo: document.getElementById("titulo").value,
tipo: document.getElementById("tipo").value,
status: document.getElementById("status").value
};

await fetch(API, {
method: "POST",
headers: {
"Content-Type": "application/json"
},
body: JSON.stringify(item)
});

carregar();

}

// ⭐ FETCH DELETE
async function deletar(id) {

await fetch(`${API}/${id}`, {
method: "DELETE"
});

carregar();

}

carregar();
