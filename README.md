#  Inventário Mágico 

## O Desafio do Inventário Mágico 
Você é um poderoso mago em um mundo de RPG e precisa gerenciar seu inventário de itens mágicos. Seu objetivo é implementar funcionalidades que permitam:

- Adicionar itens ao inventário.
- Remover itens existentes.
- Listar todos os itens atuais no inventário.

### Características
- O inventário é inicializado como uma lista vazia.
- Os itens podem ser representados por strings, como:
  - 📜 Pergaminho de Fogo
  - ⚔️ Espada de Luz
  - 🛡️ Escudo Mágico

---

## 📥 Entrada
Uma ação como **'adicionar'**, **'remover'** ou **'listar'**, e, quando necessário, o nome do item.

---

## 📤 Saída
- **Adicionar**:  
  Retorna: `Item adicionado com sucesso.`

- **Remover**:  
  Retorna: `Item removido com sucesso.`  
  Caso o item não esteja presente, retorna uma mensagem de erro.

- **Listar**:  
  Retorna todos os itens do inventário. Se o inventário estiver vazio, retorna:  
  `Inventário vazio.`

---

![Capturar](https://github.com/user-attachments/assets/fce5e8d3-c2e5-4625-8910-6a3ce3843272)


---

## 🛠️ Planejamento do Projeto
O projeto foi desenvolvido seguindo as etapas abaixo:

### 1. **Definição do Escopo**
- Garantir que o inventário inicializasse vazio e permitisse operações básicas como adicionar, remover e listar itens.
- Focar em uma interface gráfica simples e interativa.
- Incluir elementos visuais e dinâmicos que remetessem ao tema RPG, como ícones mágicos e efeitos visuais.

### 2. **Tecnologias**
- **Python**: Proposto no desafio.
- **Tkinter**: Para a construção de uma interface gráfica amigável e funcional.
- **Pillow**: Para manipulação e redimensionamento de imagens, aprimorando a estética da aplicação.

### 3. **Estrutura do Código**
O código foi dividido em funções claras e independentes:
- **Adicionar Itens**: Permite adicionar itens específicos ao inventário.
- **Remover Itens**: Remove o último item adicionado ao inventário.
- **Listar Itens**: Exibe todos os itens presentes no inventário ou informa que está vazio.
- **Interface Gráfica**: Inclui botões estilizados, efeitos hover e um fundo personalizado.

### 4. **Design e Responsividade**
- O layout foi planejado para ocupar toda a tela de forma proporcional.
- Botões e labels foram estilizados para proporcionar uma experiência imersiva e visualmente agradável.
- A paleta de cores foi escolhida para reforçar a temática mágica, utilizando tons escuros com destaques contrastantes.

---

## 📂 Implementação e Funcionalidades

### Funcionalidades Desenvolvidas
1. **Adicionar Itens**
   - O usuário seleciona itens em categorias como "Itens Mágicos" ou "Poções e Consumíveis".
   - Os itens são adicionados ao inventário com um clique.

2. **Remover Itens**
   - Remove o último item adicionado ao inventário.
   - Atualiza a interface com a confirmação da ação.

3. **Listar Itens**
   - Exibe todos os itens no inventário de forma formatada.
   - Informa caso o inventário esteja vazio.

4. **Interface Gráfica**
   - Background temático configurado com a biblioteca Pillow.
   - Botões com efeitos hover e design responsivo.
   - Labels dinâmicas para exibir mensagens de sucesso ou erros.

### Recursos Visuais
- Ícones mágicos, como:  
  📜 **Pergaminho de Fogo**, ⚔️ **Espada de Luz**, 🛡️ **Escudo Mágico**.  
- Paleta de cores escura com destaque para botões e textos.

---

## 🧪 Conclusão
Este projeto cumpriu todos os objetivos propostos:
- Uma interface gráfica intuitiva e imersiva, adequada ao tema RPG.
- Implementar funcionalidades básicas de gerenciamento de inventário.
- Garantir uma aplicação responsiva e visualmente atraente.

### Aprendizados
- Aplicação prática de bibliotecas como Tkinter e Pillow para construir uma interface funcional e personalizada.
- Planejamento e execução.
- Utilização de boas práticas para organizar e modularizar o código.

---

## 🎯 Próximos Passos
- Adicionar a funcionalidade de salvar e carregar o inventário.
- Implementar categorias personalizadas criadas pelo usuário.
- Incluir animações para tornar a experiência ainda mais dinâmica.

---

## 📝 Créditos
Desenvolvido por **Tiago Ferreira da Silva**.
