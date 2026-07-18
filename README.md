# 🏆 Alura Album - Copa do Mundo Tech

O **Alura Album** é um tributo interativo à história e evolução do desenvolvimento de software, reunindo as mentes mais brilhantes nacionais e internacionais que moldam o futuro da tecnologia. 

Este projeto simula um álbum de figurinhas físico no formato digital, com páginas folheáveis em 3D, efeitos de iluminação realistas, sons procedurais gerados via código e integração dinâmica com uma API backend para colagem das figurinhas.

---

## 🎯 Objetivo do Projeto

O objetivo principal deste projeto é consolidar conceitos de desenvolvimento web moderno (HTML5, CSS3, JavaScript assíncrono e APIs web) através de uma aplicação altamente interativa e rica visualmente. O álbum é dividido em categorias temáticas para homenagear personalidades marcantes:
- **IA**: Pioneiros da Inteligência Artificial (ex: Alan Turing, John McCarthy, Sam Altman).
- **Python**: Criadores e contribuidores da linguagem Python (ex: Guido van Rossum, Tim Peters).
- **Banco de Dados**: Arquitetos e inventores de SGBDs e estruturas de dados (ex: Edgar F. Codd, Salvatore Sanfilippo).
- **Sistemas Operacionais**: Criadores da computação moderna (ex: Linus Torvalds, Dennis Ritchie, Steve Jobs).
- **Brasil (Vol. 1 e 2)**: Educadores, influenciadores e celebridades da tecnologia no Brasil (ex: Paulo Silveira, Rafaela Ballerini, Gustavo Guanabara).

---

## 🚀 Principais Funcionalidades

1. **Folheamento de Páginas 3D (PageFlip)**:
   - Navegação interativa que imita o comportamento de um livro ou álbum físico.
   - Suporte a gestos de arrastar (`drag`) com mouse e touch screen, controle pelo teclado (setas esquerda/direita) e botões laterais de navegação.
   - Sombra e curvatura dinâmica nas lombadas e páginas durante a transição.

2. **Síntese de Som Procedural (Web Audio API)**:
   - Efeitos sonoros realistas de papel virando gerados dinamicamente no navegador (sem necessidade de carregar arquivos pesados de áudio).
   - Utilização de ruído branco, filtros passa-banda (*bandpass*) e passa-baixa (*lowpass*) com varredura de frequência para simular a fricção do papel.
   - Controle de ativação/mudo de som acessível por botão flutuante.

3. **Integração Dinâmica com Backend (API)**:
   - Carregamento assíncrono de figurinhas a partir de uma API executada localmente (por padrão em `http://localhost:8000/figurinhas`).
   - Mapeamento e colagem automática de figurinhas nos slots correspondentes via JavaScript.
   - Transição animada suave (*fade-in* e escala) para simular o ato de "colar" a figurinha quando a imagem é carregada com sucesso.

4. **Identidade Visual Premium (CSS Moderno)**:
   - Efeitos visuais avançados, incluindo tipografia *glitch* na capa, esfera 3D centralizada com anéis orbitais brilhantes e cards flutuantes na capa.
   - Slots de figurinhas vazios com bordas tracejadas e números grandes, que se transformam em imagens com overlays de nomes no carregamento.

---

## 📁 Arquivos do Projeto

Abaixo estão descritos os arquivos principais que compõem o frontend da aplicação:

### 1. 📄 [index.html](file:///c:/Users/alexe/Downloads/i-arq-ia-alura-album-main/i-arq-ia-alura-album-main/index.html)
Contém toda a marcação estrutural e semântica do álbum.
- Define a capa do álbum, a contracapa e as páginas internas subdivididas em seções.
- Estrutura os slots (`.sticker-slot`) onde as figurinhas dinâmicas serão renderizadas.
- Importa a biblioteca externa `page-flip` via CDN e o script local `app.js`.

### 2. 🎨 [style.css](file:///c:/Users/alexe/Downloads/i-arq-ia-alura-album-main/i-arq-ia-alura-album-main/style.css)
Responsável por toda a estilização, efeitos de transição e paleta de cores.
- Implementa um tema escuro e futurista com gradientes radiais profundos (`--color-blue-universe`, `--color-deep-blue`, `--color-new-black`).
- Estiliza os slots normais e especiais (`.special-slot`), além do comportamento responsivo da imagem da figurinha (`.sticker-img`).
- Define animações complexas:
  - Animação de *glitch* para o título na capa.
  - Flutuação suave dos mini cards na capa (`mc-turing`, `mc-guido`, `mc-jobs`).
  - Rotação e pulso da esfera tecnológica (`tech-sphere`) e seus anéis (`ring-1`, `ring-2`).

### 3. ⚙️ [app.js](file:///c:/Users/alexe/Downloads/i-arq-ia-alura-album-main/i-arq-ia-alura-album-main/app.js)
Controla a interatividade e comportamento dinâmico do site.
- **Configuração da API**: Conecta ao servidor local para buscar os metadados e imagens das figurinhas.
- **Inicialização do PageFlip**: Configura dimensões da página, tempos de transição e implementa o arraste manual preciso.
- **Síntese de Áudio**: Cria a função `playPaperTurnSound()` que sintetiza o barulho de papel virando em tempo real através da API Web Audio do navegador.
- **Controles Auxiliares**: Gerencia atalhos de teclado (setas esquerda e direita), controle de mudo e visibilidade das setas laterais.

---

## 🛠️ Como Executar o Projeto

### Requisitos Mínimos
- Um navegador web moderno com suporte a ES6 e Web Audio API.
- Um servidor local simples para servir o frontend (necessário para evitar políticas de CORS em chamadas de API).

### Executando o Frontend
Você pode abrir o projeto usando qualquer servidor web estático local:
* **VS Code**: Utilize a extensão **Live Server**.
* **Python**: Execute o comando abaixo no terminal da pasta do projeto:
  ```bash
  python -m http.server 8080
  ```
  Depois, acesse `http://localhost:8080` no navegador.

### Conectando ao Backend (Opcional - Dia 3 da Imersão)
Para que as figurinhas apareçam coladas no álbum, é necessário executar o backend que fornece os dados na porta `8000`:
1. Navegue até a pasta correspondente ao backend (ex: `cd backend/dia-3`).
2. Instale as dependências necessárias (FastAPI e Uvicorn).
3. Inicie o servidor:
   ```bash
   uvicorn main:app --reload
   ```
4. Recarregue o frontend. As figurinhas serão baixadas e coladas automaticamente.
