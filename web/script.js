const API = "http://localhost:5000/items";

let editandoId = null;

document.getElementById("form").addEventListener("submit", enviarForm);

function msg(texto){
    const el = document.getElementById("msg");
    if(!el) return;
    el.textContent = texto;
    el.style.display = "block";
}

function limparMsg(){
    const el = document.getElementById("msg");
    if(!el) return;
    el.textContent = "";
    el.style.display = "none";
}

async function carregar(){

    try{
        msg("Carregando...");

        const tipo = document.getElementById("filtroTipo")?.value || "";
        const status = document.getElementById("filtroStatus")?.value || "";

        let url = API;

        const params = [];
        if(tipo) params.push(`tipo=${encodeURIComponent(tipo)}`);
        if(status) params.push(`status=${encodeURIComponent(status)}`);

        if(params.length > 0){
            url = `${API}?${params.join("&")}`;
        }

        const res = await fetch(url);
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
                    <button onclick="editar(${item.id}, '${item.titulo}', '${item.tipo}', '${item.status}')">Editar</button>

                    <select id="status-${item.id}">
                        <option value="ativo" ${item.status === "ativo" ? "selected" : ""}>ativo</option>
                        <option value="concluido" ${item.status === "concluido" ? "selected" : ""}>concluido</option>
                        <option value="cancelado" ${item.status === "cancelado" ? "selected" : ""}>cancelado</option>
                    </select>

                    <button onclick="mudarStatus(${item.id})">Mudar status</button>
                    <button onclick="deletar(${item.id})">Excluir</button>
                </td>
            </tr>
            `;
        });

        limparMsg();

    }catch{
        msg("Erro ao carregar dados.");
    }
}

function editar(id, titulo, tipo, status){

    editandoId = id;

    document.getElementById("titulo").value = titulo;
    document.getElementById("tipo").value = tipo;
    document.getElementById("status").value = status;

    const btn = document.querySelector("#form button[type='submit']");
    if(btn) btn.textContent = "Salvar edição";
}

async function enviarForm(e){

    e.preventDefault();

    const item = {
        titulo: document.getElementById("titulo").value,
        tipo: document.getElementById("tipo").value,
        status: document.getElementById("status").value
    };

    try{

        msg("Salvando...");

        if(editandoId === null){

            await fetch(API,{
                method:"POST",
                headers:{ "Content-Type":"application/json" },
                body: JSON.stringify(item)
            });

        }else{

            await fetch(`${API}/${editandoId}`,{
                method:"PUT",
                headers:{ "Content-Type":"application/json" },
                body: JSON.stringify(item)
            });

            editandoId = null;

            const btn = document.querySelector("#form button[type='submit']");
            if(btn) btn.textContent = "Salvar";
        }

        msg("Salvo com sucesso!");
        setTimeout(limparMsg,1200);

        document.getElementById("titulo").value = "";
        document.getElementById("tipo").value = "caminhada";
        document.getElementById("status").value = "ativo";

        carregar();

    }catch{
        msg("Erro ao salvar.");
    }
}

async function mudarStatus(id){

    try{

        msg("Atualizando status...");

        const novoStatus = document.getElementById(`status-${id}`).value;

        await fetch(`${API}/${id}/status`,{
            method:"PATCH",
            headers:{ "Content-Type":"application/json" },
            body: JSON.stringify({ status: novoStatus })
        });

        msg("Status atualizado!");
        setTimeout(limparMsg,1200);

        carregar();

    }catch{
        msg("Erro ao atualizar status.");
    }
}

async function deletar(id){

    try{

        msg("Excluindo...");

        await fetch(`${API}/${id}`,{
            method:"DELETE"
        });

        msg("Item removido!");
        setTimeout(limparMsg,1200);

        carregar();

    }catch{
        msg("Erro ao excluir.");
    }
}

function aplicarFiltros(){
    carregar();
}

function limparFiltros(){

    document.getElementById("filtroTipo").value = "";
    document.getElementById("filtroStatus").value = "";

    carregar();
}

carregar();