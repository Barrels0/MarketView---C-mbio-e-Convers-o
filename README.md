# 📈 MarketView - Câmbio e Conversão

<p align="center">
  <a href="https://marketviewnickolas.streamlit.app/" target="_blank">
    <img src="https://img.shields.io/badge/🔴_ACESSAR_PROJETO_ONLINE-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Acessar Projeto Online">
  </a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit">
  <img src="https://img.shields.io/badge/API-005571?style=for-the-badge&logo=api&logoColor=white" alt="API REST">
</p>

O **MarketView** é uma aplicação web interativa desenvolvida em Python que consome dados de uma API REST pública para exibir cotações de moedas em tempo real, tendências de mercado e realizar conversões cambiais dinâmicas.

---

## 🚀 Funcionalidades Principais

* **Cotações em Tempo Real:** Conexão com a *AwesomeAPI* para buscar valores atualizados do Dólar (USD), Euro (EUR) e Bitcoin (BTC), incluindo indicadores visuais de variação diária (Alta/Baixa).
* **Gráficos de Tendência (Data Viz):** Consumo de endpoints históricos para renderização de gráficos de linha, permitindo a análise do comportamento do Dólar nos últimos 7 dias.
* **Calculadora de Câmbio:** Motor de conversão cruzada entre moedas fiduciárias e criptomoedas, utilizando o Real como base de cálculo.
* **Memória de Sessão (State Management):** Utilização avançada do `st.session_state` do Streamlit para armazenar e exibir o extrato de conversões realizadas pelo usuário durante o uso do aplicativo.

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Função |
| :--- | :--- |
| **Python** | Lógica de negócios e processamento de dados |
| **Streamlit** | Criação da interface web (Dashboard), deploy na nuvem e gerenciamento de estado |
| **Requests** | Biblioteca para requisições HTTP (GET) à API REST |
| **AwesomeAPI** | Provedor dos dados financeiros em formato JSON |

## ⚙️ Como executar o projeto localmente

### 1. Pré-requisitos
* [Python 3.x](https://www.python.org/) instalado na sua máquina.

### 2. Instalação
Clone o repositório e instale as dependências listadas no `requirements.txt`:
```bash
git clone [https://github.com/Barrels0/MarketView---C-mbio-e-Convers-o-Nome-de-sistema-corporativo-.git](https://github.com/Barrels0/MarketView---C-mbio-e-Convers-o-Nome-de-sistema-corporativo-.git)
cd NOME_DO_REPO
pip install -r requirements.txt